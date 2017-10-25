const m = require('mithril')

const Index = require('./views/Index')
const Profile = require('./views/Profile')
const Login = require('./views/Login')
const Register = require('./views/Register')
const ThankYou = require('./views/ThankYou')

const Auth = require('./models/Auth')

const root = document.querySelector('app')

m.route(root, '/app', {
  '/app': Index,
  '/login': Login,
  '/register': Register,
  '/thank-you': ThankYou,
  '/profile': {
    onmatch () {
      if (!Auth.user.loggedIn) {
        m.route.set('/login')
      } else {
        return Profile
      }
    }
  }
})
