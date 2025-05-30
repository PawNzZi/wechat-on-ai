from wxauto import WeChat
from utils.config import load_config
from utils.logger import logger
import random
import time
import threading


class WeChatClient:
    def __init__(self):
        logger.info("Initializing WeChatClient...")
        self.wx = WeChat()
        try:
            config = load_config()
            self.monitor_user = config.get("monitor_user")
            self.llm = config.get("llm")
            self.ml = config.get("ml")
            self.nick_name = config.get("wechat_nickname")
            self.processing_message_event = threading.Event()  # 用于do_something和get_listen_message之间的同步
            logger.info("WeChatClient initialized successfully with config.")
            from llm.llm import LLMClient
            self.llm_client = LLMClient(
                llm=self.llm
            )
            self.wx.ChatWith(who='文件传输助手')
            for i in self.monitor_user:
                self.wx.AddListenChat(who=i, savepic=True)
            logger.info("WeChatClient listening for messages...")
        except Exception as e:
            logger.error(f"Failed to initialize WeChatClient: {e}")
            raise  # Re-raise the exception after logging

    # 监听消息
    def get_listen_message(self):
        logger.info("Starting to listen for messages...")
        
        wait = 3  # 设置3秒查看一次是否新消息
        while True:
            try:
                # logger.info("Starting ")
                msgs = self.wx.GetListenMessage()
                for chat in msgs:
                    one_msgs = msgs.get(chat)  # 获取消息内容
                    for msg in one_msgs:
                        if msg.type == 'sys':
                            logger.info(f'【系统消息】{msg.content}')
                        elif msg.type == 'friend':
                            self.processing_message_event.set()  # 收到好友消息，设置事件，暂停do_something
                            sender = msg.sender  # 这里可以将msg.sender改为msg.sender_remark，获取备注名
                            # logger.info(f'<{sender.center(10, "-")}>：{msg.content}')
                            if msg.content == '[聊天记录]':
                                content_list = msg.parse()
                                formatted_messages = []
                                for item in content_list:
                                    if item[0] == self.nick_name:
                                        sender = "我"
                                    else:
                                        sender = item[0]
                                    message = item[1]
                                    # 在消息内容后面添加句号
                                    formatted_messages.append(f"{sender}：{message}。")
                                message = "\n".join(formatted_messages)
                            else:
                                message = msg.content

                            logger.info(f"Sending message to LLM: {message}")
                            try:
                                llm_response = self.llm_client.chat_completion(message)
                                logger.info(f"Received response from LLM: {llm_response}")
                                msg.quote(llm_response)
                            except Exception as llm_e:
                                logger.error(f"Error calling LLM: {llm_e}")
                                msg.quote(f"对不起，我暂时无法回答您的问题。{llm_e}")
                                
                            self.processing_message_event.clear()  # 处理完毕，清除事件，恢复do_something
                        elif msg.type == 'self':
                            logger.info(f'<{msg.sender.center(10, "-")}>：{msg.content}')
                        elif msg.type == 'time':
                            logger.info(f'\n【时间消息】{msg.time}')
                        elif msg.type == 'recall':
                            logger.info(f'【撤回消息】{msg.content}')
                time.sleep(wait)
            except KeyboardInterrupt:
                logger.error(f'KeyboardInterrupt')
                break

    # 模拟操作
    def do_something(self):
        logger.info("Starting timed random operations...")
        operations = [
            ("ChatWith File Transfer Assistant", lambda: self.wx.ChatWith(who='文件传输助手')),
            ("SwitchToChat", lambda: self.wx.SwitchToChat()),
            ("ChatWith Monitor User", lambda: self.wx.ChatWith(who=self.monitor_user[0]))
        ]

        while True:
            try:
                # 检查是否正在处理消息，如果是，则等待
                # logger.info("进入while循环")
                if self.processing_message_event.is_set():
                    logger.info("do_something: Waiting for message processing to complete...")
                    self.processing_message_event.wait()  # 等待事件被清除

                # 随机选择一个操作
                op_name, chosen_operation = random.choice(operations)
                logger.info(f"Executing random operation: {op_name}")
                chosen_operation()

                # 随机等待一段时间（例如，5到15秒）
                wait_time = random.randint(5, 15)
                logger.info(f"Waiting for {wait_time} seconds before next operation.")
                time.sleep(wait_time)
            except Exception as e:
                logger.error(f"Error during random operation: {e}")
                time.sleep(5)  # 发生错误时等待一段时间再重试
