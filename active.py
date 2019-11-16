import sys
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWebEngineWidgets import *

if __name__ == '__main__':
    app = QApplication(sys.argv)
 
    web = QWebEngineView()
    web.load(QUrl(sys.argv[1]))
    web.show()
    
    sys.exit(app.exec_())