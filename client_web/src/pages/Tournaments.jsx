import React from 'react'
import Nav from '../components/Nav.jsx'
import { NavLink } from 'react-router-dom'

const Tournaments = () => {
  return (
      <>
        <Nav/>
        <h1>Tournaments</h1>
        <NavLink to="/tournament/create">Create tournament</NavLink>
      </>
  )
}

export default Tournaments
