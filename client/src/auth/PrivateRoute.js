import React, { useContext } from 'react'
import { AuthContext } from './AuthContext'
import { Spin } from 'antd'
import { Route, Redirect } from 'wouter'

const PrivateRoute = (props) => {
  const { isAuthenticated, loading } = useContext(AuthContext)
  if (loading) {
    return <Spin />
  }
  console.log(`This is a private route, you ${isAuthenticated ? 'are' : 'are not'} authenticated`)
  return isAuthenticated ? <Route {...props} /> : <Redirect to='/login' />
}

export default PrivateRoute
