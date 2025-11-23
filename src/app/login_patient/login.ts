import { Component, inject } from '@angular/core';
import { HttpClient, HttpErrorResponse, HttpHeaders } from '@angular/common/http'; // 👈 Added HttpHeaders and HttpErrorResponse
import { Router } from '@angular/router'; // 👈 IMPORT THE ROUTER
import { FormsModule } from '@angular/forms'; // Assuming you still need this for the template

@Component({
  // Assuming a standard component setup; adjust as needed
  selector: 'app-login',
  standalone: true, 
  imports: [FormsModule], 
  templateUrl: './login.html',
  styleUrl: './login.css' 
})
export class LoginComponent { // Renamed from 'Login' to 'LoginComponent' for Angular standards
  
  // Inject the HTTP client service
  private http = inject(HttpClient);
  private router = inject(Router); // 👈 Inject the Router Service
  
  // Define your backend endpoint URL
  private readonly apiUrl = 'http://localhost:8000/login'; 
  
  // Data model to store the form input (CNP and Parola)
  loginData = {
    cnp: '',         
    parola: ''      
  };

  errorMessage: string | null = null; // Variable to hold the error message
  
  // Method to send data to the backend
  onSubmit() {
    this.errorMessage = null; // Clear previous errors
    
    // Explicitly set headers for robust communication
    const headers = new HttpHeaders({'Content-Type': 'application/json'});
    
    console.log('Sending data for Autentificare:', this.loginData);
    
    // Send a POST request with the user's CNP and parola
    this.http.post(this.apiUrl, this.loginData, { headers: headers }).subscribe({
      next: (response: any) => {
        console.log('Autentificare Reușită (Login Success)!', response);
        // SUCCESS: Store the user data/token
        localStorage.setItem('currentUser', JSON.stringify(response));
        
        // 💥 Navigate to the main page 💥
        this.router.navigate(['/main-screen']); 
      },
      error: (rawError) => {
        console.error('Eroare Autentificare (Login Failed):', rawError);
        
        // FAILURE: Extract and display the specific error (e.g., from 401)
        if (rawError instanceof HttpErrorResponse) {
             // Use the 'detail' field from your FastAPI error response
             this.errorMessage = rawError.error.detail || `Eroare Autentificare: Status ${rawError.status}.`;
        } else {
             this.errorMessage = 'A apărut o eroare neașteptată.';
        }
      }
    });
  }
}