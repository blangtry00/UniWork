from flask import Flask, Blueprint, render_template, request
from werkzeug.middleware.proxy_fix import ProxyFix
from argparse import ArgumentParser
from CVD_breast_cancer_model import *

appweb = Blueprint('hello', __name__)

@appweb.route('/')
def home():
    return render_template("index.html")

@appweb.route('/send', methods=['POST'])

#Creating menu for web app
def send(predict = None):

    if request.method == 'POST':

        radiusMean =request.form['radius_m']
        textureMean = request.form['texture_m']
        perimeterMean = request.form['perimeter_m']
        areaMean= request.form['area_m']
        smoothnessMean = request.form['smoothness_m']
        compactnessMean = request.form['compactness_m']
        concavityMean = request.form['concavity_m']
        concaveMean = request.form['concave_m']
        symmetryMean =request.form['symmetry_m']
        fractalMean = request.form['frac_dim_m']

        #Gets standard Error
        radiusSE =request.form['radius_se']
        textureSE = request.form['texture_se']
        perimeterSE = request.form['perimeter_se']
        areaSE= request.form['area_se']
        smoothnessSE = request.form['smoothness_se']
        compactnessSE = request.form['compactness_se']
        concavitySE = request.form['concavity_se']
        concaveSE = request.form['concave_point_se']
        symmetrySE =request.form['symmetry_se']
        fractalSE = request.form['frac_dim_se']

        #Gets worst Mean
        radiusWorst =request.form['radius_worst']
        textureWorst = request.form['texture_worst']
        perimeterWorst = request.form['perimeter_worst']
        areaWorst= request.form['area_worst']
        smoothnessWorst = request.form['smoothness_worst']
        compactnessWorst = request.form['compactness_worst']
        concavityWorst = request.form['concavity_worst']
        concaveWorst = request.form['concave_point_worst']
        symmetryWorst =request.form['symmetry_worst']
        fractalWorst = request.form['frac_dim_worst']

        #gets model
        model.fit(x_train, y_train)
        acc = model.score(x_train, y_train)
        #predicts the outcome based on input data
        predict_real = model.predict([[radiusMean, textureMean, perimeterMean, areaMean, smoothnessMean, compactnessMean,
            concavityMean, concaveMean, symmetryMean, fractalMean, radiusSE, textureSE, perimeterSE,
            areaSE, smoothnessSE, compactnessSE, concavitySE, concaveSE, symmetrySE, fractalSE,
            radiusWorst, textureWorst, perimeterWorst, areaWorst, smoothnessWorst, compactnessWorst,
            concavityWorst, concaveWorst, symmetryWorst, fractalWorst]])

            #1 = benign and 0 = malignant
        if (predict_real == [1]):
            predict = "The result returned with " + str(
                round(acc, 2) * 100) + "% accuracy and you have low chance of having breast cancer"
        else:
            predict = "The result returned with " + str(
                round(acc, 2) * 100) + "% accuracy and you have a high chance of having breast cancer"

        return render_template('index.html', predict=predict)

    else:

        return render_template('index.html', predict=predict)



@appweb.route('/about')
def about():
    return render_template("about.html")



if __name__ == '__main__':

    # arg parser for the standard anaconda-project options
    parser = ArgumentParser(prog="home",
                            description="Simple Flask Application")
    parser.add_argument('--anaconda-project-host', action='append', default=[],
                        help='Hostname to allow in requests')
    parser.add_argument('--anaconda-project-port', action='store', default=8086, type=int,
                        help='Port to listen on')
    parser.add_argument('--anaconda-project-iframe-hosts',
                        action='append',
                        help='Space-separated hosts which can embed us in an iframe per our Content-Security-Policy')
    parser.add_argument('--anaconda-project-no-browser', action='store_true',
                        default=False,
                        help='Disable opening in a browser')
    parser.add_argument('--anaconda-project-use-xheaders',
                        action='store_true',
                        default=False,
                        help='Trust X-headers from reverse proxy')
    parser.add_argument('--anaconda-project-url-prefix', action='store', default='',
                        help='Prefix in front of urls')
    parser.add_argument('--anaconda-project-address',
                        action='store',
                        #default='0.0.0.0',
                        help='IP address the application should listen on.')

    args = parser.parse_args()

    app = Flask(__name__)
    app.register_blueprint(appweb, url_prefix = args.anaconda_project_url_prefix)

    app.config['PREFERRED_URL_SCHEME'] = 'https'

    app.wsgi_app = ProxyFix(app.wsgi_app)
    app.run(host=args.anaconda_project_address, port=args.anaconda_project_port)

#Reference
#Author: Unknown
#Date: Trimester 1 2023
#Title: Program called Heart Disease Predictor Capstone Project
#Version 1
#Source Code
#Template used from https://uclearn.canberra.edu.au/courses/14056/pages/week-10-project-assignment-workshop?module_item_id=1064187
