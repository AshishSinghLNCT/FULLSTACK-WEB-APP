import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class UserService {

  constructor() { }
}
// src/app/services/state.service.ts


import { BehaviorSubject, Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class StateService {
  private userSubject: BehaviorSubject<any[]> = new BehaviorSubject<any[]>([]);
  public users$: Observable<any[]> = this.userSubject.asObservable();

  constructor() {}

  setUsers(users: any[]): void {
    this.userSubject.next(users);
  }
}
