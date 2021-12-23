from repository import *
import json

class BaseParser():
    def __init__(self):
        self.config_file = "config.json"


class JsonParser(BaseParser):

    def get_base(self):
        with open(self.config_file, "r") as read_file:
            data = json.load(read_file)
        return data['database']

    def get_connection_data(self):
        with open(self.config_file, "r") as read_file:
            data = json.load(read_file)
        return data['data']

class BaseAuthorizator():
    def __init__(self):
        pass

class Authorizator(BaseAuthorizator):
    def auhorizate(self, login, password):
        employers = EmployersStore().get_all()
        for employee in employers:
            if (employee.login == login and employee.password == password):
                return employee
        return

class ConnectionException(Exception):
    def __init__(self, message, *errors):
        Exception.__init__(self, message)
        self.errors = errors

class DataBaseConnector():
    def __init__(self):
        pass

class PostgresqlConnector(DataBaseConnector):
    def connect(self, auth_data):
        try:
            if auth_data.db == "PostgreSQL":
                dat = PostgresqlDatabase(auth_data.dbname,
                                        user=auth_data.user,
                                        password=auth_data.password,
                                        host=auth_data.host,
                                        port=auth_data.port)
            elif auth_data.db == "MySQL":
                dat = SqliteDatabase(auth_data.dbname,
                                     user=auth_data.user,
                                     password=auth_data.password,
                                     host=auth_data.host,
                                     port=auth_data.port)
            db.initialize(dat)
            db.connect()
            '''db.init(auth_data.dbname,
                    user=auth_data.user,
                    password=auth_data.password,
                    host=auth_data.host,
                    port=auth_data.port)
            db.connect()'''
            #print("Connected as " + auth_data.user + "\n")
        except Exception as e:
            raise ConnectionException('error connecting')
        '''if (user.role == "system_administrator"):
            try:
                data = JsonParser().
                db.init('BankStructure', user='postgres',
                        password='forest123ry',
                        host='localhost',
                        port='5432')
                db.connect()
                print("Connected as sysadmin.\n")
            except Exception as e:
                raise ConnectionException('error connecting as sysadmin')
        elif (user.role == "manager"):
            try:
                db.init('BankStructure', user='manager',
                        password='1234',
                        host='localhost',
                        port='5432')
                db.connect()
                print("Connected as manager.\n")
            except Exception as e:
                raise ConnectionException('error connecting as manager')
        elif (user.role == "administrator"):
            try:
                db.init('BankStructure', user='administrator',
                        password='1234',
                        host='localhost',
                        port='5432')
                db.connect()
                print("Connected as administrator.\n")
            except Exception as e:
                raise ConnectionException('error connecting as administrator')
        elif (user.role == "director"):
            try:
                db.init('BankStructure', user='director',
                        password='1234',
                        host='localhost',
                        port='5432')
                db.connect()
                print("Connected as director.\n")
            except Exception as e:
                raise ConnectionException('error connecting as director')
        elif (user.role == "reader"):
            try:
                db.init('BankStructure', user='reader',
                        password='1234',
                        host='localhost',
                        port='5432')
                db.connect()
                print("Connected as reader.\n")
            except Exception as e:
                raise ConnectionException('error connecting as reader')'''

    def disconnect(self):
        try:
            db.close()
        except Exception as e:
            raise ConnectionException('error disconnecting')
