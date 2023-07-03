import React from 'react'
// import { AuthContext } from '../auth/AuthContext'
import { HorizontalNavBar, Logo } from '../components'
import { Row, Col } from 'antd'

const HomePage = () => {
  // const { logOut } = useContext(AuthContext)

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
      <Row>
        <Col span={8}>
          <Logo />
        </Col>
        <Col span={16} />
      </Row>
      <Row>
        <Col span={2} />
        <Col span={20}>
          <HorizontalNavBar items={items} />
        </Col>
      </Row>
      <Row>
        <Col span={2} />
        <Col span={20}>
          <p>You are logged in</p>
        </Col>
      </Row>
    </div>
  )
}

export default HomePage
