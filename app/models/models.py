from app import db, login
from datetime import datetime
from flask_login import UserMixin

@login.user_loader
def load_user(user_id):
    return Maba.query.get(user_id)

class Maba(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    nik = db.Column(db.String(20), nullable=False)
    nama = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(50), nullable=False, unique=True)
    status = db.Column(db.String(20), nullable=True)
    prodi1 = db.Column(db.String(15), nullable=False)
    prodi2 = db.Column(db.String(15), nullable=False)
    no_seleksi = db.Column(db.String(10), nullable=True)
    jenis_kelamin = db.Column(db.String(15), nullable=False)
    ttl = db.Column(db.String(100), nullable=False)
    alamat = db.Column(db.String(100), nullable=False)
    agama = db.Column(db.String(10), nullable=False)
    no_hp = db.Column(db.String(15), nullable=True)
    asal_sekolah = db.Column(db.String(30), nullable=False)
    tahun_lulus = db.Column(db.Integer, nullable=False)
    jurusan_sma = db.Column(db.String(20), nullable=False)
    nama_wali = db.Column(db.String(50), nullable=False)
    pekerjaan_wali = db.Column(db.String(30), nullable=False)
    penghasilan_wali = db.Column(db.Integer, nullable=False)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        return db.session.commit()
    