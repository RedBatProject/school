
import sys
import json
import jdatetime
from PyQt5.QtWidgets import (QListWidget, QPushButton, QWidget, QHBoxLayout,
    QMessageBox, QApplication, QVBoxLayout)
import PyQt5.QtWidgets
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *

class Example(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        time = jdatetime.datetime.now()
        inday = time.day
        inmonth = time.month
        inyear = time.year
        vbox = QVBoxLayout(self)
        hbox = QHBoxLayout()
        # listupset=[]
        def search(self,datee):
            time = jdatetime.datetime.now()
            inday = time.day
            inmonth = time.month
            inyear = time.year
            # vbox = QVBoxLayout(self)
            # hbox = QHBoxLayout()

            try:
                with open('datafordaily.json') as json_sdaily:
                    # print("7")
                    datafordaily = json.load(json_sdaily)
                    datafordaily[f'{inyear}-{inmonth}-{inday}']=[]

            except:
                datafordaily = {}
                with open('datafordaily.json','w+') as json_sdaily:
                    json.dump(datafordaily , json_sdaily)
                with open('datafordaily.json') as json_sdaily:
                    # print("7")
                    datafordaily = json.load(json_sdaily)
                datafordaily[f'{inyear}-{inmonth}-{inday}']=[]


            self.listWidget = QListWidget(self)
            # try:
            # print("6")
            with open('datadaily.json') as json_filedaily:
                # print("7")
                datadaily = json.load(json_filedaily)
            with open('data.json') as outfile:
                # print("8")
                data = json.load(outfile)
            datee = f'{inyear}-{inmonth}-{inday}'
            person_num = 0
            for i in range(len(datadaily['0'])):
                # print("1")
                if datadaily[datee][i]['today']==0:
                    # print("2")
                    for person in range(len(data)):
                        # print("3")
                        if data[person]['ID']==datadaily[datee][i]['ID']:
                            datafordaily[f'{inyear}-{inmonth}-{inday}'].append({
                                'ID':data[person]["ID"],
                                'year': time.minute,
                                'hour':time.hour,
                                        })
                            # print("5")
                            # listWidget.addItem(f'{data[person]['name']} {data[person]['family']}, {data[person]['tell']}')
                            spacee = "  "
                            ne =30-len(data[person]["name"])
                            # listupset.append(f'{data[person]["name"]}{spacee*ne}'+f'{data[person]["family"]}')
                            self.listWidget.addItem(f'{person_num+1}  :  {data[person]["name"]}{spacee*ne}'+f'{data[person]["family"]}')
                            person_num+=1
            with open('datafordaily.json','w+') as json_sdaily:
                json.dump(datafordaily , json_sdaily)
        search(self,f'{inyear}-{inmonth}-{inday}')

        countBtn = QPushButton('جست و جو  با تاریخ ', self)
        countBtn.clicked.connect(self.onsearchbydateClicked)
        countBtn.setStyleSheet(
        '''*{
            color: 'black';
            font-family: 'Arial';
            font-size: 16px;
            padding:3px;
            border-radius: 12px;
            font-weight: 400;
            background: transparent;
            background-color: rgba(100, 100, 100, 0.4);

        }
        *:hover{
            color: 'black';
            font-family: 'Arial';
            font-size: 16px;
            padding:3px;
            font-weight: 4;
            border-radius: 12px;
            background: transparent;
            background-color: rgba(100, 100, 100, 0.9);
        }''')
        countrepeat_1 = QPushButton('کارت های تکراری ',self)
        countrepeat_1.clicked.connect(self.count_repeat)
        countrepeat_1.setStyleSheet(
        '''*{
            color: 'black';
            font-family: 'Arial';
            font-size: 16px;
            padding:3px;
            border-radius: 12px;
            font-weight: 400;
            background: transparent;
            background-color: rgba(100, 100, 100, 0.4);

        }
        *:hover{
            color: 'black';
            font-family: 'Arial';
            font-size: 16px;
            padding:3px;
            font-weight: 4;
            border-radius: 12px;
            background: transparent;
            background-color: rgba(100, 100, 100, 0.9);
        }''')

        clearBtn = QPushButton('ارسال پیامک', self)
        clearBtn.clicked.connect(self.onClearClicked)
        clearBtn.setStyleSheet(
        '''*{
            color: 'black';
            font-family: 'Arial';
            font-size: 16px;
            padding:3px;
            border-radius: 12px;
            font-weight: 400;
            background: transparent;
            background-color: rgba(100, 100, 100, 0.4);

        }
        *:hover{
            color: 'black';
            font-family: 'Arial';
            font-size: 16px;
            padding:3px;
            font-weight: 400;
            border-radius: 12px;
            background: transparent;
            background-color: rgba(100, 100, 100, 0.9);
        }''')
        searchBtn = QPushButton('جست و جو برای شخص', self)
        searchBtn.clicked.connect(self.onsearchClicked)
        searchBtn.setStyleSheet(
        '''*{
            color: 'black';
            font-family: 'Arial';
            font-size: 16px;
            padding:3px;
            border-radius: 12px;
            font-weight: 400;
            background: transparent;
            background-color: rgba(100, 100, 100, 0.4);

        }
        *:hover{
            color: 'black';
            font-family: 'Arial';
            font-size: 16px;
            padding:3px;
            font-weight: 400;
            border-radius: 12px;
            background: transparent;
            background-color: rgba(100, 100, 100, 0.9);
        }''')

        vbox.addWidget(self.listWidget)
        hbox.addWidget(clearBtn)
        hbox.addWidget(countBtn)
        hbox.addWidget(searchBtn)
        hbox.addWidget(countrepeat_1)
        vbox.addLayout(hbox)

        self.listWidget.itemDoubleClicked.connect(self.onClicked)
        
        # vbox.addWidget(self.listWidget)
        self.setLayout(vbox)

        self.setGeometry(300, 300, 450, 350)
        self.setWindowTitle('لیست غایبان امروز ')
        self.show()

    def onsearchClicked(self):
        self.listWidget.clear()
        name, done1 = QtWidgets.QInputDialog.getText(
            self, ' ','نام شخص را وارد کنید')
        family, done2 = QtWidgets.QInputDialog.getText(
            self,'', 'تافامیل شخص را وارد کنید')
        with open('datadailys.json') as json_filedailys:
            datadailys = json.load(json_filedailys)
        with open('data.json') as outfile:
            data = json.load(outfile)
        spacee="  "
        person_num=0
        for person4 in range(len(data)):
        	ne =20-len(data[person4]["name"])
        	# print(data[person4]["name"])
        	if data[person4]["name"]==name and data[person4]["family"]==family:

        		for person3 in range(len(data)):
        			if datadailys[person3]["ID"]==data[person4]["ID"]:
        				self.listWidget.addItem(f'{person_num+1}  :  {data[person4]["name"]}{spacee*(30-len(data[person4]["name"]))}'+f'{data[person4]["family"]}'+'\n'+'روز های غیبت: '+f'{(20-len(datadailys[person3]["today"]))*spacee}'+f'{datadailys[person3]["today"]}')
        				person_num+=1
        	# else:
        	# 	QMessageBox.information(self, "اطلاعات",'نام و یا نام خانوادگی نامعتبر است')

        	# 	break
    def count_repeat(self):
        self.listWidget.clear()
        time = jdatetime.datetime.now()
        inday = time.day
        inmonth = time.month
        inyear = time.year
        # repeatclick = []
        with open('datadaily.json') as datadaily:
            datadaily = json.load(datadaily)
        with open('data.json') as data:
            data = json.load(data)
        # try:
        for i in range(len(datadaily[f'{inyear}-{inmonth}-{inday}'])):
            ffff=0
            if datadaily[f'{inyear}-{inmonth}-{inday}'][i]['repeat']>=2:
                ffff=datadaily[f'{inyear}-{inmonth}-{inday}'][i]['repeat']
                self.listWidget.addItem(f'{data[i]["name"]}'+'   '+f'{data[i]["family"]}'+'                  '+f'{ffff}')
        # except:
            # pass     

            


    def onClearClicked(self):
        pass

    def onsearchbydateClicked(self):
        time = jdatetime.datetime.now()
        inday = time.day
        inmonth = time.month
        inyear = time.year
        name, done1 = QtWidgets.QInputDialog.getText(
            self, 'تاریخ  ','تاریخ را مطابق پایین وارد کنید  :'+'\n\n'+'                        '+ f'{inday}-{inmonth}-{inyear}')
        # print(type(name))
        try:
            self.listWidget.clear()
            with open('datafordaily.json') as json_filedaily:
                # print("7")
                datafordaily = json.load(json_filedaily)
            with open('data.json') as outfile:
                # print("8")
                data = json.load(outfile)
            for person in range(len(datafordaily[name])):
                for person2 in range(len(data)):
                    if datafordaily[name][person]["ID"]==data[person2]["ID"]:
                        spacee = " "
                        ne =20-len(data[person]["name"])
                        # listupset.append(f'{data[person]["name"]}{spacee*ne}'+f'{data[person]["family"]}')
                        self.listWidget.addItem(f'{person2}  :  {data[person2]["name"]}{spacee*ne}'+f'{data[person2]["family"]}')          

            # self.listWidget.addItem('تاریخ اشتباه وارد شده است')
        except:
            self.listWidget.clear()
            QMessageBox.information(self, "اطلاعات",'تاریخ اشتباه است')


    def onClicked(self, item):

        QMessageBox.information(self, "اطلاعات", item.text())



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
