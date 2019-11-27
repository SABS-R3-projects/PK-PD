import sys
from PKPD.gui.abstractGui import AbstractMainWindow
from PyQt5.QtWidgets import QApplication, QMenuBar, QStatusBar
from PyQt5.QtWidgets import QPlainTextEdit, QLabel


class MainWindow(AbstractMainWindow):
    # How QMainWindow works (has a nice diagram): https://www.riverbankcomputing.com/static/Docs/PyQt4/qmainwindow.html
    def __init__(self):
        super().__init__()
        self.top_bar = QMenuBar()
        self.tab_view = None
        self.bottom_bar = QStatusBar()
        self.testUI()  # Temporary until more is built


    def _set_geometry(self):
        """Function which sets the layout of the main window"""
        self.setMenuBar(self.top_bar)
        self.setCentralWidget(self.tab_view)
        self.setStatusBar(self.bottom_bar)
        # we can add more stuff here once the Program gets more complicated

    def testUI(self):
        """Temporary function to see whether it is possible to build the window"""
        self.top_bar.addMenu('File')
        self.tab_view = QPlainTextEdit()
        version_number = QLabel('Version: 0.0.0')
        self.bottom_bar.addWidget(version_number)
        self._set_geometry()

        self.setWindowTitle('PKPD')
        self.showMaximized()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    sys.exit(app.exec_())
