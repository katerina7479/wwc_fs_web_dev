import React from 'react'
import { Input as AntdInput } from 'antd'
import './Input.css'

// Create your own Input component
const Input = ({ type, ...props }) => {
  // Choose the correct Antd component based on the 'type' prop
  let Component
  switch (type) {
    case 'password':
      Component = AntdInput.Password
      break
    default:
      Component = AntdInput
  }

  return <Component type={type} className={'form-input'} {...props} />
}

export default Input
