from PySide6 import QtWidgets, QtCore




class Window(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)


        self.initUi()

    def initUi(self) -> None:

        """
        Инициализация интерфейса

        :return: None
        """

        LabelLogin = QtWidgets.QLabel("Логин")
        LabelLogin.setMinimumSize(90, 0)  #TODO Создайте виджет QLabel с текстом "Логин"

        LabelPassword = QtWidgets.QLabel()
        LabelPassword.setMinimumSize(90, 0)
        LabelPassword.setText("Пароль")


        self.pushButtonRegistartion = QtWidgets.QPushButton()
        self.pushButtonRegistartion.setText("Регистрация") # TODO Создайте виджет QLabel с текстом "Регистрация"

        self.LineEditLogin = QtWidgets.QLineEdit()  # TODO создайте виджет QLineEdit
        self.LineEditLogin.setPlaceholderText("Введите логин")  # TODO добавьте placeholderText "Введите логин" с помощью метода .setPlaceholderText()

        self.LineEditPassword = QtWidgets.QLineEdit()   # TODO создайте виджет QLineEdit
        self.LineEditPassword.setPlaceholderText("Введите пароль")  # TODO добавьте placeholderText "Введите пароль"
        self.LineEditPassword.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password) # TODO установите ограничение видимости вводимых знаков с помощью метода .setEchoMode()

        self.pushButtonLogin = QtWidgets.QPushButton()  # TODO создайте виджет QPushButton
        self.pushButtonLogin.setText("Войти")  # TODO установите текст "Войти" с помощью метода setText()

        self.pushButtonRegistration = QtWidgets.QPushButton() # TODO создайте виджет QPushButton
        self.pushButtonRegistration.setText("Регистрация")  # TODO установите текст "Регистрация" с помощью метода setText()

        LayoutLogin = QtWidgets.QHBoxLayout()# TODO Создайте QHBoxLayout
        LayoutLogin.addWidget(LabelLogin)
        LayoutLogin.addWidget(self.LineEditLogin)        # TODO с помощью метода .addWidget() добавьте self.lineEditLogin

        LayoutPassword = QtWidgets.QHBoxLayout()
        LayoutPassword.addWidget(LabelPassword)
        LayoutPassword.addWidget(self.LineEditPassword)

        LayoutPassword = QtWidgets.QHBoxLayout()  # TODO Создайте QHBoxLayout
        LayoutPassword.addWidget(self.LineEditPassword)  # TODO с помощью метода .addWidget() добавьте labelRegistration
        LayoutPassword.addWidget(self.LineEditPassword)  # TODO с помощью метода .addWidget() добавьте self.lineEditPassword

        LayoutButtons = QtWidgets.QHBoxLayout()  # TODO Создайте QHBoxLayout
        LayoutButtons.addWidget(self.pushButtonLogin) # TODO с помощью метода .addWidget() добавьте self.pushButtonLogin
        LayoutButtons.addWidget(self.pushButtonRegistartion)  # TODO с помощью метода .addWidget() добавьте self.pushButtonRegistration

        LayoutMain = QtWidgets.QHBoxLayout()  # TODO Создайте QVBoxLayout
        LayoutMain.addLayout(LayoutLogin)  # TODO с помощью метода .addLayout() добавьте layoutLogin
        LayoutMain.addLayout(LayoutPassword) # TODO с помощью метода .addLayout() добавьте layoutPassword
        LayoutMain.addLayout(LayoutButtons) # TODO с помощью метода .addLayout() добавьте layoutButtons


        self.setLayout(LayoutMain)  # TODO с помощью метода setLayout установите layoutMain на основной виджет


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()
