import React from 'react'
import { NavLink } from 'react-router-dom'

const Nav = () => {
  return (
    <nav>
      <NavLink to='/'>Home</NavLink>
      <NavLink to='/players'>Players</NavLink>
      <NavLink to='/tournaments'>Tournaments</NavLink>
      <NavLink to='/reports'>Reports</NavLink>
    </nav>
  )
}

export default Nav
