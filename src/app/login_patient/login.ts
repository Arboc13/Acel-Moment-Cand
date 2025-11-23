import { Component, inject } from '@angular/core';
import { CommonModule } from '@angular/common'; 
import { FormsModule } from '@angular/forms'; 
import { HttpClient } from '@angular/common/http'; // 1. Necessary for backend communication

@Component({
  selector: 'app-login',
  standalone: true, // IMPORTANT: Enable standalone mode
  imports: [
    CommonModule, 
    FormsModule 
  ], 
  templateUrl: './login.html',
  styleUrl: './login.css',
})
export class Login {
  
  // Inject the HTTP client service
  private http = inject(HttpClient);
  
  // Define your backend endpoint URL (MAKE SURE THIS IS CORRECT!)
  private readonly apiUrl = 'http://localhost:8000/login'; 
  
  // Data model to store the form input (CNP and Parola)
  loginData = {
    cnp: '',         
    parola: ''      
  };

  // Method to send data to the backend
  onSubmit() {
    console.log('Sending data for Autentificare:', this.loginData);
    
    // Send a POST request with the user's CNP and parola
    this.http.post(this.apiUrl, this.loginData).subscribe({
      next: (response) => {
        console.log('Autentificare Reușită (Login Success)!', response);
        // SUCCESS: You would handle authentication tokens and navigation here
      },
      error: (error) => {
        console.error('Eroare Autentificare (Login Failed):', error);
        // FAILURE: Display an error message to the user
      }
    });
  }
}