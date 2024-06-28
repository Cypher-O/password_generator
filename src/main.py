import sys
from PyQt5.QtWidgets import QApplication
from view.pwd_generator_view import PasswordView
from controller.pwd_generator_controller import PasswordController

def main():
    app = QApplication(sys.argv)

    view = PasswordView()
    controller = PasswordController(view)

    view.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()