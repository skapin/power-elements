import HomeBase from './pages/home/Base';
import LoginPage from './pages/login-form/LoginPage';
import AccountCreationPage from './pages/login-form/AccountCreationPage';
import UserPage from './pages/user-page/UserPage';


export default [
  { name: 'home', path: '/', component: HomeBase },
  { name: 'userPage', path: '/user-page', component: UserPage },
  { name: 'loginPage', path: '/login-page', component: LoginPage },
  { name: 'accountCreationPage', path: '/account-creation-page', component: AccountCreationPage },
];
