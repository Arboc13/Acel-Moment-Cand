// --- app.routes.ts (FIXED SYNTAX) ---

import { Routes } from '@angular/router';
import { LoginComponent } from './login_patient/login'; // 👈 MAKE SURE THIS IS IMPORTED
import { MainScreenComponent } from './main-screen/main-screen';

export const routes: Routes = [
  // 💥 FIXED LINE: Component MUST be defined here 💥
  { path: 'login', component: LoginComponent }, 
  
  // This line looks correct:
  { path: '', redirectTo: '/login', pathMatch: 'full' }, 
  
  // ... rest of your routes (like the redirects) ...
  { path: 'main-screen', component: MainScreenComponent}
];