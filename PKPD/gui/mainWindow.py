import sys
from PKPD.gui.abstractGui import AbstractMainWindow, AbstractTab
from PyQt5.QtWidgets import QApplication, QMenuBar, QStatusBar, QTabWidget


class MainWindow(AbstractMainWindow):
    # How QMainWindow works (has a nice diagram): https://www.riverbankcomputing.com/static/Docs/PyQt4/qmainwindow.html
    def __init__(self):
        super().__init__()
        self.top_bar = QMenuBar()
        self.tab_view = None
        self.bottom_bar = QStatusBar()

        self.tabs = []  # list containing all the pages currently available for tabbing

    def _set_geometry(self):
        """Method which sets the layout of the main window"""
        self._set_tab_structure()
        self.setMenuBar(self.top_bar)
        self.setCentralWidget(self.tab_view)
        self.setStatusBar(self.bottom_bar)
        # we can add more stuff here once the Program gets more complicated

    def _set_tab_structure(self):
        """Method which sets the structure of tabs within the window"""
        self.tab_view = QTabWidget()
        for tab in self.tabs:
            self.tab_view.addTab(tab, tab.name)
