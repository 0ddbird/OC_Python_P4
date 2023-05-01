import React, { useState, useEffect } from 'react'
import PropTypes from 'prop-types'
import APIService from '../api/ApiService.js'
import GameForm from './GameForm'

const Game = ({ gameData, players }) => {
  const [loaded, setIsLoaded] = useState(false)
  const [p1Score, setP1Score] = useState(gameData.p1_score)
  const [p2Score, setP2Score] = useState(gameData.p2_score)
  const player1 = players.find((player) => player.id === gameData.p1_id)
  const player2 = players.find((player) => player.id === gameData.p2_id)

  useEffect(() => {
    if (player1 && player2) {
      setIsLoaded(true)
    }
  }, [player1, player2])

  const playerResults = {
    null: 'TO SET',
    1.0: 'WIN',
    0.5: 'TIE',
    0.0: 'LOSE'
  }

  function setPlayersScores(e) {
    e.preventDefault()
    if (e.target.value === '') {
      setP2Score('')
      return
    }
    const score = parseFloat(e.target.value)
    setP1Score(score)
    setP2Score(1.0 - score)
  }

  async function handleGameSubmit(e) {
    e.preventDefault()
    try {
      const response = await APIService.updateGame(gameData.id, p1Score, p2Score)

      if (response.statusCode === 201) {
        window.location.reload()
      }
    } catch (e) {
      console.log(e)
    }
  }

  if (!loaded) return <div>Loading</div>

  return (
    player1 &&
      player2 &&
      gameData.status === 'OVER'
      ? (
              <div className="game_results">
                <h3>Game {gameData.id}</h3>
                <div>Player 1: {player1.first_name}</div>
                <div>Player 1 {playerResults[gameData.p1_score]}</div>
                <div>Player 2: {player2.first_name}</div>
                <div>Player 2 {playerResults[gameData.p2_score]}</div>
              </div>
        )
      : (
              <GameForm
                  p1={player1}
                  p2={player2}
                  p1Score={p1Score}
                  p2Score={p2Score}
                  playerResults={playerResults}
                  setPlayersScores={setPlayersScores}
                  handleGameSubmit={handleGameSubmit}
              />
        )
  )
}

Game.propTypes = {
  gameData: PropTypes.object,
  players: PropTypes.array
}

export default Game
