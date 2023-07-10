import React, { useState } from 'react'
import { Controller, useForm } from 'react-hook-form'
import { Redirect, Link } from 'wouter'

import axios from 'axios'
import { message, Col, Row } from 'antd'
import { Input, Button } from '../components'
import BannerHeader from '../components/BannerHeader'
import './RegistrationForm.css'

const Registration = () => {
  const {
    control,
    handleSubmit,
    watch,
    formState: { errors }
  } = useForm()
  const [loading, setLoading] = useState(false)
  const [nextPage, setNextPage] = useState(null)

  const onSubmit = (data) => {
    setLoading(true)
    axios
      .post(`${process.env.REACT_APP_API_BASE_URL}/auth/registration/`, data)
      .then(() => {
        message.success('Registration successful. Please login.')
        setNextPage('/login')
      })
      .catch((error) => {
        message.error(`Registration failed. Please try again: ${error}`)
      })
      .finally(() => {
        setLoading(false)
      })
  }

  console.log(errors)

  if(nextPage){
    return <Redirect to={nextPage} />
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
                name='first_name'
                control={control}
                defaultValue=''
                rules={{ required: true }}
                render={({ field }) => <Input placeholder='First Name' {...field} />}
              />
              <Controller
                name='last_name'
                control={control}
                defaultValue=''
                rules={{ required: true }}
                render={({ field }) => <Input placeholder='Last Name' {...field} />}
              />
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
                render={({ field }) => <Input type='password' placeholder='Password' {...field} />}
              />

              <Controller
                name='password2'
                control={control}
                defaultValue=''
                rules={{
                  required: true,
                  validate: (value) => value === watch('password')
                }}
                render={({ field }) => <Input type='password' placeholder='Confirm Password' {...field} />}
              />

              <Button type='primary' htmlType='submit' loading={loading}>
                Register
              </Button>
            </form>
            <Button type={'link'} loading={loading}>
              <Link to='/login'>Log In</Link>
            </Button>
          </div>
        </Col>
        <Col span={6}></Col>
      </Row>
      <Row>
        <Col span={24}>
          <div className='footer'></div>
        </Col>
      </Row>
    </div>
  )
}

export default Registration
