import React, { useState } from 'react'
import { Layout, Menu } from 'antd'
const { Content, Sider } = Layout
import BaseLayout from '../../components/BaseLayout'
import { useLocation } from 'wouter'
import MenuPageForm from './MenuPageForm'

const exampleMenuList = [
  {
    label: 'Menu1',
    key: '1'
  },
  {
    label: 'Menu2',
    key: '2'
  },
  {
    label: 'Menu3',
    key: '3'
  }
]

const Index = ({ params }) => {
  const { menuId } = params
  const [selectedMenu, setSelectedMenu] = useState(menuId || '')
  const [_location, setLocation] = useLocation()
  const items = [{ label: 'New Menu', key: 'newMenu' }, ...exampleMenuList]

  const handleMenuSelect = (e) => {
    setSelectedMenu(e.key)
    setLocation(`/menu/${e.key}`)
  }

  return (
    <BaseLayout currentPage={'menu'}>
      <Layout>
        <Sider>
          <Menu selectedKeys={[selectedMenu]} items={items} onClick={handleMenuSelect} />
        </Sider>
        <Content>
          <MenuPageForm menuId={selectedMenu} />
        </Content>
      </Layout>
    </BaseLayout>
  )
}

export default Index
