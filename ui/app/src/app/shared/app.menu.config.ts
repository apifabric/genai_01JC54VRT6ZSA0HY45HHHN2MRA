import { MenuRootItem } from 'ontimize-web-ngx';

import { CompanyCardComponent } from './Company-card/Company-card.component';

import { CustomerCardComponent } from './Customer-card/Customer-card.component';

import { DepartmentCardComponent } from './Department-card/Department-card.component';

import { EmployeeCardComponent } from './Employee-card/Employee-card.component';

import { InventoryCardComponent } from './Inventory-card/Inventory-card.component';

import { InvoiceCardComponent } from './Invoice-card/Invoice-card.component';

import { OrderCardComponent } from './Order-card/Order-card.component';

import { PaymentCardComponent } from './Payment-card/Payment-card.component';

import { ProductCardComponent } from './Product-card/Product-card.component';

import { ProjectCardComponent } from './Project-card/Project-card.component';

import { ShipmentCardComponent } from './Shipment-card/Shipment-card.component';

import { SupplierCardComponent } from './Supplier-card/Supplier-card.component';


export const MENU_CONFIG: MenuRootItem[] = [
    { id: 'home', name: 'HOME', icon: 'home', route: '/main/home' },
    
    {
    id: 'data', name: ' data', icon: 'remove_red_eye', opened: true,
    items: [
    
        { id: 'Company', name: 'COMPANY', icon: 'view_list', route: '/main/Company' }
    
        ,{ id: 'Customer', name: 'CUSTOMER', icon: 'view_list', route: '/main/Customer' }
    
        ,{ id: 'Department', name: 'DEPARTMENT', icon: 'view_list', route: '/main/Department' }
    
        ,{ id: 'Employee', name: 'EMPLOYEE', icon: 'view_list', route: '/main/Employee' }
    
        ,{ id: 'Inventory', name: 'INVENTORY', icon: 'view_list', route: '/main/Inventory' }
    
        ,{ id: 'Invoice', name: 'INVOICE', icon: 'view_list', route: '/main/Invoice' }
    
        ,{ id: 'Order', name: 'ORDER', icon: 'view_list', route: '/main/Order' }
    
        ,{ id: 'Payment', name: 'PAYMENT', icon: 'view_list', route: '/main/Payment' }
    
        ,{ id: 'Product', name: 'PRODUCT', icon: 'view_list', route: '/main/Product' }
    
        ,{ id: 'Project', name: 'PROJECT', icon: 'view_list', route: '/main/Project' }
    
        ,{ id: 'Shipment', name: 'SHIPMENT', icon: 'view_list', route: '/main/Shipment' }
    
        ,{ id: 'Supplier', name: 'SUPPLIER', icon: 'view_list', route: '/main/Supplier' }
    
    ] 
},
    
    { id: 'settings', name: 'Settings', icon: 'settings', route: '/main/settings'}
    ,{ id: 'about', name: 'About', icon: 'info', route: '/main/about'}
    ,{ id: 'logout', name: 'LOGOUT', route: '/login', icon: 'power_settings_new', confirm: 'yes' }
];

export const MENU_COMPONENTS = [

    CompanyCardComponent

    ,CustomerCardComponent

    ,DepartmentCardComponent

    ,EmployeeCardComponent

    ,InventoryCardComponent

    ,InvoiceCardComponent

    ,OrderCardComponent

    ,PaymentCardComponent

    ,ProductCardComponent

    ,ProjectCardComponent

    ,ShipmentCardComponent

    ,SupplierCardComponent

];