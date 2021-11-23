{\rtf1\ansi\ansicpg1252\cocoartf2578
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 from flask import Flask, render_template\
from smbus import SMBus\
\
addr = 0x8\
bus = SMBus(1)\
\
app = Flask(__name__)\
\
@app.route('/')\
def index():\
	return render_template('ws.html')\
\
@app.route('/on-link/')\
def on_link():\
 	print ('On selected')\
 	bus.write_byte(addr, 0x1)\
 	return render_template("ws.html")\
\
@app.route('/off-link/')\
def off_link():\
 	print('Off selected')\
 	bus.write_byte(addr, 0x0)\
 	return render_template("ws.html")\
\
if __name__ == '__main__':\
 	app.run(host='0.0.0.0')\
\
}