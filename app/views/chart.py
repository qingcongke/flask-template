from flask import Blueprint,render_template


mod = Blueprint('chart',__name__,url_prefix='/chart')

@mod.route('/')
def index():
	print("Hello")
	return render_template(
		'chart/index.html',
		name='jeffrey'
	)	
