from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout, QPushButton
from PyQt6.QtCore import Qt


class SettingsPage(QWidget):
    def __init__(self, parent):
        super().__init__(parent)

        # Label
        label = QLabel("Settings Page")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Back button
        back_button = QPushButton("Back to Home")
        back_button.clicked.connect(parent.switch_to_home)

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(label)
        layout.addWidget(back_button, alignment=Qt.AlignmentFlag.AlignCenter)
        self.setLayout(layout)
