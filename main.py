from controller import *
from view import *
#from parser import JsonConfigParser

def main():
    pass

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    controller = Controller()
    #view = ConsoleView(controller)
    #view.auth_menu()
    mywin = Interface()
    mywin.set_controller(controller)
    mywin.show()
    sys.exit(app.exec_())
    #main()