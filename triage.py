from triage_systems import START
from PyQt5 import QtWidgets, uic

from debugwindow import Ui_MainWindow
"""
Here's an example of what I think the script can look like. Of course with more triage systems defined the user can
input which they want. I just wrote the script with what I wrote for the Start one. Also this is subject to change, this
is just how I thought it could work :)
"""

def main():
    """"
    ls = Start.get_questions()
    patient_vector = []
    for question in ls:
        print(question[0])
        if question[1] is bool:
            patient_vector.append(input("Yes or no?\n"))
        if question[1] is int:
            patient_vector.append(input("Please enter a whole number.\n"))
    # TODO: Add more if statements
    """
    class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
        def __init__(self, *args, obj=None, **kwargs):
            super(MainWindow, self).__init__(*args, **kwargs)
            self.setupUi(self)

    app = QtWidgets.QApplication([])

    window = MainWindow()
    window.show()
    app.exec()
    print(window.heart_rate_value.text())


if __name__ == "__main__":
    main()
