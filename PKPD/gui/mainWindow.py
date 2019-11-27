import sys
from PKPD.gui.abstractGui import AbstractMainWindow, AbstractTab
from PyQt5.QtWidgets import QApplication, QMenuBar, QStatusBar, QTabWidget
from PyQt5.QtWidgets import QPlainTextEdit, QLabel, QVBoxLayout


class MainWindow(AbstractMainWindow):
    # How QMainWindow works (has a nice diagram): https://www.riverbankcomputing.com/static/Docs/PyQt4/qmainwindow.html
    def __init__(self):
        super().__init__()
        self.top_bar = QMenuBar()
        self.tab_view = None
        self.bottom_bar = QStatusBar()

        self.tabs = []  # list containing all the pages currently available for tabbing

        self.testUI()  # Temporary until more is built

    def _set_geometry(self):
        """Method which sets the layout of the main window"""
        self.setMenuBar(self.top_bar)
        self.setCentralWidget(self.tab_view)
        self.setStatusBar(self.bottom_bar)
        # we can add more stuff here once the Program gets more complicated

    def _set_tab_structure(self):
        """Method which sets the structure of tabs within the window"""
        self.tab_view = QTabWidget()
        for tab in self.tabs:
            self.tab_view.addTab(tab, tab.name)


    def testUI(self):
        """Temporary function to see whether it is possible to build the window"""
        self.top_bar.addMenu('File')
        tab1, tab2 = test_tab("Model"), test_tab("Simulation")
        self.tabs = [tab1, tab2]
        self._set_tab_structure()
        version_number = QLabel('Version: 0.0.0')
        self.bottom_bar.addWidget(version_number)
        self._set_geometry()

        self.setWindowTitle('PKPD')
        self.showMaximized()

class test_tab(AbstractTab):
    """temporary tab class to test the functionality of tab production in MainWindow"""
    def __init__(self, tab_name):
        super().__init__()
        layout = QVBoxLayout()
        text = QPlainTextEdit()
        layout.addWidget(text)
        self.setLayout(layout)
        self.name = tab_name


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    sys.exit(app.exec_())
