import { Component } from '@angular/core';
import { MainScreenComponent } from './main-screen/main-screen';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [MainScreenComponent],
import { Component, signal } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { Login } from "./login_patient/login";

@Component({
  selector: 'app-root',
  imports: [Login],
  templateUrl: './app.html',
  styleUrl: './app.css'
})
// MAKE SURE THIS SAYS 'AppComponent'
export class AppComponent { 
}