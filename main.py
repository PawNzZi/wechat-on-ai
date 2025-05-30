from auto.client import WeChatClient
from utils.logger import logger
import threading
import time

if __name__ == "__main__":
    logger.info("Starting WeChatBot...")
    client = WeChatClient()

    # 在单独的线程中运行 get_listen_message
    listen_thread = threading.Thread(target=client.get_listen_message)
    listen_thread.daemon = True  # 设置为守护线程，主线程退出时子线程也退出
    listen_thread.start()

    # 在单独的线程中运行 do_something
    do_something_thread = threading.Thread(target=client.do_something)
    do_something_thread.daemon = True  # 设置为守护线程
    do_something_thread.start()

    # 保持主线程运行，以便守护线程可以继续执行
    try:
        while True:
            time.sleep(1)  # 避免CPU空转
    except KeyboardInterrupt:
        logger.info("WeChatBot stopped by user.")