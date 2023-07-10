import React, {useContext, useState} from 'react'
import { AuthContext } from '../auth/AuthContext'
import { Logo } from '../components'
import {Row, Col, Button, Menu} from 'antd'
import './BaseLayout.css'
import {horizontalMenuItems} from "../constants/routing";
import {Redirect} from "wouter";

const BaseLayout = (props) => {
  const { children, currentPage } = props
  const [nextPage, setNextPage] = useState(null)
  const { logOut } = useContext(AuthContext)
  console.log("Rendering BaseLayout for LoggedIn pages")

  const handleNavigate = (e) => {
    const path = horizontalMenuItems.filter((i) => i.key === e.key)[0].path
    console.log("Redirecting to", path)
    setNextPage(path)
  }

  const handleLogOut = async () => {
    await logOut()
    setNextPage('/login')
  }


  if(nextPage){
    return <Redirect to={nextPage} />
  }


  return (
    <div>
      <Row>
        <Col span={1}><Button onClick={handleLogOut}>Logout</Button></Col>
        <Col span={8}>
          <Logo />
        </Col>
        <Col span={16} />
      </Row>
      <Row>
        <Col span={2} />
        <Col span={20}>
          <Menu className='horizontal-menu' onClick={handleNavigate} selectedKeys={[currentPage]} mode='horizontal' items={horizontalMenuItems} />
        </Col>
      </Row>
      <Row>
        <Col span={2} />
        <Col span={20}>{children}</Col>
      </Row>
    </div>
  )
}

export default BaseLayout;
