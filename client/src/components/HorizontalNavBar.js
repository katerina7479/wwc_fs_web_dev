import React from 'react'
import { Menu } from 'antd'
import './HorizontalNavBar.css'

const HorizontalNavBar = ({ onClick, current, items }) => {
  return <Menu classname='horizontal-menu' onClick={onClick} selectedKeys={[current]} mode='horizontal' items={items} />
}

export default HorizontalNavBar
