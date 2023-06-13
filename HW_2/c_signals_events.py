"""
Реализация программу проверки состояния окна:
Форма для приложения (ui/c_signals_events.ui)

Программа должна обладать следующим функционалом:

1. Возможность перемещения окна по заданным координатам.
2. Возможность получения параметров экрана (вывод производить в plainTextEdit + добавлять время).
    * Кол-во экранов
    * Текущее основное окно
    * Разрешение экрана
    * На каком экране окно находится
    * Размеры окна
    * Минимальные размеры окна
    * Текущее положение (координаты) окна
    * Координаты центра приложения
    * Отслеживание состояния окна (свернуто/развёрнуто/активно/отображено)
3. Возможность отслеживания состояния окна (вывод производить в консоль + добавлять время).
    * При перемещении окна выводить его старую и новую позицию
    * При изменении размера окна выводить его новый размер"""

import sys
from datetime import datetime
from typing import Tuple
from PySide6.QtCore import QEvent, Qt
from PySide6 import QtWidgets, QtGui
from PySide6.QtGui import QMoveEvent, QResizeEvent, QHideEvent, QShowEvent

class Window(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Window manager")
        self.setGeometry(100, 100, 400, 300)

        self.timestamp = datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%fZ") + ":"

        self.initUi()
        self.initSignals()

    def initUi(self) -> None:

        """ инициализация окна"""
        self.spinBoxX = QtWidgets.QSpinBox(self)
        self.spinBoxX.setMinimumWidth(60)

        self.spinBoxY = QtWidgets.QSpinBox(self)
        self.spinBoxY.setMinimumWidth(60)

        layout = QtWidgets.QHBoxLayout()
        layout.addWidget(self.spinBoxX)
        layout.addWidget(self.spinBoxY)

        self.moveButtonLT = QtWidgets.QPushButton("LT")
        self.moveButtonRT = QtWidgets.QPushButton("RT")
        self.moveButtonCenter = QtWidgets.QPushButton("Center")
        self.moveButtonLB = QtWidgets.QPushButton("LB")
        self.moveButtonRB = QtWidgets.QPushButton("RB")
        self.moveButtonMoveCoords = QtWidgets.QPushButton("Move")
        self.moveButtonGetData = QtWidgets.QPushButton("Get Data")

        grid = QtWidgets.QGridLayout()
        grid.addWidget(self.moveButtonLT, 0, 0)
        grid.addWidget(self.moveButtonRT, 0, 1)
        grid.addWidget(self.moveButtonCenter, 0, 2)
        grid.addWidget(self.moveButtonLB, 1, 0)
        grid.addWidget(self.moveButtonRB, 1, 1)
        grid.addWidget(self.moveButtonMoveCoords, 1, 2)
        grid.addWidget(self.moveButtonGetData, 2, 0, 1, 3)

        self.plainTextEdit = QtWidgets.QPlainTextEdit(self)
        self.plainTextEdit.setReadOnly(True)

        mainLayout = QtWidgets.QVBoxLayout(self)
        mainLayout.addLayout(layout)
        mainLayout.addLayout(grid)
        mainLayout.addWidget(self.plainTextEdit)

        self.moveEventCount = 0
        self.resizeEventCount = 0

    def initSignals(self) -> None:
        self.moveButtonLT.clicked.connect(self.onPushButtonLT)
        self.moveButtonRT.clicked.connect(self.onPushButtonRT)
        self.moveButtonCenter.clicked.connect(self.onPushButtonCenter)
        self.moveButtonLB.clicked.connect(self.onPushButtonLB)
        self.moveButtonRB.clicked.connect(self.onPushButtonRB)
        self.moveButtonMoveCoords.clicked.connect(self.onPushButtonMoveCoordsClicked)
        self.moveButtonGetData.clicked.connect(self.onPushButtonGetDataClicked)

    """
    Обработка сигналов нажатия кнопок .

    :return: None
    """
    def onPushButtonLT(self) -> None:

        self.move(0, 0)

    def onPushButtonRT(self) -> None:
        screen_width, _ = self.screenResolution()
        window_width, _ = self.windowSize()

        x = screen_width - window_width
        y = 0

        self.move(x, y)

    def onPushButtonCenter(self) -> None:
        screen_width, screen_height = self.screenResolution()
        window_width, window_height = self.windowSize()

        x = int(screen_width / 2 - window_width / 2)
        y = int(screen_height / 2 - window_height / 2)

        self.move(x, y)

    def onPushButtonLB(self) -> None:
        _, screen_height = self.screenResolution()
        _, window_height = self.windowSize()

        x = 0
        y = screen_height - window_height

        self.move(x, y)

    def onPushButtonRB(self) -> None:
        screen_width, screen_height = self.screenResolution()
        window_width, window_height = self.windowSize()

        x = screen_width - window_width
        y = screen_height - window_height

        self.move(x, y)

    def onPushButtonMoveCoordsClicked(self) -> None:
        x = self.spinBoxX.value()
        y = self.spinBoxY.value()

        self.move(x, y)

    def onPushButtonGetDataClicked(self) -> None:
        log_list = [self.timestamp]

        screen_number = self.screenNumber()
        log_list.append(f"Количество экранов: {screen_number}")

        current_screen = self.currentScreen()
        log_list.append(f"Актуальный основной экран: {current_screen}")

        resolution_width, resolution_height = self.screenResolution()
        log_list.append(f"Разрешение экрана: {resolution_width} x {resolution_height}")

        log_list.append(f"Окно находится на экране: {self.windowOnWhichScreen()}")

        current_width, current_height = self.windowSize()
        log_list.append(f"Размеры окна: ширина - {current_width}, высота - {current_height}")

        min_width, min_height = self.minWindowSize()
        log_list.append(f"Минимальные размеры окна: ширина - {min_width}, высота - {min_height}")

        current_x, current_y = self.currentWindowPos()
        log_list.append(f"Актуальное положение (координаты) окна: ({current_x}, {current_y})")

        window_center_x, window_center_y = self.appCenterPos()
        log_list.append(f"Координаты центра приложения: ({window_center_x}, {window_center_x})")

        self.plainTextEdit.appendPlainText("\n".join(log_list))

    def screenNumber(self) -> int:
        """Определение количества экранов
        """

        return len(QtWidgets.QApplication.screens())

    """
        Determine the current primary screen.
        :return: str
        """
    def currentScreen(self) -> str:
        return QtWidgets.QApplication.primaryScreen().name()

    def screenResolution(self) -> Tuple[int, int]:
        """
        Определение разрешения экрана в пикселях.

        :return: Tuple[int, int]
        """
        width = self.screen().size().width()
        height = self.screen().size().height()
        return width, height

    """
    Определите экран, на котором расположено окно.
    :return: str
    
    """

    def windowOnWhichScreen(self) -> str:
        return self.screen().name()

    """
       Определение размера экрана
       :return: str

       """
    def windowSize(self) -> Tuple[int, int]:
        width = self.size().width()
        height = self.size().height()
        return width, height

    def minWindowSize(self) -> Tuple[int, int]:
        min_width = self.minimumSize().width()
        min_height = self.minimumSize().height()
        return min_width, min_height


    def currentWindowPos(self) -> Tuple[int, int]:
        x = self.pos().x()
        y = self.pos().y()
        return x, y

    def appCenterPos(self) -> Tuple[int, int]:
        window_cur_x, window_cur_y = self.currentWindowPos()
        window_cur_width, window_cur_height = self.windowSize()

        center_x = int(window_cur_x + window_cur_width / 2)
        center_y = int(window_cur_y + window_cur_height / 2)

        return center_x, center_y

    """
             Определить координаты центра приложения.

             :return: Кортеж[int, int]
             """
    def event(self, event: QtGui.QKeyEvent) -> bool:
        if event.type() == QEvent.WindowActivate:
            print(f"{self.timestamp} Окно активно")
        elif event.type() == QEvent.WindowDeactivate:
            print(f"{self.timestamp} Окно неактивно")
        return super().event(event)

    """ Переопределение метода event() для обработки событий окна."""


    def moveEvent(self, event: QtGui.QMoveEvent) -> None:
        old_x, old_y = event.oldPos().x(), event.oldPos().y()
        new_x, new_y = event.pos().x(), event.pos().y()

        print(f"{self.timestamp} Прежние координаты окна {old_x, old_y}, текущие координаты окна {new_x, new_y}")

    def resizeEvent(self, event: QtGui.QResizeEvent) -> None:
        new_width, new_height = event.size().width(), event.size().height()

        print(f"{self.timestamp} Новый размер окна {new_width, new_height}")

    def hideEvent(self, event: QtGui.QHideEvent) -> None:
        print(f"{self.timestamp} Окно  свернуто")

    def showEvent(self, event: QtGui.QShowEvent) -> None:
        print(f"{self.timestamp} Окно  развернуто")


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()






