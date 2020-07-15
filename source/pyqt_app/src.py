import sys
from PyQt5.QtWidgets import * 
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import *
from models import *

class Window(QWidget):
    

    def __init__(self):
        super().__init__()
        
        self.sirState = 0
        self.seirdState = 0
        self.initUI()
    
    def initUI(self):
        self.sirRadiobutton = QRadioButton(self)
        self.seirdRadiobutton = QRadioButton(self)
        
        self.sirLabel = QLabel('Build a SIR model')
        self.seirdLabel = QLabel('Build a SEIRD model')
        self.buildButton = QPushButton('Build') 
        
        hSirButtonBox = QHBoxLayout()
        hSirButtonBox.addWidget(self.sirLabel)
        hSirButtonBox.addWidget(self.sirRadiobutton)

        hSeirdButtonBox = QHBoxLayout()
        hSeirdButtonBox.addWidget(self.seirdLabel)
        hSeirdButtonBox.addWidget(self.seirdRadiobutton)

        vlBox = QVBoxLayout()
        vlBox.addLayout(hSirButtonBox)
        vlBox.addLayout(hSeirdButtonBox)
        vlBox.addWidget(self.buildButton)
        
        grid = QGridLayout()
        names = ['Susceptible', 'Exposed',
                 'Infected', 'Recovered',
                 'Dead', 'Beta (x1000)', 'Gamma (x1000)',
                 'Mu (x1000)', 'Delta (x1000)'
        ]
        self.widgetList = []
        label = QLabel()
        slider = QSlider()
        spinbox = QSpinBox()
        for i in range(9):
            for j in range(3):
                label = QLabel()
                slider = QSlider()
                spinbox = QSpinBox()
                if(j == 0):
                    label = QLabel(names[i], self)
                    grid.addWidget(label, i, j)
                    self.widgetList.append(label)
                if(j == 1 and i < 5):
                    slider = QSlider(Qt.Horizontal, self)
                    slider.setRange(0, 1000000000)
                    grid.addWidget(slider, i, j)
                    self.widgetList.append(slider)
                if(j == 1 and i > 4):
                    slider = QSlider(Qt.Horizontal, self)
                    slider.setRange( 0, 5000)
                    grid.addWidget(slider, i, j)
                    self.widgetList.append(slider)
                if(j == 2 and i < 5):
                    spinbox = QSpinBox(self)
                    spinbox.setRange(0, 1000000000)
                    grid.addWidget(spinbox, i, j)
                    self.widgetList.append(spinbox)
                if(j == 2 and i > 4):
                    spinbox = QSpinBox(self)
                    spinbox.setRange(0, 5000)
                    grid.addWidget(spinbox, i, j)
                    self.widgetList.append(spinbox)


        for i in range(9):
            sl = self.widgetList[i*3 + 1]
            sp = self.widgetList[i*3 + 2]
            sl.valueChanged.connect(sp.setValue)
            sp.valueChanged.connect(sl.setValue)
        
        self.sirRadiobutton.toggled.connect(lambda:self.buttonState(1))
        self.seirdRadiobutton.toggled.connect(lambda:self.buttonState(2))
        self.buildButton.clicked.connect(self.buildModel)
        commonBox = QHBoxLayout()
        commonBox.addLayout(vlBox)
        commonBox.addLayout(grid)
    
        self.setLayout(commonBox)
    

    def buttonState(self, n):
        if n == 1:
            if self.sirRadiobutton.isChecked() == True:
                self.sirState = 1
            else:
                self.sirState = 0
                
                
        if n == 2:
            if self.seirdRadiobutton.isChecked() == True:
                self.seirdState = 1
            else:
                self.seirdState = 0


    def buildModel(self):
        if self.sirState == 1:
            self.buildSir()
        if self.seirdState == 1:
            self.buildSeird()        
        
        
    def buildSir(self):
        S0 = int(self.widgetList[1].value())
        I0 = int(self.widgetList[7].value())
        R0 = int(self.widgetList[10].value())
        b = float(self.widgetList[16].value()) / 1000
        g = float(self.widgetList[19].value()) / 1000
        SIR_instance = SIR(b, g, S0, I0, R0)
        SIR_instance.build()


    def buildSeird(self):
        S0 = int(self.widgetList[1].value())
        E0 = int(self.widgetList[4].value())
        I0 = int(self.widgetList[7].value())
        R0 = int(self.widgetList[10].value())
        D0 = int(self.widgetList[13].value())
        b = float(self.widgetList[16].value()) / 1000
        g = float(self.widgetList[19].value()) / 1000
        m = float(self.widgetList[22].value()) / 1000
        d = float(self.widgetList[25].value()) / 1000
        SEIRD_instance = SEIRD(b, g, d, m,  S0, E0, I0, R0, D0)
        SEIRD_instance.s_build()


class MainWindow(QMainWindow):


    def __init__(self):
        super().__init__()
        self.initUI()


    def initUI(self):
        self.initMenubar()
        win = Window()
        self.setCentralWidget(win)
        win.sirRadiobutton.toggled.connect(self.toggledEvent)
        win.seirdRadiobutton.toggled.connect(self.toggledEvent)
        
        self.statusBar().showMessage('Choose the type of your model:')


        self.resize(700, 350)
        self.center()

        self.setWindowTitle('Pandemic statistics')
        self.setWindowIcon(QIcon('graphic.png'))
        self.show()
    

    def initMenubar(self):
        exitAction = QAction(QIcon('exit.png'), '&Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(qApp.quit)

        openAction = QAction(QIcon('open.png'), '&Open', self)
        openAction.setShortcut('Ctrl+O')
        openAction.setStatusTip('Open file')
        
        infoAction = QAction(QIcon('info.png'), '&Info', self)
        infoAction.setShortcut('Ctrl+I')
        infoAction.setStatusTip('Read info')

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(exitAction)
        fileMenu.addAction(openAction)

        infoMenu = menubar.addMenu('&Info')
        infoMenu.addAction(infoAction)


    def toggledEvent(self):
        self.statusBar().showMessage('Press the "Build" button to build your model:')


    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Message',
            'Are you sure want to quit?', QMessageBox.Yes |
            QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


    def center(self):

        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = MainWindow()
    sys.exit(app.exec_())