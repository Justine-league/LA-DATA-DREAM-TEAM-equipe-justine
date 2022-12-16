import sys
import subprocess
import json
from os.path import exists

from pages.form_to_predict import Form_to_predict
from pages.form_to_predict import Form_to_predict


def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])


# subprocess.Popen('echo "Geeks 4 Geeks"', shell=True)

pips_install = ['numpy', 'pandas', "Flask ", "flask-restful", "flask-cors"]

# for pip in pips_install:
#     try:
#         install(pip)
#     except:
#         print(f"impossible d'installer {pip}")

from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from flask_cors import CORS


app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
api = Api(app)


# simple get
# class Engrenages(Resource):
#     def get(self):
#         return getEngrenages()
# api.add_resource(Engrenages, '/api/getEngrenages')

# get with id
# class Engrenage(Resource):
#     def get(self, engrenageid):
#         return getEngrenage(engrenageid)
# api.add_resource(Engrenage, '/api/getEngrenages/<engrenageid>')


# post with multiple value get a json from interface class object from ts
class formualaire_predict(Resource):
    form = None
    def post(self):
        res = request.get_json()
        largeur_cm = res.get("largeur_cm")
        longueur_cm = res.get("longueur_cm")
        hauteur_cm = res.get("hauteur_cm")
        poids_g = res.get("poids_g")
        long_customer = res.get("long_customer")
        lat_customer = res.get("lat_customer")
        long_seller = res.get("long_seller")
        lat_seller = res.get("lat_seller")
        self.form = Form_to_predict(largeur_cm, longueur_cm, hauteur_cm, poids_g, lat_seller, long_seller, lat_customer, long_customer)
        print(
            json.dumps(self, default=lambda form: self.form.__dict__,
                       sort_keys=True, indent=4)

        )
        json_form = json.dumps(self, default=lambda form: self.form.__dict__,
                       sort_keys=True, indent=4)
        return json_form


api.add_resource(formualaire_predict, '/api/formualaire_predict', methods=["POST"])


# class formualaire_predict(Resource):
#     def get(self, engrenageid):
#         return getForUpdateEngrenageSQL(engrenageid)
#     def post(self):
#         res = request.get_json()
#         nomEngrenage = res.get("nomEngrenage")
#         idEngrenage = res.get("id")
#         avantage = res.get("avantage")
#         inconvenient = res.get("inconvenient")
#         image = res.get("image")
#         Date = res.get("Date")
#         userName = res.get("userName")
#         updateEngrenageSQL(idEngrenage, nomEngrenage, avantage, inconvenient, image, Date, userName)
# api.add_resource(formualaire_predict, '/api/updateEngrenages/<engrenageid>')


if __name__ == '__main__':
    app.run(debug=True)