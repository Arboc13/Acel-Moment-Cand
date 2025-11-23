import { Component } from '@angular/core';
import { MainScreenComponent } from './main-screen/main-screen';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [MainScreenComponent],
  templateUrl: './app.html',
  styleUrl: './app.css'
})
// MAKE SURE THIS SAYS 'AppComponent'
export class AppComponent { 
}