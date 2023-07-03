import React, { useContext, useState } from 'react'
import { Controller, useForm } from 'react-hook-form'
import { Link, useNavigate } from 'react-router-dom'
import { Col, message, Row } from 'antd'
import { Input, Button } from '../components'
import { AuthContext } from '../auth/AuthContext'
import './LoginForm.css'
import BannerHeader from '../components/BannerHeader'

const Login = () => {
  const {
    control,
    handleSubmit,
    formState: { errors }
  } = useForm()
  const { logIn } = useContext(AuthContext) // Get logIn from context
  const [loading, setLoading] = useState(false)
  const navigate = useNavigate()

  const onSubmit = (data) => {
    setLoading(true)
    logIn(data.email, data.password) // Call logIn method with the email and password
      .then(() => {
        navigate('/')
      })
      .catch(() => {
        message.error('Login failed. Please check your password and try again.')
        console.log(errors)
      })
      .finally(() => {
        setLoading(false)
      })
  }

  return (
    <div className='page'>
      <BannerHeader />
      <Row>
        <Col span={6}></Col>
        <Col span={12}>
          <div className='form-container'>
            <form onSubmit={handleSubmit(onSubmit)}>
              <Controller
                name='email'
                control={control}
                defaultValue=''
                rules={{ required: true }}
                render={({ field }) => <Input placeholder='Email' {...field} />}
              />

              <Controller
                name='password'
                control={control}
                defaultValue=''
                rules={{ required: true }}
                render={({ field }) => <Input type={'password'} placeholder='Password' {...field} />}
              />

              <Button type='primary' htmlType='submit' loading={loading}>
                Login
              </Button>
            </form>
            <Button size={'large'} type={'link'} loading={loading}>
              <Link to='/register'>Registration</Link>
            </Button>
          </div>
        </Col>
      </Row>
      <Row>
        <Col span={24}>
          <div className='footer'></div>
        </Col>
      </Row>
    </div>
  )
}

export default Login
