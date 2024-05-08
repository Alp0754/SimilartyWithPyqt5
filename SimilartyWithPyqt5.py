from PyQt5 import QtWidgets
import sqlite3
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class KarsilastirmaPenceresi1(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Karsilastirma Ekranı")
        self.setGeometry(600, 200, 600, 600)

        self.textbox = QtWidgets.QTextEdit(self)
        self.textbox.move(250, 200)
        self.textbox.resize(100, 50)
        
 
        buton = QtWidgets.QPushButton(self)
        buton.setText('Seç')
        buton.move(350, 200)

        self.textbox1= QtWidgets.QTextEdit(self)
        self.textbox1.move(250, 300)
        self.textbox1.resize(100, 50)

        buton1 = QtWidgets.QPushButton(self)
        buton1.setText('Seç')
        buton1.move(350, 300)

        self.etiket = QtWidgets.QLabel(self)
        self.etiket.setText('Cosinüs Benzerlik:')
        self.etiket.move(250, 400)
        buton.clicked.connect(self.dosyaSec)
        buton1.clicked.connect(self.dosyaSec1)
        
        buton2 = QtWidgets.QPushButton(self)
        buton2.setText('Karşılaştır')
        buton2.move(300, 450)
        buton2.clicked.connect(self.handleKarsilastir)

    def dosyaSec(self):
        dosyaisim, _ = QtWidgets.QFileDialog.getOpenFileName(self, 'Dosya Seç', '')    
        if dosyaisim:
            self.textbox.setText(dosyaisim)
    def dosyaSec1(self):
        dosyaisim, _ = QtWidgets.QFileDialog.getOpenFileName(self, 'Dosya Seç', '')    
        if dosyaisim:
            self.textbox1.setText(dosyaisim)        
    def handleKarsilastir(self):
        dosyayolu=self.textbox.toPlainText()
        dosyayolu1=self.textbox1.toPlainText()
        dosya=open(dosyayolu,"r")
        text1=dosya.read()
        dosya2=open(dosyayolu1,"r")
        text2=dosya2.read()
        vectorizer = CountVectorizer().fit_transform([text1, text2])
        vectors = vectorizer.toarray()
        cos_sim = cosine_similarity([vectors[0]], [vectors[1]])[0][0]
        self.etiket.setText(f"Benzerlik Oranı: {cos_sim}")






class KarsilastirmaPenceresi(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Karsilastirma Ekranı")
        self.setGeometry(600, 200, 600, 600)

        self.textbox = QtWidgets.QTextEdit(self)
        self.textbox.move(250, 200)
        self.textbox.resize(100, 50)
        
 
        buton = QtWidgets.QPushButton(self)
        buton.setText('Seç')
        buton.move(350, 200)

        self.textbox1= QtWidgets.QTextEdit(self)
        self.textbox1.move(250, 300)
        self.textbox1.resize(100, 50)

        buton1 = QtWidgets.QPushButton(self)
        buton1.setText('Seç')
        buton1.move(350, 300)

        self.etiket = QtWidgets.QLabel(self)
        self.etiket.setText('Jaccard Benzerlik:')
        self.etiket.move(250, 400)
        buton.clicked.connect(self.dosyaSec)
        buton1.clicked.connect(self.dosyaSec1)
        
        buton2 = QtWidgets.QPushButton(self)
        buton2.setText('Karşılaştır')
        buton2.move(300, 450)
        buton2.clicked.connect(self.handleKarsilastir)

    def dosyaSec(self):
        dosyaisim, _ = QtWidgets.QFileDialog.getOpenFileName(self, 'Dosya Seç', '')    
        if dosyaisim:
            self.textbox.setText(dosyaisim)
    def dosyaSec1(self):
        dosyaisim, _ = QtWidgets.QFileDialog.getOpenFileName(self, 'Dosya Seç', '')    
        if dosyaisim:
            self.textbox1.setText(dosyaisim)        
    def handleKarsilastir(self):
        dosyayolu=self.textbox.toPlainText()
        dosyayolu1=self.textbox1.toPlainText()
        dosya=open(dosyayolu,"r")
        text1=dosya.read()
        dosya2=open(dosyayolu1,"r")
        text2=dosya2.read()
        kume1=set(text1.split())
        kume2=set(text2.split())
        kesisim=len(kume1 & kume2)
        birlesim=len(kume1|kume2)
        benzerlik=kesisim/birlesim
        self.etiket.setText(f"Benzerlik Oranı: {benzerlik}")


class DegistirPenceresi(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Sifre Güncelleme Ekranı")
        self.setGeometry(600, 200, 600, 600)
        
        etiket = QtWidgets.QLabel(self)
        etiket.setText('Kullanıcı Adı Giriniz')
        etiket.move(350, 200)

        self.giris = QtWidgets.QLineEdit(self)
        self.giris.move(350, 230)

        etiket1 = QtWidgets.QLabel(self)
        etiket1.setText('Yeni Şifreyi Giriniz')
        etiket1.move(350, 260)

        self.giris1 = QtWidgets.QLineEdit(self)
        self.giris1.move(350, 290)
        
        buton = QtWidgets.QPushButton(self)
        buton.setText('Güncelle')
        buton.move(350, 320)
        
        buton.clicked.connect(self.guncelle)

    def guncelle(self):
        ad=self.giris.text()
        sifre=int(self.giris1.text())
        imlec.execute("SELECT * FROM kullaniciBilgi WHERE Ad=?", (ad,))
        kullanici = imlec.fetchone()
        if kullanici:
            imlec.execute("UPDATE kullaniciBilgi SET Sifre=? WHERE Ad=?", (sifre, ad))
            baglan.commit()
            QtWidgets.QMessageBox.information(self, "Başarılı", "Şifre başarıyla güncellendi.")
        else:
            QtWidgets.QMessageBox.warning(self, "Hatalı", "Kullanıcı bulunamadı.")


class MenuPenceresi(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Menü")
        self.resize(400, 400)
        menubar = self.menuBar()
        karsilastir = menubar.addMenu("Karşılaştır")
        islemler = menubar.addMenu("İşlemler")
        cikis = menubar.addMenu("Çıkış")
        

        degistir = QtWidgets.QAction("Degiştir", self)
        sifre=islemler.addMenu('Şifre')
        sifre.addAction(degistir)
        
        metinY = QtWidgets.QAction("metniJaccardAlgoritmasıKullanarakKarsilastir", self)
        karsilastir.addAction(metinY)

        metinX = QtWidgets.QAction("metniCosinüsAlgoritmasıKullanarakKarsilastir", self)
        karsilastir.addAction(metinX)
        def DegistirPencere():
            self.guncelle_penceresi = DegistirPenceresi()
            self.guncelle_penceresi.show()
        

        degistir.triggered.connect(DegistirPencere)

        cikisYap=QtWidgets.QAction('CikisYap',self)
        cikis.addAction(cikisYap)

        cikisYap.triggered.connect(QtWidgets.qApp.quit)
        
        def KarsilastirPencere():
            self.karsi_penceresi = KarsilastirmaPenceresi()
            self.karsi_penceresi.show()
        def KarsilastirPencere1():
            self.karsi_penceresi = KarsilastirmaPenceresi1()
            self.karsi_penceresi.show()
        metinY.triggered.connect(KarsilastirPencere)    
        metinX.triggered.connect(KarsilastirPencere1)
class GirisPenceresi(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Giriş Ekranı")
        self.setGeometry(600, 200, 800, 800)

        etiket = QtWidgets.QLabel(self)
        etiket.setText('Kullanıcı Adı Giriniz')
        etiket.move(350, 200)

        self.giris = QtWidgets.QLineEdit(self)
        self.giris.move(350, 230)

        etiket1 = QtWidgets.QLabel(self)
        etiket1.setText('Şifre Giriniz')
        etiket1.move(350, 260)

        self.giris1 = QtWidgets.QLineEdit(self)
        self.giris1.setEchoMode(QtWidgets.QLineEdit.Password)
        self.giris1.move(350, 290)

        buton = QtWidgets.QPushButton(self)
        buton.setText('Giriş')
        buton.move(350, 320)

        buton1 = QtWidgets.QPushButton(self)
        buton1.setText('Kayıt Ol')
        buton1.move(500, 320)

        buton.clicked.connect(self.girisYap)
        buton1.clicked.connect(self.kayitOl)

    def girisYap(self):
        ad = self.giris.text()
        sifre = int(self.giris1.text())
        imlec.execute("SELECT * FROM kullaniciBilgi WHERE Ad=? AND Sifre=?", (ad, sifre))
        kullanici = imlec.fetchone()
        if kullanici:
            QtWidgets.QMessageBox.information(self, "Başarılı Giriş", "Giriş Başarılı!")
            self.menu_penceresi = MenuPenceresi()
            self.menu_penceresi.show()     
        else:
            QtWidgets.QMessageBox.warning(self, "Hatalı Giriş", "Hatalı Kullanıcı Adı veya Şifre!")

    def kayitOl(self):
        ad = self.giris.text()
        sifre = int(self.giris1.text())
        imlec.execute("SELECT * FROM kullaniciBilgi WHERE Ad=?", (ad,))
        kullanici = imlec.fetchone()
        if kullanici:
            QtWidgets.QMessageBox.warning(self, "Kayıt Hatası", "Bu kullanıcı zaten kayıtlı!")
        else:
            imlec.execute("INSERT INTO kullaniciBilgi VALUES(?, ?)", (ad, sifre))
            baglan.commit()
            QtWidgets.QMessageBox.information(self, "Başarılı Kayıt", "Kayıt başarıyla eklendi.")
    
if __name__ == "__main__":
    
    uyg = QtWidgets.QApplication([])

    baglan = sqlite3.connect('kullaniciVeritabani.db')
    imlec = baglan.cursor()
    imlec.execute("CREATE TABLE IF NOT EXISTS kullaniciBilgi(Ad TEXT, Sifre INT)")

    pencere = GirisPenceresi()
    pencere.show()

    uyg.exec_()
    baglan.close()

