#Copyright © 2021 Rauan Asetov. All rights reserved.
#License: http://opensource.org/licenses/MIT
from recording import Logging
from response import Request
from datetime import datetime as dt
from time import sleep
from Gui import design
import sys  # sys нужен для передачи argv в QApplication
from PyQt5 import QtWidgets
#from PyQt5.QtCore import QUrl, QSize, Qt
import config
import threading

class Checker(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.repetitionSpinBox.setMaximum(config.MaxValue)
        self.repetitionSpinBox.setMinimum(config.MinValue)
        self.start.clicked.connect(self.dispatch)


    def dispatch(self):
        self._repetition = int(self.repetitionSpinBox.value())
        self._url = self.urlLine.text()
        if self._url == '':
            self._url = config.DefaultUrl
        else:
            pass
        print(self._url)

        try:
            self._time = int(self.timerLine.text())
        except ValueError:
            self._time = config.DefaultTime
            print(self._time)
            self.output.addItem('Starting')
            self.t = threading.Thread(target=self.request)
            self.t.start()
        else:
            self.output.addItem('Starting')
            self.t = threading.Thread(target=self.request)
            self.t.start()

    def request(self):
        for i in range(self._repetition):
            sleep(self._time)
            self._r = Request(self._url)
            self._log = Logging(self._r, self._url, dt.now())
            self.output.addItem(f'url:{self._url} | status:{self._r} | date:{dt.now()} ')
        self.output.addItem('End')

if __name__ == '__main__':
    QtWidgets.QApplication.setStyle("fusion")
    app = QtWidgets.QApplication(sys.argv)
    App = Checker()
    App.show()
    app.exec_()  # и запускаем приложение
