#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Form implementation generated from reading ui file 'botvac.ui'
#
# Created by: PyQt4 UI code generator 4.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
#!/usr/bin/env python
from subprocess import call as run
from subprocess import check_output
from os.path import exists as chkf
import sys
import json

reload(sys)  
sys.setdefaultencoding('utf8')
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
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(472, 323)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.tab)
        self.verticalLayout_2.setMargin(0)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.startButton = QtGui.QPushButton(self.tab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.startButton.sizePolicy().hasHeightForWidth())
        self.startButton.setSizePolicy(sizePolicy)
        self.startButton.setObjectName(_fromUtf8("startButton"))
        self.verticalLayout_2.addWidget(self.startButton)
        self.pauseButton = QtGui.QPushButton(self.tab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pauseButton.sizePolicy().hasHeightForWidth())
        self.pauseButton.setSizePolicy(sizePolicy)
        self.pauseButton.setObjectName(_fromUtf8("pauseButton"))
        self.verticalLayout_2.addWidget(self.pauseButton)
        self.resumeButton = QtGui.QPushButton(self.tab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.resumeButton.sizePolicy().hasHeightForWidth())
        self.resumeButton.setSizePolicy(sizePolicy)
        self.resumeButton.setObjectName(_fromUtf8("resumeButton"))
        self.verticalLayout_2.addWidget(self.resumeButton)
        self.stopButton = QtGui.QPushButton(self.tab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stopButton.sizePolicy().hasHeightForWidth())
        self.stopButton.setSizePolicy(sizePolicy)
        self.stopButton.setObjectName(_fromUtf8("stopButton"))
        self.verticalLayout_2.addWidget(self.stopButton)
        self.send2baseButton = QtGui.QPushButton(self.tab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.send2baseButton.sizePolicy().hasHeightForWidth())
        self.send2baseButton.setSizePolicy(sizePolicy)
        self.send2baseButton.setObjectName(_fromUtf8("send2baseButton"))
        self.verticalLayout_2.addWidget(self.send2baseButton)
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.tab_2)
        self.verticalLayout_3.setMargin(0)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.textEdit = QtGui.QTextEdit(self.tab_2)
        self.textEdit.setReadOnly(True)
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.verticalLayout_3.addWidget(self.textEdit)
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.verticalLayout.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 472, 26))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuAbout = QtGui.QMenu(self.menubar)
        self.menuAbout.setObjectName(_fromUtf8("menuAbout"))
        MainWindow.setMenuBar(self.menubar)
        self.actionNeato_Account = QtGui.QAction(MainWindow)
        self.actionNeato_Account.setObjectName(_fromUtf8("actionNeato_Account"))
        self.actionMy_robot = QtGui.QAction(MainWindow)
        self.actionMy_robot.setObjectName(_fromUtf8("actionMy_robot"))
        self.actionThis_software = QtGui.QAction(MainWindow)
        self.actionThis_software.setObjectName(_fromUtf8("actionThis_software"))
        self.menuAbout.addAction(self.actionMy_robot)
        self.menubar.addAction(self.menuAbout.menuAction())
	
        
            
            
        def getAvailCmds():
            run(["python","aneatocli.py","--gc"])
            with open("robotstate.json","r") as json_file:
                data=json.load(json_file)
                
            def setbuttonState(dictstr,obj):
                if data[dictstr]:
                    obj.setEnabled(True)
                else:
                    obj.setEnabled(False)
            setbuttonState("start",self.startButton)
            setbuttonState("stop",self.stopButton)
            setbuttonState("pause",self.pauseButton)
            setbuttonState("resume",self.resumeButton)
            setbuttonState("goToBase",self.send2baseButton)

        getAvailCmds()
        
        # Penser à râfraichir l'état du robot de manière moins dégueulasse avec UN thread (même si c'est chaud en python wlh. Au moins toutes les 10-15secondes
        
        
        
        def __start(self):
            run(["python","aneatocli.py","--go"])
            getAvailCmds()
           
        def __stop(self):
            run(["python","aneatocli.py","--stp"])
            getAvailCmds()
        
        def __pause(self):
           run(["python","aneatocli.py","--pse"])
           getAvailCmds() 
            
            
            
        def __resume(self):
           run(["python","aneatocli.py","--res"])
           getAvailCmds()
        
        
        def __return(self):
           run(["python","aneatocli.py","--base"])
           getAvailCmds()
        
        self.startButton.clicked.connect(__start)
        self.stopButton.clicked.connect(__stop)
        self.pauseButton.clicked.connect(__pause)
        self.resumeButton.clicked.connect(__resume)
        self.send2baseButton.clicked.connect(__return)



        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Neato Control", None))
        self.startButton.setText(_translate("MainWindow", "Start", None))
        self.pauseButton.setText(_translate("MainWindow", "Pause", None))
        self.resumeButton.setText(_translate("MainWindow", "Resume", None))
        self.stopButton.setText(_translate("MainWindow", "Stop", None))
        self.send2baseButton.setText(_translate("MainWindow", "Send to base", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Commands", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Info", None))
        self.menuAbout.setTitle(_translate("MainWindow", "My robot", None))
        self.actionNeato_Account.setText(_translate("MainWindow", "Neato Account", None))
        self.actionMy_robot.setText(_translate("MainWindow", "Account Infos", None))
        self.actionThis_software.setText(_translate("MainWindow", "This software", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

