import flask
import pprint
import numpy as np
from flask import request, jsonify, Response
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
from numpy import *
app=flask.Flask(_name_)
app.config["DEBUG"]=True

matrix = [
[0,0,0,0,0],
[1,0,0,0,5],
[0,2,0,4,0],
[0,0,3,0,0],
[0,0,0,0,0],
]
# use dictionary comprehension
dic_rc = {(rx, cx): c for rx, r in enumerate(matrix)\
                for cx, c in enumerate(r)}
pprint.pprint(matrix, width=30)
print('-'*32)
# show the dictionary of the matrix
pprint.pprint(dic_rc)
print('-'*30)

[x1,x2] = [3,3]
[y1,y2] = [2,2]
[z1,z2] = [1,1]

[v1,v2]= [(y1-x1),(y2-x2)]
[w1,w2]= [(z1-y1),(z2-y2)]

[ans1,ans2]=[(v1+w1+y1),(v2+w2+y2)]

print([ans1,ans2])

from matplotlib import pyplot as plt

def f(t):
	data = np.array([
		[3,3],
		[2,2],
		[1,1],
		[2,3],
		[1,4]
	])
	x, y = data.T
	plt.scatter(x,y)
	plt.scatter(ans1,ans2,color='red')
	plt.show()


@app.route('/', methods=['GET'])
def home():
    return '''<h1>Distant Reading Archive</h1>
<p>A prototype API for distant reading of science fiction novels.</p>'''

@app.route('/plot')
def func():
	data = np.array([
	[3,3],
	[2,2],
	[1,1],
	[2,3],
	[1,4]
	])
	x, y = data.T
	plt.scatter(x,y)
	plt.scatter(ans1,ans2,color='red')
	plt.show()

@app.route('/plot.png')
def plot_png():
    fig = create_figure()
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')

def create_figure():
    fig = Figure()
    axis = fig.add_subplot(1, 1, 1)
    xs = range(100)
    ys = [random.randint(1, 50) for x in xs]
    axis.plot(xs, ys)
    return fig



# A route to return all of the available entries in our catalog.
@app.route('/api/v1/resources/dic_rc/all', methods=['GET'])
def api_all():
    return jsonify(dic_rc)
app.run()