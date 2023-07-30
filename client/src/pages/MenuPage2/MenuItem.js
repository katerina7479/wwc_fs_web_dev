// Item.jsx
import React from 'react'

const Item = ({ data, editItem }) => {
  return <input type='text' value={data} onChange={(e) => editItem(e.target.value)} />
}

export default Item
