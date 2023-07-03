import React from 'react'
import { Menu } from 'antd'

const HorizontalNavBar = ({ onClick, current, items }) => {
  return <Menu onClick={onClick} selectedKeys={[current]} mode='horizontal' items={items} />
}

export default HorizontalNavBar
