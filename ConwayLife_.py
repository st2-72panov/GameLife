from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QMainWindow
from PyQt5.QtCore import QThread
from random import randint
import numpy as np


# globals
size = 10
painting_field = [33 * [0], [0] + 2 * ([0] + [1]) + 2 * (3 * [0] + [1]) + 2 * [0] + 9 * ([1] + [0]),
                  2 * ([0] + [1]) + 2 * (3 * [0] + [1]) + 4 * [0] + [1] + 2 * [0] + 7 * ([0] + [1]),
                  5 * [0] + 3 * ([1] + 3 * [0]) + [0] + [1] + 14 * [0], 2 * ([0] + [1]) + 2 * [0] +
                  + 2 * ([1] + 3 * [0]) + [1] + [0] + [1] + 2 * [0] + 7 * ([0] + [1]),
                  [0] + 3 * (3 * [0] + [1]) + 5 * [0] + [1] + 2 * [0] + 6 * ([1] + [0]),
                  2 * ([1] + 2 * [0]) + [0] + 2 * ([1] + 3 * [0]) + 3 * ([1] + [0]) + 12 * [0],
                  2 * (2 * [0] + [1]) + 2 * (3 * [0] + [1]) + 2 * [0] + [1] + 4 * [0] + 6 * ([1] + [0]),
                  18 * [0] + [1] + 14 * [0]]


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(464, 277)
        MainWindow.setWindowIcon(QtGui.QIcon('icons_\gliderIcon.ico'))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # Создание layout`а для заставки
        self.painting_layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.painting_layoutWidget.setGeometry(QtCore.QRect(0, 6, 464, 128))
        self.painting_layoutWidget.setStyleSheet("background-color: #C0C0C0")
        self.painting_layoutWidget.setObjectName("painting_layoutWidget")
        self.painting_layout = QtWidgets.QGridLayout(self.painting_layoutWidget)
        self.painting_layout.setContentsMargins(2, 2, 2, 2)
        self.painting_layout.setHorizontalSpacing(2)
        self.painting_layout.setVerticalSpacing(2)
        self.painting_layout.setObjectName("painting_layout")

        # Картина "Сад Эдема"
        painting_field = [33 * [0], [0] + 2 * ([0] + [1]) + 2 * (3 * [0] + [1]) + 2 * [0] + 9 * ([1] + [0]),
                          2 * ([0] + [1]) + 2 * (3 * [0] + [1]) + 4 * [0] + [1] + 2 * [0] + 7 * ([0] + [1]),
                          5 * [0] + 3 * ([1] + 3 * [0]) + [0] + [1] + 14 * [0], 2 * ([0] + [1]) + 2 * [0] +
                          + 2 * ([1] + 3 * [0]) + [1] + [0] + [1] + 2 * [0] + 7 * ([0] + [1]),
                          [0] + 3 * (3 * [0] + [1]) + 5 * [0] + [1] + 2 * [0] + 6 * ([1] + [0]),
                          2 * ([1] + 2 * [0]) + [0] + 2 * ([1] + 3 * [0]) + 3 * ([1] + [0]) + 12 * [0],
                          2 * (2 * [0] + [1]) + 2 * (3 * [0] + [1]) + 2 * [0] + [1] + 4 * [0] + 6 * ([1] + [0]),
                          18 * [0] + [1] + 14 * [0]]

        # Создание клеток по картине
        for y in range(9):
            for x in range(33):
                new_label = QtWidgets.QLabel(self.centralwidget)
                if painting_field[y][x] == 1:
                    new_label.setStyleSheet('background-color: #fff')
                else:
                    new_label.setStyleSheet('background-color: #000')
                self.painting_layout.addWidget(new_label, y, x)

        self.lcdNumber = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber.setGeometry(QtCore.QRect(230, 170, 191, 51))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.lcdNumber.setFont(font)
        self.lcdNumber.setObjectName("lcdNumber")
        self.horizontalSlider = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider.setGeometry(QtCore.QRect(230, 230, 191, 22))
        self.horizontalSlider.setMinimum(10)
        self.horizontalSlider.setMaximum(100)
        self.horizontalSlider.setSingleStep(10)
        self.horizontalSlider.setPageStep(10)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.horizontalSlider.setObjectName("horizontalSlider")

        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(40, 150, 101, 111))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")

        self.button_play = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.button_play.setStyleSheet("background-color: rgb(255, 170, 127);")
        self.button_play.setObjectName("button_play")
        self.gridLayout.addWidget(self.button_play, 0, 0, 1, 1)
        self.button_info = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.button_info.setStyleSheet("background-color: rgb(255, 227, 212);")
        self.button_info.setObjectName("button_info")
        self.gridLayout.addWidget(self.button_info, 1, 0, 1, 1)

        self.bg_LCD = QtWidgets.QLabel(self.centralwidget)
        self.bg_LCD.setGeometry(QtCore.QRect(230, 170, 191, 51))
        self.bg_LCD.setStyleSheet("background-color: rgb(181, 181, 181);")
        self.bg_LCD.setText("")
        self.bg_LCD.setObjectName("bg_LCD")
        self.label_size = QtWidgets.QLabel(self.centralwidget)
        self.label_size.setGeometry(QtCore.QRect(260, 130, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setItalic(True)
        self.label_size.setFont(font)
        self.label_size.setObjectName("label_size")
        self.bg_size = QtWidgets.QLabel(self.centralwidget)
        self.bg_size.setGeometry(QtCore.QRect(220, 140, 211, 121))
        self.bg_size.setStyleSheet("background-color: rgb(223, 223, 223);")
        self.bg_size.setText("")
        self.bg_size.setObjectName("bg_size")
        self.life = QtWidgets.QLabel(self.centralwidget)
        self.life.setGeometry(QtCore.QRect(200, 30, 81, 71))
        font = QtGui.QFont()
        font.setPointSize(30)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        font.setKerning(True)
        self.life.setFont(font)
        self.life.setAutoFillBackground(False)
        self.life.setStyleSheet("")
        self.life.setObjectName("life")
        self.life_border_1 = QtWidgets.QLabel(self.centralwidget)
        self.life_border_1.setGeometry(QtCore.QRect(197, 30, 81, 71))
        font = QtGui.QFont()
        font.setPointSize(32)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.life_border_1.setFont(font)
        self.life_border_1.setStyleSheet("color: rgb(255, 255, 255);")
        self.life_border_1.setObjectName("life_border_1")
        self.life_border_2 = QtWidgets.QLabel(self.centralwidget)
        self.life_border_2.setGeometry(QtCore.QRect(218, 30, 51, 71))
        font = QtGui.QFont()
        font.setPointSize(32)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.life_border_2.setFont(font)
        self.life_border_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.life_border_2.setObjectName("life_border_2")
        self.life_border_3 = QtWidgets.QLabel(self.centralwidget)
        self.life_border_3.setGeometry(QtCore.QRect(228, 30, 51, 71))
        font = QtGui.QFont()
        font.setPointSize(32)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.life_border_3.setFont(font)
        self.life_border_3.setStyleSheet("color: rgb(255, 255, 255);")
        self.life_border_3.setObjectName("life_border_3")
        self.life_border_4 = QtWidgets.QLabel(self.centralwidget)
        self.life_border_4.setGeometry(QtCore.QRect(240, 30, 51, 71))
        font = QtGui.QFont()
        font.setPointSize(32)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.life_border_4.setFont(font)
        self.life_border_4.setStyleSheet("color: rgb(255, 255, 255);")
        self.life_border_4.setObjectName("life_border_4")
        self.bg_size.raise_()
        self.bg_LCD.raise_()
        self.lcdNumber.raise_()
        self.horizontalSlider.raise_()
        self.gridLayoutWidget.raise_()
        self.label_size.raise_()
        self.life_border_1.raise_()
        self.life_border_2.raise_()
        self.life_border_3.raise_()
        self.life_border_4.raise_()
        self.life.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Меню"))
        self.button_play.setText(_translate("MainWindow", "Play!"))
        self.button_info.setText(_translate("MainWindow", "Info"))
        self.label_size.setText(_translate("MainWindow", "Размер поля"))
        self.life.setText(_translate("MainWindow", "Life"))
        self.life_border_1.setText(_translate("MainWindow", "L"))
        self.life_border_2.setText(_translate("MainWindow", "i"))
        self.life_border_3.setText(_translate("MainWindow", "f"))
        self.life_border_4.setText(_translate("MainWindow", "e"))


class Ui_Game_Itself(object):
    def setupUi(self, Game_Itself):
        Game_Itself.setObjectName("Game_Itself")
        Game_Itself.setWindowIcon(QtGui.QIcon('icons_\gliderIcon.ico'))
        if size == 33:
            size_y = 9
            Game_Itself.resize(484, 122)
        else:
            size_y = int(size * 0.5625 - 50 / 19 * (size > 97))
            Game_Itself.resize(2 + 18 * size, int(19 * size * 0.5625) - 50 * (size > 97))
        self.centralwidget = QtWidgets.QWidget(Game_Itself)
        self.centralwidget.setStyleSheet("background-color: #C0C0C0")
        self.centralwidget.setObjectName("centralwidget")

        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")

        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setContentsMargins(2, 2, 2, 2)
        self.gridLayout.setHorizontalSpacing(2)
        self.gridLayout.setVerticalSpacing(2)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout.addLayout(self.gridLayout)

        # Создание клеток в grid layout
        self.screen = [[] for _ in range(size_y)]
        for y in range(size_y):
            for x in range(size):
                new_label = QtWidgets.QLabel(self.centralwidget)
                new_label.setObjectName(f'label{x + y}')
                new_label.setStyleSheet(f'background-color: {color_dead}')
                self.gridLayout.addWidget(new_label, y, x)
                self.screen[y].append(new_label)

        self.toolBar_ = QtWidgets.QFrame(self.centralwidget)
        self.toolBar_.setMinimumSize(QtCore.QSize(0, 20))
        self.toolBar_.setMaximumSize(QtCore.QSize(16777215, 20))
        self.toolBar_.setStyleSheet("background-color: #DEB887")
        self.toolBar_.setObjectName("toolBar_")
        self.toolBar = QtWidgets.QHBoxLayout(self.toolBar_)
        self.toolBar.setContentsMargins(0, 0, 0, 0)
        self.toolBar.setSpacing(0)
        self.toolBar.setObjectName("toolBar")
        self.stopButton = QtWidgets.QPushButton(self.toolBar_)
        self.stopButton.setObjectName("stopButton")
        self.toolBar.addWidget(self.stopButton, 0, QtCore.Qt.AlignRight)
        self.verticalLayout.addWidget(self.toolBar_)
        Game_Itself.setCentralWidget(self.centralwidget)

        Game_Itself.setCentralWidget(self.centralwidget)

        self.retranslateUi(Game_Itself)
        QtCore.QMetaObject.connectSlotsByName(Game_Itself)

    def retranslateUi(self, Game_Itself):
        _translate = QtCore.QCoreApplication.translate
        Game_Itself.setWindowTitle(_translate('Game_Itself', f'Игра «Жизнь{" без смерти" * (ruleS == set(range(9)))}»'))
        self.stopButton.setText(_translate('Game_Itself', 'Pause'))


class Simulation(QThread):
    def __init__(self):
        QThread.__init__(self)

        if size == 33:
            self.field = np.array(painting_field[:])
            self.size_y = 9
        else:
            self.size_y = int(size * 0.5625 - 50 / 19 * (size > 97))
            self.field = np.zeros((self.size_y, size), dtype=np.int8)
            if size == 34:
                for pos in ((0, 1), (1, 2), (2, 0), (2, 1), (2, 2)):
                    self.field[pos[0] + 8, pos[1] + 16] = 1
            elif size == 57:
                for pos in (
                        (0, 4), (0, 5), (0, 6), (0, 8), (0, 9),
                        (1, 1), (1, 2), (1, 7), (1, 8), (1, 9),
                        (2, 1), (2, 2), (2, 3), (2, 5), (2, 10),
                        (3, 0), (3, 5), (3, 7), (3, 8), (3, 9),
                        (4, 1), (4, 2), (4, 3), (4, 8), (4, 9),
                        (5, 1), (5, 2), (5, 4), (5, 5), (5, 6)
                ):
                    self.field[pos[0] + self.size_y // 2, pos[1] + 23] = 1
            elif size == 84:
                for pos in (
                        (0, 0), (0, 2), (2, 1),
                        (1, 0), (1, 1), (1, 2)
                ):
                    self.field[pos[0] + self.size_y // 2, pos[1] + 41] = 1
            else:
                try:
                    population0 = int(size * self.size_y * alive0)
                except Exception:
                    population0 = randint(0, size * self.size_y)
                for _ in range(population0):
                    self.field[randint(0, self.size_y - 1), randint(0, size - 1)] = 1

    def run(self):
        x = size
        y = self.size_y
        previousField = np.copy(self.field)
        self.field = np.zeros((y, x), dtype=np.int8)

        if ruleS == {2, 3} and ruleB == {3}:
            # Проверка клеток для следующего поколения: сбор данных по соседям клетки
            for i in range(y):
                for j in range(x):
                    c = (previousField[i - 1, j - 1] + previousField[i - 1, j] + previousField[i - 1, j - x + 1]
                         + previousField[i, j - 1] + previousField[i, j - x + 1] + previousField[i - y + 1, j - 1]
                         + previousField[i - y + 1, j] + previousField[i - y + 1, j - x + 1])
                    # Интерпретация данных согласно основному условию Жизни
                    if c == 3 or previousField[i, j] == 1 and c == 2:
                        self.field[i, j] = 1
        else:
            # Проверка клеток для следующего поколения: сбор данных по соседям клетки
            for i in range(y):
                for j in range(x):
                    c = (previousField[i - 1, j - 1] + previousField[i - 1, j] + previousField[i - 1, j - x + 1]
                         + previousField[i, j - 1] + previousField[i, j - x + 1] + previousField[i - y + 1, j - 1]
                         + previousField[i - y + 1, j] + previousField[i - y + 1, j - x + 1])
                    # Интерпретация данных согласно основному условию Жизни
                    if previousField[i, j] == 0 and c in ruleB or previousField[i, j] == 1 and c in ruleS:
                        self.field[i, j] = 1

class Game_Itself(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.game_ui = Ui_Game_Itself()
        self.game_ui.setupUi(self)
        self.game = Simulation()

        self.timer = QtCore.QTimer()
        self.timer.start(tts)
        self.timer.timeout.connect(self.displaying)

        self.working = True
        self.game_ui.stopButton.clicked.connect(self.stop)

    def stop(self):
        if self.working:
            self.timer.stop()
            self.game_ui.stopButton.setText('Resume')
        else:
            self.game_ui.stopButton.setText('Pause')
            self.timer.start(tts)
        self.working = not self.working

    def displaying(self):
        for y, row in enumerate(self.game.field):
            for x, value in enumerate(row):
                if value == 1:
                    self.game_ui.screen[y][x].setStyleSheet(f'background-color: {color_alive}')
                else:
                    self.game_ui.screen[y][x].setStyleSheet(f'background-color: {color_dead}')
        self.game.run()

class SplashScreen(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.mainFont = QtGui.QFont()
        self.mainFont.setPointSize(15)
        self.mainFont.setItalic(True)

        self.customFont = QtGui.QFont()
        self.customFont.setPointSize(12)
        self.customFont.setItalic(True)

        self.ui.lcdNumber.display(size)
        self.ui.horizontalSlider.setValue(size)
        self.ui.horizontalSlider.valueChanged.connect(lambda: self.size_changing())
        self.button_clicking()

        self.show()

    def size_changing(self):
        global size
        number = self.ui.horizontalSlider.value()
        self.ui.lcdNumber.display(number)
        size = number
        if size == 34:
            self.ui.label_size.setText('Поле: Глайдер')
            self.ui.label_size.setFont(self.customFont)  # Уменьшить размер текста
        elif size == 33:
            self.ui.label_size.setText('Поле: Сад Эдема')
            self.ui.label_size.setFont(self.customFont)
        elif size == 57:
            self.ui.label_size.setText('Поле: Симметрия')
            self.ui.label_size.setFont(self.customFont)
        elif size == 84:
            self.ui.label_size.setText('Поле: Рассцвет жизни')
            customFont = QtGui.QFont()
            customFont.setPointSize(9)
            customFont.setItalic(True)
            self.ui.label_size.setFont(customFont)
        else:
            self.ui.label_size.setText('Размер поля')
            self.ui.label_size.setFont(QtGui.QFont(self.mainFont))

    def button_clicking(self):
        self.ui.button_info.clicked.connect(self.informing)
        self.ui.button_play.clicked.connect(self.starting_game)

    def informing(self):
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText('Игра «Жизнь» - это игра с 0 игроков (такие игры называют автоматами), '
                       'придуманная английским математиком Джоном Конвеем в 1970 году.'
                       '\nВ этой игре вам предстоит наблюдать за развитием колонии клеток'
                       ' по следующей схеме:'
                       '\n*Если живую (белую) клетку окружают 2 или 3 живых соседа, '
                       'то в следующем поколении она продолжает жить.'
                       '\n*Если мёртвую клетку окружают ровно '
                       '3 живых соседа, она становится живой.'
                       '\n\nВы также можете установить свои настройки, '
                       'создав Gl_settings.txt в одном хранилище с игрой и указав её значние в миллисекундах.'
                       '\n P.S. Создав новый файл Gl, старый удалится')
        msgBox.setWindowTitle('Info')
        msgBox.setStandardButtons(QMessageBox.Cancel)
        msgBox.addButton('Создать Gl_settings', QMessageBox.HelpRole)

        returnValue = msgBox.exec()
        if returnValue == 0:
            self.setSettings()

    def setSettings(self):
        with open('Gl_settings.txt', 'w') as gl:
            gl.write(
"""/*Пояснения*/
# Чтобы изменить настройки симуляции, введите параметр и через двоеточие с пробелом укажите аргумент.
# Не указывайте параметры, чтобы оставить их по умолчанию. Доступные параметры указаны ниже:

# color-alive - цвет живой клетки
# color-dead - цвет неживой клетки
# tts - скорость смены поколений, в мс
# P.S. Не рекомендуется ставить tts ниже 100 на полях с большим количеством клеток:
# низкие настройки могут привести к вылету программы.

# alive0 - доля живых клеток от всего игрового поля (задаётся дробью 0 до 1)
# в начальной колонии (по умолчанию задаётся случайно). P.S. в целях оптимизации
# не всегда задаёт точное значение

# rule - правила игры Жизнь. Указываются по форме B___/S___ . B (от birth, рождение) означает,
# сколько соседей нужно клетке, чтобы стать живой. S (от survival, выживание) означает, сколько
# соседей нужно клетке, чтобы остаться живой. Вместо пропусков стоят цифры (не числа) от [0 до 8].
# Стандартная конфигурация - B3/S23

# P.S. Загляните на поля с размерами 33, 34, 57 и 84

/*Настройки*/
rule: B5678/S45678
color-alive: #317f43
color-dead: #000
tts: 200
alive0: 0.7
""")

    def starting_game(self):
        self.main = Game_Itself()
        self.close()
        self.main.show()


if __name__ == '__main__':
    import sys

    try:
        with open('Gl_settings.txt') as of:
            settings = {line.strip().split(': ')[0] : line.strip().split(': ')[-1] for line in of.readlines()}
    except Exception:
        settings = ''
    if 'tts' in settings:
        tts = int(settings['tts'])
    else:
        tts = 400
    if 'color-alive' in settings:
        color_alive = settings['color-alive']
    else:
        color_alive = '#000'
    if 'color-dead' in settings:
        color_dead = settings['color-dead']
    else:
        color_dead = '#fff'
    if 'alive0' in settings:
        alive0 = float(settings['alive0'])

    if 'rule' in settings:
        try:
            rules_ = settings['rule'].lower()
            if 's' in rules_:
                ruleS = set()
                for i in range(rules_.index('s') + 1, len(rules_)):
                    ruleS.add(int(rules_[i]))
                if 9 in ruleS:
                    ruleS.discard(9)
            else:
                ruleS = {2, 3}

            if 'b' in rules_:
                ruleB = set()
                j = rules_.index('/') if '/' in rules_ else len(rules_)
                for i in range(1, j):
                    ruleB.add(int(rules_[i]))
                if 9 in ruleB:
                    ruleB.discard(9)
            else:
                ruleB = {3}
        except Exception:
            ruleS = {2, 3}
            ruleB = {3}
    else:
        ruleB = {3}
        ruleS = {2, 3}

    # print(tts, color_alive, color_dead, ruleB, ruleS, sep='; ')

    app = QtWidgets.QApplication(sys.argv)
    window = SplashScreen()
    sys.exit(app.exec_())
