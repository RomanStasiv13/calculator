from calculator_interface import Ui_MainWindow


class Control:
    def __init__(self, window):
        self.twice = False
        self.ui = Ui_MainWindow()
        self.ui.setupUi(window)
        self.ui.pushButton.clicked.connect(self.press_button('1'))
        self.ui.pushButton_2.clicked.connect(self.press_button('2'))
        self.ui.pushButton_3.clicked.connect(self.press_button('3'))
        self.ui.pushButton_4.clicked.connect(self.press_button('4'))
        self.ui.pushButton_5.clicked.connect(self.press_button('5'))
        self.ui.pushButton_6.clicked.connect(self.press_button('6'))
        self.ui.pushButton_7.clicked.connect(self.press_button('7'))
        self.ui.pushButton_8.clicked.connect(self.press_button('8'))
        self.ui.pushButton_9.clicked.connect(self.press_button('9'))
        self.ui.pushButton_10.clicked.connect(self.press_button('0'))
        self.ui.pushButton_11.clicked.connect(self.press_operation_button('+'))
        self.ui.pushButton_12.clicked.connect(self.press_operation_button('-'))
        self.ui.pushButton_13.clicked.connect(self.equal)
        self.ui.pushButton_14.clicked.connect(self.press_operation_button('*'))
        self.ui.pushButton_15.clicked.connect(self.press_operation_button('/'))
        self.ui.pushButton_16.clicked.connect(self.press_button('.'))
        self.ui.pushButton_17.clicked.connect(self.clear)
        self.ui.pushButton_18.clicked.connect(self.press_button('('))
        self.ui.pushButton_19.clicked.connect(self.press_button(')'))
        self.ui.pushButton_20.clicked.connect(self.plus_minus)
        self.ui.pushButton_21.clicked.connect(self.backspace)

        window.show()



    def press_button(self, symbol):
        def click(*args, **kwargs):
            if self.ui.lineEdit.text() == '0' and symbol != '.':
                txt = symbol
            else:
                txt = self.ui.lineEdit.text() + symbol
            self.ui.lineEdit.setText(txt)
            self.twice = True
        return click

    def press_operation_button(self, symbol):
        def click(*args, **kwargs):
            if self.twice:
                if self.ui.lineEdit.text() == '0' and symbol != '.':
                    txt = symbol
                else:
                    txt = self.ui.lineEdit.text() + symbol
                self.ui.lineEdit.setText(txt)
            self.twice = False
        return click


    def equal(self):
        self.check_error()
        txt = self.ui.lineEdit.text()
        try:
            result = str(eval(txt))
        except SyntaxError:
            result = 'ERROR'
        self.ui.lineEdit.setText(result)

    def clear(self):
        self.ui.lineEdit.clear()
        self.ui.lineEdit.setText('0')


    def plus_minus(self):
        screen = self.ui.lineEdit.text()
        if '-' == screen[0]:
            screen = screen[1:]
            self.ui.lineEdit.setText(screen)
        else:
            self.ui.lineEdit.setText(f'-{screen}')

    def backspace(self):
        self.check_error()
        screen = self.ui.lineEdit.text()
        if len(screen) == 1:
            screen = '0'
        if screen != '0':
            screen = screen[0:(len(screen) - 1)]

        self.ui.lineEdit.setText(screen)

    def check_error(self):
        if 'ERROR' in self.ui.lineEdit.text():
            self.ui.lineEdit.setText('0')