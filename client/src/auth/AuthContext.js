import React, { createContext, useEffect, useState } from 'react'
import axios from './AxiosConfig'
import { BASE_API_URL } from '../constants'
import { Redirect } from 'wouter'

export const AuthContext = createContext()

export function AuthProvider({ children }) {
  const [isAuthenticated, setIsAuthenticated] = useState(false)
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState(null)

  // Check if the user is authenticated when the component mounts
  useEffect(() => {
    const access = localStorage.getItem('access')
    const refresh = localStorage.getItem('refresh')

    // Validate the token and set isAuthenticated to true if it's valid
    // Replace `validateToken` with your actual validation logic
    if (access && refresh) {
      setIsAuthenticated(true)
    }
    setLoading(false)
  }, [])

  async function logIn(email, password) {
    setLoading(true)
    try {
      const response = await axios.post(`${BASE_API_URL}/auth/login/`, { email, password })

      if (response.status === 200) {
        localStorage.setItem('access', response.data.access)
        localStorage.setItem('refresh', response.data.refresh)
        axios.defaults.headers.common['Authorization'] = `Bearer ${localStorage.getItem('access')}`
        setIsAuthenticated(true)
        setError(null)
      } else {
        setError('Login failed')
      }
    } catch (err) {
      setError(err.message)
    } finally {
      setLoading(false)
    }
  }

  async function logOut() {
    setLoading(true)
    try {
      const response = await axios.post(`${BASE_API_URL}/auth/logout/`, { email, password })

      if (response.status === 200) {
        localStorage.setItem('access', null)
        localStorage.setItem('refresh', null)
        axios.defaults.headers.common['Authorization'] = null
        setIsAuthenticated(false)
        setError(null)
      } else {
        setError('Logout failed')
      }
    } catch (err) {
      setError(err.message)
    } finally {
      setLoading(false)
    }
  }
  return <AuthContext.Provider value={{ isAuthenticated, logIn, logOut, loading, error }}>{children}</AuthContext.Provider>
}
