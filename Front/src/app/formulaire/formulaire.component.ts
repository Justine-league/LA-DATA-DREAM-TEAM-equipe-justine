import {Component} from '@angular/core';
import {NgForm} from '@angular/forms'
import {HttpClient} from '@angular/common/http';
import {Predict} from "../Class/Predict";
import {IPredict} from "../Interface/IPredict";
import {JSONFile} from "@angular/cli/src/utilities/json-file";


@Component({
  selector: 'app-formulaire',
  templateUrl: './formulaire.component.html',
  styleUrls: ['./formulaire.component.scss']
})
export class FormulaireComponent {
  private _data_bdd_response: Predict | undefined;


  get data_bdd_response(): Predict | undefined {
    return this._data_bdd_response;
  }

  set data_bdd_response(value: Predict | undefined) {
    this._data_bdd_response = value;
  }

  constructor(
    private http: HttpClient
  ) {
  }

  submit(form: NgForm) {
    let date: Date = new Date()
    let dateStr: string = date.toISOString().split('T')[0];
    let predict = new Predict(
      form.value.largeur_cm,
      form.value.longueur_cm,
      form.value.hauteur_cm,
      form.value.poids_g,
      form.value.long_customer,
      form.value.lat_customer,
      form.value.long_seller,
      form.value.lat_seller,
      form.value.price_product,
    )
    console.log(predict)


    let request =
      this.http.post(`http://127.0.0.1:5000/api/formualaire_predict`,
        {
          "price_product": predict.price_product,
          "largeur_cm": predict.largeur_cm,
          "longueur_cm": predict.longueur_cm,
          "hauteur_cm": predict.hauteur_cm,
          "poids_g": predict.poids_g,
          "long_customer": predict.long_customer,
          "lat_customer": predict.lat_customer,
          "long_seller": predict.long_seller,
          "lat_seller": predict.lat_seller
        })

    request.subscribe((json) => {
      this._data_bdd_response = JSON.parse(<string>json);
      console.log(this._data_bdd_response)

    });


  }

  reloadCurrentPage() {
    window.location.reload();
  }
}
