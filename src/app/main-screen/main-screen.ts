import { Component, signal, computed } from '@angular/core';
import { CommonModule } from '@angular/common';

interface Tab {
  id: string;
  name: string;
  icon: string;
}

@Component({
  selector: 'main-screen',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './main-screen.html',
  styleUrl: './main-screen.css'
})
export class MainScreenComponent {
  userRole = signal<'patient' | 'medic'>('patient');
  activeTab = signal<string>(''); // Start empty so only the buttons show at first

  computedTabs = computed<Tab[]>(() => {
    const role = this.userRole();
    return role === 'patient' 
      ? [
          { id: 'history', name: 'Medical History', icon: '📋' }, 
          { id: 'schedule', name: 'Appointments', icon: '📅' }
        ]
      : [
          { id: 'history', name: 'Patient Records', icon: '📂' }, 
          { id: 'schedule', name: 'My Schedule', icon: '🩺' }
        ];
  });

  toggleRole() {
    this.userRole.update(role => (role === 'patient' ? 'medic' : 'patient'));
    this.activeTab.set(''); // Close details when switching roles
  }

  setActiveTab(tabId: string) {
    // If clicking the same tab, close it (toggle effect), otherwise open it
    if (this.activeTab() === tabId) {
        this.activeTab.set('');
    } else {
        this.activeTab.set(tabId);
    }
  }

  getTabClasses(tabId: string): string {
    const isActive = this.activeTab() === tabId;

    if (isActive) {
      // Active: Dark Indigo background, White text, Shadow, Pop out effect
      return 'bg-indigo-600 text-white shadow-2xl scale-105 ring-4 ring-indigo-200';
    } else {
      // Inactive: White background, Dark text, Hover effect
      return 'bg-white text-gray-800 shadow-md hover:shadow-xl hover:bg-gray-50 hover:scale-102 border border-gray-200';
    }
  }
}