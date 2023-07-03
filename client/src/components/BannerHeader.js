import React from 'react'
import { Row, Col } from 'antd'
import './BannerHeader.css'

const BannerHeader = () => {
  return (
    <Row height={200}>
      <Col span={24}>
        <div className='container'>
          <img className='banner' src='/images/or-banner.png' alt={'banner'} />
        </div>
      </Col>
    </Row>
  )
}

export default BannerHeader
