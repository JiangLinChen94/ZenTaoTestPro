# 简单日志
import os
import logging

current_path = os.path.dirname(__file__)
log_file_path = os.path.join(current_path,'../logs/test.log')

# 创建一个日志对象，定义一个名称
logger = logging.getLogger(__name__)

# 设置全局日志级别debug info warning error fatal..
logger.setLevel(level=logging.INFO)

# 创建一个控制台输出日志的对象
console = logging.StreamHandler()
# 设置日志格式
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
console.setFormatter(formatter)
# 自定义日志级别，设定的级别越高，会自动过滤该级别以下的错误日志
console.setLevel(level=logging.DEBUG)

# 输出日志到文件中
file_log = logging.FileHandler(log_file_path)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_log.setFormatter(formatter)

# 日志独享配置在控制台输出
logger.addHandler(console)

# 日志对象配置在文件输出
logger.addHandler(file_log)

# 替换之前的print
logger.debug("查错")
logger.warning("警告")
logger.info("提示")
logger.error("错误")
