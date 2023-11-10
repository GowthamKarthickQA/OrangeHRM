import configparser

config = configparser.RawConfigParser()
config.read(".\\Configuration\\config.ini")

class ReadConfig:

    @staticmethod
    def getApplicationURL():
        url = config.get('common info','baseURL')
        return url

    @staticmethod
    def getUsername():
        username = config.get('common info','username')
        return username

    @staticmethod
    def getPassword():
        password = config.get('common info','password')
        return password

    @staticmethod
    def getUsername_valid():
        username_valid = config.get('common info', 'username_valid')
        return username_valid

    @staticmethod
    def getPassword_invalid():
        password_invalid = config.get('common info', 'password_invalid')
        return password_invalid

    @staticmethod
    def getFirstname():
        firstname = config.get('common info','firstname')
        return firstname

    @staticmethod
    def getMiddlename():
        middlename = config.get('common info', 'middlename')
        return middlename

    @staticmethod
    def getLastname():
        lastname = config.get('common info', 'lastname')
        return lastname

    @staticmethod
    def getEmp_id():
        empid = config.get('common info', 'empid')
        return empid

