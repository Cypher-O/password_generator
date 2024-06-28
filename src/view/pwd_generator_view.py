from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QCheckBox
from utils.config import *

class PasswordView(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        # Set up the window
        self.setWindowTitle(APPLICATION_NAME)
        self.setGeometry(100, 100, 400, 200)

        # Create layout
        layout = QVBoxLayout()

        # Minimum Length
        min_length_layout = QHBoxLayout()
        self.min_length_label = QLabel(MINIMUM_LENGTH)
        self.min_length_input = QLineEdit()
        min_length_layout.addWidget(self.min_length_label)
        min_length_layout.addWidget(self.min_length_input)
        layout.addLayout(min_length_layout)

        # Include Numbers
        self.include_numbers = QCheckBox(INCLUDE_NUMBERS)
        self.include_numbers.setChecked(True)
        layout.addWidget(self.include_numbers)

        # Include Special Characters
        self.include_special_characters = QCheckBox(INCLUDE_SPECIAL_CHARACTERS)
        self.include_special_characters.setChecked(True)
        layout.addWidget(self.include_special_characters)

        # Generate Button
        self.generate_button = QPushButton(GENERATE_PASSWORD)
        layout.addWidget(self.generate_button)

        # Result
        self.result_label = QLabel(PASSWORD_GENERATED)
        self.result_display = QLineEdit()
        self.result_display.setReadOnly(True)
        layout.addWidget(self.result_label)
        layout.addWidget(self.result_display)

        # Set main layout
        self.setLayout(layout)
