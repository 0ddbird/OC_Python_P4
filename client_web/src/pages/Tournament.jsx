import React, { useEffect, useState } from 'react'
import { NavLink, useParams } from 'react-router-dom'
import APIService from '../api/ApiService.js'

const Tournament = () => {
  const { id } = useParams()
  const [tournament, setTournament] = useState(null)
  const [isLoaded, setIsLoaded] = useState(false)
  const isToStart = tournament?.status === 'TO_START'
  const isStarted = tournament?.status === 'STARTED'
  const hasOpenRound = tournament?.status === 'ROUND_OPEN'
  const canStartRound = tournament?.status === isToStart || isStarted

  useEffect(() => {
    (async() => {
      const response = await APIService.getTournament(id)
      if (response.ok) {
        const jsonResponse = await response.json()
        const tournamentData = jsonResponse.payload
        const tournament = {
          id: tournamentData.id,
          name: tournamentData.name,
          startDatetime: tournamentData.start_datetime,
          endDatetime: tournamentData.end_datetime,
          maxRounds: tournamentData.max_rounds,
          currentRound: tournamentData.current_round,
          description: tournamentData.description,
          playersIDs: tournamentData.players_ids,
          location: tournamentData.location,
          status: tournamentData.status,
          roundsIDs: tournamentData.rounds_ids
        }
        setTournament(tournament)
        setIsLoaded(true)
      }
    })()
  }, [])

  async function handleCreateRound() {
    try {
      await APIService.createRound(id)
    } catch (e) {
      console.log('Error while resuming tournament')
    }
  }

  return isLoaded
    ? <>
        <h1 className="tournament_name">{tournament.name}</h1>
        <p className="tournament_status">Status: {tournament.status}</p>
        <p className="tournament_creation_date">Start datetime: {tournament.startDatetime}</p>
        <p className="tournament_creation_date">End datetime: {tournament.endDatetime}</p>
        <p className="tournament_location">Location: {tournament.location}</p>
        <p className="tournament description">Description: {tournament.description}</p>
        <p className="tournament_max_rounds">Max rounds: {tournament.maxRounds}</p>
        <p className="tournament_current_round">Current round: {tournament.currentRound}</p>
        <div>Players: {tournament.playersIDs}</div>
        {canStartRound && <button id="tournament_start_button" onClick={handleCreateRound}>Start</button>}
        {
            hasOpenRound && <NavLink to={`/tournaments/${tournament.id}/${tournament.currentRound}`}>Round</NavLink>
        }
      </>
    : <>
        <div>Loading</div>
      </>
}

export default Tournament
