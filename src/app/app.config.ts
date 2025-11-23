import { ApplicationConfig } from '@angular/core';
import { provideRouter } from '@angular/router';
import { provideHttpClient } from '@angular/common/http'; // 👈 IMPORT THIS

import { routes } from './app.routes';

export const appConfig: ApplicationConfig = {
  providers: [
    // 💥 THIS WAS MISSING AND IS CRITICAL FOR YOUR LOGIN! 💥
    provideHttpClient(), 

    // The other providers you already had:
    // NOTE: We can remove provideBrowserGlobalErrorListeners for simplicity here
    provideRouter(routes) 
  ]
};