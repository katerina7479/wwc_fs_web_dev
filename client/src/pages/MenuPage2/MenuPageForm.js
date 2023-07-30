// MenuPageForm.jsx
import React, {useEffect, useState} from 'react'
import MenuSection from './MenuSection'
import useAxios from 'axios-hooks'
import { BASE_API_URL } from '../../constants'
import axios from "axios";

const MenuPageForm = (menuId) => {
  const [currentMenuSections, setCurrentMenuSections] = useState([])

  const [allSections, setAllSections] = useState([])
  const [items, setItems] = useState([])

  useEffect(() => {
    Promise.all([
      axios.get('/api/sections'),
      axios.get('/api/items')
    ])
    .then(([{ data: sectionsData }, { data: itemsData }]) => {
      setSections(sectionsData)
      setItems(itemsData)
    })
    .catch((error) => {
      // Handle error here
      console.error(error)
    })
  }, [])

  if (loading) return <p>Loading...</p>
  if (error) return <p>Error!</p>

  // Now data should hold your fetched sections
  useEffect(() => {
    if (data) {
      setAllSections(data) // update your local state with the fetched data
    }
  }, [data])
  // handlers to add, edit, delete sections
  const addMenuSection = () => {
    setCurrentMenuSections([...currentMenuSections, { title: `Section ${currentMenuSections.length + 1}`, items: [] }])
  }

  return (
    <div>
      {currentMenuSections.map((section, index) => (
        <MenuSection
          key={index}
          data={section}
          // pass handlers as needed
        />
      ))}
      <button onClick={addMenuSection}>Add Section</button>
    </div>
  )
}

export default MenuPageForm
