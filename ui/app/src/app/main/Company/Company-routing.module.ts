import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { CompanyHomeComponent } from './home/Company-home.component';
import { CompanyNewComponent } from './new/Company-new.component';
import { CompanyDetailComponent } from './detail/Company-detail.component';

const routes: Routes = [
  {path: '', component: CompanyHomeComponent},
  { path: 'new', component: CompanyNewComponent },
  { path: ':id', component: CompanyDetailComponent,
    data: {
      oPermission: {
        permissionId: 'Company-detail-permissions'
      }
    }
  },{
    path: ':company_id/Department', loadChildren: () => import('../Department/Department.module').then(m => m.DepartmentModule),
    data: {
        oPermission: {
            permissionId: 'Department-detail-permissions'
        }
    }
}
];

export const COMPANY_MODULE_DECLARATIONS = [
    CompanyHomeComponent,
    CompanyNewComponent,
    CompanyDetailComponent 
];


@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class CompanyRoutingModule { }