from flask import Flask, render_template
from smbus import SMBus

addr = 0x8
bus = SMBus(1)

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('ws.html')

@app.route('/on-link/')
def on_link():
 	print ('On selected')
 	bus.write_byte(addr, 0x1)
 	return render_template("ws.html")

@app.route('/off-link/')
def off_link():
 	print('Off selected')
 	bus.write_byte(addr, 0x0)
 	return render_template("ws.html")

if __name__ == '__main__':
 	app.run(host='0.0.0.0')
}
