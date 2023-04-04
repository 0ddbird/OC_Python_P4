import React, { useEffect, useState } from 'react'
import { useParams } from 'react-router-dom'
import Round from '../components/Round.jsx'
import Router from '../router/Router.js'

const Tournament = () => {
  const { id } = useParams()
  const [name, setName] = useState('')
  const [creationDate, setCreationDate] = useState('')
  const [maxRounds, setMaxRounds] = useState('')
  const [currentRound, setCurrentRound] = useState('')
  const [rounds, setRounds] = useState([])
  const [description, setDescription] = useState('')
  const [playersIDs, setPlayersIDs] = useState('')
  const [location, setLocation] = useState('')
  const [status, setStatus] = useState('')
  const [isLoaded, setIsLoaded] = useState(false)
  const isEnded = status === 'Ended'

  useEffect(() => {
    (async() => {
      const response = await Router.getTournament(id)
      if (response.ok) {
        const jsonResponse = await response.json()
        const tournament = jsonResponse.payload
        setName(tournament.name)
        setCreationDate(tournament.creation_date)
        setMaxRounds(tournament.max_rounds)
        setCurrentRound(tournament.current_round)
        setRounds(tournament.rounds)
        setDescription(tournament.description)
        setPlayersIDs(tournament.players_ids)
        setLocation(tournament.location)
        setStatus(tournament.status)
        setIsLoaded(true)
      }
    })()
  }, [])

  async function handleNextRound() {
    const response = await Router.handleNextRound(id)
    if (response.status === 200) {
      const tournament = response.payload
      setRounds(tournament.rounds)
      setCurrentRound(tournament.current_round)
    } else console.log('Error while resuming tournament')
  }

  return isLoaded
    ? <>
        <h1 className="tournament_name">{name}</h1>
        <p className="tournament_status">Status: {status}</p>
        <p className="tournament_creation_date">Creation date: {creationDate}</p>
        <p className="tournament_location">Location: {location}</p>
        <p className="tournament description">Description: {description}</p>
        <p className="tournament_max_rounds">Max rounds: {maxRounds}</p>
        <p className="tournament_current_round">Current round: {currentRound}</p>
        <div>Players: {playersIDs}</div>
        {
            rounds && rounds.map(round => <Round key={round.round_id} games={round.games}/>)
        }

        {!isEnded && <button onClick={handleNextRound}>Start</button>}
      </>
    : <>
        <div>Loading</div>
      </>
}

export default Tournament
