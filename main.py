import sys
from custome_errors import *
sys.excepthook = my_excepthook
import random
from webbrowser import open as openLink
import language
import app
import PyQt6.QtWidgets as qt
import PyQt6.QtGui as qt1
from PyQt6.QtCore import Qt
language.init_translation()
class main (qt.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle(app.name + _("version : ") + str(app.version))
        self.kbl=qt.QCheckBox(_("capital letters"))
        self.kbl.setChecked(True)
        self.sml=qt.QCheckBox(_("small letters"))
        self.sml.setChecked(True)
        self.num=qt.QCheckBox(_("numbers"))
        self.num.setChecked(True)
        self.sy=qt.QCheckBox(_("symboles"))
        self.sy.setChecked(True)
        self.length=qt.QSlider()
        self.length.setRange(5,5000000)
        self.length.setAccessibleName(_("password length"))
        self.generate=qt.QPushButton(_("generate"))
        self.generate.setDefault(True)
        self.generate.clicked.connect(self.fgenrate)
        self.re=qt.QTextEdit()
        self.re.setAccessibleName(_("result"))
        self.re.setReadOnly(True)
        layout=qt.QVBoxLayout()
        layout.addWidget(self.kbl)
        layout.addWidget(self.sml)
        layout.addWidget(self.num)
        layout.addWidget(self.sy)
        layout.addWidget(self.length)
        layout.addWidget(self.generate)
        layout.addWidget(self.re)
        w=qt.QWidget()
        w.setLayout(layout)
        self.setCentralWidget(w)
        mb=self.menuBar()
        help=mb.addMenu(_("help"))
        cus=help.addMenu(_("contact us"))
        telegram=qt1.QAction("telegram",self)
        cus.addAction(telegram)
        telegram.triggered.connect(lambda:openLink("https://t.me/mesteranasm"))
        telegramc=qt1.QAction(_("telegram channel"),self)
        cus.addAction(telegramc)
        telegramc.triggered.connect(lambda:openLink("https://t.me/tprogrammers"))
        donate=qt1.QAction(_("donate"),self)
        help.addAction(donate)
        donate.triggered.connect(lambda:openLink("https://www.paypal.me/AMohammed231"))
        about=qt1.QAction(_("about"),self)
        help.addAction(about)
        about.triggered.connect(lambda:qt.QMessageBox.information(self,_("about"),_("{} version: {} description: {} developer: {}").format(app.name,str(app.version),app.description,app.creater)))
        self.setMenuBar(mb)
    def fgenrate(self):
        all=[]
        sy="! @ # $ % ^ & * /"
        sml="a b c d e f g h i j k l m n o p q r s t u v x y z"
        kbl=sml.upper()
        num="1 2 3 4 5 6 7 8 9 0"
        if self.sy.isChecked():
            all.extend(sy.split(" "))
        if self.sml.isChecked():
            all.extend(sml.split(" "))
        if self.kbl.isChecked():
            all.extend(kbl.split(" "))
        if self.num.isChecked():
            all.extend(num.split(" "))
        if all==[]:
            qt.QMessageBox.information(self,_("error"),_("please choose 1 to generate password"))
            return
        re=[]
        for i in range(0,self.length.value()):
            re.append(random.choice(all))
        self.re.setText("".join(re))
        self.re.setFocus()

App=qt.QApplication([])
w=main()
w.show()
App.exec()