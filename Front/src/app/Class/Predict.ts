export class Predict {

  largeur_cm: number;
  longueur_cm: number;
  hauteur_cm: number;
  poids_g: number;
  long_customer: number;
  lat_customer: number;
  long_seller: number;
  lat_seller: number;
  distance: number | null;


  constructor(largeur_cm: number, longueur_cm: number, hauteur_cm: number, poids_g: number, long_customer: number, lat_customer: number, long_seller: number, lat_seller: number, distance: number | null = null ) {
    this.largeur_cm = largeur_cm;
    this.longueur_cm = longueur_cm;
    this.hauteur_cm = hauteur_cm;
    this.poids_g = poids_g;
    this.long_customer = long_customer;
    this.lat_customer = lat_customer;
    this.long_seller = long_seller;
    this.lat_seller = lat_seller;
    this.distance = distance;
  }


}
