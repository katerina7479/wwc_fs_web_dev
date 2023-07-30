// Section.jsx
import React from 'react'
import Item from './Item'

const MenuSection = ({ data, editSectionTitle }) => {
  // handlers to add, edit, delete items
  const addItem = (index) => {
    const newSections = [...sections]
    newSections[index].items.push(`Item ${newSections[index].items.length + 1}`)
    setSections(newSections)
  }

  return (
    <div>
      <input type='text' value={data.title} onChange={(e) => editSectionTitle(e.target.value)} />
      {data.items.map((item, index) => (
        <Item
          key={index}
          data={item}
          // pass handlers as needed
        />
      ))}
      <button onClick={addItem}>Add Item</button>
    </div>
  )
}

export default MenuSection
