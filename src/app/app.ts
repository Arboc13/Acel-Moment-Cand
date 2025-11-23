import { Component, signal } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { Login } from "./login_patient/login";

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [
    RouterOutlet,
    Login,
  ],
  templateUrl: './app.html',
  styleUrl: './app.css'
})
export class AppComponent { 
  // All good now, this class is properly defined.
}