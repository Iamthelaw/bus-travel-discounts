const m = require('mithril')

const Index = require('./views/Index')
const Profile = require('./views/Profile')
const Login = require('./views/Login')
const Register = require('./views/Register')
const ThankYou = require('./views/ThankYou')
const City = require('./views/City')

const Auth = require('./models/Auth')

const root = document.querySelector('app')

const validate = (condition, redirect, success) => ({
  onmatch () {
    if (condition) {
      m.route.set(redirect)
    } else {
      return success
    }
  }
})

m.route(root, '/app', {
  '/app': Index,
  '/thank-you': ThankYou,
  '/city/:name': City,
  '/login': validate(Auth.user.loggedIn, '/app', Login),
  '/register': validate(Auth.user.loggedIn, '/app', Register),
  '/profile': validate(!Auth.user.loggedIn, '/login', Profile)
})
