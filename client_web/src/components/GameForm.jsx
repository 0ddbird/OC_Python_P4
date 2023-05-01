import React from 'react'
import PropTypes from 'prop-types'

const GameForm = ({ p1, p2, p1Score, p2Score, playerResults, setPlayersScores, handleGameSubmit }) => {
  return <>
    <form className="game_form" onSubmit={(e) => handleGameSubmit(e)}>
      <fieldset className="player_result">
        <div>Player 1: {p1.name}</div>
        <label htmlFor="player-1_result">Player 1 result</label>
        <select className="player_result_select" id="player-1_result" value={playerResults[p1Score]} onChange={(e) => setPlayersScores(e)}>
          <option value={''}>To set</option>
          <option value={1.0}>WIN</option>
          <option value={0.0}>LOSE</option>
          <option value={0.5}>TIE</option>
        </select>
      </fieldset>
      <fieldset className="player_result">
        <div>Player 2: {p2.name}</div>
        <div>Player 2 result: {playerResults[p2Score]}</div>
      </fieldset>
      <button type="submit">Submit results</button>
    </form>
  </>
}

GameForm.propTypes = {
  p1: PropTypes.object,
  p2: PropTypes.object,
  p1Score: PropTypes.number,
  p2Score: PropTypes.number,
  playerResults: PropTypes.object,
  setPlayersScores: PropTypes.func,
  handleGameSubmit: PropTypes.func
}

export default GameForm
