"""
Реализовать виджет, который будет работать с потоком SystemInfo из модуля a_threads

Создавать форму можно как в ручную, так и с помощью программы Designer

Форма должна содержать:
1. поле для ввода времени задержки
2. поле для вывода информации о загрузке CPU
3. поле для вывода информации о загрузке RAM
4. поток необходимо запускать сразу при старте приложения
5. установку времени задержки сделать "горячей", т.е. поток должен сразу
реагировать на изменение времени задержки
"""
import time

import psutil
import sys

from PySide6 import QtCore
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QSpinBox
from PySide6.QtCore import Qt, QThread, Signal, QTimer

from a_threads import SystemInfo


class SystemInfoWidget(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.progressBar = None
        self.timer = None
        self.threadSI = SystemInfo()
        self.threadSI.systemInfoReceived.connect(self.reportSystemInfo)
        self.initSignals()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("PC scanner")

        self.spinBoxDelaySI = QSpinBox()
        self.spinBoxDelaySI.setSuffix(' сек')
        self.spinBoxDelaySI.setMinimum(1)
        self.spinBoxDelaySI.valueChanged.connect(self.spinBoxDelaySIChanged)

        labelspinBoxDelaySI = QLabel("pause  load:")
        labelspinBoxDelaySI.setBuddy(self.spinBoxDelaySI)

        self.labelCPU = QLabel("<big><b style='color: red'>ЦП</b> <i style='color: green'>load on      %</i></big>")
        self.labelCPU.setAlignment(Qt.AlignCenter)

        self.labelRAM = QLabel("<big><b style='color: red'>ОЗУ</b> <i style='color: green'>load on      %</i></big>")
        self.labelRAM.setAlignment(Qt.AlignCenter)

        layout = QVBoxLayout()
        layout.addWidget(labelspinBoxDelaySI)
        layout.addWidget(self.spinBoxDelaySI)
        layout.addWidget(self.labelCPU)
        layout.addWidget(self.labelRAM)

        self.setLayout(layout)

        self.threadSI.start()


    def spinBoxDelaySIChanged(self, value):
        self.threadSI.delay = value

    def reportSystemInfo(self, data):
        def getColor(value):
            if value < 25.0:
                return 'red'
            elif 25.0 <= value < 50.0:
                return 'gold'
            elif 50.0 <= value < 75.0:
                return 'orange'
            else:
                return 'blue'

        colorCPU = getColor(data[0])
        colorRAM = getColor(data[1])
        self.labelCPU.setText(
            f"<big><b style='color: {colorCPU}'>ЦП</b> <i style='color: {colorCPU}'>загружен на {data[0]} %</i></big>"
        )
        self.labelRAM.setText(
            f"<big><b style='color: {colorRAM}'>ОЗУ</b> <i style='color: {colorRAM}'>загружено на {data[1]} %</i></big>"
        )

    def initSignals(self) -> None:
        """
        :return:
        """

        self.timer.timeout.connect(self.get_CPU_percent)
    def get_CPU_percent(self) -> None:
        """
        :return:
        """

        percent = psutil.cpu_percent()
        self.plainTextEdit.appendPlainText(f"{time.ctime()} >>> Загрузка CPU: {percent} %")
        self.progressBar.setValue(int(percent))

        if self.checkBoxLogEnable.isChecked():
            with open("cpu.log", "a") as f:
                f.write(f"{time.ctime()} >>> Загрузка CPU: {percent} %\n")

    def closeEvent(self, event):
        self.threadSI.status = False
        self.threadSI.wait()
        self.threadSI.deleteLater()
        super().closeEvent(event)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = SystemInfoWidget()
    window.show()

    sys.exit(app.exec())



"""from PySide6 import QtWidgets, QtCore, QtGui

from a_threads import SystemInfo

class SystemInfoWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.initThreads()
        self.initUi()
        self.initSignals()

    def initThreads(self) -> None:
        self.threadSystemInfo = SystemInfo()
        self.threadSystemInfo.status = True
        self.threadSystemInfo.start()

    def initUi(self):
        self.setWindowTitle("информвция о ПК")
        size = QtCore.QSize(300, 200)
        self.setFixedSize(size)

        #System load info------------------------------------------
        label_CPU = QtWidgets.QLabel()
        label_CPU.setText ("CPU load:")
        label_RAM = QtWidgets.QLabel()
        label_RAM.setText("RAM load:")


        self.plainTextEdit = QtWidgets.QPlainTextEdit()
        self.plainTextEdit.setReadOnly(True)
        self.checkBoxLogEnable = QtWidgets.QCheckBox("Записывать в файл")
        self.progressBar = QtWidgets.QProgressBar()

        layout = QtWidgets.QVBoxLayout()
        layout.CPU = QtWidgets.QHBoxLayout()
        layout.RAM = QtWidgets.QHBoxLayout()

        layout.addWidget(self.plainTextEdit)
        layout.addWidget(self.progressBar)
        layout.addWidget(self.checkBoxLogEnable)

        # Spinbox------------------------------------------
        labelSpinBox = QtWidgets.QLabel("Задержка обновления: ")
        self.spinBoxDelay = QtWidgets.QSpinBox()
        self.spinBoxDelay.setMinimum(1)

        self.lineEditRAM = QtWidgets.QLineEdit()
        self.lineEditRAM.setEnabled(False)"""

