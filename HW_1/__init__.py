from PySide6 import QtWidgets, QtCore


class MyFirstTITLE(QtWidgets.QWidget):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.initUi()

    def initUi(self) -> None:
        """ доинициализация"""
        self.setWindowTitle("Вход в приложение")
        size = QtCore.QSize(500, 500)
        self.setFixedSize(size)

        label_Login = QtWidgets.QLabel()
        label_Login.setText("Логин")

        label_Password = QtWidgets.QLabel()
        label_Password.setText("Пароль")

        self.LineEdithLogin = QtWidgets.QLineEdit()
        self.LineEdithPassword = QtWidgets.QLineEdit()

        self.pushButtonregistartion = QtWidgets.QPushButton()
        self.pushButtonregistartion.setText("Регистрация")

        self.pushButtonOK = QtWidgets.QPushButton()
        self.pushButtonOK.setText("OK")

        self.pushButtonCancel = QtWidgets.QPushButton()
        self.pushButtonCancel.setText("Отмена")

        # Layouts
        LayoutLogin = QtWidgets.QHBoxLayout()

        LayoutLogin.addWidget(label_Login)
        LayoutLogin.addWidget(self.LineEdithLogin)
        LayoutPassword = QtWidgets.QHBoxLayout()
        LayoutPassword.addWidget(label_Password)
        LayoutPassword.addWidget(self.LineEdithPassword)
        LayoutRegistration = QtWidgets.QHBoxLayout()
        LayoutRegistration.addSpacerItem(
            QtWidgets.QSpacerItem(
                20, 10, QtWidgets.QSizePolicy.Policy.Expanding)
        )
        LayoutRegistration.addWidget(self.pushButtonregistartion)

        LayoutHandle = QtWidgets.QHBoxLayout()
        LayoutHandle.addSpacerItem(
            QtWidgets.QSpacerItem(
                20, 10, QtWidgets.QSizePolicy.Policy.Expanding)
        )
        LayoutHandle.addWidget(self.pushButtonOK)

        LayoutMain = QtWidgets.QHBoxLayout()
        LayoutMain.addLayout(LayoutLogin)
        LayoutMain.addLayout(LayoutPassword)
        LayoutMain.addLayout(LayoutRegistration)
        LayoutMain.addLayout(LayoutHandle)

        self.setLayout(LayoutMain)

        # self.resize(200,100)
        # self.resize(QtCore.QSize(300,100))

if __name__ == '__main__':
 app = QtWidgets.QApplication()

 win = MyFirstTITLE()
 win.show()

app.exec()
