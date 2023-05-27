import React, { useEffect, useState } from 'react'
import { NavLink, useParams } from 'react-router-dom'
import APIService from '../api/ApiService.js'
import Round from '../components/Round.jsx'
import Leaderboard from '../components/Leaderboard.jsx'

const Tournament = () => {
  const { id } = useParams()
  const [tournament, setTournament] = useState(null)
  const [players, setPlayers] = useState(null)
  const [isLoaded, setIsLoaded] = useState(false)
  const [reload, toggleReload] = useState(false)
  const rounds = true

  useEffect(() => {
    (async() => {
      const response = await APIService.getTournament(id, rounds)
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
          location: tournamentData.location,
          status: tournamentData.status,
          rounds: tournamentData.rounds,
          leaderboard: tournamentData.leaderboard,
          players: tournamentData.players
        }
        setTournament(tournament)
        setPlayers(tournamentData.players)
        setIsLoaded(true)
        console.log(tournament)
      }
    })()
  }, [reload])

  async function handleCreateRound() {
    try {
      const response = await APIService.createRound(id)
      if (response.ok) {
        toggleReload(!reload)
      }
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

        {
            tournament.leaderboard && <Leaderboard players={players} leaderboardData={tournament.leaderboard}/>
        }

        <div>Players</div>
        {
            tournament.status === 'TO_START' && <button id="tournament_start_button" onClick={handleCreateRound}>Start</button>
        }
        {
            tournament.status === 'STARTED' && <button id="tournament_start_button" onClick={handleCreateRound}>Next round</button>
        }
        {
            tournament.status === 'ROUND_OPEN' && <NavLink to={`/tournaments/${tournament.id}/${tournament.currentRound}`}>Round</NavLink>
        }
        {
            tournament.rounds && tournament.rounds.map(round => <Round key={round.id} roundData={round} players={players} reload={reload} toggleReload={toggleReload}/>
            )
        }
      </>
    : <>
        <div>Loading</div>
      </>
}

export default Tournament
