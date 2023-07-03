import React from 'react'
import { Button as AntdButton } from 'antd'
import './Button.css'

// Create your own Button component
const Button = ({ ...props }) => {
  return <AntdButton className={'form-button'} size={'large'} block={true} {...props} />
}

export default Button
