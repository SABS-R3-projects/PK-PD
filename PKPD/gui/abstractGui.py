from PyQt5.QtWidgets import QMainWindow, QWidget
from abc import ABC, abstractmethod


class AbstractMainWindow(QMainWindow):
    def __init__(self):
        # initialise window size, style, icon, windowname, tab structure
        super().__init__()

    def _set_window_size(self):
        # set the default window size (make sure not fixed)
        raise NotImplementedError

    def _set_geometry(self):
        # set the window layout
        raise NotImplementedError

    def _set_style(self):
        # set style
        raise NotImplementedError

    def _set_icon(self):
        # st application icon
        raise NotImplementedError

    def _set_windowname(self):
        # set window name for top
        raise NotImplementedError

    def _set_tab_structure(self):
        # set the structure of tabs within the window
        raise NotImplementedError

    def _change_tab(self):
        # redraw to a different tab type
        raise NotImplementedError

    def _exit(self):
        # exit the application gracefully
        raise NotImplementedError


class AbstractTab(QWidget):
    def _make_button(self):
        # draw a button
        raise NotImplementedError

    def _make_multiline_textbox(self):
        # draw a textbox for text input
        raise NotImplementedError

    def _make_graph(self):
        # instantiate a graph object
        raise NotImplementedError

    def _make_table(self):
        # make a tabular object
        raise NotImplementedError

