from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout, QToolButton, QMenu
from PyQt6.QtCore import Qt


class HomePage(QWidget):
    def __init__(self, parent):
        super().__init__(parent)

        # Greeting Label
        greeting = QLabel("Hello, User!")
        greeting.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop)

        # Hamburger Menu
        menu_button = QToolButton(self)
        menu_button.setText("≡")
        menu_button.setPopupMode(QToolButton.ToolButtonPopupMode.InstantPopup)
        menu = QMenu()
        settings_action = menu.addAction("Settings")
        settings_action.triggered.connect(parent.switch_to_settings)
        menu_button.setMenu(menu)

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(greeting)
        layout.addWidget(menu_button, alignment=Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignRight)
        layout.addStretch()  # Push everything to the top
        self.setLayout(layout)
