import React, { useEffect, useState } from 'react'
import APIService from '../api/ApiService.js'
import { useParams } from 'react-router-dom'
import Game from './Game.jsx'
import './_rounds.scss'

const Round = () => {
  const { tournamentID, roundNumber } = useParams()
  const [round, setRound] = useState(null)
  const [gamesResult, setGamesResult] = useState({})
  const [isLoaded, setIsLoaded] = useState(false)
  const [initialScores, setInitialScores] = useState({})

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
        setRound(round)

        const initialScoresData = {}
        for (const gameID of round.gamesIDs) {
          const gameResponse = await APIService.getGame(gameID)
          if (gameResponse.ok) {
            const gameJsonResponse = await gameResponse.json()
            const gameData = gameJsonResponse.payload
            initialScoresData[gameID] = gameData.p1_score
          }
        }
        setInitialScores(initialScoresData)

        setIsLoaded(true)
      }
    })()
  }, [])

  async function handleResultsSubmit() {
    const allResultsSet = round.gamesIDs.every((gameID) => Object.prototype.hasOwnProperty.call(gamesResult, gameID))
    if (!allResultsSet) {
      console.log(round.gamesIDs, gamesResult)
      alert('Please set results for all games before submitting.')
      return
    }
    try {
      await APIService.updateAllRoundGames(round.id, gamesResult)
    } catch (e) {
      console.log(e)
    }
  }

  return isLoaded
    ? <div>
        <div>ID: {round.id}</div>
        <div>Tournament ID: {round.tournamentID}</div>
        <div>Status: {round.status}</div>
        <div>Round number: {round.roundNumber}</div>
        <div>Games IDs: {round.gamesIDs}</div>
        <div>Start datetime: {round.startDatetime}</div>
        <div>End datetime: {round.endDatetime}</div>
        <form id="round_games_form" onSubmit={handleResultsSubmit}>
          {
              round.gamesIDs && round.gamesIDs.map(gameID => (
                  <Game
                      key={`game-${gameID}`}
                      gameID={gameID}
                      gameResult={gamesResult}
                      setGamesResult={setGamesResult}
                      initialScores={initialScores}
                  />
              ))
          }
          <button type="submit">Submit games results</button>
        </form>
      </div>
    : <div>Loading</div>
}

export default Round
