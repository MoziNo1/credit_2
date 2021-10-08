import logging


class Logger(object):

    @staticmethod
    def get_logger(level='DEBUG', file_name='log.txt'):
        # 首先创建日志收集器对象
        logger = logging.getLogger(name='log_output')
        # 设置日志收集器收集日志信息的等级
        logger.setLevel(level)
        format_log = f'[%(asctime)s][%(threadName)s:%(thread)d][task_id:%(name)s][%(filename)s:%(lineno)d]' \
                     f'[%(levelname)s][%(message)s]'
        # 创建控制台收集渠道
        format_logger = logging.Formatter(format_log)
        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(format_logger)
        stream_handler.setLevel(level)
        # 创建文件收集渠道
        file_handler = logging.FileHandler(filename=file_name, encoding='utf-8')
        file_handler.setFormatter(format_logger)
        file_handler.setLevel(level)
        logger.addHandler(stream_handler)
        logger.addHandler(file_handler)

        return logger


log = Logger.get_logger(level="DEBUG")

