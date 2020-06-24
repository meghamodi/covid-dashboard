from flask import Flask, render_template, jsonify, request, json
from flask_restful import Resource, Api
import matplotlib
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import io
import base64
import os
import plotly
import plotly.plotly as py
import plotly.graph_objs as go
import numpy as np

# browser caching for last updated
def dir_last_updated(folder):
    return str(max(os.path.getmtime(os.path.join(root_path, f))
                   for root_path, dirs, files in os.walk(folder)
                   for f in files))

companies = [{"id": 1, "name": "Company One"}, {"id": 2, "name": "Company Two"}]
app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True

@app.route('/')
def line():
    count = 500
    xScale = np.linspace(0, 100, count)
    yScale = np.random.randn(count)

    # Create a trace
    trace = go.Scatter(
        x = xScale,
        y = yScale
    )

    data = [trace]
    graphJSON = json.dumps(data, cls=plotly.utils.PlotlyJSONEncoder)
    return render_template('dashboard.html',
                               graphJSON=graphJSON)

@app.route("/")
# def plot_view():
#     fig = Figure()
#     axis = fig.add_subplot(1, 1, 1)
#     axis.set_title("title")
#     axis.set_xlabel("x-axis")
#     axis.set_ylabel("y-axis")
#     axis.grid()
#     axis.plot(range(5), range(5), "ro-")
#
#
#     png_image = io.BytesIO()
#     FigureCanvas(fig).print_png(png_image)
#
#     png_img = "data:image/png;base64,"
#     png_img += base64.b64encode(png_image.getvalue()).decode('utf-8')
#
#     return render_template("dashboard.html",picture=png_img,last_updated=dir_last_updated('static'))

def hello_world():
    return render_template("dashboard.html",last_updated=dir_last_updated('static'))


@app.route('/companies', methods=['GET'])
def get_companies():
  return json.dumps(companies)

if __name__== "__main__":
    app.run(debug=True, threaded=True)
