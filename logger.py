import datetime
import inspect
from entities import User

class Logger():
    def __init__(self):
        self.logfile = "log.txt"

    def basicConfig(self, filename):
        if filename.find(".txt") > 0:
            self.logfile = filename

    def info(self, msg, func_name):
        f = open(self.logfile, "a")
        f.write("[" + str(datetime.datetime.now().replace(microsecond=0)) + "] " + " INFO: "
                + msg + " |in " + func_name + "\n")
        f.close()

    def warning(self, msg, func_name):
        f = open(self.logfile, "a")
        f.write("[" + str(datetime.datetime.now().replace(microsecond=0)) + "] " + " WARNING: "
                + msg + " |in " + func_name + "\n")
        f.close()

    def error(self, msg, func_name):
        f = open(self.logfile, "a")
        f.write("[" + str(datetime.datetime.now().replace(microsecond=0)) + "] " + " ERROR: "
                + msg + " |in " + func_name + "\n")
        f.close()

class RoleLogger(Logger):
    def info(self, msg, func_name, user):
        f = open(self.logfile, "a")
        f.write("[" + str(datetime.datetime.now().replace(microsecond=0)) + "] " + " INFO: "
                + msg + " |in " + func_name + " by " + user.role + " " + user.name + "\n")
        f.close()

    def warning(self, msg, func_name, user):
        f = open(self.logfile, "a")
        f.write("[" + str(datetime.datetime.now().replace(microsecond=0)) + "] " + " WARNING: "
                + msg + " |in " + func_name + " by " + user.role + " " + user.name + "\n")
        f.close()

    def error(self, msg, func_name, user):
        f = open(self.logfile, "a")
        f.write("[" + str(datetime.datetime.now().replace(microsecond=0)) + "] " + " ERROR: "
                + msg + " |in " + func_name + " by " + user.role + " " + user.name + "\n")
        f.close()
