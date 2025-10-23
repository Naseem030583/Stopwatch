from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout
from PyQt5.QtCore import QTimer, Qt
from PyQt5.QtGui import QFont
import sys


class Stopwatch(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("⏱️ Stopwatch")
        self.setGeometry(300, 300, 400, 250)
        self.setStyleSheet("background-color: #2C3E50;")

        # Variables
        self.running = False
        self.time_elapsed = 0  # in milliseconds

        # Timer
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_time)

        # Create UI
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        # Title
        title = QLabel("⏱️ STOPWATCH")
        title.setAlignment(Qt.AlignCenter)
        title.setFont(QFont("Arial", 16, QFont.Bold))
        title.setStyleSheet("color: #ECF0F1; padding: 10px;")
        layout.addWidget(title)

        # Time Display
        self.time_label = QLabel("00:00:00:00")
        self.time_label.setAlignment(Qt.AlignCenter)
        self.time_label.setFont(QFont("Courier New", 48, QFont.Bold))
        self.time_label.setStyleSheet("""
            background-color: #34495E;
            color: #2ECC71;
            padding: 20px;
            border: 3px solid #1A1A1A;
            border-radius: 10px;
        """)
        layout.addWidget(self.time_label)

        # Buttons
        button_layout = QHBoxLayout()

        self.start_button = QPushButton("START")
        self.start_button.setFont(QFont("Arial", 12, QFont.Bold))
        self.start_button.setStyleSheet("""
            QPushButton {
                background-color: #27AE60;
                color: white;
                padding: 10px 20px;
                border-radius: 5px;
                min-width: 100px;
            }
            QPushButton:hover {
                background-color: #229954;
            }
            QPushButton:disabled {
                background-color: #7F8C8D;
            }
        """)
        self.start_button.clicked.connect(self.start)

        self.stop_button = QPushButton("STOP")
        self.stop_button.setFont(QFont("Arial", 12, QFont.Bold))
        self.stop_button.setStyleSheet("""
            QPushButton {
                background-color: #E74C3C;
                color: white;
                padding: 10px 20px;
                border-radius: 5px;
                min-width: 100px;
            }
            QPushButton:hover {
                background-color: #C0392B;
            }
            QPushButton:disabled {
                background-color: #7F8C8D;
            }
        """)
        self.stop_button.clicked.connect(self.stop)
        self.stop_button.setEnabled(False)

        self.reset_button = QPushButton("RESET")
        self.reset_button.setFont(QFont("Arial", 12, QFont.Bold))
        self.reset_button.setStyleSheet("""
            QPushButton {
                background-color: #3498DB;
                color: white;
                padding: 10px 20px;
                border-radius: 5px;
                min-width: 100px;
            }
            QPushButton:hover {
                background-color: #2980B9;
            }
        """)
        self.reset_button.clicked.connect(self.reset)

        button_layout.addWidget(self.start_button)
        button_layout.addWidget(self.stop_button)
        button_layout.addWidget(self.reset_button)

        layout.addLayout(button_layout)
        self.setLayout(layout)

    def update_time(self):
        self.time_elapsed += 10  # 10 milliseconds

        # Calculate time components
        milliseconds = (self.time_elapsed // 10) % 100
        seconds = (self.time_elapsed // 1000) % 60
        minutes = (self.time_elapsed // 60000) % 60
        hours = self.time_elapsed // 3600000

        # Update display
        time_string = f"{hours:02d}:{minutes:02d}:{seconds:02d}:{milliseconds:02d}"
        self.time_label.setText(time_string)

    def start(self):
        if not self.running:
            self.running = True
            self.timer.start(10)  # Update every 10ms
            self.start_button.setEnabled(False)
            self.stop_button.setEnabled(True)

    def stop(self):
        if self.running:
            self.running = False
            self.timer.stop()
            self.start_button.setEnabled(True)
            self.stop_button.setEnabled(False)

    def reset(self):
        self.running = False
        self.timer.stop()
        self.time_elapsed = 0
        self.time_label.setText("00:00:00:00")
        self.start_button.setEnabled(True)
        self.stop_button.setEnabled(False)


# Main Program
if __name__ == "__main__":
    app = QApplication(sys.argv)
    stopwatch = Stopwatch()
    stopwatch.show()
    sys.exit(app.exec_())