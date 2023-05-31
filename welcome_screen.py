import sys
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import *


class WelcomePage(QWidget):

    def __init__(self):
        super().__init__()

        # Set window properties
        self.setWindowTitle('Welcome to EpiVision')
        screen = QDesktopWidget().screenGeometry()

        # Calculate the center point
        center_x = int(screen.width() / 2)
        center_y = int(screen.height() / 2)

        self.setGeometry(750, 350, 500, 300)

        # Create layout
        layout = QVBoxLayout()

        # Create label with Epi Vision text in center
        label = QLabel('EpiVision', self)
        font = QFont()
        font.setPointSize(30)
        label.setFont(font)
        label.setAlignment(Qt.AlignCenter)

        # Add label to layout
        layout.addWidget(label)

        # Create progress bar and add it to layout
        self.progress_bar = QProgressBar(self)
        layout.addWidget(self.progress_bar)

        # Set layout for the window
        self.setLayout(layout)

        # Show the window
        self.show()

        # Start timer for progress bar
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_progress_bar)
        self.timer.start(50)

    def update_progress_bar(self):
        # Update progress bar value
        self.progress_bar.setValue(self.progress_bar.value() + 1)

        # Stop timer after 5 seconds
        if self.progress_bar.value() >= 100:
            self.timer.stop()
            self.close()


# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     welcome_page = WelcomePage()
#     sys.exit(app.exec_())
