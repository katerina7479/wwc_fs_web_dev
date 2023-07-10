import React from 'react'
import { Switch, Route } from 'wouter'

import MenuPage from './pages/MenuPage'
import AboutPage from './pages/AboutPage'
import LoginForm from './pages/LoginForm'
import RegistrationForm from './pages/RegistrationForm'
import CalendarPage from './pages/CalendarPage'
import LocationPage from './pages/LocationPage'
import ErrorPage from './pages/ErrorPage'
import { AuthProvider } from './auth/AuthContext'

import './App.css'
import PrivateRoute from "./auth/PrivateRoute";

function App() {
  console.log("Rendering App")
  return (
    <AuthProvider>
        <Route path='/login' component={LoginForm} />
        <Route path='/register' component={RegistrationForm} />
        <Route path='/about' component={AboutPage} />

        <Switch>
            <PrivateRoute path='/' component={MenuPage} />
            <PrivateRoute path='/menu' component={MenuPage} />
            <PrivateRoute path='/menu/:menuId' component={MenuPage} />
            <PrivateRoute path='/location' component={LocationPage} />
            <PrivateRoute path='/location/:locationId' component={LocationPage} />
            <PrivateRoute path='/calendar' component={CalendarPage} />
            <Route component={ErrorPage}/>
        </Switch>
    </AuthProvider>
  )
}

export default App
