#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Form implementation generated from reading ui file 'botvac.ui'
#
# Created by: PyQt4 UI code generator 4.12.1
#
# WARNING! All changes made in this file will be lost!
from subprocess import call as run
from webbrowser import open_new_tab as webnt
import globals,json
try:
    from PyQt4 import QtCore, QtGui
except:
    print("PyQt4 package is not installed.\n\nPlease run 'pip install PyQt4' from your command prompt\n")
    raise


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
        MainWindow.resize(653, 375)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/neato")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setIconSize(QtCore.QSize(24, 20))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.tab)
        self.verticalLayout_2.setMargin(0)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.startButton = QtGui.QPushButton(self.tab)
        self.startButton.setEnabled(False)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.startButton.sizePolicy().hasHeightForWidth())
        self.startButton.setSizePolicy(sizePolicy)
        self.startButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/start")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.startButton.setIcon(icon1)
        self.startButton.setIconSize(QtCore.QSize(20, 20))
        self.startButton.setObjectName(_fromUtf8("startButton"))
        self.verticalLayout_2.addWidget(self.startButton)
        self.stopButton = QtGui.QPushButton(self.tab)
        self.stopButton.setEnabled(False)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stopButton.sizePolicy().hasHeightForWidth())
        self.stopButton.setSizePolicy(sizePolicy)
        self.stopButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/stop")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.stopButton.setIcon(icon2)
        self.stopButton.setIconSize(QtCore.QSize(20, 20))
        self.stopButton.setObjectName(_fromUtf8("stopButton"))
        self.verticalLayout_2.addWidget(self.stopButton)
        self.pauseButton = QtGui.QPushButton(self.tab)
        self.pauseButton.setEnabled(False)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pauseButton.sizePolicy().hasHeightForWidth())
        self.pauseButton.setSizePolicy(sizePolicy)
        self.pauseButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/pause")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pauseButton.setIcon(icon3)
        self.pauseButton.setIconSize(QtCore.QSize(20, 20))
        self.pauseButton.setObjectName(_fromUtf8("pauseButton"))
        self.verticalLayout_2.addWidget(self.pauseButton)
        self.resumeButton = QtGui.QPushButton(self.tab)
        self.resumeButton.setEnabled(False)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.resumeButton.sizePolicy().hasHeightForWidth())
        self.resumeButton.setSizePolicy(sizePolicy)
        self.resumeButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8(":/resume")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.resumeButton.setIcon(icon4)
        self.resumeButton.setIconSize(QtCore.QSize(20, 20))
        self.resumeButton.setObjectName(_fromUtf8("resumeButton"))
        self.verticalLayout_2.addWidget(self.resumeButton)
        self.send2baseButton = QtGui.QPushButton(self.tab)
        self.send2baseButton.setEnabled(False)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.send2baseButton.sizePolicy().hasHeightForWidth())
        self.send2baseButton.setSizePolicy(sizePolicy)
        self.send2baseButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8(":/base")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.send2baseButton.setIcon(icon5)
        self.send2baseButton.setIconSize(QtCore.QSize(20, 20))
        self.send2baseButton.setObjectName(_fromUtf8("send2baseButton"))
        self.verticalLayout_2.addWidget(self.send2baseButton)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(_fromUtf8(":/robot")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.tab, icon6, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.tab_2)
        self.verticalLayout_3.setMargin(0)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.refreshInfosButton = QtGui.QPushButton(self.tab_2)
        self.refreshInfosButton.setEnabled(False)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(_fromUtf8(":/refresh")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.refreshInfosButton.setIcon(icon7)
        self.refreshInfosButton.setObjectName(_fromUtf8("refreshInfosButton"))
        self.verticalLayout_3.addWidget(self.refreshInfosButton)
        self.infoTextEdit = QtGui.QPlainTextEdit(self.tab_2)
        self.infoTextEdit.setStyleSheet(_fromUtf8("border:2px inset grey;\n"
"color:rgb(204, 136, 18)"))
        self.infoTextEdit.setReadOnly(True)
        self.infoTextEdit.setObjectName(_fromUtf8("infoTextEdit"))
        self.verticalLayout_3.addWidget(self.infoTextEdit)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(_fromUtf8(":/cloudquest")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.tab_2, icon8, _fromUtf8(""))
        self.verticalLayout.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 653, 26))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuAbout = QtGui.QMenu(self.menubar)
        self.menuAbout.setObjectName(_fromUtf8("menuAbout"))
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        MainWindow.setMenuBar(self.menubar)
        self.statusBar = QtGui.QStatusBar(MainWindow)
        self.statusBar.setObjectName(_fromUtf8("statusBar"))
        MainWindow.setStatusBar(self.statusBar)
        self.actionNeato_Account = QtGui.QAction(MainWindow)
        self.actionNeato_Account.setObjectName(_fromUtf8("actionNeato_Account"))
        self.actionMy_robot = QtGui.QAction(MainWindow)
        self.actionMy_robot.setObjectName(_fromUtf8("actionMy_robot"))
        self.actionThis_software = QtGui.QAction(MainWindow)
        self.actionThis_software.setObjectName(_fromUtf8("actionThis_software"))
        self.actionLogin = QtGui.QAction(MainWindow)
        self.actionLogin.setObjectName(_fromUtf8("actionLogin"))
        self.actionRobot_s = QtGui.QAction(MainWindow)
        self.actionRobot_s.setEnabled(False)
        self.actionRobot_s.setObjectName(_fromUtf8("actionRobot_s"))
        self.actionMap_s = QtGui.QAction(MainWindow)
        self.actionMap_s.setObjectName(_fromUtf8("actionMap_s"))
        self.actionWhat_it_this = QtGui.QAction(MainWindow)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(_fromUtf8(":/info")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionWhat_it_this.setIcon(icon9)
        self.actionWhat_it_this.setObjectName(_fromUtf8("actionWhat_it_this"))
        self.actionAbout_Neato_Control = QtGui.QAction(MainWindow)
        self.actionAbout_Neato_Control.setIcon(icon)
        self.actionAbout_Neato_Control.setObjectName(_fromUtf8("actionAbout_Neato_Control"))
        self.actionInfo = QtGui.QAction(MainWindow)
        self.actionInfo.setObjectName(_fromUtf8("actionInfo"))
        self.actionAdd_Robot = QtGui.QAction(MainWindow)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(_fromUtf8(":/impex")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionAdd_Robot.setIcon(icon10)
        self.actionAdd_Robot.setObjectName(_fromUtf8("actionAdd_Robot"))
        self.actionInfos = QtGui.QAction(MainWindow)
        self.actionInfos.setObjectName(_fromUtf8("actionInfos"))
        self.actionReport_a_bug = QtGui.QAction(MainWindow)
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(_fromUtf8(":/bugrep")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionReport_a_bug.setIcon(icon11)
        self.actionReport_a_bug.setObjectName(_fromUtf8("actionReport_a_bug"))
        self.actionRefresh_Robot = QtGui.QAction(MainWindow)
        self.actionRefresh_Robot.setEnabled(False)
        self.actionRefresh_Robot.setIcon(icon7)
        self.actionRefresh_Robot.setObjectName(_fromUtf8("actionRefresh_Robot"))
        self.actionSecret_info = QtGui.QAction(MainWindow)
        self.actionSecret_info.setEnabled(False)
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap(_fromUtf8(":/secrets")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSecret_info.setIcon(icon12)
        self.actionSecret_info.setObjectName(_fromUtf8("actionSecret_info"))
        self.menuAbout.addAction(self.actionAdd_Robot)
        self.menuAbout.addAction(self.actionRefresh_Robot)
        self.menuAbout.addAction(self.actionSecret_info)
        self.menuHelp.addAction(self.actionWhat_it_this)
        self.menuHelp.addAction(self.actionAbout_Neato_Control)
        self.menuHelp.addAction(self.actionReport_a_bug)
        self.menubar.addAction(self.menuAbout.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        # MAIN CODE HERE #


        def readRobotJson(filename):
            try:
                with open(filename,"r") as json_file:
                    robotcreds=json.load(json_file)
                globals.currentRobot=robotcreds["name"]
            except:
                print("Couldn't load the robot creds. Exiting")
                raise
        
        def importCreds(self):
            globals.robFilename=QtGui.QFileDialog.getOpenFileName(MainWindow, 'Open file',"Robot credentials files (*.json)")
            getAvailCmds()
         
        def bugReport():
        	webnt("https://github.com/MIQUELLIONEL/neatocontrols/issues")
        	
        def whatitthis():
            webnt("https://github.com/MIQUELLIONEL/neatocontrols/")
           
        def robotSecretInfos():
            try:
                with open(globals.robFilename,"r") as json_file:
                    creds=json.load(json_file)
                robsecMessBox = QtGui.QMessageBox()
                robsecMessBox.setIcon(robsecMessBox.NoIcon)
                robsecMessBox.setWindowIcon(QtGui.QIcon(":neato"))
                robsecMessBox.setWindowTitle("Robot Secret Infos")
                robsecMessBox.setText("""<p align='left'>
                <strong>Robot name : </strong>"""+creds["name"]+"""<br/>
                <strong>Serial ID : </strong>"""+creds["serialID"]+"""<br/>
                <strong>Secret ID :</strong>"""+creds["secretID"]+"""<br/>
                <strong>Traits : </strong>"""+creds["traits"]+"""<br/>
                </p>""")
                robsecMessBox.exec_()
                robsecMessBox=""
            except:
                print("File doesn't exist.")
                exit()
     
        def aboutNeatoControls():
            aboutNC_MsgBox = QtGui.QMessageBox()
            aboutNC_MsgBox.setStyleSheet("img{"
            "\ndisplay: block;"
            "\nmargin-left: auto;"
            "\nmargin-right: auto;"
            "\nwidth: 50%;"
            #for whatever reason the following line doesn't work lol. if anyone knows feel free to open an issue
            #"\nborder: 1px solid black"
            "\n}")
            aboutNC_MsgBox.setIcon(aboutNC_MsgBox.NoIcon)
            aboutNC_MsgBox.setWindowIcon(QtGui.QIcon(":neato"))
            aboutNC_MsgBox.setWindowTitle("About Neato Control")
            aboutNC_MsgBox.setText("<p align='center'><img src=':neato' alt='logo qtmangen'/><br />Neato Control - A Qt interface for controlling your Neato Robotics device.<br /><br />Made by  <a href='mailto:lionel.miquel46@gmail.com'>Miquel Lionel</a>.<br /><br /><a href='https://github.com/MIQUELLIONEL/neatocontrols'>https://github.com/MIQUELLIONEL/neatocontrols</a><br /><br />2018.</p>")
            aboutNC_MsgBox.exec_()
            aboutNC_MsgBox=""
            
        def getInfos():
            globals.robinfoFilename=globals.currentRobot+"-robotinfos.json"
            run(["python","aneatocli.py","--gi",globals.currentRobot])
            try:
                self.infoTextEdit.clear()
                with open(globals.robinfoFilename,"r") as info_file:
                    infos=info_file.read().splitlines()
                    for line in infos:
                        self.infoTextEdit.appendPlainText(line)
                
            except:
                print("Couldn't load the info file"+globals.robinfoFilename+". Exiting")
                raise
            
        def getAvailCmds():
            readRobotJson(globals.robFilename)
            run(["python","aneatocli.py","--gc",globals.currentRobot])
            #we read the available current robot commands
            try:
            	with open(globals.currentRobot+"-robotcommands.json","r") as json_file:
                	data=json.load(json_file)
                
            	def setbuttonState(dictstr,obj):
		        if data[dictstr]:
		            obj.setEnabled(True)
		        else:
		            obj.setEnabled(False)
                self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", globals.currentRobot, None))
                self.actionRefresh_Robot.setEnabled(True)
                self.actionSecret_info.setEnabled(True)
                self.refreshInfosButton.setEnabled(True)
            except:
                self.actionRefresh_Robot.setEnabled(False)
                self.actionSecret_info.setEnabled(False)
                self.refreshInfosButton.setEnabled(False)
                print "Error while opening the file"
                raise
            
            setbuttonState("start",self.startButton)
            setbuttonState("stop",self.stopButton)
            setbuttonState("pause",self.pauseButton)
            setbuttonState("resume",self.resumeButton)
            setbuttonState("goToBase",self.send2baseButton)

        
            
       
        # Penser à râfraichir l'état du robot de manière moins dégueulasse avec UN thread (même si c'est chaud en python wlh. Au moins toutes les 10-15secondes
        def __do(act):
           getAvailCmds()				
           run(["python","aneatocli.py",act,globals.currentRobot])
           getAvailCmds()
            
        def __start(self):
           __do("--go")
           
        def __stop(self):
            __do("--stp")
            
        def __pause(self):
            __do("--pse")              
            
        def __resume(self):
            __do("--res")
           
        def __return(self):
           __do("--base")  
           
        
        self.startButton.clicked.connect(__start)
        self.stopButton.clicked.connect(__stop)
        self.pauseButton.clicked.connect(__pause)
        self.resumeButton.clicked.connect(__resume)
        self.send2baseButton.clicked.connect(__return)
        self.refreshInfosButton.clicked.connect(getInfos)
        
        
        self.actionAdd_Robot.triggered.connect(importCreds)
        self.actionRefresh_Robot.triggered.connect(getAvailCmds)
        self.actionReport_a_bug.triggered.connect(bugReport)
        self.actionAbout_Neato_Control.triggered.connect(aboutNeatoControls)
        self.actionWhat_it_this.triggered.connect(whatitthis)
        self.actionSecret_info.triggered.connect(robotSecretInfos)

        # END OF MAIN CODE #
        


        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Neato Control", None))
        self.startButton.setText(_translate("MainWindow", "Start", None))
        self.stopButton.setText(_translate("MainWindow", "Stop", None))
        self.pauseButton.setText(_translate("MainWindow", "Pause", None))
        self.resumeButton.setText(_translate("MainWindow", "Resume", None))
        self.send2baseButton.setText(_translate("MainWindow", "Send to base", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "robot1", None))
        self.refreshInfosButton.setText(_translate("MainWindow", "Refresh", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Infos", None))
        self.menuAbout.setTitle(_translate("MainWindow", "Robot", None))
        self.menuHelp.setTitle(_translate("MainWindow", "Help", None))
        self.actionNeato_Account.setText(_translate("MainWindow", "Neato Account", None))
        self.actionMy_robot.setText(_translate("MainWindow", "Account Infos", None))
        self.actionThis_software.setText(_translate("MainWindow", "This software", None))
        self.actionLogin.setText(_translate("MainWindow", "Import credentials", None))
        self.actionRobot_s.setText(_translate("MainWindow", "Available robot(s)", None))
        self.actionMap_s.setText(_translate("MainWindow", "Map(s)", None))
        self.actionWhat_it_this.setText(_translate("MainWindow", "What it this ?", None))
        self.actionWhat_it_this.setShortcut(_translate("MainWindow", "F1", None))
        self.actionAbout_Neato_Control.setText(_translate("MainWindow", "About Neato Control", None))
        self.actionAbout_Neato_Control.setShortcut(_translate("MainWindow", "Alt+A", None))
        self.actionInfo.setText(_translate("MainWindow", "Info", None))
        self.actionAdd_Robot.setText(_translate("MainWindow", "Load a robot", None))
        self.actionAdd_Robot.setShortcut(_translate("MainWindow", "Ctrl+O", None))
        self.actionInfos.setText(_translate("MainWindow", "Infos", None))
        self.actionReport_a_bug.setText(_translate("MainWindow", "Report a bug", None))
        self.actionReport_a_bug.setShortcut(_translate("MainWindow", "Alt+B", None))
        self.actionRefresh_Robot.setText(_translate("MainWindow", "Refresh state", None))
        self.actionRefresh_Robot.setShortcut(_translate("MainWindow", "Ctrl+R", None))
        self.actionSecret_info.setText(_translate("MainWindow", "Secret info", None))
        self.actionSecret_info.setShortcut(_translate("MainWindow", "Ctrl+S", None))

import rsc_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

