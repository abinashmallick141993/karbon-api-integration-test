import configparser


def getconfig():
    config = configparser.ConfigParser()
    config.read('/pythonProjectAPI/Utilities/properties.ini')
    return config

#C:\Users\AbinashMallick\PycharmProjects\pythonProjectAPI\Utilities\properties.ini