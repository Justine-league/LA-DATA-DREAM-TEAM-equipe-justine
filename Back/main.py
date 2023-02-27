import sys
import subprocess
import json
from os.path import exists

from pages.form_to_predict import Form_to_predict
from pages.form_to_predict import Form_to_predict
from pages.Model_predict_price import Model_predict_price
from pages.Model_predict_delai import Model_predict_delai


def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])


# subprocess.Popen('echo "Geeks 4 Geeks"', shell=True)

pips_install = ['numpy', 'pandas', "Flask ", "flask-restful", "flask-cors"]


# for pip in pips_install:
#     try:
#         install(pip)
#     except:
#         print(f"impossible d'installer {pip}")


##Run prediction model
prediction_model_price = Model_predict_price()
prediction_model_delai = Model_predict_delai()

from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from flask_cors import CORS


app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
api = Api(app)





# post with multiple value get a json from interface class object from ts
class formualaire_predict(Resource):
    def post(self):
        form = None
        res = request.get_json()
        price_product = res.get("price_product")
        largeur_cm = res.get("largeur_cm")
        longueur_cm = res.get("longueur_cm")
        hauteur_cm = res.get("hauteur_cm")
        poids_g = res.get("poids_g")
        long_customer = res.get("long_customer")
        lat_customer = res.get("lat_customer")
        long_seller = res.get("long_seller")
        lat_seller = res.get("lat_seller")
        self.form = Form_to_predict(price_product, largeur_cm, longueur_cm, hauteur_cm, poids_g, lat_seller, long_seller, lat_customer, long_customer)
        res_price_delivery = prediction_model_price.predict_ExtraTreesRegressor([[price_product, poids_g, longueur_cm, hauteur_cm, largeur_cm, self.form.distance]])
        res_delai_delivery = prediction_model_delai.predict_GradientBoostingRegressor([[price_product, self.form.distance]])
        self.form.price_deliverydef(round(float(res_price_delivery[0]), 2))
        self.form.delai_deliverydef(round(round(res_delai_delivery[0]), 2))
        print(
            json.dumps(self, default=lambda form: self.form.__dict__,
                       sort_keys=True, indent=4)

        )
        json_form = json.dumps(self, default=lambda form: self.form.__dict__,
                       sort_keys=True, indent=4)
        return json_form


api.add_resource(formualaire_predict, '/api/formualaire_predict', methods=["POST"])





if __name__ == '__main__':
    app.run(debug=True)