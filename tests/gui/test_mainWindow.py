import sys
from PKPD.gui import mainWindow as mw, abstractGui as abs
from PyQt5.QtWidgets import QPlainTextEdit, QLabel, QVBoxLayout, QApplication


def test_ui(visualise=False):
    """Sees whether it is possible to build the main window"""
    app = QApplication(sys.argv)
    window = mw.MainWindow()

    window.top_bar.addMenu('File')
    tab1, tab2 = TestTab("Model"), TestTab("Simulation")
    window.tabs = [tab1, tab2]
    version_number = QLabel('Version: 0.0.0')
    window.bottom_bar.addWidget(version_number)
    window._set_geometry()
    window.setWindowTitle('PKPD')

    if visualise:
        window.showMaximized()
        sys.exit(app.exec_())
    else:
        app.quit()


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
    test_ui()
    # test_ui(visualise=True)
