from PyQt5.QtWidgets import *
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import QFont
# from login import Ui_MainWindow
from rtsp import *
from welcome_screen import WelcomePage
import time
from login import *


class Window_1(QMainWindow):
    def __init__(self):
        super().__init__()

        # set the title of main window
        self.setWindowTitle('Epi-Vision')
        icon = QIcon("Finally_Desktop_app\doctor.png")
        self.setWindowIcon(icon)

        # set the size of window
        self.Width = 800
        self.height = int(0.618 * self.Width)
        self.resize(self.Width, self.height)

        # add all widgets
        self.btn_1 = QPushButton('Dashboard', self)
        self.btn_2 = QPushButton('RTSP Stream', self)
        self.btn_3 = QPushButton('Webcam', self)
        self.btn_4 = QPushButton('Open File', self)

        self.btn_1.clicked.connect(self.button1)
        self.btn_2.clicked.connect(self.button2)
        self.btn_3.clicked.connect(self.button3)
        self.btn_4.clicked.connect(self.button4)

        # add tabs
        self.tab1 = self.ui1()
        self.tab2 = self.ui2()
        self.tab3 = self.ui3()
        self.tab4 = self.ui4()

        self.initUI()

    def initUI(self):
        left_layout = QVBoxLayout()
        left_layout.addWidget(self.btn_1)
        left_layout.addWidget(self.btn_2)
        left_layout.addWidget(self.btn_3)
        left_layout.addWidget(self.btn_4)
        left_layout.addStretch(5)
        left_layout.setSpacing(20)
        left_widget = QWidget()
        left_widget.setLayout(left_layout)

        self.right_widget = QTabWidget()
        self.right_widget.tabBar().setObjectName("mainTab")

        self.right_widget.addTab(self.tab1, '')
        self.right_widget.addTab(self.tab2, '')
        self.right_widget.addTab(self.tab3, '')
        self.right_widget.addTab(self.tab4, '')

        self.right_widget.setCurrentIndex(0)
        self.right_widget.setStyleSheet('''QTabBar::tab{width: 0; \
            height: 0; margin: 0; padding: 0; border: none;}''')

        main_layout = QHBoxLayout()
        main_layout.addWidget(left_widget)
        main_layout.addWidget(self.right_widget)
        main_layout.setStretch(0, 40)
        main_layout.setStretch(1, 200)
        main_widget = QWidget()
        main_widget.setLayout(main_layout)
        self.setCentralWidget(main_widget)

    # -----------------
    # buttons

    def button1(self):
        self.right_widget.setCurrentIndex(0)

    def button2(self):
        self.right_widget.setCurrentIndex(1)

    def button3(self):
        self.right_widget.setCurrentIndex(2)

    def button4(self):
        self.right_widget.setCurrentIndex(3)

    # -----------------
    # pages

    def ui1(self):
        main_layout = QVBoxLayout()

        label = QLabel('DASHBOARD')
        label.setAlignment(Qt.AlignCenter)  # Set alignment to center
        font = QFont()  # Create a font object
        font.setBold(True)  # Set font weight to bold
        font.setPointSize(15)
        label.setFont(font)  # Apply the font to the label widget
        main_layout.addWidget(label)

        main_layout.addStretch(5)

        main = QWidget()
        main.setLayout(main_layout)
        return main

    # def ui2(self):
    #     main_layout = QVBoxLayout()
    #     main_layout.addWidget(QLabel('RTSP STREAM'))
    #     main_layout.addStretch(5)
    #     main = QWidget()
    #     main.setLayout(main_layout)
    #     return main

    def ui2(self):
        main_layout = QVBoxLayout()

        label = QLabel('RTSP STREAM')
        label.setAlignment(Qt.AlignCenter)  # Set alignment to center
        font = QFont()  # Create a font object
        font.setBold(True)  # Set font weight to bold
        font.setPointSize(15)
        label.setFont(font)  # Apply the font to the label widget
        main_layout.addWidget(label)

        main_layout.addStretch(1)

        # Create a new horizontal layout for the input fields and button
        hbox_layout = QHBoxLayout()

        label_rtsp = QLabel('RTSP Link:')
        hbox_layout.addWidget(label_rtsp)

        input_rtsp = QLineEdit()
        hbox_layout.addWidget(input_rtsp)

        button_go = QPushButton('Go')
        hbox_layout.addWidget(button_go)

        def call():
            other_window = MainWindow(rtsp_link=input_rtsp.text())
            main_layout.addWidget(other_window)

        button_go.clicked.connect(lambda: call())

        # Add the horizontal layout to the main layout
        main_layout.addLayout(hbox_layout)
        main_layout.addStretch(3)
        # RTSP STREAM PLAYER FILE

        main_layout.addStretch(5)
        main = QWidget()
        main.setLayout(main_layout)
        return main

    def ui3(self):
        main_layout = QVBoxLayout()
        main_layout.addWidget(QLabel('page 3'))
        main_layout.addStretch(5)
        main = QWidget()
        main.setLayout(main_layout)
        return main

    def ui4(self):
        main_layout = QVBoxLayout()
        main_layout.addWidget(QLabel('page 4'))
        main_layout.addStretch(5)
        main = QWidget()
        main.setLayout(main_layout)
        return main


if __name__ == '__main__':
    app = QApplication(sys.argv)
    wc = WelcomePage()
    wc.show()

    mainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(mainWindow)

    ex = Window_1()

    def show_window(widget):
        widget.show()

    def show_window_dash(widget):
        widget.show()

    # Start a QTimer with a timeout of 6000 milliseconds (6 seconds)
    timer = QTimer.singleShot(6000, lambda: show_window(mainWindow))
    timer1 = QTimer.singleShot(10000, lambda: show_window_dash(ex))
    mainWindow.hide()
    # ex.show()
    # Define a function to show the window widget

    sys.exit(app.exec_())
