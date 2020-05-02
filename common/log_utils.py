import os
import logging

current_path = os.path.dirname(__file__)  # 获取文件当前路径
log_path = os.path.join(current_path, '../logs/log.txt')


class LogUtils:
    def __init__(self, log_file_path=log_path):
        self.log_file_path = log_file_path
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(level=logging.INFO)
        console = logging.StreamHandler()
        formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
        console.setFormatter(formatter)

        file_log = logging.FileHandler(log_path)
        file_log.setFormatter(formatter)
        self.logger.addHandler(console)
        self.logger.addHandler(file_log)

    def info(self, message):
        self.logger.info(message)

    def error(self, message):
        self.logger.error(message)


logger = LogUtils()


if __name__ == '__main__':
    # log_utils = LogUtils()
    logger.info('hello, word')