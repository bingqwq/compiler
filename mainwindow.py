# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from newdag import *
from targetCode import *
import os
import time
from config import WENFA_DICT
import threading


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Compiler")
        MainWindow.resize(820, 620)

        qr = MainWindow.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        MainWindow.move(qr.topLeft())

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(0, 0, 551, 531))
        self.textEdit.setObjectName("textEdit")
        self.textEdit.setFont(QFont("Ubuntu", 14))

        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(550, 0, 281, 531))
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser.setFont(QFont("Ubuntu", 14))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.open_files = QtWidgets.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/open.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.open_files.setIcon(icon)
        self.open_files.setObjectName("open_files")
        self.born_mid_codes = QtWidgets.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("images/siyuanshi.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.born_mid_codes.setIcon(icon1)
        self.born_mid_codes.setObjectName("born_mid_codes")
        self.born_mid_codes_better = QtWidgets.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("images/youhua.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.born_mid_codes_better.setIcon(icon2)
        self.born_mid_codes_better.setObjectName("born_mid_codes_better")
        self.born8086 = QtWidgets.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("images/huibian.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.born8086.setIcon(icon3)
        self.born8086.setObjectName("born8086")
        self.quit_action = QtWidgets.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("images/quit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.quit_action.setIcon(icon4)
        self.quit_action.setObjectName("quit_action")
        self.toolBar.addAction(self.open_files)
        self.toolBar.addAction(self.born_mid_codes)
        self.toolBar.addAction(self.born_mid_codes_better)
        self.toolBar.addAction(self.born8086)
        self.toolBar.addAction(self.quit_action)

        hbox = QHBoxLayout()
        hbox.addWidget(self.textEdit)
        hbox.addWidget(self.textBrowser)
        widget_for_layout = QWidget()
        widget_for_layout.setLayout(hbox)
        MainWindow.setCentralWidget(widget_for_layout)



        self.retranslateUi(MainWindow)
        self.quit_action.triggered['bool'].connect(MainWindow.close)
        self.open_files.triggered['bool'].connect(self.open_file)
        self.born_mid_codes_better.triggered['bool'].connect(self.get_mid_code_better)
        self.born_mid_codes.triggered['bool'].connect(self.get_mid_code)
        self.born8086.triggered['bool'].connect(self.born8086_run)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.open_files.setText(_translate("MainWindow", "打开文件"))
        self.open_files.setToolTip(_translate("MainWindow", "打开文件"))
        self.open_files.setShortcut(_translate("MainWindow", "Ctrl+N"))
        self.born_mid_codes.setText(_translate("MainWindow", "生成四元式"))
        self.born_mid_codes.setToolTip(_translate("MainWindow", "生成四元式"))
        self.born_mid_codes.setShortcut(_translate("MainWindow", "F9"))
        self.born_mid_codes_better.setText(_translate("MainWindow", "优化四元式生成"))
        self.born_mid_codes_better.setToolTip(_translate("MainWindow", "生成优化四元式"))
        self.born_mid_codes_better.setShortcut(_translate("MainWindow", "F10"))
        self.born8086.setText(_translate("MainWindow", "汇编生成"))
        self.born8086.setToolTip(_translate("MainWindow", "生成汇编代码"))
        self.born8086.setShortcut(_translate("MainWindow", "F11"))
        self.quit_action.setText(_translate("MainWindow", "退出"))
        self.quit_action.setToolTip(_translate("MainWindow", "退出程序"))
        self.quit_action.setShortcut(_translate("MainWindow", "Ctrl+Q"))

    def open_file(self):
        openfile_name, file_type = QFileDialog.getOpenFileName(self, '选择文件', '', 'C (*.c , *.cpp)')

        with open(openfile_name) as f:
            code = f.read()

        self.textEdit.setText(code)

    def get_mid_code_better(self):
        code = self.textEdit.toPlainText()
        with open("v.cpp", "w") as f:
            f.write(code)
        v = LR()
        v.run()
        WENFA_DICT['chanshenshi'].pop('#S')
        mid_codes = v.get_result()
        o = Optimizer()
        o.load_mid_codes(mid_codes)
        o.run()
        mid_codes = o.result
        res = str()
        for m in mid_codes:
            if str(m) == "":
                continue
            res += str(m)
            res += "\n"
        self.textBrowser.setText(res)
        del v

    def get_mid_code(self):
        code = self.textEdit.toPlainText()
        with open("v.cpp", "w") as f:
            f.write(code)


        v = LR()
        v.run()

        WENFA_DICT['chanshenshi'].pop('#S')

        mid_codes = v.get_result()
        res = str()
        for m in mid_codes:
            if str(m) == "":
                continue
            res += str(m)
            res += "\n"
        self.textBrowser.setText(res)

    def born8086_run(self):
        # TODO 输出8086代码

        v = LR()
        v.run()
        WENFA_DICT['chanshenshi'].pop('#S')
        mid_codes = v.get_result()
        o = Optimizer()
        o.load_mid_codes(mid_codes)
        o.run()
        mid_codes = o.get_result()
        t = Target_fun()
        t.load_mid_codes(mid_codes)
        t.run()
        res = str()

        for l in t.out_put_block:
            res += l
            res += "\n"
        self.textBrowser.setText(res)

        with open("/home/bing/Masm/V.ASM", "w") as f:
            for l in t.out_put_block:
                f.write(l)
                f.write("\n")




        t2 = threading.Thread(target=self.dos, args=("dosbox",))
        t2.start()


        # os.system("dosbox")

    def dos(self, line):
        os.system(line)



