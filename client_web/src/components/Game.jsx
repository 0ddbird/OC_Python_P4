import React, { useEffect, useState } from 'react'
import APIService from '../api/ApiService.js'
import PropTypes from 'prop-types'
import './_game.scss'

const Game = ({ gameID, gamesResult, setGamesResult, initialScores }) => {
  const [isLoaded, setIsLoaded] = useState(false)
  const [p1ID, setP1ID] = useState(null)
  const [p2ID, setP2ID] = useState(null)
  const [p1Score, setP1Score] = useState('')
  const [p2Score, setP2Score] = useState('')
  const playerResults = {
    null: 'TO SET',
    1.0: 'WIN',
    0.5: 'TIE',
    0.0: 'LOSE'
  }

  useEffect(() => {
    (async() => {
      const response = await APIService.getGame(gameID)
      if (response.ok) {
        const jsonResponse = await response.json()
        const gameData = jsonResponse.payload
        setP1ID(gameData.p1_id)
        setP2ID(gameData.p2_id)
        setP1Score(initialScores[gameID])
        setP2Score(1.0 - initialScores[gameID])
        setIsLoaded(true)
      }
    })()
  }, [])

  function setPlayersScores(e) {
    if (e.target.value === '') {
      setP2Score('')
      return
    }
    const score = parseFloat(e.target.value)
    setP1Score(score)
    setP2Score(1.0 - score)
    const updatedGamesResult = { ...gamesResult }
    updatedGamesResult[gameID] = score
    setGamesResult(updatedGamesResult)
  }

  return isLoaded
    ? <>
        <h3>Game {gameID}</h3>
        <div>
          <div>Player 1: {p1ID}</div>
          <label htmlFor="player-1_result">Player 1 result</label>
          <select className="player_result_select" id="player-1_result" value={p1Score} onChange={(e) => setPlayersScores(e)}>
            <option value={''}>To set</option>
            <option value={1.0}>WIN</option>
            <option value={0.0}>LOSE</option>
            <option value={0.5}>TIE</option>
          </select>
          <div>Player 2: {p2ID}</div>
          <div>Player 2 result: {playerResults[p2Score]}</div>
        </div>
      </>
    : <div>Loading</div>
}

Game.propTypes = {
  gameID: PropTypes.number,
  gamesResult: PropTypes.object,
  setGamesResult: PropTypes.func,
  initialScores: PropTypes.object
}

export default Game
