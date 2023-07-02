import React, { useContext } from 'react'
import { AuthContext } from '../auth/AuthContext'
import NavBar from '../components/NavBar'

const HomePage = () => {
  const { logOut } = useContext(AuthContext)

  return (
    <div>
      <NavBar />
      You are logged in
      <button onClick={logOut}>Log Out</button>
    </div>
  )
}

export default HomePage
