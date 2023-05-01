import React, { useState } from 'react'
import APIService from '../api/ApiService.js'
import PropTypes from 'prop-types'
import './_game.scss'
import usePlayer from '../hooks/usePlayer.jsx'

const Game = ({ gameData }) => {
  const [p1Score, setP1Score] = useState('')
  const [p2Score, setP2Score] = useState('')
  const player1 = usePlayer(gameData.p1_id)
  const player2 = usePlayer(gameData.p2_id)
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

  async function handleGameResultsSubmit(e) {
    e.preventDefault()
    try {
      await APIService.updateGame(gameData.id, p1Score, p2Score)
    } catch (e) {
      console.log(e)
    }
  }

  return (
      <>
        <form className="game_form" onSubmit={(e) => handleGameResultsSubmit(e)}>
          <h3>Game {gameData.id}</h3>
          <fieldset className="player_result">
            <div>Player 1: {player1 ? player1.name : 'Loading'}</div>
            <label htmlFor="player-1_result">Player 1 result</label>
            <select className="player_result_select" id="player-1_result" value={p1Score} onChange={(e) => setPlayersScores(e)}>
              <option value={''}>To set</option>
              <option value={1.0}>WIN</option>
              <option value={0.0}>LOSE</option>
              <option value={0.5}>TIE</option>
            </select>
          </fieldset>
          <fieldset className="player_result">
            <div>Player 2: {player2 ? player2.name : 'Loading'}</div>
            <div>Player 2 result: {playerResults[p2Score]}</div>
          </fieldset>
          <button type="submit">Submit results</button>
        </form>
      </>
  )
}

Game.propTypes = {
  gameData: PropTypes.object
}

export default Game
