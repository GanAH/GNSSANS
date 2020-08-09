# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'coorSystemTranWight.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from numpy import rad2deg
from database.database import Database
from measureTool.coordinationTran import CoordinationTran


class Ui_Form(QtCore.QObject):
    infoEmit = QtCore.pyqtSignal(str, str)
    tranResult = []
    dataList = []

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1166, 736)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./source/icon/note.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tableWidget_sourceCoor = QtWidgets.QTableWidget(self.groupBox)
        self.tableWidget_sourceCoor.setObjectName("tableWidget_sourceCoor")
        self.tableWidget_sourceCoor.setColumnCount(4)
        self.tableWidget_sourceCoor.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_sourceCoor.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_sourceCoor.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_sourceCoor.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_sourceCoor.setHorizontalHeaderItem(3, item)
        self.verticalLayout.addWidget(self.tableWidget_sourceCoor)
        self.horizontalLayout_3.addWidget(self.groupBox)
        self.toolBox = QtWidgets.QToolBox(Form)
        self.toolBox.setMaximumSize(QtCore.QSize(245, 260))
        self.toolBox.setStyleSheet("color: rgb(0, 0, 127);\n"
                                   "border-color: rgb(255, 255, 0);")
        self.toolBox.setObjectName("toolBox")
        self.page = QtWidgets.QWidget()
        self.page.setGeometry(QtCore.QRect(0, 0, 252, 169))
        self.page.setObjectName("page")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.page)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.groupBox_3 = QtWidgets.QGroupBox(self.page)
        self.groupBox_3.setMaximumSize(QtCore.QSize(230, 230))
        self.groupBox_3.setTitle("")
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.groupBox_3)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.comboBox_coorSystemTran = QtWidgets.QComboBox(self.groupBox_3)
        self.comboBox_coorSystemTran.setObjectName("comboBox_coorSystemTran")
        self.comboBox_coorSystemTran.addItem("")
        self.comboBox_coorSystemTran.addItem("")
        self.comboBox_coorSystemTran.addItem("")
        self.comboBox_coorSystemTran.addItem("")
        self.comboBox_coorSystemTran.addItem("")
        self.comboBox_coorSystemTran.addItem("")
        self.horizontalLayout.addWidget(self.comboBox_coorSystemTran)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.button_coorSystemTran = QtWidgets.QPushButton(self.groupBox_3)
        self.button_coorSystemTran.setObjectName("button_coorSystemTran")
        self.verticalLayout_3.addWidget(self.button_coorSystemTran)
        self.verticalLayout_5.addWidget(self.groupBox_3)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("./source/icon/Bulldozer.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolBox.addItem(self.page, icon1, "")
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setGeometry(QtCore.QRect(0, 0, 256, 198))
        self.page_2.setObjectName("page_2")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.page_2)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.page_2)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.comboBox_coorProjection = QtWidgets.QComboBox(self.page_2)
        self.comboBox_coorProjection.setObjectName("comboBox_coorProjection")
        self.comboBox_coorProjection.addItem("")
        self.comboBox_coorProjection.addItem("")
        self.comboBox_coorProjection.addItem("")
        self.comboBox_coorProjection.addItem("")
        self.comboBox_coorProjection.addItem("")
        self.horizontalLayout_2.addWidget(self.comboBox_coorProjection)
        self.verticalLayout_6.addLayout(self.horizontalLayout_2)
        self.button_coorProjection = QtWidgets.QPushButton(self.page_2)
        self.button_coorProjection.setObjectName("button_coorProjection")
        self.verticalLayout_6.addWidget(self.button_coorProjection)
        self.groupBox_4 = QtWidgets.QGroupBox(self.page_2)
        self.groupBox_4.setMaximumSize(QtCore.QSize(230, 230))
        self.groupBox_4.setTitle("")
        self.groupBox_4.setObjectName("groupBox_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.groupBox_4)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.textEdit = QtWidgets.QTextEdit(self.groupBox_4)
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout_4.addWidget(self.textEdit)
        self.verticalLayout_6.addWidget(self.groupBox_4)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("./source/icon/Crawlercrane.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolBox.addItem(self.page_2, icon2, "")
        self.horizontalLayout_3.addWidget(self.toolBox)
        self.groupBox_2 = QtWidgets.QGroupBox(Form)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.tableWidget_result = QtWidgets.QTableWidget(self.groupBox_2)
        self.tableWidget_result.setObjectName("tableWidget_result")
        self.tableWidget_result.setColumnCount(4)
        self.tableWidget_result.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_result.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_result.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_result.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_result.setHorizontalHeaderItem(3, item)
        self.verticalLayout_2.addWidget(self.tableWidget_result)
        self.horizontalLayout_3.addWidget(self.groupBox_2)

        self.retranslateUi(Form)
        self.toolBox.setCurrentIndex(0)
        self.button_coorSystemTran.clicked.connect(self.actionCoorSystemTranButton)
        self.comboBox_coorSystemTran.currentIndexChanged.connect(self.actionChangedTableHead)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.groupBox.setTitle(_translate("Form", "原始数据"))
        item = self.tableWidget_sourceCoor.horizontalHeaderItem(0)
        item.setText(_translate("Form", "ID"))
        item = self.tableWidget_sourceCoor.horizontalHeaderItem(1)
        item.setText(_translate("Form", "X"))
        item = self.tableWidget_sourceCoor.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Y"))
        item = self.tableWidget_sourceCoor.horizontalHeaderItem(3)
        item.setText(_translate("Form", "Z"))
        self.label.setText(_translate("Form", "坐标系转换："))
        self.comboBox_coorSystemTran.setItemText(0, _translate("Form", "XYZ to BLH"))
        self.comboBox_coorSystemTran.setItemText(1, _translate("Form", "XYZ to NEH"))
        self.comboBox_coorSystemTran.setItemText(2, _translate("Form", "BLH to XYZ"))
        self.comboBox_coorSystemTran.setItemText(3, _translate("Form", "BLH to NEH"))
        self.comboBox_coorSystemTran.setItemText(4, _translate("Form", "NEH to BLH"))
        self.comboBox_coorSystemTran.setItemText(5, _translate("Form", "NEH to XYZ"))
        self.button_coorSystemTran.setText(_translate("Form", "执行转换"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page), _translate("Form", "笛卡尔坐标系转换(展开)"))
        self.label_2.setText(_translate("Form", "坐标系转换："))
        self.comboBox_coorProjection.setItemText(0, _translate("Form", "高斯坐标正算"))
        self.comboBox_coorProjection.setItemText(1, _translate("Form", "高斯坐标反算"))
        self.comboBox_coorProjection.setItemText(2, _translate("Form", "横轴墨卡托投影"))
        self.comboBox_coorProjection.setItemText(3, _translate("Form", "大地主题正算"))
        self.comboBox_coorProjection.setItemText(4, _translate("Form", "大地主题反算"))
        self.button_coorProjection.setText(_translate("Form", "执行转换"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_2), _translate("Form", "坐标投影(展开)"))
        self.groupBox_2.setTitle(_translate("Form", "转换结果"))
        item = self.tableWidget_result.horizontalHeaderItem(0)
        item.setText(_translate("Form", "ID"))
        item = self.tableWidget_result.horizontalHeaderItem(1)
        item.setText(_translate("Form", "B"))
        item = self.tableWidget_result.horizontalHeaderItem(2)
        item.setText(_translate("Form", "L"))
        item = self.tableWidget_result.horizontalHeaderItem(3)
        item.setText(_translate("Form", "H"))

    def actionChangedTableHead(self):
        # 获取参数
        text = self.comboBox_coorSystemTran.currentText()
        # 更换表头
        self.tableWidget_sourceCoor.horizontalHeaderItem(1).setText(text[0])
        self.tableWidget_sourceCoor.horizontalHeaderItem(2).setText(text[1])
        self.tableWidget_sourceCoor.horizontalHeaderItem(3).setText(text[2])
        self.tableWidget_result.horizontalHeaderItem(1).setText(text[-3])
        self.tableWidget_result.horizontalHeaderItem(2).setText(text[-2])
        self.tableWidget_result.horizontalHeaderItem(3).setText(text[-1])

    def actionCoorSystemTran(self):
        # 从数据库获取文件路径
        sourceFilePath = Database.coorSystemTranSourcePath
        # 获取椭球参数
        ellipsoid = Database.ellipsoid["WGS84"]
        # 读取文件

    def actionShowSourceData(self):
        # 从数据库获取文件路径
        sourceFilePath = Database.coorSystemTranSourcePath
        self.dataList = []
        with open(sourceFilePath, "r") as F:
            for line in F:
                lineList = line.strip().split()
                if len(lineList) != 4:
                    lineList = line.strip().split(",")
                if len(lineList) != 4:
                    lineList = line.strip().split("，")
                # 开始执行插入操作
                if len(lineList) == 4:
                    self.dataList.append(lineList)
                else:
                    self.sendTopInfo("W", "输入的文件数据格式有误！请参照如下格式：\n ID,X,Y,Z 或 ID X　Y Z")
                    break
        F.close()
        if len(self.dataList) > 0:
            # 设定表格大小
            self.tableWidget_sourceCoor.setRowCount(len(self.dataList))
            for i in range(len(self.dataList)):
                for k in range(4):
                    self.tableWidget_sourceCoor.setItem(i, k, QtWidgets.QTableWidgetItem())
                    self.tableWidget_sourceCoor.item(i, k).setText(self.dataList[i][k])
                    self.tableWidget_sourceCoor.item(i, k).setTextAlignment(QtCore.Qt.AlignCenter)

    def actionCoorSystemTranButton(self):
        # try:
        if len(self.dataList) > 0:
            # 获取转换目标
            index = self.comboBox_coorSystemTran.currentText()
            # 获取椭球参数
            elliPara = Database.userCheckEllipsoid
            # 实例化坐标转换对象
            coorDinationTran = CoordinationTran(elliPara)
            for i in range(len(self.dataList)):
                tranLine = self.lineDataTran(coorDinationTran, list(map(float, self.dataList[i][1:])), index)
                # 弧度转度
                tranLine[0] = rad2deg(tranLine[0])
                tranLine[1] = rad2deg(tranLine[1])
                tranLine = list(map(str, tranLine))
                tranLine.insert(0, self.dataList[i][0])
                self.tranResult.append(tranLine)
            # 显示最终结果
            self.tableWidget_result.setRowCount(len(self.tranResult))
            for i in range(len(self.tranResult)):
                for k in range(4):
                    self.tableWidget_result.setItem(i, k, QtWidgets.QTableWidgetItem())
                    if k != 0:
                        self.tableWidget_result.item(i, k).setText(str(round(float(self.tranResult[i][k]), 5)))
                    else:
                        self.tableWidget_result.item(i, k).setText(self.tranResult[i][k])
                    self.tableWidget_result.item(i, k).setTextAlignment(QtCore.Qt.AlignCenter)
        # except Exception as e:
        #     self.sendTopInfo("E", "异常错误！具体信息：" + e.__str__())

    def lineDataTran(self, coorCla, lineList, type):
        tranLine = None
        if type == "XYZ to BLH":
            tranLine = coorCla.XYZ_to_BLH(lineList)
        elif type == "XYZ to NEH":
            tranLine = coorCla.XYZ_to_NEH(lineList)
        elif type == "BLH to XYZ":
            tranLine = coorCla.BLH_to_XYZ(lineList)
        elif type == "BLH to NEH":
            tranLine = coorCla.BLH_to_NEH(lineList)
        elif type == "NEH to XYZ":
            tranLine = coorCla.NEH_to_XYZ(lineList)
        else:
            tranLine = coorCla.NEH_to_BLH(lineList)
        return list(tranLine)

    def sendTopInfo(self, type, strInfo):
        self.infoEmit.emit(type, strInfo)

    def getTranResult(self):

        return self.tranResult

    def report(self,filePath):
        with open(filePath, "w+") as f:
            text = self.comboBox_coorSystemTran.currentText()
            headList = ["ID",text[-3]+"/°",text[-2]+"/°",text[-1]+"/m"]
            head = ""
            for i in range(len(headList)):
                if i == 0:
                    head += " {0:{1}<10}\t".format(headList[i], "")
                else:
                    head += "{0:{1}<15}\t".format(headList[i],"")
            head += "\n"
            f.write(head)
            for i in range(len(self.tranResult)):
                line = ""
                for k in range(len(self.tranResult[0])):
                    if k == 0:
                        line += " {0:{1}<10}\t".format(self.tranResult[i][k], "")
                    else:
                        line += "{0:{1}<15}\t".format(self.tranResult[i][k], "")
                line += "\n"
                f.write(line)
        f.close()
        self.sendTopInfo("T", "已导出坐标系统转换结果")
