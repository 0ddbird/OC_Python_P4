import React from 'react'
import PropTypes from 'prop-types'
import Game from './Game.jsx'
import './_rounds.scss'

const Round = ({ roundData }) => {
  return (
      <div>
        <h3>Round {roundData.round_number}</h3>
        <div>Status: {roundData.status}</div>
        <div>Start datetime: {roundData.startDatetime}</div>
        <div>End datetime: {roundData.endDatetime}</div>
        <div className="games_container">
          {
              roundData.games && roundData.games.map(game => (
                  <Game
                      key={`game-${game.id}`}
                      gameData={game}
                  />
              ))
          }
        </div>
      </div>
  )
}

Round.propTypes = {
  roundData: PropTypes.object
}

export default Round
