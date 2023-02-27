from math import radians, cos, sin, asin, sqrt

class Form_to_predict:
    largeur_cm: int
    longueur_cm: int
    hauteur_cm: int
    poids_g: int
    lat_seller: float
    long_seller: float
    lat_customer: float
    long_customer: float
    price_product: float
    price_delivery: float
    delai_delivery: float


    def __init__(self, price_product, largeur_cm, longueur_cm, hauteur_cm, poids_g, lat_seller, long_seller, lat_customer, long_customer):
        self.lat_seller = lat_seller
        self.long_seller = long_seller
        self.lat_customer = lat_customer
        self.long_customer = long_customer
        self.largeur_cm = largeur_cm
        self.longueur_cm = longueur_cm
        self.hauteur_cm = hauteur_cm
        self.poids_g = poids_g
        self.price_product = price_product
        self.distance = self.calculate_distance(lat_seller, long_seller, lat_customer, long_customer)

    def __repr__(self):
        print(self.largeur_cm)
        print(self.longueur_cm)
        print(self.hauteur_cm)
        print(self.poids_g)
        print(self.long_customer)
        print(self.lat_customer)
        print(self.long_seller)
        print(self.lat_seller)
        print(self.price_product)
        print(self.distance)
        print(self.price_delivery)
        print(self.delai_delivery)

    def calculate_distance(self,lon1: float, lat1: float, lon2: float, lat2: float):
            """
            Calculate the great circle distance between two points
            on the earth (specified in decimal degrees)
            """
            # convert decimal degrees to radians
            lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
            # haversine formula
            dlon = lon2 - lon1
            dlat = lat2 - lat1
            a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
            c = 2 * asin(sqrt(a))
            # Radius of earth in kilometers is 6371
            km = 6371 * c
            return round(km, 2)

    def price_deliverydef(self,price_delivery):
        self.price_delivery = price_delivery

    def delai_deliverydef(self, delai_delivery):
        self.delai_delivery = delai_delivery


