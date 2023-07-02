import React from 'react'
import { Menu } from 'antd'
import { Link } from 'react-router-dom'

const NavBar = () => {
  return (
    <Menu mode='horizontal'>
      <Menu.Item key='home'>
        <Link to='/'>Home</Link>
      </Menu.Item>
    </Menu>
  )
}

export default NavBar
