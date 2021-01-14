import sys
from PyQt5.QtWidgets import QWidget, QDesktopWidget, QApplication, QLabel, QHBoxLayout
from PyQt5 import Qt, QtCore, QtTest
from PyQt5.QtGui import QPixmap
import csv
from random import shuffle, uniform, choice
from time import time, localtime, strftime

class Multitasking(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle('Multitasking')
        self.setStyleSheet("background-color: black;")

        # self.correct = 1 #ответы
        # self.wrong = 2
        # self.slow = 3

        # self.data = [] #результаты
        # self.load_data() #подгружаем csv табличку с готовыми вариантами тестов 

        self.width = QApplication.desktop().width()
        self.height = QApplication.desktop().height()
        
        self.frame = QPixmap("doc/pictures/frame.png") #картиночки
        self.s1 = QPixmap("doc/pictures/shape1fill1.png")
        self.s2 = QPixmap("doc/pictures/shape1fill2.png")
        self.s3 = QPixmap("doc/pictures/shape2fill1.png")
        self.s4 = QPixmap("doc/pictures/shape2fill2.png")
        self.countdown = QPixmap('doc/pictures/countdown.png')
        self.countdown1 = QPixmap('doc/pictures/countdown1.png')
        self.countdown2 = QPixmap('doc/pictures/countdown2.png')
        self.countdown3 = QPixmap('doc/pictures/countdown3.png')
        self.wrongkey = QPixmap('doc/pictures/wrongkey.png')
        self.tooslow = QPixmap('doc/pictures/tooslow.png')
        self.shapeinstruction = QPixmap('doc/pictures/shapeinstruction.png')
        self.fillinginstruction = QPixmap('doc/pictures/fillinginstruction.png')
        self.gomixshapefilling = QPixmap('doc/pictures/gomixshapefilling.png')

        self.dont_press_space = True
        self.dont_press_button = True

        self.instruction = True #для инструкции, чтобы переключались только слайды
        self.instr = 1
        self.instr_1()

        self.test_number = 1
        self.count_list = [0, 10, 10, 20, 48, 48, 92]
        

    def instr_1(self): 
        hbox = QHBoxLayout(self)
        title = QPixmap("doc/pictures/info1.png")
        self.title = QLabel(self)
        self.title.setPixmap(title)
        hbox.addWidget(self.title)
        self.setLayout(hbox)
        self.title.setAlignment(QtCore.Qt.AlignCenter)
        self.showFullScreen()


    def instr_2(self):
        self.stimul_lbl = QLabel(self)
        self.dont_press_space = False

        if self.test_number == 1 or self.test_number == 4:
            gojustshape = QPixmap('doc/pictures/gojustshape.png')
            self.title.setPixmap(gojustshape)
            self.stimul_lbl.setGeometry(self.width/2-125, self.height/2-290, 250, 250)
        elif self.test_number == 2 or self.test_number == 5:
            gojustfilling = QPixmap('doc/pictures/gojustfilling.png')
            self.title.setPixmap(gojustfilling)
            self.stimul_lbl.setGeometry(self.width/2-125, self.height/2+30, 250, 250)
        elif self.test_number == 3 or self.test_number == 6:
            gomixshapefilling = QPixmap('doc/pictures/gomixshapefilling.png')
            self.title.setPixmap(self.gomixshapefilling)
                        
        
    def test(self):
        self.count = 1
        self.title.setPixmap(self.frame)
        self.s = self.random_stimul()
        # if self.test_number == 3:
        #     self.s = self.random_stimul_20()
        # elif self.test_number == 1 or self.test_number == 2:
        #     self.s = self.random_stimul_10()
        # elif self.test_number == 4 or self.test_number == 5:
        #     self.s = self.random_stimul_48()
        # elif self.test_number == 6:
        #     self.s = self.random_stimul_92()
        self.training_1()
        

    def training_1(self): 
        self.stimul = self.s[self.count]
        picture = f'self.s{self.stimul}'

        self.resp = self.stimul

        self.stimul_lbl.setPixmap(eval(picture))
        if self.test_number == 3 or self.test_number == 6:
            position_list = [-290, 30]
            self.position = choice(position_list)
            self.stimul_lbl.setGeometry(self.width/2-125, self.height/2+self.position, 250, 250)
        self.stimul_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.stimul_lbl.show()

        self.dont_press_button = False

        self.timer = QtCore.QTimer()
        self.timer.start(4000)
        self.timer.timeout.connect(self.slow_4sec)


    def slow_4sec(self):
        self.dont_press_button = True
        self.timer.stop()
        self.stimul_lbl.hide()
        self.title.setPixmap(self.tooslow)
        QtTest.QTest.qWait(2000)
        if self.test_number == 1 or self.test_number == 4:
            self.title.setPixmap(self.shapeinstruction)
        elif self.test_number == 2 or self.test_number == 5:
            self.title.setPixmap(self.fillinginstruction)
        elif self.test_number == 3 or self.test_number == 6:
            if self.position == -290:
                self.title.setPixmap(self.shapeinstruction)
            else:
                self.title.setPixmap(self.fillinginstruction)
        QtTest.QTest.qWait(2000)
        self.title.setPixmap(self.frame)
        if self.count < self.count_list[self.test_number]:
            self.count += 1
            self.training_1()
        else:
            self.stimul_lbl.hide()
            self.test_number += 1  
            self.instr_2()

        
    def random_stimul(self):
        list = [1, 2, 3, 4]
        l = []
        for i in range(24):
            shuffle(list)
            l += list
        n = 0 
        while n < self.count_list[self.test_number]:
            if l[n] == l[n+1]:
                l.pop(n)
                n = 0
            n += 1

        if self.test_number == 3:
            return l[:21]
        elif self.test_number == 1 or self.test_number == 2:
            return l[:11]
        elif self.test_number == 4 or self.test_number == 5:
            return l[:49]
        elif self.test_number == 6:
            return l[:93]


    def wrong(self):
        self.dont_press_button = True
        self.stimul_lbl.clear()
        self.stimul_lbl.hide()
        self.title.setPixmap(self.wrongkey)
        QtTest.QTest.qWait(1000) 

        if self.test_number == 1 or self.test_number == 4:
            self.title.setPixmap(self.shapeinstruction)
        elif self.test_number == 2 or self.test_number == 5:
            self.title.setPixmap(self.fillinginstruction)
        elif self.test_number == 3 or self.test_number == 6:
            if self.position == -290:
                self.title.setPixmap(self.shapeinstruction)
            else:
                self.title.setPixmap(self.fillinginstruction)
        QtTest.QTest.qWait(2000)
        self.title.setPixmap(self.frame)

        if self.count < self.count_list[self.test_number]:
            self.training_1()
        else:
            self.stimul_lbl.hide()
            self.test_number += 1  
            self.instr_2()


    def concentrate(self):
        self.dont_press_button = True
        self.dont_press_space = True
        self.title.setPixmap(self.countdown)
        QtTest.QTest.qWait(1000)
        self.title.setPixmap(self.countdown1)
        QtTest.QTest.qWait(1000)
        self.title.setPixmap(self.countdown2)
        QtTest.QTest.qWait(1000)
        self.title.setPixmap(self.countdown3)
        QtTest.QTest.qWait(1000)
        self.test()
    

    def keyPressEvent(self, e):
        
        if e.key() == QtCore.Qt.Key_Space:
            if self.instruction:
                if self.instr <= 9:
                    self.instr += 1
                    instr = QPixmap('doc/pictures/info' + str(self.instr) + '.png')
                    self.title.setPixmap(instr)
                else:
                    self.instruction = False
                    self.instr_2()
            else:
                if not self.dont_press_space:
                    self.concentrate()

        if e.key() == QtCore.Qt.Key_B:
            if not self.dont_press_button:
                self.timer.stop()
                self.dont_press_button = True
                
                if self.count <= self.count_list[self.test_number]:
                    self.count += 1
                    if self.test_number == 1 or self.test_number == 4:
                        
                        if self.resp == 1 or self.resp == 2:
                            self.stimul_lbl.clear()
                            QtTest.QTest.qWait(500)
                            self.training_1()
                        else:
                            self.wrong()

                    elif self.test_number == 2 or self.test_number == 5:
                                                
                        if self.resp == 1 or self.resp == 3:
                            self.stimul_lbl.clear()
                            QtTest.QTest.qWait(500)
                            self.training_1()
                        else:
                            self.wrong()

                    elif self.test_number == 3 or self.test_number == 6:
                         
                        if self.position == -290:
                            if self.resp == 1 or self.resp == 2:
                                self.stimul_lbl.clear()
                                QtTest.QTest.qWait(500)
                                self.training_1()
                            else:
                                self.wrong()
                        elif self.position == 30:
                            if self.resp == 1 or self.resp == 3:
                                self.stimul_lbl.clear()
                                QtTest.QTest.qWait(500)
                                self.training_1()
                            else:
                                self.wrong()

                else:
                    self.stimul_lbl.hide()
                    self.test_number += 1  
                    self.instr_2()
                    

        if e.key() == QtCore.Qt.Key_N:
            if not self.dont_press_button:
                self.timer.stop()
                self.dont_press_button = True
                if self.count <= self.count_list[self.test_number]:
                    self.count += 1
                
                    if self.test_number == 1 or self.test_number == 4:
                        
                        if self.resp == 3 or self.resp == 4:
                            self.stimul_lbl.clear()
                            QtTest.QTest.qWait(500)
                            self.training_1()
                        else:
                            self.wrong()

                    elif self.test_number == 2 or self.test_number == 5:    
                                          
                        if self.resp == 2 or self.resp == 4:
                            self.stimul_lbl.clear()
                            QtTest.QTest.qWait(500)
                            self.training_1()
                        else:
                            self.wrong()

                    elif self.test_number == 3 or self.test_number == 6:   
                            
                        if self.position == -290:
                            if self.resp == 3 or self.resp == 4:
                                self.stimul_lbl.clear()
                                QtTest.QTest.qWait(500)
                                self.training_1()
                            else:
                                self.wrong()
                        elif self.position == 30:
                            if self.resp == 2 or self.resp == 4:
                                self.stimul_lbl.clear()
                                QtTest.QTest.qWait(500)
                                self.training_1()
                            else:
                                self.wrong()

                else:
                    self.stimul_lbl.hide()
                    self.test_number += 1  
                    self.instr_2() 

            
        if e.key() == QtCore.Qt.Key_Escape:
            # self.write_csv()
            self.close()
            

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Multitasking()
    sys.exit(app.exec_()) 




 # def write_csv(self): #при закрытии теста результаты сохраняются в файл
    #     path = 'results/' + str(strftime('%d-%b-%Y-%H-%M', localtime(time()))) + '.csv'
    #     with open(path, "w", newline='') as csv_file:
    #         writer = csv.writer(csv_file, delimiter=',')
    #         writer.writerow(['SOA', 's1', 's2', 'x1', 'y2', 'target present', 'RT', 'response'])
    #         writer.writerows(self.data)


    # def load_data(self): #подгружается таблица, заранее сгенерированная, для демонстрации раундов
    #     with open("doc/table/tableAB.csv", encoding='utf-8') as tableAB:
    #         table = csv.reader(tableAB, delimiter = ",")
    #         self.rows = [row for row in table]
    #         shuffle(self.rows)
    #     return self.rows


    # def processing(self):
    #     self.box_1.setPixmap(self.box)
    #     self.box_2.setPixmap(self.box)
    #     self.box_3.setPixmap(self.box)
    #     self.box_4.setPixmap(self.box)
        
    #     row = self.rows[self.count]

    #     t = int(row[0])

    #     QtTest.QTest.qWait(uniform(0, 500)) 

    #     pictures_1 = f'self.{row[1]}'
    #     pictures_2 = f'self.{row[2]}'

    #     x_1 = int(row[3])
    #     if x_1 == -200:
    #         self.box_4.setPixmap(eval(pictures_1))
    #         QtTest.QTest.qWait(57)
    #         self.box_4.setPixmap(self.mask)
    #         QtTest.QTest.qWait(250)
    #     if x_1 == 200:
    #         self.box_2.setPixmap(eval(pictures_1))
    #         QtTest.QTest.qWait(57)
    #         self.box_2.setPixmap(self.mask)
    #         QtTest.QTest.qWait(250)

    #     QtTest.QTest.qWait(t - 57 - 250)
        
    #     y_2 = int(row[4])
    #     if y_2 == -200:
    #         self.box_1.setPixmap(eval(pictures_2))
    #         self.dont_touch = False
    #         self.dont_press = False
    #         self.step_1 = time()
    #         QtTest.QTest.qWait(57)
    #         self.box_1.setPixmap(self.mask)
    #         QtTest.QTest.qWait(250)
    #     if y_2 == 200:
    #         self.box_3.setPixmap(eval(pictures_2))
    #         self.dont_touch = False
    #         self.dont_press = False
    #         self.step_1 = time()
    #         QtTest.QTest.qWait(57)
    #         self.box_3.setPixmap(self.mask)
    #         QtTest.QTest.qWait(250)

    #     self.response = int(row[5])
    #     t_result = row[6]

    #     self.data_row = [str(t_result), row[1], row[2], str(x_1), str(y_2), str(self.response)]

    #     self.timer.start(3750)
    #     self.stop = True
    #     self.timer.timeout.connect(self.slow_4sec)


    # def slow_4sec(self):
    #     if self.stop == False:
    #         self.timer.stop()
    #     else:
    #         self.answer.setPixmap(self.bad)
    #         self.answer.show()
    #         self.data_row += ['0']
    #         self.data_row += [str(self.slow)]
    #         self.data += [self.data_row]
    #         self.stop = False
    #         self.dont_next = False

    # def random_stimul(self):
    #     list = [1, 2, 3, 4]
    #     l = []
    #     for i in range(13):
    #         shuffle(list)
    #         l += list
    #     n = 0 
    #     p = 0
    #     while n < len(l)-p-1:
    #         n += 1
    #         if l[n] == l[n+1]:
    #             l.remove(l[n])
    #             p += 1
    #     while len(l) != 40:
    #         l.pop()
    #     return l


    # def random_stimul_10(self):
    #     list = [1, 2, 3, 4]
    #     l = []
    #     for i in range(4):
    #         shuffle(list)
    #         l += list
    #     n = 0 
    #     while n < 10:
    #         if l[n] == l[n+1]:
    #             l.pop(n)
    #             n = 0
    #         n += 1
    #     return l[:11]

    # def random_stimul_20(self):
    #     list = [1, 2, 3, 4]
    #     l = []
    #     for i in range(7):
    #         shuffle(list)
    #         l += list
    #     n = 0 
    #     while n < 20:
    #         if l[n] == l[n+1]:
    #             l.pop(n)
    #             n = 0
    #         n += 1
    #     return l[:21]

    # def random_stimul_48(self):
    #     list = [1, 2, 3, 4]
    #     l = []
    #     for i in range(14):
    #         shuffle(list)
    #         l += list
    #     n = 0 
    #     while n < 48:
    #         if l[n] == l[n+1]:
    #             l.pop(n)
    #             n = 0
    #         n += 1
    #     return l[:49]

    # def random_stimul_92(self):
    #     list = [1, 2, 3, 4]
    #     l = []
    #     for i in range(24):
    #         shuffle(list)
    #         l += list
    #     n = 0 
    #     while n < 92:
    #         if l[n] == l[n+1]:
    #             l.pop(n)
    #             n = 0
    #         n += 1
    #     return l[:93]