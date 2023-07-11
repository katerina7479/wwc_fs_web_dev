import { message, Select } from 'antd'
import React, { useState, useEffect } from 'react'

const MenuPageSection = ({ selectedSection, sectionOptions }) => {
  const [options, setOptions] = useState([...sectionOptions])

  const handleSectionChange = (data) => {
    setLoading(true)
    console.log(data)
  }

  return (
    <Select
      mode='tags'
      style={{ width: '100%' }}
      placeholder='Enter Section'
      defaultValue={selectedSection}
      onChange={handleSectionChange}
      options={options}
    />
  )
}

export default MenuPageSection
