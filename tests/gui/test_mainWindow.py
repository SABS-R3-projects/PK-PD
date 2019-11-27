import sys
from PKPD.gui import mainWindow as mw, abstractGui as abs
from PyQt5.QtWidgets import QPlainTextEdit, QLabel, QVBoxLayout, QApplication


def testUI(wind):
    """Sees whether it is possible to build the main window"""
    wind.top_bar.addMenu('File')
    tab1, tab2 = TestTab("Model"), TestTab("Simulation")
    wind.tabs = [tab1, tab2]
    wind._set_tab_structure()
    version_number = QLabel('Version: 0.0.0')
    wind.bottom_bar.addWidget(version_number)
    wind._set_geometry()

    wind.setWindowTitle('PKPD')
    wind.showMaximized()


class TestTab(abs.AbstractTab):
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
    window = mw.MainWindow()
    testUI(window)
    sys.exit(app.exec_())
