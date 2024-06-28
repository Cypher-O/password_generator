from PyQt5.QtWidgets import QMessageBox
from model.pwd_generator_model import PasswordModel
from utils.config import *

class PasswordController:
    def __init__(self, view):
        self.view = view
        self.view.generate_button.clicked.connect(self.on_generate)

    def on_generate(self):
        try:
            min_length = int(self.view.min_length_input.text())
            if min_length <= 0:
                raise ValueError(MINIMUM_LENGTH_MESSAGE)
        except ValueError:
            QMessageBox.critical(self.view, INVALID_INPUT, VALID_POSITIVE_INTEGER_MESSAGE)
            return
        
        has_numbers = self.view.include_numbers.isChecked()
        has_special = self.view.include_special_characters.isChecked()
        
        pwd = PasswordModel.generate_password(min_length, has_numbers, has_special)
        self.view.result_display.setText(pwd)
