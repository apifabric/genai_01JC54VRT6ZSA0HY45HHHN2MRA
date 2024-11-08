import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';

import { MainComponent } from './main.component';

export const routes: Routes = [
  {
    path: '', component: MainComponent,
    children: [
        { path: '', redirectTo: 'home', pathMatch: 'full' },
        { path: 'about', loadChildren: () => import('./about/about.module').then(m => m.AboutModule) },
        { path: 'home', loadChildren: () => import('./home/home.module').then(m => m.HomeModule) },
        { path: 'settings', loadChildren: () => import('./settings/settings.module').then(m => m.SettingsModule) },
      
    
        { path: 'Company', loadChildren: () => import('./Company/Company.module').then(m => m.CompanyModule) },
    
        { path: 'Customer', loadChildren: () => import('./Customer/Customer.module').then(m => m.CustomerModule) },
    
        { path: 'Department', loadChildren: () => import('./Department/Department.module').then(m => m.DepartmentModule) },
    
        { path: 'Employee', loadChildren: () => import('./Employee/Employee.module').then(m => m.EmployeeModule) },
    
        { path: 'Inventory', loadChildren: () => import('./Inventory/Inventory.module').then(m => m.InventoryModule) },
    
        { path: 'Invoice', loadChildren: () => import('./Invoice/Invoice.module').then(m => m.InvoiceModule) },
    
        { path: 'Order', loadChildren: () => import('./Order/Order.module').then(m => m.OrderModule) },
    
        { path: 'Payment', loadChildren: () => import('./Payment/Payment.module').then(m => m.PaymentModule) },
    
        { path: 'Product', loadChildren: () => import('./Product/Product.module').then(m => m.ProductModule) },
    
        { path: 'Project', loadChildren: () => import('./Project/Project.module').then(m => m.ProjectModule) },
    
        { path: 'Shipment', loadChildren: () => import('./Shipment/Shipment.module').then(m => m.ShipmentModule) },
    
        { path: 'Supplier', loadChildren: () => import('./Supplier/Supplier.module').then(m => m.SupplierModule) },
    
    ]
  }
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class MainRoutingModule { }