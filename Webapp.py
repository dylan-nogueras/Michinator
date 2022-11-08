from flask import Flask, render_template, url_for, request, redirect, current_app
from Michi import Michi

app = Flask(__name__, static_url_path='/static')

@app.route('/index.html', methods=['GET', 'POST'])
def home():
	michi = Michi().generate_michi()
	return render_template('index.html', archivo=michi['img'], descripcion=michi['title'])

if __name__ == '__main__':
   app.run()
   
