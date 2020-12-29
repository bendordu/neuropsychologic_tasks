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
        self.center()

        self.count = 0 #счетчик раундов 

        self.correct = 1 #ответы
        self.wrong = 2
        self.slow = 3

        # self.data = [] #результаты
        # self.load_data() #подгружаем csv табличку с готовыми вариантами тестов 
        # self.timer = QtCore.QTimer() #сразу создаем таймер

        self.width = QApplication.desktop().width()
        self.height = QApplication.desktop().height()

        # self.right = QPixmap("doc/pictures/right.png") #картиночки
        # self.bad = QPixmap("doc/pictures/wrong.png")
        # self.fix = QPixmap("doc/pictures/fix.png")
        # self.box = QPixmap("doc/pictures/box.png")
        # self.mask = QPixmap("doc/pictures/mask.png")
        # self.t1 = QPixmap("doc/pictures/L1.png")
        # self.n1 = QPixmap("doc/pictures/n1.png")
        # self.n2 = QPixmap("doc/pictures/n2.png")
        # self.n3 = QPixmap("doc/pictures/n3.png")

        self.dont_touch = False #чтобы во время показа target нельзя было нажать
        self.dont_press = True #чтобы не было одновременного нажатия B/N
        self.dont_next = False #чтобы не переключалось по нжатию на пробел, если не ответа B/N

        # self.instruction = True #для инструкции, чтобы переключались только слайды
        # self.instr = 0
        # self.instr_1()
        self.test()
        

    # def instr_1(self):

    #     hbox = QHBoxLayout(self)
    #     title = QPixmap("doc/pictures/title.png")
    #     self.title = QLabel(self)
    #     self.title.setPixmap(title)
    #     hbox.addWidget(self.title)
    #     self.setLayout(hbox)
    #     self.title.setAlignment(QtCore.Qt.AlignCenter)
    #     self.showFullScreen()
           

    # def instr_2(self):
    #     instr = QPixmap("doc/pictures/ins_5.png")
    #     self.title.setPixmap(instr)


    def test(self):
        # self.title.clear()
        hbox = QHBoxLayout(self)
        frame = QPixmap("doc/pictures/frame.png")
        self.frame = QLabel(self)
        self.frame.setPixmap(frame)
        self.frame.setGeometry(0, 0, 5, 5)
        hbox.addWidget(self.frame)
        self.setLayout(hbox)
        self.frame.setAlignment(QtCore.Qt.AlignCenter)
        self.showFullScreen()

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

   
    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


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
    

    def keyPressEvent(self, e):
        
        if e.key() == QtCore.Qt.Key_Space:
            if self.instruction:
                self.instr += 1
                if self.instr == 1:
                    self.instr_2()
                if self.instr == 2:
                    self.test()
            else:
                if self.dont_touch == False and self.dont_next == False:
                    if self.count < 105:
                        self.count += 1 
                        self.answer.clear()
                        self.dont_touch = True
                        self.dont_next = True
                        self.processing()
                    else:
                        self.write_csv()
                        self.close()

        if e.key() == QtCore.Qt.Key_B:
            if self.dont_touch == False and self.dont_press == False:
                self.stop = False
                self.slow_4sec()
                rt = round((time() - self.step_1)*1000, 1)
                self.data_row += [str(rt)]
                if self.response == 1:
                    self.answer.setPixmap(self.right)
                    self.data_row += [str(self.correct)]
                else:
                    self.answer.setPixmap(self.bad)
                    self.data_row += [str(self.wrong)]
                self.answer.show()
                self.data += [self.data_row]
                self.dont_press = True
                self.dont_next = False
            

        if e.key() == QtCore.Qt.Key_N:
            if self.dont_touch == False and self.dont_press == False:
                self.stop = False
                self.slow_4sec()
                rt = round((time() - self.step_1)*1000, 1)
                self.data_row += [str(rt)]
                if self.response == 1:
                    self.answer.setPixmap(self.bad)
                    self.data_row += [str(self.wrong)]
                else:
                    self.answer.setPixmap(self.right)
                    self.data_row += [str(self.correct)]
                self.answer.show()
                self.data += [self.data_row]
                self.dont_press = True
                self.dont_next = False
            
        if e.key() == QtCore.Qt.Key_Escape:
            # self.write_csv()
            self.close()
            

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Multitasking()
    sys.exit(app.exec_()) 