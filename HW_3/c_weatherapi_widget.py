"""
Реализовать виджет, который будет работать с потоком WeatherHandler из модуля a_threads

Создавать форму можно как в ручную, так и с помощью программы Designer

Форма должна содержать:
1. поле для ввода широты и долготы (после запуска потока они должны блокироваться)
2. поле для ввода времени задержки (после запуска потока оно должно блокироваться)
3. поле для вывода информации о погоде в указанных координатах
4. поток необходимо запускать и останавливать при нажатие на кнопку
"""


from PySide6 import QtWidgets, QtCore, QtGui
from a_threads import WeatherHandler

class GetWeatherWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.threadFlag = False

        self.initUi()
        self.initSignals()

    def initUi(self) -> None:
        self.setWindowTitle("WeatherHandler Widget")
        GetWeatherWindow = QtCore.QSize(400, 200)

        # Set delay layout --------------------------------------------------------------------------------------------
        self.labelSetDelay = QtWidgets.QLabel("Set delay:")

        self.spinBoxSetDelay = QtWidgets.QSpinBox()
        self.spinBoxSetDelay.setValue(1)

        setDelayLayout = QtWidgets.QHBoxLayout()
        setDelayLayout.addWidget(self.labelSetDelay)
        setDelayLayout.addWidget(self.spinBoxSetDelay)

        # coordinates layout ------------------------------------------------------------------------------------------
        self.labelLatitude = QtWidgets.QLabel("Latitude:")
        self.labelLongitude = QtWidgets.QLabel("Longitude:")

        self.lineEditLatitude = QtWidgets.QLineEdit()
        self.lineEditLatitude.setText('60')

        self.lineEditLongitude = QtWidgets.QLineEdit()
        self.lineEditLongitude.setText('40')

        coordinatesLayout = QtWidgets.QHBoxLayout()
        coordinatesLayout.addWidget(self.labelLatitude)
        coordinatesLayout.addWidget(self.lineEditLatitude)
        coordinatesLayout.addWidget(self.labelLongitude)
        coordinatesLayout.addWidget(self.lineEditLongitude)



        # Result button and text edit ---------------------------------------------------------------------------------
        self.resultTextEdit = QtWidgets.QTextEdit()
        self.resultTextEdit.setReadOnly(True)

        self.resultPushButton = QtWidgets.QPushButton("Start Get Weather")

        # Group box layout --------------------------------------------------------------------------------------------
        groupBoxLayout = QtWidgets.QVBoxLayout()
        groupBoxLayout.addLayout(coordinatesLayout)
        groupBoxLayout.addLayout(setDelayLayout)
        groupBoxLayout.addWidget(self.resultTextEdit)
        groupBoxLayout.addWidget(self.resultPushButton)

        self.groupBoxSystemInfo = QtWidgets.QGroupBox("Get Weather")
        self.groupBoxSystemInfo.setLayout(groupBoxLayout)

        self.setCentralWidget(self.groupBoxSystemInfo)  # Set the group box as the central widget



    def initSignals(self) -> None:
        self.resultPushButton.clicked.connect(self.onResultPushButtonClickedTread)

    def onResultPushButtonClickedTread(self) -> None:
        if self.lineEditLatitude.text().isdigit() and self.lineEditLongitude.text().isdigit():
            if not self.threadFlag:
                self.resultPushButton.setText("Stop info Weather")
                self.threadGetWeather = WeatherHandler(self.lineEditLatitude.text(), self.lineEditLongitude.text())
                self.threadGetWeather.delay = self.spinBoxSetDelay.value()
                self.threadGetWeather.status = True
                self.threadGetWeather.start()
                self.lineEditLatitude.setEnabled(False)
                self.lineEditLongitude.setEnabled(False)
                self.spinBoxSetDelay.setEnabled(False)
                self.threadGetWeather.weatherResponsed.connect(self.getWeather)
                self.threadFlag = True
            else:
                self.threadGetWeather.status = False
                self.threadGetWeather.finished.connect(self.threadGetWeather.deleteLater)
                self.lineEditLatitude.setEnabled(True)
                self.lineEditLongitude.setEnabled(True)
                self.spinBoxSetDelay.setEnabled(True)
                self.resultPushButton.setText("Start Get Weather")
                self.threadFlag = False
        else:
            self.resultTextEdit.setText("please input numbers")

    def getInfoWeather(self, data) -> None:
        self.resultTextEdit.setText(str(data))

    def StopEvent(self, event: QtGui.QCloseEvent) -> None:
        if self.threadFlag:
            self.threadGetWeather.status = False
            self.threadGetWeather.wait(deadline=(self.threadGetWeather.delay * 1000))
            self.threadGetWeather.finished.connect(self.threadGetWeather.deleteLater)


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = GetWeatherWindow()
    window.show()

    app.exec()






