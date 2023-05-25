import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { NavComponent } from './nav/nav.component';

const routes: Routes = [
  { path: 'Home', component: NavComponent },
  { path: 'Menu', component: NavComponent },
  { path: 'Articles', component: NavComponent },
  { path: 'Setting', component: NavComponent }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule],
  declarations: [AppRoutingModule]
})

export class AppRoutingModule {}
