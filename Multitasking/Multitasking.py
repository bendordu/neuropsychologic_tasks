import sys
from PyQt5.QtWidgets import QWidget, QDesktopWidget, QApplication, QLabel, QHBoxLayout
from PyQt5 import Qt, QtCore, QtTest
from PyQt5.QtGui import QPixmap
import csv
from random import shuffle, uniform
from time import time, localtime, strftime

class Multitasking(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle('Multitasking')
        self.setStyleSheet("background-color: black;")

        self.count = 0 #счетчик раундов 

        # self.correct = 1 #ответы
        # self.wrong = 2
        # self.slow = 3

        # self.data = [] #результаты
        # self.load_data() #подгружаем csv табличку с готовыми вариантами тестов 
        # self.timer = QtCore.QTimer() #сразу создаем таймер

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

        self.dont_press_space = False

        self.instruction = True #для инструкции, чтобы переключались только слайды
        self.instr = 1
        self.instr_1()
        

    def instr_1(self):
        hbox = QHBoxLayout(self)
        title = QPixmap("doc/pictures/info1.png")
        self.title = QLabel(self)
        self.title.setPixmap(title)
        hbox.addWidget(self.title)
        self.setLayout(hbox)
        self.title.setAlignment(QtCore.Qt.AlignCenter)
        self.showFullScreen()


    def test(self):
        self.title.setPixmap(self.frame)
        self.training_1()
        

    def training_1(self):
        stimul = self.random_stimul_10()[self.count]
        picture = f'self.s{stimul}'
        self.resp = stimul
        print(stimul)
        self.stimul_lbl = QLabel(self)
        self.stimul_lbl.setPixmap(eval(picture))
        self.stimul_lbl.setGeometry(self.width/2-125, self.height/2-290, 250, 250)
        self.stimul_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.stimul_lbl.show()

        # self.instruction = False
                
        # self.fix_point = QLabel(self) #показ ячеек и центральной точки
        # self.fix_point.setPixmap(self.fix)
        # self.fix_point.setGeometry(self.width/2-100, self.height/2-100, 200, 200)
        # self.fix_point.show()

        # self.box_1 = QLabel(self)
        # self.box_1.setPixmap(self.box)
        # self.box_1.setGeometry(self.width/2-100, self.height/2+200, 200, 200)
        # self.box_1.show()

        # self.box_2 = QLabel(self)
        # self.box_2.setPixmap(self.box)
        # self.box_2.setGeometry(self.width/2+200, self.height/2-100, 200, 200)
        # self.box_2.show()

        # self.box_3 = QLabel(self)
        # self.box_3.setPixmap(self.box)
        # self.box_3.setGeometry(self.width/2-100, self.height/2-400, 200, 200)
        # self.box_3.show()

        # self.box_4 = QLabel(self)
        # self.box_4.setPixmap(self.box)
        # self.box_4.setGeometry(self.width/2-400, self.height/2-100, 200, 200)
        # self.box_4.show()

        # self.answer = QLabel(self)
        # self.answer.setGeometry(self.width/2-150, self.height/2+30, 280, 105)


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

    def random_stimul_10(self):
        list = [1, 2, 3, 4]
        l = []
        for i in range(3):
            shuffle(list)
            l += list
        n = 0 
        p = 0
        while n < len(l)-p-2:
            n += 1
            if l[n] == l[n+1]:
                l.remove(l[n])
                p += 1
        while len(l) != 10:
            l.pop()
        return l


    def concentrate(self):
        self.title.setPixmap(self.countdown)
        QtTest.QTest.qWait(1000)
        self.title.setPixmap(self.countdown1)
        QtTest.QTest.qWait(1000)
        self.title.setPixmap(self.countdown2)
        QtTest.QTest.qWait(1000)
        self.title.setPixmap(self.countdown3)
        self.test()
    

    def keyPressEvent(self, e):
        
        if e.key() == QtCore.Qt.Key_Space:
            if self.instruction:
                if self.instr <= 10:
                    self.instr += 1
                    instr = QPixmap('doc/pictures/info' + str(self.instr) + '.png')
                    self.title.setPixmap(instr)
                else:
                    self.concentrate()
                    self.instruction = False
                    self.dont_press_space = True
            else:
                pass
                # if self.dont_touch == False and self.dont_next == False:
                #     if self.count < 105:
                #         self.count += 1 
                #         self.answer.clear()
                #         self.dont_touch = True
                #         self.dont_next = True
                #         self.processing()
                #     else:
                #         self.write_csv()
                #         self.close()

        if e.key() == QtCore.Qt.Key_B:
            if self.count < 9:
                self.count += 1
                if self.resp == 1 or self.resp == 2:
                    self.training_1()
                else:
                    self.stimul_lbl.clear()
                    self.concentrate()
            # if self.dont_touch == False and self.dont_press == False:
            #     self.stop = False
            #     self.slow_4sec()
            #     rt = round((time() - self.step_1)*1000, 1)
            #     self.data_row += [str(rt)]
            #     if self.response == 1:
            #         self.answer.setPixmap(self.right)
            #         self.data_row += [str(self.correct)]
            #     else:
            #         self.answer.setPixmap(self.bad)
            #         self.data_row += [str(self.wrong)]
            #     self.answer.show()
            #     self.data += [self.data_row]
            #     self.dont_press = True
            #     self.dont_next = False
            

        if e.key() == QtCore.Qt.Key_N:
            if self.count < 9:
                self.count += 1
                if self.resp == 3 or self.resp == 4:
                    self.training_1()
                else:
                    self.stimul_lbl.clear()
                    self.concentrate()
            # if self.dont_touch == False and self.dont_press == False:
            #     self.stop = False
            #     self.slow_4sec()
            #     rt = round((time() - self.step_1)*1000, 1)
            #     self.data_row += [str(rt)]
            #     if self.response == 1:
            #         self.answer.setPixmap(self.bad)
            #         self.data_row += [str(self.wrong)]
            #     else:
            #         self.answer.setPixmap(self.right)
            #         self.data_row += [str(self.correct)]
            #     self.answer.show()
            #     self.data += [self.data_row]
            #     self.dont_press = True
            #     self.dont_next = False
            
        if e.key() == QtCore.Qt.Key_Escape:
            # self.write_csv()
            self.close()
            

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Multitasking()
    sys.exit(app.exec_()) 