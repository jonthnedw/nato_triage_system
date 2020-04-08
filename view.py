import controller
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

from MainWindow import Ui_MainWindow

"""
The view is responsible for taking info from and rendering results to the user. The view communicates with the
controller in a worker thread and continuously sends it the data it needs to route to the model. The view also 
continuously requests updated info from the model (through the controller) in another worker thread to display to the 
user.
"""


class Worker(QRunnable):
    """
    Worker thread with abstracted run function that will execute any given Python function with args.
    """

    def __init__(self, fn, *args, **kwargs):
        super(Worker, self).__init__()
        self.fn = fn
        self.args = args
        self.kwargs = kwargs

    @pyqtSlot()
    def run(self):
        self.fn(*self.args, **self.kwargs)


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.threadpool = QThreadPool()

    """ 
    Listener for changed parameters, updates vitals by calling controller's update_parameter function in a new
    worker thread. Queueing is handled by QThreadPool.
    """
    def parameterChanged(self, value):
        worker = Worker(controller.update_parameter, self.sender().objectName(), value)
        self.threadpool.start(worker)


def display():
    app = QApplication([])

    window = MainWindow()
    window.show()
    app.exec()


if __name__ == "__main__":
    display()