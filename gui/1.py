# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '1.ui'
#
# Created by: PyQt4 UI code generator 4.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(470, 388)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(120, 350, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.widget = QtGui.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(0, 150, 224, 181))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.formLayout = QtGui.QFormLayout(self.widget)
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setMargin(0)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.xInput = QtGui.QLabel(self.widget)
        self.xInput.setObjectName(_fromUtf8("xInput"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.xInput)
        self.xLineEdit = QtGui.QLineEdit(self.widget)
        self.xLineEdit.setObjectName(_fromUtf8("xLineEdit"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.xLineEdit)
        self.zInput = QtGui.QLabel(self.widget)
        self.zInput.setObjectName(_fromUtf8("zInput"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.zInput)
        self.zLineEdit = QtGui.QLineEdit(self.widget)
        self.zLineEdit.setObjectName(_fromUtf8("zLineEdit"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.zLineEdit)
        self.yInput = QtGui.QLabel(self.widget)
        self.yInput.setObjectName(_fromUtf8("yInput"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.yInput)
        self.yLineEdit = QtGui.QLineEdit(self.widget)
        self.yLineEdit.setObjectName(_fromUtf8("yLineEdit"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.yLineEdit)
        self.label = QtGui.QLabel(self.widget)
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label)
        self.pushButton = QtGui.QPushButton(self.widget)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.LabelRole, self.pushButton)
        self.layoutWidget = QtGui.QWidget(Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(240, 150, 224, 181))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.formLayout_2 = QtGui.QFormLayout(self.layoutWidget)
        self.formLayout_2.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_2.setMargin(0)
        self.formLayout_2.setObjectName(_fromUtf8("formLayout_2"))
        self.label_2 = QtGui.QLabel(self.layoutWidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_2)
        self.label_pic = QtGui.QLabel(Dialog)
        self.label_pic.setGeometry(QtCore.QRect(0, 10, 461, 111))
        self.label_pic.setAutoFillBackground(True)
        self.label_pic.setStyleSheet(_fromUtf8(""))
        self.label_pic.setText(_fromUtf8(""))
        self.label_pic.setPixmap(QtGui.QPixmap(_fromUtf8("../../../../../Downloads/logo.png")))
        self.label_pic.setScaledContents(True)
        self.label_pic.setObjectName(_fromUtf8("label_pic"))

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.xInput.setText(_translate("Dialog", "x", None))
        self.zInput.setText(_translate("Dialog", "z", None))
        self.yInput.setText(_translate("Dialog", "y:", None))
        self.label.setText(_translate("Dialog", "Insert x,y,z co-ordinates", None))
        self.pushButton.setText(_translate("Dialog", "Go", None))
        self.label_2.setText(_translate("Dialog", "Upload G-code", None))

