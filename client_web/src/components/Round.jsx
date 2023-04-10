import React, { useEffect, useState } from 'react'
import APIService from '../api/ApiService.js'
import { useParams } from 'react-router-dom'
import Game from './Game.jsx'
import './_rounds.scss'

const Round = () => {
  const { tournamentID, roundNumber } = useParams()
  const [round, setRound] = useState(null)
  const [isLoaded, setIsLoaded] = useState(false)

  useEffect(() => {
    (async() => {
      const response = await APIService.getRound(tournamentID, roundNumber)
      if (response.ok) {
        const jsonResponse = await response.json()
        const roundData = jsonResponse.payload
        const round = {
          gamesIDs: roundData.games_ids,
          tournamentID: roundData.tournament_id,
          roundNumber: roundData.round_number,
          status: roundData.status,
          startDatetime: roundData.start_datetime,
          endDatetime: roundData.end_datetime,
          id: roundData.id
        }
        console.log(round)
        setRound(round)
        setIsLoaded(true)
      }
    })()
  }, [])

  return isLoaded
    ? <div>
        <h3>Round {round.roundNumber}</h3>
        <div>Status: {round.status}</div>
        <div>Start datetime: {round.startDatetime}</div>
        <div>End datetime: {round.endDatetime}</div>
        <div className="games_container">
          {
              round.gamesIDs && round.gamesIDs.map(gameID => (
                  <Game
                      key={`game-${gameID}`}
                      gameID={gameID}
                  />
              ))
          }
        </div>
      </div>
    : <div>Loading</div>
}

export default Round
