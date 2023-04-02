import React, { useEffect, useState } from 'react'
import Nav from '../components/Nav.jsx'
import { NavLink, useParams } from 'react-router-dom'
import Background from '../components/Background.jsx'

async function getTournament(id) {
  const res = await fetch(`http://127.0.0.1:5000/tournaments/${id}`, {
    headers: {
      'Content-Type': 'application/json',
      Accept: 'application/json'
    },
    method: 'GET'
  })
  return await res.json()
}

const Tournament = () => {
  const { id } = useParams()
  const [name, setName] = useState('')
  const [creationDate, setCreationDate] = useState('')
  const [maxRounds, setMaxRounds] = useState('')
  const [currentRound, setCurrentRound] = useState('')
  const [description, setDescription] = useState('')
  const [playersIDs, setPlayersIDs] = useState('')
  const [location, setLocation] = useState('')
  const [status, setStatus] = useState('')
  const [isLoaded, setIsLoaded] = useState(false)
  const isToStart = currentRound === 0
  const isStarted = currentRound > 0 && currentRound < maxRounds
  const isEnded = currentRound === maxRounds
  useEffect(() => {
    getTournament(id).then((response) => {
      const tournament = response.payload
      setName(tournament.name)
      setCreationDate(tournament.creation_date)
      setMaxRounds(tournament.max_rounds)
      setCurrentRound(tournament.current_round)
      setDescription(tournament.description)
      setPlayersIDs(tournament.players_ids)
      setLocation(tournament.location)
      setStatus(tournament.status)
      setIsLoaded(true)
    })
  }, [])
  return !isLoaded
    ? <div>Loading...</div>
    : <>
      <Background />
      <Nav />
      <h1 className="tournament_name">{name}</h1>
      <p className="tournament_status">Status: {status}</p>
      <p className="tournament_creation_date">Creation date: {creationDate}</p>
      <p className="tournament_location">Location: {location}</p>
      <p className="tournament description">Description: {description}</p>
      <p className="tournament_max_rounds">Max rounds: {maxRounds}</p>
      <p className="tournament_current_round">Current round: {currentRound}</p>
      <div>Players: {playersIDs}</div>

      {isToStart && <NavLink to={`/tournament/${id}/start`}>Start</NavLink>}
      {isStarted && <NavLink to={`/tournament/${id}/round`}>Next round</NavLink>}
      {isEnded && <div>Results</div>}
    </>
}

export default Tournament
