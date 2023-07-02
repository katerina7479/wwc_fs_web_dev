import React, { useContext, useState } from 'react';
import {Controller, useForm} from 'react-hook-form';
import { Input, Button, message } from 'antd';
import { AuthContext } from '../auth/AuthContext';
import {useNavigate} from "react-router-dom";

const Login = () => {
  const { control, handleSubmit, formState: { errors } } = useForm();
  const { logIn } = useContext(AuthContext); // Get logIn from context
  const navigate = useNavigate();

  const onSubmit = data => {
    console.log("Submitting", data);
    logIn(data.email, data.password) // Call logIn method with the email and password
      .then(() => {
        message.success('Login successful.');
        navigate("/");
      })
      .catch(() => {
        message.error('Login failed. Please try again.');
      });
  };

  return (
    <div>
      <form onSubmit={handleSubmit(onSubmit)}>
        <Controller
          name="email"
          control={control}
          defaultValue=""
          rules={{ required: true }}
          render={({ field }) => <Input placeholder="Email" {...field} />}
        />

        <Controller
          name="password"
          control={control}
          defaultValue=""
          rules={{ required: true }}
          render={({ field }) => <Input.Password placeholder="Password" {...field} />}
        />

        <Button type="primary" htmlType="submit">
          Login
        </Button>
      </form>
      <a href={'/register'}>Need to register?</a>
    </div>
  );
};

export default Login;
