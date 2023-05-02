import React, { useState, useEffect } from 'react'
import PropTypes from 'prop-types'
import APIService from '../api/ApiService.js'
import GameForm from './GameForm'

const Game = ({ gameData, players, reload, toggleReload }) => {
  const [loaded, setIsLoaded] = useState(false)
  const [p1Score, setP1Score] = useState('')
  const [p2Score, setP2Score] = useState('')
  const player1 = players.find((player) => player.id === gameData.p1_id)
  const player2 = players.find((player) => player.id === gameData.p2_id)

  useEffect(() => {
    if (player1 && player2 && gameData) {
      setP1Score(gameData.p1_score)
      setP2Score(gameData.p2_score)
      setIsLoaded(true)
    }
  }, [player1, player2, gameData])

  const playerResults = {
    null: 'TO SET',
    1.0: 'WIN',
    0.5: 'TIE',
    0.0: 'LOSE'
  }

  function setPlayersScores(e) {
    e.preventDefault()
    if (e.target.value === '') {
      setP1Score('')
      setP2Score('')
      return
    }
    const p1Score = parseFloat(e.target.value)
    const p2Score = 1.0 - p1Score
    setP1Score(p1Score)
    setP2Score(p2Score)
  }

  async function handleGameSubmit(e) {
    e.preventDefault()
    try {
      const response = await APIService.updateGame(gameData.id, p1Score, p2Score)
      if (response.ok) toggleReload(!reload)
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
                <div>{player1.first_name}: {playerResults[gameData.p1_score]}</div>
                <div>{player2.first_name}: {playerResults[gameData.p2_score]}</div>

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
  players: PropTypes.array,
  toggleReload: PropTypes.func,
  reload: PropTypes.bool
}

export default Game
