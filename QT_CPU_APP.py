import sys
import psutil
from PyQt6.QtCore import QTimer, pyqtSignal
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QComboBox, QGroupBox, QGridLayout


class SystemMonitorApp(QMainWindow):
    #updateIntervalChanged = pyqtSignal(int)

    def __init__(self):
        super().__init__()

        self.setWindowTitle("System Monitor")
        self.resize(800, 600)

        self.main_widget = QWidget()
        self.setCentralWidget(self.main_widget)

        self.main_layout = QVBoxLayout()
        self.main_widget.setLayout(self.main_layout)

        self.info_groupbox = QGroupBox("System Information")
        self.info_layout = QGridLayout()
        self.info_groupbox.setLayout(self.info_layout)

        self.processes_groupbox = QGroupBox("Running Processes")
        self.processes_layout = QVBoxLayout()
        self.processes_groupbox.setLayout(self.processes_layout)

        self.services_groupbox = QGroupBox("Running Services")
        self.services_layout = QVBoxLayout()
        self.services_groupbox.setLayout(self.services_layout)

        self.tasks_groupbox = QGroupBox("Task Scheduler Tasks")
        self.tasks_layout = QVBoxLayout()
        self.tasks_groupbox.setLayout(self.tasks_layout)

        self.main_layout.addWidget(self.info_groupbox)
        self.main_layout.addWidget(self.processes_groupbox)
        self.main_layout.addWidget(self.services_groupbox)
        self.main_layout.addWidget(self.tasks_groupbox)

        self.update_interval_combo = QComboBox()
        self.update_interval_combo.addItems(["1 sec", "5 sec", "10 sec", "30 sec"])
        self.info_layout.addWidget(QLabel("Update Interval:"), 0, 0)
        self.info_layout.addWidget(self.update_interval_combo, 0, 1)

        self.cpu_label = QLabel()
        self.info_layout.addWidget(QLabel("CPU:"), 1, 0)
        self.info_layout.addWidget(self.cpu_label, 1, 1)

        self.ram_label = QLabel()
        self.info_layout.addWidget(QLabel("RAM:"), 2, 0)
        self.info_layout.addWidget(self.ram_label, 2, 1)

        self.hdd_labels = []
        self.info_layout.addWidget(QLabel("Hard Drives:"), 3, 0)
        self.hdd_layout = QVBoxLayout()
        self.info_layout.addLayout(self.hdd_layout, 3, 1)

        self.update_interval_combo.currentIndexChanged.connect(self.on_update_interval_changed)

        self.update_interval = 100000  # default update interval is 1 second
        self.update_timer = QTimer()
        self.update_timer.timeout.connect(self.update_system_info)
        self.update_timer.start(self.update_interval)

        self.update_system_info()

    def on_update_interval_changed(self, index):
        intervals = [1000, 5000, 10000, 30000]
        self.update_interval = intervals[index]
        self.update_timer.setInterval(self.update_interval)

    def update_system_info(self):
        try:
            # Update CPU information
            cpu_percent = psutil.cpu_percent()
            self.cpu_label.setText(f"{cpu_percent}%")

            # Update RAM information
            ram_percent = psutil.virtual_memory().percent
            self.ram_label.setText(f"{ram_percent}%")

            # Update hard drive information
            self.update_hard_drive_info()

            # Update running processes
            self.update_running_processes()
        except psutil.Error as e:
            print(f"Error retrieving system information: {e}")

    def update_hard_drive_info(self):
        hard_drives = psutil.disk_partitions()
        for label in self.hdd_labels:
            label.deleteLater()
        self.hdd_labels = []
        for i, drive in enumerate(hard_drives):
            try:
                total_space = psutil.disk_usage(drive.device).total
                used_space = psutil.disk_usage(drive.device).used
                hdd_label = QLabel(f"{drive.device}: {used_space}/{total_space}")
                self.hdd_layout.addWidget(hdd_label)
                self.hdd_labels.append(hdd_label)
            except psutil.Error as e:
                print(f"Error retrieving hard drive information: {e}")

    def update_running_processes(self):
        try:
            processes = psutil.process_iter()
            for widget in self.processes_layout.children():
                widget.deleteLater()
            for process in processes:
                process_label = QLabel(f"{process.pid}: {process.name()}")
                self.processes_layout.addWidget(process_label)
        except psutil.Error as e:
            print(f"Error retrieving running processes: {e}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    monitor_app = SystemMonitorApp()
    monitor_app.show()
    sys.exit(app.exec())

