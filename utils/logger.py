import logging
import os
import sys
from logging.handlers import RotatingFileHandler

if getattr(sys, 'frozen', False):
    # 如果是打包后的exe，使用sys._MEIPASS获取资源路径
    BASE_DIR = os.path.dirname(sys.executable)
else:
    # 否则，使用常规的__file__路径
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 获取项目根目录
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LOG_DIR = os.path.join(BASE_DIR, 'logs')

# 如果logs目录不存在，则创建
if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)

LOG_FILE = os.path.join(LOG_DIR, 'wechatbot.log')


def setup_logger():
    logger = logging.getLogger('wechatbot_logger')
    logger.setLevel(logging.DEBUG)  # 设置最低日志级别

    # 避免重复添加handler
    if not logger.handlers:
        # 控制台输出
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)  # 控制台只输出INFO及以上级别
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)

        # 文件输出，按大小轮转
        file_handler = RotatingFileHandler(
            LOG_FILE, maxBytes=10 * 1024 * 1024, backupCount=5, encoding='utf-8'
        )  # 10MB per file, keep 5 backup files
        file_handler.setLevel(logging.DEBUG)  # 文件记录所有DEBUG及以上级别
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    return logger


# 全局日志实例
logger = setup_logger()
