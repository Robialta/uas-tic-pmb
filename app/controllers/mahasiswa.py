from app import app, db, mail, login 
from flask import render_template, redirect, flash, url_for
from app.forms.forms import FormDaftar, FormLoginMhs, FormLoginAdmin
from app.models.models import Maba
from flask_mail import Message
from flask_login import login_user, login_required, logout_user

class Controllersmhs():
	def index(self):
		return render_template('index.html', title='Home')

	def pendaftaran(self):
		form = FormDaftar()
		if form.is_submitted():
			maba = Maba(nik=form.nik.data,
						nama=form.nama.data.upper(),
						email=form.email.data,
						status='mendaftar',
						prodi1=form.prodi1.data,
						prodi2=form.prodi2.data,
		
						jenis_kelamin=form.jenis_kelamin.data,
						ttl=form.ttl.data,
						alamat=form.alamat.data,
						agama=form.agama.data,
						no_hp=form.no_hp.data,
						asal_sekolah=form.asal_sekolah.data,
						tahun_lulus=form.tahun_lulus.data,
						jurusan_sma=form.jurusan_sma.data,
						nama_wali=form.nama_wali.data.upper(),
						pekerjaan_wali=form.pekerjaan_wali.data,
						penghasilan_wali=form.penghasilan_wali.data,
						)
			maba.save()
			flash(f'Terimakasih, pendaftaran anda berhasil!', 'success')
			return redirect('pemberitahuan')
		return render_template('pendaftaran.html', title='Pendaftaran', form=form)

	def loginmhs(self):
		form = FormLoginMhs()
		if form.is_submitted():
			maba=Maba()
			mhs = Maba.query.filter_by(no_seleksi=form.no_seleksi.data).first()
			if mhs and form.password.data== mhs.no_seleksi :
				login_user(mhs)
				flash(f'login berhasil', 'success')
				return redirect('info')
				
			else:
				flash("gagal, pastikan No. seleksi yang anda masukkan benar!", 'danger')
		return render_template('loginmhs.html', title='Login', form=form)

	def pemberitahuan(self):
		return render_template('pemberitahuan.html', title='pemberitahuan')

	def info(self):
		
		return render_template('info.html', title='Informasi ')

	def pengumuman(self):
		mhs_hasil=Maba.query.filter_by(status='LULUS')
		return render_template('pengumuman.html', title='pengumuman', mhs_hasil=mhs_hasil)

	def logoutmhs(self):
		logout_user()
		return redirect(url_for('loginmhs'))




