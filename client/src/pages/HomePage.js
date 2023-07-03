import React, { useContext } from 'react'
import { AuthContext } from '../auth/AuthContext'
import { HorizontalNavBar } from '../components'

const HomePage = () => {
  const { logOut } = useContext(AuthContext)

  const items = [
    {
      label: 'Menus',
      key: 'menus'
    },
    {
      label: 'Locations',
      key: 'locations'
    },
    {
      label: 'Calendar',
      key: 'calendar'
    }
  ]

  return (
    <div>
      <HorizontalNavBar items={items} />
      You are logged in
      <button onClick={logOut}>Log Out</button>
    </div>
  )
}

export default HomePage
