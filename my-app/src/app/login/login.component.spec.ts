import { ComponentFixture, TestBed } from '@angular/core/testing';
import { ReactiveFormsModule } from '@angular/forms';
import { AuthService } from '../auth.service';
import { LoginComponent } from './login.component';
import { HttpClientTestingModule } from '@angular/common/http/testing';

describe('LoginComponent', () => {
  let component: LoginComponent;
  let fixture: ComponentFixture<LoginComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [ReactiveFormsModule, HttpClientTestingModule],
      declarations: [LoginComponent],
      providers: [AuthService],
    }).compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(LoginComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });

  it('should have a login form', () => {
    expect(component.loginForm).toBeTruthy();
  });

  it('should have a valid form when filled correctly', () => {
    component.loginForm.controls['username'].setValue('testuser');
    component.loginForm.controls['password'].setValue('password123');
    expect(component.loginForm.valid).toBeTruthy();
  });

  it('should call AuthService login method when form is submitted', () => {
    const authService = TestBed.inject(AuthService);
    spyOn(authService, 'login').and.callThrough();

    component.loginForm.controls['username'].setValue('testuser');
    component.loginForm.controls['password'].setValue('password123');
    component.onSubmit();

    expect(authService['login']).toHaveBeenCalledWith('testuser', 'password123');
  });
});
