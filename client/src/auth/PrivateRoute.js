import React, { useContext } from 'react'
import { AuthContext } from './AuthContext'
import { Spin } from 'antd'
import { Route, Redirect } from 'wouter'

const PrivateRoute = (props) => {
  console.log("Private Route")
  const { isAuthenticated, loading } = useContext(AuthContext)
  if (loading) {
    return <Spin />
  }
  console.log('isAuthenticated', isAuthenticated)
  return isAuthenticated ? <Route {...props} /> : <Redirect to='/login' />
}

export default PrivateRoute
