from flask import Flask, render_template, request

app = Flask(__name__)
app.config["DEBUG"] = True


@app.route('/')
def baslangic():
    return render_template("anasayfa.html")


@app.route('/egitim')
def egitim_bilgileri():
    ilkokulum = "Yüzüncü Yıl " + "İlkokulu"
    okullarim = ["Muğla Anadolu Lisesi", "Ege Üniversitesi", "Boğaziçi Üniversitesi", "Trakya Üniversitesi"]
    return render_template("egitim.html", ilkokul=ilkokulum, okullarim=okullarim)


@app.route('/isdeneyimi')
def isdeneyimi_bilgileri():
    return render_template("isdeneyimi.html")


@app.route('/iletisim')
def iletisim_sayfasi():
    return render_template("iletisim.html")

@app.route('/mesajkaydet', methods=['POST'])
def mesaj_kaydet():
    adsoyad = request.form.get('adsoyad')
    eposta = request.form.get('eposta')
    telefon = request.form.get('telefon')
    mesaj = request.form.get('mesaj')
    satir = adsoyad + "||" + eposta + "||" + telefon + "||" + mesaj + "\n"
    f = open("mesajlar.txt", "a")
    f.write(satir)
    f.close()
    return "Sayın " + adsoyad + ". Mesajınız için teşekkürler."


if __name__ == "__main__":
    app.run()
