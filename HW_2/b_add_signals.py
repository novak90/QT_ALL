import random

from PySide6 import QtWidgets, QtCore


class Window(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.initUi()
        self.initSignals()

    def initUi(self) -> None:
        """
        Инициализация интерфейса

        :return: None
        """

        # comboBox -----------------------------------------------------------
        self.comboBox = QtWidgets.QComboBox()
        self.comboBox.addItem("Элемент 1")
        self.comboBox.addItem("Элемент 2")
        self.comboBox.addItems(["Элемент 3", "Элемент 4", "Элемент 5"])
        self.comboBox.insertItem(0, "")

        self.pushButtonComboBox = QtWidgets.QPushButton("Получить данные")

        layoutComboBox = QtWidgets.QHBoxLayout()
        layoutComboBox.addWidget(self.comboBox)
        layoutComboBox.addWidget(self.pushButtonComboBox)

        # lineEdit -----------------------------------------------------------
        self.lineEdit = QtWidgets.QLineEdit()
        self.lineEdit.setPlaceholderText("Введите текст")

        self.pushButtonLineEdit = QtWidgets.QPushButton("Получить данные")

        layoutLineEdit = QtWidgets.QHBoxLayout()
        layoutLineEdit.addWidget(self.lineEdit)
        layoutLineEdit.addWidget(self.pushButtonLineEdit)

        # textEdit -----------------------------------------------------------
        self.textEdit = QtWidgets.QTextEdit()
        self.textEdit.setPlaceholderText("Введите текст")

        self.pushButtonTextEdit = QtWidgets.QPushButton("Получить данные")

        layoutTextEdit = QtWidgets.QHBoxLayout()
        layoutTextEdit.addWidget(self.textEdit)
        layoutTextEdit.addWidget(self.pushButtonTextEdit)

        # plainTextEdit ------------------------------------------------------
        self.plainTextEdit = QtWidgets.QPlainTextEdit()
        self.plainTextEdit.setPlaceholderText("Введите текст")

        self.pushButtonPlainTextEdit = QtWidgets.QPushButton("Получить данные")

        layoutPlainTextEdit = QtWidgets.QHBoxLayout()
        layoutPlainTextEdit.addWidget(self.plainTextEdit)
        layoutPlainTextEdit.addWidget(self.pushButtonPlainTextEdit)

        # spinBox ------------------------------------------------------------
        self.spinBox = QtWidgets.QSpinBox()
        self.spinBox.setValue(random.randint(-50, 50))

        self.pushButtonSpinBox = QtWidgets.QPushButton("Получить данные")

        layoutSpinBox = QtWidgets.QHBoxLayout()
        layoutSpinBox.addWidget(self.spinBox)
        layoutSpinBox.addWidget(self.pushButtonSpinBox)

        # doubleSpinBox ------------------------------------------------------
        self.doubleSpinBox = QtWidgets.QDoubleSpinBox()
        self.doubleSpinBox.setValue(random.randint(-50, 50))

        self.pushButtonDoubleSpinBox = QtWidgets.QPushButton("Получить данные")

        layoutDoubleSpinBox = QtWidgets.QHBoxLayout()
        layoutDoubleSpinBox.addWidget(self.doubleSpinBox)
        layoutDoubleSpinBox.addWidget(self.pushButtonDoubleSpinBox)

        # timeEdit -----------------------------------------------------------
        self.timeEdit = QtWidgets.QTimeEdit()
        self.timeEdit.setTime(QtCore.QTime.currentTime().addSecs(random.randint(-10000, 10000)))

        self.pushButtonTimeEdit = QtWidgets.QPushButton("Получить данные")

        layoutTimeEdit = QtWidgets.QHBoxLayout()
        layoutTimeEdit.addWidget(self.timeEdit)
        layoutTimeEdit.addWidget(self.pushButtonTimeEdit)

        # dateTimeEdit -------------------------------------------------------
        self.dateTimeEdit = QtWidgets.QDateTimeEdit()
        self.dateTimeEdit.setDateTime(QtCore.QDateTime.currentDateTime().addDays(random.randint(-10, 10)))

        self.pushButtonDateTimeEdit = QtWidgets.QPushButton("Получить данные")

        layoutDateTimeEdit = QtWidgets.QHBoxLayout()
        layoutDateTimeEdit.addWidget(self.dateTimeEdit)
        layoutDateTimeEdit.addWidget(self.pushButtonDateTimeEdit)

        # plainTextEditLog ---------------------------------------------------
        self.plainTextEditLog = QtWidgets.QPlainTextEdit()

        self.pushButtonClearLog = QtWidgets.QPushButton("Очистить лог")

        layoutLog = QtWidgets.QHBoxLayout()
        layoutLog.addWidget(self.plainTextEditLog)
        layoutLog.addWidget(self.pushButtonClearLog)

        # main layout

        layoutMain = QtWidgets.QVBoxLayout()
        layoutMain.addLayout(layoutComboBox)
        layoutMain.addLayout(layoutLineEdit)
        layoutMain.addLayout(layoutTextEdit)
        layoutMain.addLayout(layoutPlainTextEdit)
        layoutMain.addLayout(layoutSpinBox)
        layoutMain.addLayout(layoutDoubleSpinBox)
        layoutMain.addLayout(layoutTimeEdit)
        layoutMain.addLayout(layoutDateTimeEdit)
        layoutMain.addLayout(layoutLog)

        self.setLayout(layoutMain)

    def initSignals(self) -> None:
        """
        Инициализация сигналов

        :return: None
        """

        self.pushButtonComboBox.clicked.connect(self.onPushButtonComboBoxClicked)  # TODO подключить слот для вывода текста из comboBox в plainTextEditLog при нажатии на кнопку
        self.pushButtonLineEdit.clicked.connect(self.onPushButtonLineEditClicked)
        self.pushButtonTextEdit.clicked.connect(self.onPushButtonTextEditClicked) # TODO подключить слот для вывода текста из textEdit в plainTextEditLog при нажатии на кнопку
        self.pushButtonPlainTextEdit.clicked.connect(self.onPushButtonPlainTextEditClicked)  # TODO подключить слот для вывода текста из plaineTextEdit в plainTextEditLog при нажатии на кнопку
        self.pushButtonSpinBox.clicked.connect(self.onPushButtonSpinBoxClicked)  # TODO подключить слот для вывода значения из spinBox в plainTextEditLog при нажатии на кнопку
        self.pushButtonDoubleSpinBox.clicked.connect(self.onPushButtonDoubleSpinBoxClicked)  # TODO подключить слот для вывода значения из doubleSpinBox в plainTextEditLog при нажатии на кнопку
        self.pushButtonTimeEdit.clicked.connect(self.onPushButtonTimeEditClicked)  # TODO подключить слот для вывода времени из timeEdit в plainTextEditLog при нажатии на кнопку
        self.pushButtonDateTimeEdit.clicked.connect(self.onPushButtonDateTimeEditClicked)  # TODO подключить слот для вывода времени из dateTimeEdit в plainTextEditLog при нажатии на кнопку
        self.pushButtonClearLog.clicked.connect(self.plainTextEditLog.clear)  # TODO подключить слот для очистки plainTextEditLog при нажатии на кнопку

        self.comboBox.currentIndexChanged.connect(self.changeComboBox)  # TODO подключить слот для вывода текста в plainTextEditLog при изменении выбранного элемента в comboBox
        self.spinBox.valueChanged.connect(self.changeSpinBox)  # TODO подключить слот для вывода значения в plainTextEditLog при изменении значения в spinBox
        self.dateTimeEdit.dateTimeChanged.connect(self.changeDateTimeEdit)  # TODO подключить слот для вывода датывремени в plainTextEditLog при изменении датывремени в dateTimeEdit

    # slots --------------------------------------------------------------
    def onPushButtonComboBoxClicked(self) -> None:
        if self.comboBox.currentText() != "":
            self.plainTextEditLog.appendPlainText(self.comboBox.currentText())

    def onPushButtonLineEditClicked(self) -> None:
        if self.lineEdit.text() != "":
            self.plainTextEditLog.appendPlainText(self.lineEdit.text())

    def onPushButtonTextEditClicked(self) -> None:
        if self.textEdit.toPlainText() != "":
            self.plainTextEditLog.appendPlainText(self.textEdit.toPlainText())

    def onPushButtonPlainTextEditClicked(self) -> None:
        if self.plainTextEdit.toPlainText() != "":
            self.plainTextEditLog.appendPlainText(self.plainTextEdit.toPlainText())

    def onPushButtonSpinBoxClicked(self) -> None:
        self.plainTextEditLog.appendPlainText(self.spinBox.text())

    def onPushButtonDoubleSpinBoxClicked(self) -> None:
        self.plainTextEditLog.appendPlainText(self.doubleSpinBox.text())

    def onPushButtonTimeEditClicked(self) -> None:
        self.plainTextEditLog.appendPlainText(self.timeEdit.text())

    def onPushButtonDateTimeEditClicked(self) -> None:
        self.plainTextEditLog.appendPlainText(self.dateTimeEdit.text())

    def onPushButtonClearLogClicked(self) -> None:
        self.plainTextEditLog.setPlainText("")

    def changeComboBox(self) -> None:
        if self.comboBox.currentText() != "":
            self.plainTextEditLog.appendPlainText(self.comboBox.currentText())

    def changeSpinBox(self) -> None:
        self.plainTextEditLog.appendPlainText(self.spinBox.text())

    def changeDateTimeEdit(self) -> None:
        self.plainTextEditLog.appendPlainText(self.dateTimeEdit.text())


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()
