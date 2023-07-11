import React, { useState } from 'react'
import { message, Typography, Button } from 'antd'
import { Controller, useForm } from 'react-hook-form'
import MenuPageSection from './MenuPageSection'
import useAxios from 'axios-hooks'
import { BASE_API_URL } from '../../constants'

const defaultMenu = {
  name: 'New Menu',
  sections: [
    {
      id: 'cljrzijen000044qff8eyes6d',
      name: 'Beverages',
      items: [
        {
          id: 'cljrzijg0000544qf1ro55srw',
          name: 'Diet Coke',
          description: 'Probably not good for you',
          price: 4.24,
          picture: 'fakeurl'
        }
      ]
    }
  ]
}

const MenuPageForm = (props) => {
  const [formState, setFormState] = useState(defaultMenu)
  const [{ sectionData, loading, error }, refetch] = useAxios(`${BASE_API_URL}/api/section/`)

  const sectionOptions =
    sectionData?.map((item) => {
      return {
        ...item,
        label: item.name,
        key: item.id
      }
    }) || []

  const setMenuName = (name) => {
    setFormState({ ...formState, name })
  }

  const handleSectionChange = (e) => {
    console.log(e)
  }

  const onSubmit = (data) => {
    console.log(data)
  }

  const walkMenu = () => {
    return formState.sections.map((section) => (
      <div>
        <MenuPageSection selectedSection={section.name} sectionOptions={sectionOptions} />
        {section.items.map((item) => {
          ;<p>{item.name}</p>
        })}
      </div>
    ))
  }

  return (
    <div>
      <Typography.Title editable={{ onChange: setMenuName, triggerType: ['text', 'icon'] }} level={1} style={{ margin: 0 }}>
        {formState.name ? formState.name : 'Menu Name'}
      </Typography.Title>
      {walkMenu()}
    </div>
  )
}

export default MenuPageForm
