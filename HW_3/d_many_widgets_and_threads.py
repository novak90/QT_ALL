"""
Реализовать окно, которое будет объединять в себе сразу два предыдущих виджета
"""
from PySide6 import QtWidgets, QtGui

from b_systeminfo_widget import SystemInfoWidget
from c_weatherapi_widget import GetInfoweather


class Window(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.initUi()

    def initUi(self) -> None:
        """
        Инициализация интерфейса
        :return: None
        """

        # window -------------------------------------------------------------
        self.setWindowTitle("setup")
        self.setMinimumSize(340, 360)
        self.setMaximumSize(340, 360)

        self.systemInfoWidget = SystemInfoWidget()
        self.weatherInfoWidget = WeatherInfoWidget()

        # layout -------------------------------------------------------------
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.systemInfoWidget)
        layout.addWidget(self.GetInfoweather)

        self.setLayout(layout)

    def closeEvent(self, event: QtGui.QCloseEvent) -> None:
        """
        Событие закрытия окна
        :param event: QtGui.QCloseEvent
        :return: None
        """

        self.systemInfoWidget.close()
        self.weatherInfoWidget.close()


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()