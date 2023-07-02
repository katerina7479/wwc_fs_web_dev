import React, { useState } from 'react'
import { Controller, useForm } from 'react-hook-form'
import { useNavigate } from 'react-router-dom'

import axios from 'axios'
import { Input, Button, message } from 'antd'

const Registration = () => {
  const {
    control,
    handleSubmit,
    watch,
    formState: { errors }
  } = useForm()
  const [loading, setLoading] = useState(false)
  const navigate = useNavigate()

  const onSubmit = (data) => {
    setLoading(true)
    axios
      .post(`${process.env.REACT_APP_API_BASE_URL}/auth/registration/`, data)
      .then(() => {
        setLoading(false)
        message.success('Registration successful. Please login.')
        navigate('/login')
      })
      .catch((error) => {
        setLoading(false)
        message.error(`Registration failed. Please try again: ${error}`)
      })
  }

  console.log(errors)

  return (
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
        render={({ field }) => <Input.Password placeholder='Password' {...field} />}
      />

      <Controller
        name='password2'
        control={control}
        defaultValue=''
        rules={{
          required: true,
          validate: (value) => value === watch('password')
        }}
        render={({ field }) => <Input.Password placeholder='Confirm Password' {...field} />}
      />

      <Button type='primary' htmlType='submit' loading={loading}>
        Register
      </Button>
    </form>
  )
}

export default Registration
