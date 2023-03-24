import React, { useContext, useEffect } from 'react'
import Nav from '../components/Nav.jsx'
import PlayersTable from '../components/PlayersTable.jsx'
import { NavLink } from 'react-router-dom'
import { AppContext } from '../App.jsx'

export async function getPlayers () {
  const res = await fetch('http://127.0.0.1:5000/players', {
    headers: {
      'Content-Type': 'application/json',
      Accept: 'application/json'
    },
    method: 'GET'
  })
  return await res.json()
}

const Players = () => {
  const { players, setPlayers } = useContext(AppContext)

  useEffect(() => {
    getPlayers().then(players => {
      setPlayers(players)
    }
    )
  }, [])

  return (
      <>
        <Nav/>
        {players && <PlayersTable players={players}/>}
        <NavLink to="/player/create">Add new player</NavLink>
      </>
  )
}

export default Players
