import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { DepartmentHomeComponent } from './home/Department-home.component';
import { DepartmentNewComponent } from './new/Department-new.component';
import { DepartmentDetailComponent } from './detail/Department-detail.component';

const routes: Routes = [
  {path: '', component: DepartmentHomeComponent},
  { path: 'new', component: DepartmentNewComponent },
  { path: ':id', component: DepartmentDetailComponent,
    data: {
      oPermission: {
        permissionId: 'Department-detail-permissions'
      }
    }
  },{
    path: ':department_id/Employee', loadChildren: () => import('../Employee/Employee.module').then(m => m.EmployeeModule),
    data: {
        oPermission: {
            permissionId: 'Employee-detail-permissions'
        }
    }
},{
    path: ':department_id/Project', loadChildren: () => import('../Project/Project.module').then(m => m.ProjectModule),
    data: {
        oPermission: {
            permissionId: 'Project-detail-permissions'
        }
    }
}
];

export const DEPARTMENT_MODULE_DECLARATIONS = [
    DepartmentHomeComponent,
    DepartmentNewComponent,
    DepartmentDetailComponent 
];


@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class DepartmentRoutingModule { }