import sys
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtCore import *


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl('http://google.com'))
        self.setCentralWidget(self.browser)
        self.showMaximized()

        #navigation Bar:
        navbar = QToolBar()
        self.addToolBar(navbar)

        #back button:
        back_button = QAction('back',self)
        back_button.triggered.connect(self.browser.back)
        navbar.addAction(back_button)

        #Foward button:
        Forward_button = QAction('forward', self)
        Forward_button.triggered.connect(self.browser.forward)
        navbar.addAction(Forward_button)

        #Reload Button
        Reload_button = QAction('reload', self)
        Reload_button.triggered.connect(self.browser.reload)
        navbar.addAction(Reload_button)

        #Home Button
        Home_button = QAction('home', self)
        Home_button.triggered.connect(self.navigate_home)
        navbar.addAction(Home_button)

        #search bar:
        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        navbar.addWidget(self.url_bar)

        #changing the url back to the url we are at:
        self.browser.urlChanged.connect(self.url_update)

    def navigate_home(self):
        self.browser.setUrl(QUrl('http://google.com'))
    def navigate_to_url(self):
        url = self.url_bar.text()
        print("Navigating to:", url)
        self.browser.setUrl(QUrl(url))
    def url_update(self, url):
        self.url_bar.text(url.toString)



app = QApplication(sys.argv)
QApplication.setApplicationName('Voyager')
window = MainWindow()
app.exec_()