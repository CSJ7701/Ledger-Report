import sys
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QLabel, QPushButton, QMenu, QMenuBar, QTabWidget, QFrame
    )
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QAction, QBrush, QPainter, QPen
from pages.home import HomePage
from pages.settings import SettingsPage

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Ledger App")
        self.setGeometry(100,100,800,600)

        # Central Widget: Stack for different pages
        container = QWidget()
        self.setCentralWidget(container)

        # Main Layout
        layout = QVBoxLayout()
        container.setLayout(layout)

        # Top Bar
        layout.addWidget(self.create_top_bar())

        # Home Screen
        layout.addLayout(self.create_home_screen())

    def create_top_bar(self):
        # Layout
        top_bar = QWidget()
        top_bar_layout = QHBoxLayout()
        top_bar.setLayout(top_bar_layout)

        # Tabs
        tabs = QTabWidget()
        tabs.addTab(QWidget(), "Home")
        tabs.addTab(QWidget(), "Reports")
        tabs.addTab(QWidget(), "Settings")
        top_bar_layout.addWidget(tabs)
        
        return top_bar

    def create_home_screen(self):
        # Layout for the home screen
        home_layout = QHBoxLayout()

        # Left side: Greeting and Pie Chart
        left_layout = QVBoxLayout()

        # Greeting
        greeting_label = QLabel("Hello, CJ!")
        greeting_label.setStyleSheet("font-size: 18px;")
        greeting_label.setAlignment(Qt.AlignmentFlag.AlignLeft)
        left_layout.addWidget(greeting_label)

        # Spacer between greeting and pie chart
        left_layout.addStretch()

        home_layout.addLayout(left_layout)


        return home_layout

if __name__ == "__main__":
    app =QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
