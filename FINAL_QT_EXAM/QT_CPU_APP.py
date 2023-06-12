import sys
import subprocess
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QTextEdit, QPushButton


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Network Monitoring App")
        self.setGeometry(100, 100, 500, 400)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        self.ping_button = QPushButton("Ping")
        self.layout.addWidget(self.ping_button)
        self.ping_button.clicked.connect(self.ping)

        self.tracert_button = QPushButton("Tracert")
        self.layout.addWidget(self.tracert_button)
        self.tracert_button.clicked.connect(self.tracert)

        self.log_label = QLabel("Log:")
        self.layout.addWidget(self.log_label)

        self.log_text = QTextEdit()
        self.layout.addWidget(self.log_text)

        self.ping_process = None
        self.tracert_process = None

    def ping(self):
        self.ping_process = subprocess.Popen(['ping', '-c', '4', 'google.com'], stdout=subprocess.PIPE,
                                             stderr=subprocess.PIPE)
        output, _ = self.ping_process.communicate()
        output = output.decode('utf-8')
        self.log_text.append(output)
        if self.ping_process.returncode == 0:
            self.log_text.append("Ping successful.")
        else:
            self.log_text.append("Ping failed.")

    def tracert(self):
        self.tracert_process = subprocess.Popen(['traceroute', 'google.com'], stdout=subprocess.PIPE,
                                                stderr=subprocess.PIPE)
        output, _ = self.tracert_process.communicate()
        output = output.decode('utf-8')
        self.log_text.append(output)


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
