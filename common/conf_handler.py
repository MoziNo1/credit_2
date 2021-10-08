from configparser import ConfigParser


class ConfRead(object):

    @staticmethod
    def get_conf():
        config = ConfigParser()
        config.read(r"D:\credit\conf\config.ini", encoding="utf-8")
        return config


conf = ConfRead.get_conf()