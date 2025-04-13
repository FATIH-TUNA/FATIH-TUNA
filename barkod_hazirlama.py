from PyQt5.QtGui import*
from PyQt5.QtCore import*
from PyQt5.QtWidgets import*
import sys,qrcode
import image

class deneme(QDialog):
    def __init__(self):
        super().__init__()
        self.qr=qrcode.QRCode(version=1,error_correction=qrcode.constants.ERROR_CORRECT_L,box_size=20,border=5)
        self.izgara=QGridLayout()

        self.izgara.addWidget(QLabel("VERI GIRINIZ: "),0,0)
        self.veri=QLineEdit()
        self.izgara.addWidget(self.veri,0,1)

        self.izgara.addWidget(QLabel("BASLIK EKLE: "),1,0)
        self.ekle=QLineEdit()
        self.izgara.addWidget(self.ekle,1,1)

        self.buton=QPushButton("TIKLA")
        self.izgara.addWidget(self.buton,2,0)
        self.buton.clicked.connect(self.tikla)


        self.setLayout(self.izgara)
        self.setWindowTitle("MFT")
        self.setGeometry(200,200,800,800)
    def tikla(self):
        self.giris=str(self.veri.text())
        self.baslik=str(self.ekle.text())
        self.qr.add_data(self.giris)
        self.qr.make(fit=True)
        self.resim=self.qr.make_image(fill_color="black",back_color="white")
        self.resim.save(self.baslik)

app=QApplication(sys.argv)
pencere=deneme()
pencere.show()
sys.exit(app.exec_())