from app import app, db, mail, login 
from flask import render_template, redirect, flash, url_for
from app.forms.forms import FormDaftar, FormLoginMhs, FormLoginAdmin
from app.models.models import Maba
from flask_mail import Message
from flask_login import login_user, login_required, logout_user



class Controllersadm():

	def admin(self):
		return redirect('loginadmin')

	def loginadmin(self):
		form=FormLoginAdmin()
		if form.is_submitted():
			if form.username.data == 'admin' and form.password.data == 'admin':
				return redirect(url_for('validasi'))
				
			else:
				flash('Username dan password salah', 'danger')
		return render_template('loginadmin.html', title='Login admin', form=form)

	def validasi(self):
		mahasiswadaftar = Maba.query.filter_by(status='mendaftar').all()
		mahasiswalolos = Maba.query.filter_by(status='lolos').all()
		mahasiswagagal = Maba.query.filter_by(status='gagal').all()

		return render_template('validasi.html', title=' Halaman validasi',
							mahasiswadaftar=mahasiswadaftar, 
							mahasiswalolos=mahasiswalolos,
							mahasiswagagal=mahasiswagagal)

	def tinjau(self,id):
		mahasiswa = Maba.query.filter_by(id=id).first()
		return render_template('tinjau.html', title='Tinjau Data', mahasiswa=mahasiswa)

	def lolos(self,id):
		mhs = Maba.query.filter_by(id=id).first()
		mhs.status = 'lolos'
		mhs.no_seleksi = f"010214012{mhs.id}"
		mhs.update()
		msg = Message('Seleksi online', sender='pmb.officialtic@gmail.com', recipients=[mhs.email])
		msg.body = f'''selamat anda lolos, Gunakan kode ini untuk log in {mhs.no_seleksi}'''
		mail.send(msg)
		if mail:
			flash(f'E-mail terkirim ke {mhs.email}', 'success')
		else:
			flash(f'email gagal terkirim ke {mhs.nama}')
		return redirect(url_for('validasi'))

	def gagal(self, id):
		mhs = Maba.query.filter_by(id=id).first()
		mhs.status = 'gagal'
		mhs.update()
		msg = Message('Seleksi online', sender='obyaltha@gmail.com', recipients=[mhs.email])
		msg.body = '''jangan menyerah, tetep semangat di gramedia banyak buku untuk ternak lele '''
		mail.send(msg)
		return redirect(url_for('validasi'))

	def konfirmasi(self):
		mhsinfo=Maba.query.filter_by(status='lolos').all()
		return render_template('konfirmasi.html', title='konfirmasi',mhsinfo=mhsinfo)

	def daftarmhs(self):
		mhs=Maba.query.filter_by(status='LULUS').all()
		return render_template('daftarmhs.html', title='Daftar Mahasiswa Diterima', mhs=mhs)

	def diterima(self, id):
		mhs=Maba.query.filter_by(id=id).first()
		mhs.status='LULUS'
		mhs.update()
		return redirect(url_for('konfirmasi'))

	def ditolak(self, id):
		mhs=Maba.query.filter_by(id=id).first()
		mhs.status='ditolak'
		mhs.update()
		return redirect(url_for('konfirmasi'))


