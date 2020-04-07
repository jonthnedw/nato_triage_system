from PyQt5 import QtWidgets, uic
from MainWindow import Ui_MainWindow

"""
The view is responsible for taking info from and rendering results to the user. The view communicates with the
controller in a worker thread and continuously sends it the data it needs to route to the model. The view also 
continuously requests updated info from the model (through the controller) in another worker thread to display to the 
user.
"""

def main():
    class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
        def __init__(self, *args, obj=None, **kwargs):
            super(MainWindow, self).__init__(*args, **kwargs)
            self.setupUi(self)

    app = QtWidgets.QApplication([])

    window = MainWindow()
    window.show()
    app.exec()
    print(window.heart_rate_value.text())

    # TODO multithread the GUI and create the two placeholder worker threads as described above

if __name__ == "__main__":
    main()
