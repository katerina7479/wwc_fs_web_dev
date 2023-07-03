import React from 'react'
import './Logo.css'

const Logo = () => {
  return (
    <div className='header'>
      <div className='container'>
        <img className='logo' src='/images/or-logo.png' alt={'logo'} />
        <h1 className='typography'>Open Restaurant</h1>
      </div>
    </div>
  )
}

export default Logo
