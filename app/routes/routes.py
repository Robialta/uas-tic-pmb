from app import app, db, mail, login 
from flask_mail import Message
from flask_login import login_user, login_required, logout_user
from app.controllers.admin import Controllersadm
from app.controllers.mahasiswa import Controllersmhs



@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
	 return Controllersmhs().index()

@app.route('/pendaftaran', methods=['POST', 'GET'])
def pendaftaran():
	return Controllersmhs().pendaftaran()

@app.route('/loginmhs', methods=['GET', 'POST'])
def loginmhs():
	return Controllersmhs().loginmhs()

@app.route('/pemberitahuan')
def pemberitahuan():
	return Controllersmhs().pemberitahuan()

@app.route('/info')
@login_required
def info():
	return Controllersmhs().info()

@app.route('/pengumuman')
@login_required
def pengumuman():
	return Controllersmhs().pengumuman()

@app.route('/logoutmhs')
def logoutmhs():
	return Controllersmhs().logoutmhs()





# admin
@app.route('/admin')
def admin():
	return Controllersadm().admin()

@app.route('/loginadmin', methods=['GET', 'POST'])
def loginadmin():
	return Controllersadm().loginadmin()



@app.route('/validasi')
def validasi():
	return Controllersadm().validasi()

@app.route('/tinjau/<int:id>')
def tinjau(id):
	return Controllersadm().tinjau(id)


@app.route('/lolos/<int:id>')
def lolos(id):
	return Controllersadm().lolos(id)

@app.route('/gagal/<int:id>')
def gagal(id):
	return Controllersadm().gagal(id)

@app.route('/konfirmasi')
def konfirmasi():
	return Controllersadm().konfirmasi()

@app.route('/daftarmhs')
def daftarmhs():
	return Controllersadm().daftarmhs()

@app.route('/diterima/<id>', methods=['GET', 'POST'])
def diterima(id):
	return Controllersadm().diterima(id)

@app.route('/ditolak/<id>', methods=['GET', 'POST'])
def ditolak(id):
	return Controllersadm().ditolak(id)

