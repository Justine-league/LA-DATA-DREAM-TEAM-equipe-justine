import { Component, OnInit } from '@angular/core';
import {HttpClient} from "@angular/common/http";
import {NgForm} from "@angular/forms";
// import {User} from "../Class/User";

@Component({
  selector: 'app-navbar',
  templateUrl: './navbar.component.html',
  styleUrls: ['./navbar.component.scss']
})
export class NavbarComponent implements OnInit {

  // result: string = '';
  // private _connectedUSer = false
  // private _user: User|undefined = undefined

  constructor(
    // private http: HttpClient
  ) {}

  // deconnectUser(){
  //   this.connectedUSer = false
  //
  //   this.user = undefined
  // }
  //
  // submitUserCo (form: NgForm) {
  //   this._user = new User(
  //     form.value.userName,
  //     form.value.password,
  //   )
  //
  //
  //   let request =
  //     this.http.post(`http://127.0.0.1:5000/api/connectUser`,
  //       {
  //         "nom" : this._user.nom,
  //         "password" : this._user.password
  //       })
  //
  //   request.subscribe((data) => {
  //     console.dir(this._connectedUSer);
  //     if (data == true) {
  //       this._connectedUSer = true
  //     } else {
  //       this._connectedUSer = false
  //
  //     }
  //     console.dir(this._connectedUSer);
  //   })
  // }

  ngOnInit(): void {
  }


  // get connectedUSer(): boolean {
  //   return this._connectedUSer;
  // }
  //
  // set connectedUSer(value: boolean) {
  //   this._connectedUSer = value;
  // }
  //
  // get user(): User | undefined {
  //   return this._user;
  // }
  //
  // set user(value: User | undefined) {
  //   this._user = value;
  // }
}
