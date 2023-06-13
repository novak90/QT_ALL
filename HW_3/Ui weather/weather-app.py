# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'weather-app.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import QCoreApplication, QMetaObject, QRect, QSize
from PySide6.QtGui import QFont
from PySide6.QtWidgets import (
    QFormLayout,
    QGroupBox,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QSpinBox,
    QVBoxLayout,
    QApplication,
    QMainWindow,
)


class Ui_FormwidgetWEather(object):
    def setupUi(self, FormwidgetWEather):
        if not FormwidgetWEather.objectName():
            FormwidgetWEather.setObjectName(u"FormwidgetWEather")
        FormwidgetWEather.resize(532, 569)
        self.groupBox = QGroupBox(FormwidgetWEather)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(40, 50, 161, 213))
        self.formLayout = QFormLayout(self.groupBox)
        self.formLayout.setObjectName(u"formLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(43, 20))

        self.verticalLayout_2.addWidget(self.label_5)

        self.lineEdit_2 = QLineEdit(self.groupBox)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setMinimumSize(QSize(133, 20))

        self.verticalLayout_2.addWidget(self.lineEdit_2)

        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(8)
        self.label.setFont(font)

        self.verticalLayout_2.addWidget(self.label)

        self.lineEdit = QLineEdit(self.groupBox)
        self.lineEdit.setObjectName(u"lineEdit")

        self.verticalLayout_2.addWidget(self.lineEdit)

        self.formLayout.setLayout(0, QFormLayout.LabelRole, self.verticalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(60, 50))

        self.horizontalLayout.addWidget(self.label_2)

        self.spinBox = QSpinBox(self.groupBox)
        self.spinBox.setObjectName(u"spinBox")

        self.horizontalLayout.addWidget(self.spinBox)

        self.formLayout.setLayout(1, QFormLayout.LabelRole, self.horizontalLayout)

        self.pushButton = QPushButton(self.groupBox)
        self.pushButton.setObjectName(u"Stop/Start info Weather")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.pushButton)

        self.retranslateUi(FormwidgetWEather)

        QMetaObject.connectSlotsByName(FormwidgetWEather)

    def retranslateUi(self, FormwidgetWEather):
        FormwidgetWEather.setWindowTitle(QCoreApplication.translate("FormwidgetWEather", u"Form", None))
        self.groupBox.setTitle(QCoreApplication.translate("FormwidgetWEather", u"Weather app", None))
        self.label_5.setText(QCoreApplication.translate("FormwidgetWEather", u"Longitude:", None))
        self.label.setText(QCoreApplication.translate("FormwidgetWEather", u"Latitude:", None))
        self.label_2.setText(QCoreApplication.translate("FormwidgetWEather", u"set delay():", None))
        self.pushButton.setText(QCoreApplication.translate("FormwidgetWEather", u"PushButton", None))


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.ui = Ui_FormwidgetWEather()
        self.ui.setupUi(self)


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
