#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt4 UI code generator 4.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import back
import serialCom_v2 as sc
import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d as plt3d
from mpl_toolkits.mplot3d import Axes3D
import time
from PIL.ImageQt import ImageQt
from PIL import Image
import math
import numpy as np
import csv


option =2
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


class Ui_MainWindow(object):
	def resizeEvent(self, event):
		print("resize")
		
	def setupUi(self, MainWindow):
		ui.closeEvent = self.closeEvent
		app.aboutToQuit.connect(self.closeEvent)
		self.filename = ''
		self.MAX_Z = 0.7
		self.MIN_Z = 0
		self.MAX_X = 0.98
		self.MIN_X = 0
		self.MAX_Y = 0.98
		self.MIN_Y = 0
		self.fixed = False
		self.mode = None
		self.realRobot = True
		self.jog_event = None
		self.responses = []
		self.currents = []
		self.wait_variable = False

		MainWindow.setObjectName(_fromUtf8("MainWindow"))
		MainWindow.resize(800, 900)
		print(MainWindow.width())
		self.magnet = 0
		self.stop_cmd = [
		'0 m 0 1;',
		'1 m 0 1;',
		'2 m 0 1;',
		'3 m 0 1;']
		if self.realRobot==True:
			self.tivaSerial = sc.SerialCOm('/dev/ttyUSB0')
		MainWindow.setStyleSheet("background-color: purple;")

		self.centralwidget = QtGui.QWidget(MainWindow)
		self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
		self.label_pic = QtGui.QLabel(self.centralwidget)
		self.label_pic.setGeometry(QtCore.QRect(0, 0, MainWindow.width(), MainWindow.height()/4))
		self.label_pic.setAutoFillBackground(True)
		self.label_pic.setStyleSheet(_fromUtf8(""))
		self.label_pic.setText(_fromUtf8(""))
		self.label_pic.setPixmap(QtGui.QPixmap(_fromUtf8("Logo.png")))
		self.label_pic.setScaledContents(True)
		self.label_pic.setObjectName(_fromUtf8("label_pic"))

		self.comboBox = QtGui.QComboBox(self.centralwidget)
		self.comboBox.addItem("Select method")
		self.comboBox.addItem("Single points")
		self.comboBox.addItem("CSV points")
		self.comboBox.addItem("Homing")
		self.comboBox.move(0, 250)
		self.comboBox.activated[str].connect(self.style_choice)

		self.pushButton = QtGui.QPushButton(self.centralwidget)
		self.pushButton.setGeometry(QtCore.QRect(0, 400, 121, 71))
		self.pushButton.setObjectName(_fromUtf8("pushButton"))
		self.pushButton.clicked.connect(self.btnstate)
		self.pushButton.setStyleSheet("color: White;")

		self.pushButton2 = QtGui.QPushButton(self.centralwidget)
		self.pushButton2.setGeometry(QtCore.QRect(150, 400, 121, 71))
		self.pushButton2.setObjectName(_fromUtf8("pushButton2"))
		self.pushButton2.clicked.connect(self.picktoggle)
		self.pushButton2.setStyleSheet("color: White;")
		self.pushButton2.setCheckable(True)

		self.pushButton3 = QtGui.QPushButton(self.centralwidget)
		self.pushButton3.setGeometry(QtCore.QRect(300, 400, 121, 71))
		self.pushButton3.setObjectName(_fromUtf8("pushButton3"))
		self.pushButton3.clicked.connect(self.homesave)
		self.pushButton3.setStyleSheet("color: White;")

		self.pushButton4 = QtGui.QPushButton(self.centralwidget)
		self.pushButton4.setGeometry(QtCore.QRect(450, 400, 121, 71))
		self.pushButton4.setObjectName(_fromUtf8("pushButton4"))
		self.pushButton4.clicked.connect(self.homego)
		self.pushButton4.setStyleSheet("color: White;")

		self.label_pic_2 = QtGui.QLabel(self.centralwidget)
		self.label_pic_2.setGeometry(QtCore.QRect(0, 490, 581, 291))
		self.label_pic_2.setAutoFillBackground(True)
		self.label_pic_2.setStyleSheet(_fromUtf8(""))
		self.label_pic_2.setText(_fromUtf8(""))
		self.label_pic_2.setPixmap(QtGui.QPixmap())
		self.label_pic_2.setScaledContents(True)
		self.label_pic_2.setObjectName(_fromUtf8("label_pic_2"))
		self.layoutWidget = QtGui.QWidget(self.centralwidget)
		self.layoutWidget.setGeometry(QtCore.QRect(0, 750, MainWindow.width(), 100))
		self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
		self.horizontalLayout = QtGui.QHBoxLayout(self.layoutWidget)
		self.horizontalLayout.setMargin(0)
		self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
		self.ESTOP_2 = QtGui.QPushButton(self.layoutWidget)
		self.ESTOP_2.setStyleSheet("color: White;")
		palette = QtGui.QPalette()
		brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
		brush.setStyle(QtCore.Qt.SolidPattern)
		palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
		brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
		brush.setStyle(QtCore.Qt.SolidPattern)
		palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
		brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
		brush.setStyle(QtCore.Qt.SolidPattern)
		palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
		brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
		brush.setStyle(QtCore.Qt.SolidPattern)
		palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
		brush = QtGui.QBrush(QtGui.QColor(159, 158, 158))
		brush.setStyle(QtCore.Qt.SolidPattern)
		palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
		brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
		brush.setStyle(QtCore.Qt.SolidPattern)
		palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
		self.ESTOP_2.setPalette(palette)
		self.ESTOP_2.setObjectName(_fromUtf8("ESTOP_2"))
		self.ESTOP_2.clicked.connect(self.Run)
		self.horizontalLayout.addWidget(self.ESTOP_2)
		self.ESTOP_3 = QtGui.QPushButton(self.layoutWidget)
		self.ESTOP_3.setStyleSheet("color: White;")

		palette = QtGui.QPalette()
		brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
		brush.setStyle(QtCore.Qt.SolidPattern)
		palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
		brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
		brush.setStyle(QtCore.Qt.SolidPattern)
		palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
		brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
		brush.setStyle(QtCore.Qt.SolidPattern)
		palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
		brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
		brush.setStyle(QtCore.Qt.SolidPattern)
		palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
		brush = QtGui.QBrush(QtGui.QColor(159, 158, 158))
		brush.setStyle(QtCore.Qt.SolidPattern)
		palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
		brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
		brush.setStyle(QtCore.Qt.SolidPattern)
		palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
		self.ESTOP_3.setPalette(palette)
		self.ESTOP_3.setObjectName(_fromUtf8("ESTOP_3"))
		self.ESTOP_3.clicked.connect(self.pause)
		self.ESTOP_3.setCheckable(True)
		self.horizontalLayout.addWidget(self.ESTOP_3)
		self.ESTOP = QtGui.QPushButton(self.layoutWidget)
		self.ESTOP.setStyleSheet("color: White;")

		palette = QtGui.QPalette()
		brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
		brush.setStyle(QtCore.Qt.SolidPattern)
		palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
		brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
		brush.setStyle(QtCore.Qt.SolidPattern)
		palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
		brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
		brush.setStyle(QtCore.Qt.SolidPattern)
		palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
		brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
		brush.setStyle(QtCore.Qt.SolidPattern)
		palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
		brush = QtGui.QBrush(QtGui.QColor(200, 0, 0))
		brush.setStyle(QtCore.Qt.SolidPattern)
		palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
		brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
		brush.setStyle(QtCore.Qt.SolidPattern)
		palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
		self.ESTOP.setPalette(palette)
		self.ESTOP.setObjectName(_fromUtf8("ESTOP"))
		self.ESTOP.clicked.connect(self.STOP)

		self.horizontalLayout.addWidget(self.ESTOP)

		self.splitter = QtGui.QSplitter(self.centralwidget)
		self.splitter.setGeometry(QtCore.QRect(0, 280, MainWindow.width(), 100))
		self.splitter.setOrientation(QtCore.Qt.Horizontal)
		self.splitter.setObjectName(_fromUtf8("splitter"))

		self.layoutWidget1 = QtGui.QWidget(self.splitter)
		self.layoutWidget1.setObjectName(_fromUtf8("layoutWidget1"))
		self.layoutWidget1.setHidden(True)
		self.formLayout = QtGui.QFormLayout(self.layoutWidget1)
		self.layoutWidget1.setStyleSheet("color: White;")
		self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
		self.formLayout.setMargin(0)
		self.formLayout.setObjectName(_fromUtf8("formLayout"))
		self.label = QtGui.QLabel(self.layoutWidget1)
		self.label.setObjectName(_fromUtf8("label"))
		self.label.setStyleSheet("color: White;")
		self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label)
		self.xInput = QtGui.QLabel(self.layoutWidget1)
		self.xInput.setObjectName(_fromUtf8("xInput"))
		self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.xInput)
		self.xLineEdit = QtGui.QLineEdit(self.layoutWidget1)
		self.xLineEdit.setObjectName(_fromUtf8("xLineEdit"))
		self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.xLineEdit)
		self.yInput = QtGui.QLabel(self.layoutWidget1)
		self.yInput.setObjectName(_fromUtf8("yInput"))
		self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.yInput)
		self.yLineEdit = QtGui.QLineEdit(self.layoutWidget1)
		self.yLineEdit.setObjectName(_fromUtf8("yLineEdit"))
		self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.yLineEdit)
		self.zInput = QtGui.QLabel(self.layoutWidget1)
		self.zInput.setObjectName(_fromUtf8("zInput"))
		self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.zInput)
		self.zLineEdit = QtGui.QLineEdit(self.layoutWidget1)
		self.zLineEdit.setObjectName(_fromUtf8("zLineEdit"))

		self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.zLineEdit)
		self.layoutWidget_2 = QtGui.QWidget(self.splitter)
		self.layoutWidget_2.setObjectName(_fromUtf8("layoutWidget_2"))
		self.layoutWidget_2.setHidden(True)
		self.formLayout_2 = QtGui.QFormLayout(self.layoutWidget_2)
		self.formLayout_2.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
		self.formLayout_2.setMargin(0)
		self.formLayout_2.setObjectName(_fromUtf8("formLayout_2"))

		self.label_3 = QtGui.QLabel(self.layoutWidget_2)
		self.label_3.setObjectName(_fromUtf8("label_3"))
		self.label_3.setStyleSheet("color: White;")
		self.formLayout_2.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_3)

		self.upButton = QtGui.QPushButton(self.layoutWidget_2)
		self.upButton.setGeometry(QtCore.QRect(450, 200, 121, 71))
		self.upButton.setObjectName(_fromUtf8("upButton"))
		self.upButton.clicked.connect(self.open)
		self.upButton.setStyleSheet("color: White;")
		self.formLayout_2.setWidget(0, QtGui.QFormLayout.LabelRole, self.upButton)

		self.layoutWidget_3 = QtGui.QWidget(self.splitter)
		self.layoutWidget_3.setObjectName(_fromUtf8("layoutWidget_2"))
		self.layoutWidget_3.setHidden(True)
		self.formLayout_3  = QtGui.QGridLayout(self.layoutWidget_3)

		self.formLayout_3.setObjectName(_fromUtf8("formLayout_3"))

		self.Home1 = QtGui.QPushButton(self.layoutWidget_3)
		self.Home1.setStyleSheet("color: White;")
		self.Home1.setPalette(palette)
		self.Home1.setObjectName(_fromUtf8("Home1"))
		self.Home1.clicked.connect(self.startHome)
		self.formLayout_3.addWidget(self.Home1, 0, 0, 1, 2)

		self.Home2 = QtGui.QPushButton(self.layoutWidget_3)
		self.Home2.setStyleSheet("color: White;")
		self.Home2.setPalette(palette)
		self.Home2.setObjectName(_fromUtf8("Home2"))
		self.Home2.clicked.connect(self.completeHome)
		self.formLayout_3.addWidget(self.Home2, 0, 2, 1, 2)

		self.motor_0 = QtGui.QLabel(self.layoutWidget_3)
		self.motor_0.setObjectName(_fromUtf8("motor_0"))
		self.motor_0.setStyleSheet("color: White;")
		self.formLayout_3.addWidget(self.motor_0, 1, 0)

		self.Motor0_up = QtGui.QToolButton(self.layoutWidget_3)
		self.Motor0_up.setStyleSheet("color: White;")
		self.Motor0_up.setPalette(palette)
		self.Motor0_up.setObjectName(_fromUtf8("Motor0_up"))
		self.Motor0_up.pressed.connect(self.motor0_jog_up)
		self.Motor0_up.setArrowType(Qt.UpArrow)
		self.Motor0_up.setIconSize(QSize(100, 100))
		self.formLayout_3.addWidget(self.Motor0_up, 2, 0)

		self.Motor0_down = QtGui.QToolButton(self.layoutWidget_3)
		self.Motor0_down.setStyleSheet("color: White;")
		self.Motor0_down.setPalette(palette)
		self.Motor0_down.setObjectName(_fromUtf8("Motor0_down"))
		self.Motor0_down.clicked.connect(self.motor0_jog_down)
		self.Motor0_down.setArrowType(Qt.DownArrow)
		self.Motor0_down.setIconSize(QSize(100, 100))
		self.formLayout_3.addWidget(self.Motor0_down, 3, 0)

		self.motor_1 = QtGui.QLabel(self.layoutWidget_3)
		self.motor_1.setObjectName(_fromUtf8("motor_1"))
		self.motor_1.setStyleSheet("color: White;")
		self.formLayout_3.addWidget(self.motor_1, 1, 1)

		self.Motor1_up = QtGui.QToolButton(self.layoutWidget_3)
		self.Motor1_up.setStyleSheet("color: White;")
		self.Motor1_up.setPalette(palette)
		self.Motor1_up.setObjectName(_fromUtf8("Motor1_up"))
		self.Motor1_up.clicked.connect(self.motor1_jog_up)
		self.Motor1_up.setArrowType(Qt.UpArrow)
		self.Motor1_up.setIconSize(QSize(100, 100))
		self.formLayout_3.addWidget(self.Motor1_up, 2, 1)

		self.Motor1_down = QtGui.QToolButton(self.layoutWidget_3)
		self.Motor1_down.setStyleSheet("color: White;")
		self.Motor1_down.setPalette(palette)
		self.Motor1_down.setObjectName(_fromUtf8("Motor1_down"))
		self.Motor1_down.clicked.connect(self.motor1_jog_down)
		self.Motor1_down.setArrowType(Qt.DownArrow)
		self.Motor1_down.setIconSize(QSize(100, 100))
		self.formLayout_3.addWidget(self.Motor1_down, 3, 1)

		self.motor_2 = QtGui.QLabel(self.layoutWidget_3)
		self.motor_2.setObjectName(_fromUtf8("motor_2"))
		self.motor_2.setStyleSheet("color: White;")
		self.formLayout_3.addWidget(self.motor_2, 1, 2)

		self.Motor2_up = QtGui.QToolButton(self.layoutWidget_3)
		self.Motor2_up.setStyleSheet("color: White;")
		self.Motor2_up.setPalette(palette)
		self.Motor2_up.setObjectName(_fromUtf8("Motor2_up"))
		self.Motor2_up.clicked.connect(self.motor2_jog_up)
		self.Motor2_up.setArrowType(Qt.UpArrow)
		self.Motor2_up.setIconSize(QSize(100, 100))
		self.formLayout_3.addWidget(self.Motor2_up, 2, 2)

		self.Motor2_down = QtGui.QToolButton(self.layoutWidget_3)
		self.Motor2_down.setStyleSheet("color: White;")
		self.Motor2_down.setPalette(palette)
		self.Motor2_down.setObjectName(_fromUtf8("Motor2_down"))
		self.Motor2_down.clicked.connect(self.motor2_jog_down)
		self.Motor2_down.setArrowType(Qt.DownArrow)
		self.Motor2_down.setIconSize(QSize(100, 100))
		self.formLayout_3.addWidget(self.Motor2_down, 3, 2)

		self.motor_3 = QtGui.QLabel(self.layoutWidget_3)
		self.motor_3.setObjectName(_fromUtf8("motor_3"))
		self.motor_3.setStyleSheet("color: White;")
		self.formLayout_3.addWidget(self.motor_3, 1, 3)

		self.Motor3_up = QtGui.QToolButton(self.layoutWidget_3)
		self.Motor3_up.setStyleSheet("color: White;")
		self.Motor3_up.setPalette(palette)
		self.Motor3_up.setObjectName(_fromUtf8("Motor3_up"))
		self.Motor3_up.clicked.connect(self.motor3_jog_up)
		self.Motor3_up.setArrowType(Qt.UpArrow)
		self.Motor3_up.setIconSize(QSize(100, 100))
		self.formLayout_3.addWidget(self.Motor3_up, 2, 3)

		self.Motor3_down = QtGui.QToolButton(self.layoutWidget_3)
		self.Motor3_down.setStyleSheet("color: White;")
		self.Motor3_down.setPalette(palette)
		self.Motor3_down.setObjectName(_fromUtf8("Motor3_down"))
		self.Motor3_down.clicked.connect(self.motor3_jog_down)
		self.Motor3_down.setArrowType(Qt.DownArrow)
		self.Motor3_down.setIconSize(QSize(100, 100))
		self.formLayout_3.addWidget(self.Motor3_down, 3, 3)

		# self.label_2 = QtGui.QLabel(self.layoutWidget_2)
		# self.label_2.setObjectName(_fromUtf8("label_2"))
		# self.label_2.setStyleSheet("color: White;")
		# self.formLayout_2.setWidget(5, QtGui.QFormLayout.LabelRole, self.label_2)


		MainWindow.setCentralWidget(self.centralwidget)
		self.menubar = QtGui.QMenuBar(MainWindow)
		self.menubar.setGeometry(QtCore.QRect(0, 0, 580, 25))
		self.menubar.setObjectName(_fromUtf8("menubar"))
		MainWindow.setMenuBar(self.menubar)
		self.statusbar = QtGui.QStatusBar(MainWindow)
		self.statusbar.setObjectName(_fromUtf8("statusbar"))
		MainWindow.setStatusBar(self.statusbar)



		self.retranslateUi(MainWindow)
		QtCore.QMetaObject.connectSlotsByName(MainWindow)

	def closeEvent(self):
		print("User has clicked the red x on the main window")
		
	def STOP(self):
		if self.realRobot==True:
			self.tivaSerial.writeDataPack(self.stop_cmd)
		print("Stopped")
		sys.exit()

	def pause(self):
		self.wait_variable = not self.wait_variable
		print(self.wait_variable)

	def Run(self):
		self.realRobot = True
		self.btnstate()

	def Check(self):
		self.realRobot = True
		self.btnstate()


	def retranslateUi(self, MainWindow):
		MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
		self.pushButton.setText(_translate("MainWindow", "Check trajectory", None))
		self.pushButton2.setText(_translate("MainWindow", "Pick", None))
		self.pushButton3.setText(_translate("MainWindow", "Home save", None))
		self.pushButton4.setText(_translate("MainWindow", "Home go", None))
		self.upButton.setText(_translate("MainWindow", "Upload CSV", None))
		self.ESTOP_2.setText(_translate("MainWindow", "Run", None))
		self.ESTOP_3.setText(_translate("MainWindow", "Pause", None))
		self.ESTOP.setText(_translate("MainWindow", "STOP", None))
		self.Home1.setText(_translate("MainWindow", "Save currents", None))
		self.Home2.setText(_translate("MainWindow", "Start Home", None))
		self.label.setText(_translate("MainWindow", "Insert x,y,z co-ordinates", None))
		self.xInput.setText(_translate("MainWindow", "x", None))
		self.yInput.setText(_translate("MainWindow", "y", None))
		self.zInput.setText(_translate("MainWindow", "z:", None))
		# self.label_2.setText(_translate("MainWindow", "lengths:"+str(dcb.length_list), None))
		self.label_3.setText(_translate("MainWindow", "filepath:"+str(self.filename), None))

		self.motor_0.setText(_translate("MainWindow", "Motor 0", None))
		self.motor_1.setText(_translate("MainWindow", "Motor 1", None))
		self.motor_2.setText(_translate("MainWindow", "Motor 2", None))
		self.motor_3.setText(_translate("MainWindow", "Motor 3", None))

		self.Motor0_up.setText(_translate("MainWindow", "0 up", None))
		self.Motor1_up.setText(_translate("MainWindow", "1 up", None))
		self.Motor2_up.setText(_translate("MainWindow", "2 up", None))
		self.Motor3_up.setText(_translate("MainWindow", "3 up", None))

		self.Motor0_down.setText(_translate("MainWindow", "0 down", None))
		self.Motor1_down.setText(_translate("MainWindow", "1 down", None))
		self.Motor2_down.setText(_translate("MainWindow", "2 down", None))
		self.Motor3_down.setText(_translate("MainWindow", "3 down", None))

	def homesave(self):
		curr_cmds = [['5 e SP0;']]
		if self.realRobot==True:
			self.tivaSerial.writeDataPack(curr_cmds[0])
			print("saved")

	def homego(self):
		curr_cmds = [['5 e FP0;']]
		if self.realRobot==True:
			self.tivaSerial.writeDataPack(curr_cmds[0])
			print("Gone")

	def startHome(self):
		self.currents = []
		curr_cmds = [['5 e 0IQ;'],['5 e 1IQ;'],['5 e 2IQ;'],['5 e 3IQ;']]
		if self.realRobot==True:
			for i in range(len(curr_cmds)):
				self.currents.append(self.tivaSerial.writeDataPack2(curr_cmds[i]))
			print("Currents saved")
			print(self.currents)
			try:
				for i in range(len(self.currents)):
					self.currents[i] = float((str(self.currents[i]).split("=")[1]).split("""\r""")[0])
				print(self.currents)
			except:
				try:
					for i in range(len(self.currents)):
						self.currents[i] = float((str(self.currents[i]).split("=")[1]).split("""\r""")[0])
					print(self.currents)
				except:
					print("read failed")



	def motor0_jog_up(self):
		# self.jog_event = 0
		# self.timer.start(100)
		jog_cmd = [
		'0 m 10000 0;',
		'1 m 0 1;',
		'2 m 0 1;',
		'3 m 0 1;']
		if self.realRobot==True:
			self.tivaSerial.writeDataPack(jog_cmd)
			self.tivaSerial.writeDataPack(self.stop_cmd)
		print("Jogging")
		

	def motor0_jog_down(self):
		jog_cmd = [
		'0 m 10000 1;',
		'1 m 0 1;',
		'2 m 0 1;',
		'3 m 0 1;']
		if self.realRobot==True:
			self.tivaSerial.writeDataPack(jog_cmd)
			self.tivaSerial.writeDataPack(self.stop_cmd)

	def motor1_jog_up(self):
		jog_cmd = [
		'0 m 0 1;',
		'1 m 10000 0;',
		'2 m 0 1;',
		'3 m 0 1;']
		if self.realRobot==True:
			self.tivaSerial.writeDataPack(jog_cmd)
			self.tivaSerial.writeDataPack(self.stop_cmd)

	def motor1_jog_down(self):
		jog_cmd = [
		'0 m 0 1;',
		'1 m 10000 1;',
		'2 m 0 1;',
		'3 m 0 1;',
		'4 e '+str(int(self.magnet))+' 1;']
		if self.realRobot==True:
			self.tivaSerial.writeDataPack(jog_cmd)
			self.tivaSerial.writeDataPack(self.stop_cmd)

	def motor2_jog_up(self):
		jog_cmd = [
		'0 m 0 1;',
		'1 m 0 1;',
		'2 m 10000 0;',
		'3 m 0 1;']
		if self.realRobot==True:
			self.tivaSerial.writeDataPack(jog_cmd)
			self.tivaSerial.writeDataPack(self.stop_cmd)

	def motor2_jog_down(self):
		jog_cmd = [
		'0 m 0 1;',
		'1 m 0 1;',
		'2 m 10000 1;',
		'3 m 0 1;']
		if self.realRobot==True:
			self.tivaSerial.writeDataPack(jog_cmd)
			self.tivaSerial.writeDataPack(self.stop_cmd)

	def motor3_jog_up(self):
		jog_cmd = [
		'0 m 0 1;',
		'1 m 0 1;',
		'2 m 0 1;',
		'3 m 10000 0;']
		if self.realRobot==True:
			self.tivaSerial.writeDataPack(jog_cmd)
			self.tivaSerial.writeDataPack(self.stop_cmd)

	def motor3_jog_down(self):
		jog_cmd = [
		'0 m 0 1;',
		'1 m 0 1;',
		'2 m 0 1;',
		'3 m 10000 1;']
		if self.realRobot==True:
			self.tivaSerial.writeDataPack(jog_cmd)
			self.tivaSerial.writeDataPack(self.stop_cmd)

	def completeHome(self):
		self.responses = []
		print(self.currents)
		if (len(self.currents) <4):
			return 0
		for i in range(4):
			print(i)
			for j in range(10):
				if i == 0:
					self.motor0_jog_up()
				elif i == 1:
					self.motor1_jog_up()
				elif i == 2:
					self.motor2_jog_up()
				elif i == 3:
					self.motor3_jog_up()
				
				self.responses = self.readCurrents()
				print(math.fabs(math.fabs(self.responses[i])-math.fabs(self.currents[i])))
				if math.fabs(self.responses[i])>math.fabs(self.currents[i])+6:
					print(self.responses)
					print(j)
					if i == 0:
						self.motor0_jog_down()
						self.motor0_jog_down()
					elif i == 1:
						self.motor1_jog_down()
						self.motor1_jog_down()
					elif i == 2:
						self.motor2_jog_down()
						self.motor2_jog_down()
					elif i == 3:
						self.motor3_jog_down()
						self.motor3_jog_down()
					
					break
				else:
					print(self.responses)
		self.motor0_jog_up()
		self.motor1_jog_up()
		self.motor2_jog_up()
		self.motor3_jog_up()
		dcb_real.setPos(0.49,0.49,0.1)
					

					


	def readCurrents(self):
		local_responses = []
		curr_cmds = [['5 e 0IQ;'],['5 e 1IQ;'],['5 e 2IQ;'],['5 e 3IQ;']]
		if self.realRobot==True:
			for i in range(len(curr_cmds)):
				local_responses.append(self.tivaSerial.writeDataPack2(curr_cmds[i]))
			for i in range(len(local_responses)):
				local_responses[i] = float((str(local_responses[i]).split("=")[1]).split("""\r""")[0])
			return local_responses


	def update(self):
		self.width = self.width() #update your width and height attributes to reflect the current width and height
		self.height = self.height()
		text = str(self.width) + ' , ' + str(self.height)
		self.l1.setText(text)
		self.retranslateUi(MainWindow)
		QApplication.processEvents()
		print("event")

	def open(self):
		self.filename = QtGui.QFileDialog.getOpenFileName(MainWindow,'Open File', '.')
		print 'file:', self.filename
		# data = pd.read_csv(self.filename) 
		# array = data.values
		with open(self.filename) as csv_file:
			trajectory_file = csv.reader(csv_file, delimiter=',')
			self.trajectory = list(trajectory_file)
			self.trajectory = np.array(self.trajectory).astype(float)
		print(self.trajectory)
		self.retranslateUi(MainWindow)
		QApplication.processEvents()

	def style_choice(self, text):

		if (text =="CSV points"):
			self.layoutWidget1.setHidden(True)
			self.layoutWidget_3.setHidden(True)
			self.layoutWidget_2.setHidden(False)
			self.mode = 'csv' 
		elif (text =="Single points"):
			self.mode = 'single'
			self.layoutWidget1.setHidden(False)
			self.layoutWidget_2.setHidden(True)
			self.layoutWidget_3.setHidden(True)
		elif (text =="Homing"):
			self.mode = None
			self.layoutWidget_2.setHidden(True)
			self.layoutWidget1.setHidden(True)
			self.layoutWidget_3.setHidden(False)
		elif(text =="Select method"):
			self.mode = None
			self.layoutWidget_2.setHidden(True)
			self.layoutWidget1.setHidden(True)
			self.layoutWidget_3.setHidden(True)
		self.retranslateUi(MainWindow)
		QApplication.processEvents()

	def picktoggle(self):
		print(self.magnet)
		self.magnet = not self.magnet
		print(self.magnet)
		print(int(self.magnet))
		stop_packet = [
		'0 m 0 1;',
		'1 m 0 1;',
		'2 m 0 1;',
		'3 m 0 1;',
		'4 e '+str(int(self.magnet))+' 1;']
		if self.realRobot==True:
			self.tivaSerial.writeDataPack(stop_packet)
			self.tivaSerial.writeDataPack(stop_packet)
		self.retranslateUi(MainWindow)
		QApplication.processEvents()


	# def homestate(self):
	# 	print(self.magnet)
	# 	self.magnet = not self.magnet
	# 	print(self.magnet)
	# 	print(int(self.magnet))
	# 	stop_packet = [
	# 	'0 m 0 1;',
	# 	'1 m 0 1;',
	# 	'2 m 0 1;',
	# 	'3 m 0 1;',
	# 	'4 e '+str(int(self.magnet))+' 1;']
	# 	if self.realRobot==True:
	# 		self.tivaSerial.writeDataPack(stop_packet)
		#self.tivaSerial.writeDataPack(myCmd)

	def btnstate(self):
		self.count = 0
		#test = SerialCom('COM5',8)
		#self.tivaSerial = sc.SerialCOm('/dev/ttyUSB1')
		self.length_change = [0,0,0,0]
		self.length_list = [0,0,0,0]
		self.length_list_old = [0,0,0,0]
		self.angle=[0,0,0,0]
		if self.pushButton.isChecked():
			pass
		else:
			if (self.mode==None):
				print("No mode enabled")
				return -1
			elif(self.mode=="single"):
				self.runs = 1
			else:
				self.runs = len(self.trajectory)


			for row in range(self.runs):
				if(self.mode=="single"):
					goalX, goalY, goalZ = self.xLineEdit.text(), self.yLineEdit.text(), self.zLineEdit.text()
					goalX=float(goalX)
					goalY=float(goalY)
					goalZ=float(goalZ)
				else:
					goalX=float(self.trajectory[row][0])
					goalY=float(self.trajectory[row][1])
					goalZ=float(self.trajectory[row][2])
					#self.magnet = int(self.trajectory[row][3])


				if(goalZ>self.MAX_Z):
					goalZ = self.MAX_Z
					self.fixed = True
				if(goalZ<self.MIN_Z):
					goalZ = self.MIN_Z
					self.fixed = True
				if(goalY>self.MAX_Y):
					goalY = self.MAX_Y
					self.fixed = True
				if(goalY<self.MIN_Y):
					goalY = self.MIN_Y
					self.fixed = True
				if(goalX>self.MAX_X):
					goalX = self.MAX_X
					self.fixed = True
				if(goalX<self.MIN_X):
					goalX = self.MIN_X
					self.fixed = True
				if(self.fixed == True):
					print("The dimensions entered were out of bounds")
					print("Clipped dimensions were used")

				goalPos=(goalX, goalY, goalZ)
				print(goalPos)
				dcb_real.drawGoal()
				originPos=(dcb_real.posX,dcb_real.posY,dcb_real.posZ)
				num =1
				deltax=(goalPos[0]-originPos[0])/num
				deltay=(goalPos[1]-originPos[1])/num
				deltaz=(goalPos[2]-originPos[2])/num
				

				# test = SerialCom.SerialCom1('/dev/ttyUSB0',8)
				stopCommand = "0 0 0 0 1 1 1 1 "
				for i in range(0,num+1):
					x = deltax*i+originPos[0]
					y = deltay*i+originPos[1]
					z = deltaz*i+originPos[2]
					dcb_real.setPos(x,y,z)
					for j in range(len(self.length_list)):
						self.length_list_old[j] = self.length_list[j]
					self.length_list  = dcb_real.drawGoal()
					if (i!=0):
						for j in range(len(self.length_list)):
							self.length_change[j] = self.length_list[j] - self.length_list_old[j]
					for j in range(len(self.length_change)):
						self.angle[j] = ((self.length_change[j]*200000)/(math.pi*0.06))
					print(self.angle)
					buff = io.BytesIO()
					plt.savefig(buff, format="png")
					buff.seek(1)
					image2 = Image.open(buff)
					qimage = ImageQt(image2)
					pixmap = QtGui.QPixmap.fromImage(qimage)
					if (option == 1):
						number_steps_0 = math.floor(math.fabs((self.angle[0])/(4200)))
						number_steps_1 = math.floor(math.fabs((self.angle[1])/(4200)))
						number_steps_2 = math.floor(math.fabs((self.angle[2])/(4200)))
						number_steps_3 = math.floor(math.fabs((self.angle[3])/(4200)))
					else:
						number_steps_0 = math.floor(math.fabs(self.angle[0]/(4200)))
						number_steps_1 = math.floor(math.fabs(self.angle[1]/(4200)))
						number_steps_2 = math.floor(math.fabs(self.angle[2]/(4200)))
						number_steps_3 = math.floor(math.fabs(self.angle[3]/(4200)))
					steps = np.array([number_steps_0,number_steps_1,number_steps_2,number_steps_3])
					print("steps")
					print(np.max(steps))
					
					
					self.label_pic_2.setPixmap(pixmap)
					self.retranslateUi(MainWindow)
					QApplication.processEvents()

					dirs = []
					for k in range(len(steps)):
						
						if(self.angle[k]>0):
							dirs.append('1')
						else:
							dirs.append('0')
					
					if (i>0):
						if (np.max(steps)>-1):
							if (option ==1):
								for step in range(int(np.max(steps))+1):
									speeds = []

									for k in range(len(steps)):

										if (steps[k]==step):
											extra = math.floor((math.fabs(self.angle[k]) - math.fabs((steps[k])*4200))*10)
											#print("extra "+str(int(extra)))
											speeds.append(str(int(extra)))
										elif(step>steps[k]):
											speeds.append('0')
										else:
											speeds.append('42000')
									myCmd = []
									for k in range(len(steps)):
										if (k == 0):
											myCmd.append(str(k)+' m '+ speeds[3] + " " + dirs[3] + ";")
										elif (k==1):
											myCmd.append(str(k)+' m '+ speeds[0] + " " + dirs[0] + ";")
										elif (k==3):
											myCmd.append(str(k)+' m '+ speeds[1] + " " + dirs[1] + ";")
										else:
											myCmd.append(str(k)+' m '+ speeds[k] + " " + dirs[k] + ";")



									myCmd.append("4 e "+str(int(self.magnet))+" 0;")
									print("Command")
									start_time = time.time()
									
									print(myCmd)
									print("--- %s seconds ---" % (time.time() - start_time))
									print("stop")
									if self.realRobot==True:
										self.tivaSerial.writeDataPack(myCmd)
							else:
								longest = int(np.max(steps))
								longest_mot = np.argmax(steps)
								max_speeds=[]
								for k in range(len(steps)):
									if (longest>0):
										if(math.fabs(self.angle[k]/longest)<4200):
											max_speeds.append(int(math.fabs(self.angle[k]/longest)*10))
										else:
											max_speeds.append(42000) 
								print(max_speeds)
								for step in range(int(np.max(steps))+1):
									speeds = []
									for k in range(len(steps)):
										if(step==longest):
											extra = math.floor((math.fabs(self.angle[k]) - math.fabs((steps[k])*4200))*10)
											print(math.fabs((steps[k])))
											print("extra "+str(int(extra)))
											speeds.append(str(int(extra)))
										else:
											speeds.append(str(max_speeds[k]))
									myCmd = []
									for k in range(len(steps)):
										myCmd.append(str(k)+' m '+ speeds[k] + " " + dirs[k] + ";")
									
									print(myCmd)
									myCmd.append("4 e "+str(int(self.magnet))+" 0;")
									if self.realRobot==True:
										t0 = time.time()
										self.tivaSerial.writeDataPack(myCmd)
										t1 = time.time()
										print(t1-t0)
									self.count = self.count + 1
									print(self.count)
									QApplication.processEvents()
									if self.realRobot==False:
										time.sleep(0.2)
									while(self.wait_variable):
										if self.realRobot == True:
											self.tivaSerial.writeDataPack(self.stop_cmd)
										QtCore.QCoreApplication.processEvents()
							if self.realRobot==True:
								self.tivaSerial.sendStopCommand(int(self.magnet))
			print("done")
			print(self.count)
					

			#print(dcb.length_list)


if __name__ == "__main__":
	import sys
	import io 
	dcb_real = back.DrawCableBot()
	dcb_real.initializaton()
	dcb_real.drawNodes()
	dcb_real.drawLines()

	
	app = QtGui.QApplication(sys.argv)
	qp = QPixmap()
	MainWindow = QtGui.QMainWindow()
	ui = Ui_MainWindow()
	ui.setupUi(MainWindow)
	MainWindow.show()
	sys.exit(app.exec_())

