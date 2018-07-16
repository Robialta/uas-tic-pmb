from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, PasswordField, SelectField,DateField
from wtforms.validators import ValidationError, DataRequired

class FormDaftar(FlaskForm):
	message='Data Tidak Boleh Kosong'		
	nik = StringField('NIK', validators=[DataRequired(message=message)])
	nama = StringField('Nama', validators=[DataRequired(message=message)])
	email = StringField('E-mail', validators=[DataRequired(message=message)])
	status = StringField('Status', validators=[DataRequired(message=message)])
	prodi1 = SelectField('Prodi pilihan 1', choices=[('','Pilih Jurusan'),
														('TEKNIK INFORMATIKA', 'TEKNIK INFORMATIKA'),
														('SISTEM INFORMASI','SISTEM INFORMASI'),
														('TEKNIK LINGKUNGAN','TEKNIK LINGKUNGAN'),
														('TEKNIK KOMPUTER','TEKNIK KOMPUTER'),
														('MANAJEMEN INFORMATIKA','MANAJEMEN INFORMATIKA')], validators=[DataRequired(message=message)])
	prodi2 = SelectField('Prodi pilihan 2', choices=[('','Pilih Jurusan'),
														('TEKNIK INFORMATIKA', 'TEKNIK INFORMATIKA'),
														('SISTEM INFORMASI','SISTEM INFORMASI'),
														('TEKNIK LINGKUNGAN','TEKNIK LINGKUNGAN'),
														('TEKNIK KOMPUTER','TEKNIK KOMPUTER'),
														('MANAJEMEN INFORMATIKA','MANAJEMEN INFORMATIKA')], validators=[DataRequired(message=message)])
	jenis_kelamin = SelectField('Jenis kelamin', choices=[('','Pilih jenis kelamin'),
														('Pria', 'Pria'),
														('Wanita','Wanita')], validators=[DataRequired(message=message)])
	ttl = StringField('Tempat Tanggal Lahir', validators=[DataRequired(message=message)])
	alamat = StringField('Alamat', validators=[DataRequired(message=message)])
	agama = SelectField('Agama', choices=[('','Pilih Agama'),
														('ISLAM', 'ISLAM'),
														('KRISTEN','KRISTEN'),
														('BUDHA','BUDHA'),
														('HINDU','HINDU'),
														('KONGUCHU','KONGUCHU')], validators=[DataRequired(message=message)])
	no_hp = StringField('No HP', validators=[DataRequired(message=message)])
	asal_sekolah = StringField('Asal Sekolah', validators=[DataRequired(message=message)])
	tahun_lulus = StringField('Tahun Lulus', validators=[DataRequired(message=message)])
	jurusan_sma = StringField('Jurusan di SLTA', validators=[DataRequired(message=message)])
	nama_wali = StringField('Nama Wali', validators=[DataRequired(message=message)])
	pekerjaan_wali = StringField('Pekerjaan Wali', validators=[DataRequired(message=message)])
	penghasilan_wali = SelectField('Penghasilan wali', choices=[('','Penghasilan wali'),
														(500000,'500000'),
														(1000000,'1000000'),
														(1500000,'1500000'),
														(2000000,'2000000'),], validators=[DataRequired(message=message)])
	daftar = SubmitField('Daftar')

class FormLoginMhs(FlaskForm):
	no_seleksi = StringField('Nomor Seleksi')
	password = PasswordField('Password')
	login = SubmitField('Login')

class FormLoginAdmin(FlaskForm):
	username = StringField('Username')
	password = PasswordField('Password')
	login = SubmitField('Login')