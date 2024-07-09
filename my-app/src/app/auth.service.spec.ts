import { TestBed } from '@angular/core/testing';
import { HttpClientTestingModule, HttpTestingController } from '@angular/common/http/testing';
import { AuthService } from './auth.service';

describe('AuthService', () => {
  let service: AuthService;
  let httpMock: HttpTestingController;

  beforeEach(() => {
    TestBed.configureTestingModule({
      imports: [HttpClientTestingModule],
      providers: [AuthService],
    });
    service = TestBed.inject(AuthService);
    httpMock = TestBed.inject(HttpTestingController);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });

  it('should login a user', () => {
    const mockResponse = { token: '12345' };
    service['login']('testuser', 'password123').subscribe((response: { token: any; }) => {
      expect(response.token).toEqual(mockResponse.token);
    });

    const req = httpMock.expectOne(`${service['baseUrl']}/login/`);
    expect(req.request.method).toBe('POST');
    req.flush(mockResponse);
  });

  afterEach(() => {
    httpMock.verify();
  });
});


