from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
#koneksi ke database
app.config["SQLALCHEMY_DATABASE_URI"] ='mysql://root:''@localhost/rara'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)
app.app_context().push()
class penyakit(db.Model):
    kd_penyakit = db.Column(db.Integer, primary_key=True)
    nama_penyakit = db.Column(db.String(80), unique=True)
    def __init__(self, nama_penyakit):
        self.nama_penyakit=nama_penyakit
        class gejala(db.Model):
            kd_gejala = db.Column(db.Integer, primary_key=True)
            gejala = db.Column(db.String(80), unique=True)
            def __init__(self, gejala):
                self.gejala=gejala