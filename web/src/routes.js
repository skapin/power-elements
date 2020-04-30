import HomePage from './pages/home/HomePage';
import LoginPage from './pages/login-form/LoginPage';
import AccountCreationPage from './pages/login-form/AccountCreationPage';
import UserPage from './pages/user-page/UserPage';
import InfoLegales from './pages/infos/InfosLegales';
import Merci from './pages/infos/Merci';
import Admin from './pages/admin/Admin';
import PolitiqueConfidentialite from './pages/infos/PolitiqueConfidentialite';



export default [
  { name: 'home', path: '/', component: HomePage },
  { name: 'userPage', path: '/user-page', component: UserPage },
  { name: 'loginPage', path: '/login-page', component: LoginPage },
  { name: 'accountCreationPage', path: '/account-creation-page', component: AccountCreationPage },
  { name: 'infosLegales', path: '/info-legales', component: InfoLegales },
  { name: 'politiqueConfidentialite', path: '/politique-de-confidentialité', component: PolitiqueConfidentialite },
  { name: 'merci', path: '/merci', component: Merci },
  { name: 'admin', path: '/admin', component: Admin },


];

export const whiteList = ['/login-page', '/user-page', '/account-creation-page']