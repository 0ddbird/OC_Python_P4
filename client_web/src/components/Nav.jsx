import React from 'react'
import { NavLink, useLocation } from 'react-router-dom'
import Logo from '../assets/chess-solid.svg'
const Nav = () => {
  const location = useLocation()
  const path = location.pathname
  const isPlayerPage = path.startsWith('/player') && !path.endsWith('/edit') && !path.endsWith('/create')
  const isTournamentPage = path.startsWith('/tournament') && !path.endsWith('/create')
  return (
    <nav>
      <div className="navlinks">
        <NavLink to="/" className="nav_logo_container">
          <img src={Logo} alt="logo" className="home_logo" />
          <span>CheckMate</span>
        </NavLink>
        <NavLink to="/players">Players</NavLink>
        <NavLink to="/tournaments">Tournaments</NavLink>
        <NavLink to="/reports">Reports</NavLink>
      </div>
      <div className="ctas">
        {isPlayerPage && (
          <NavLink to="/player/create" className="cta">
            Add player
          </NavLink>
        )}
        {isTournamentPage && (
          <NavLink to="/tournament/create" className="cta">
            Create tournament
          </NavLink>
        )}
      </div>
    </nav>
  )
}

export default Nav
