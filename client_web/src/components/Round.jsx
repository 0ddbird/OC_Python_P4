import React from 'react'
import PropTypes from 'prop-types'
import Game from './Game.jsx'
import './_rounds.scss'

const Round = ({ roundData, players }) => {
  return (
      <div>
        <h3>Round {roundData.round_number}</h3>
        <div>Status: {roundData.status}</div>
        <div>Start datetime: {roundData.start_datetime}</div>
        <div>End datetime: {roundData.end_datetime}</div>
        <div className="games_container">
          {
              roundData.games && roundData.games.map(game => (
                  <Game
                      key={`game-${game.id}`}
                      gameData={game}
                      players={players}
                  />
              ))
          }
        </div>
      </div>
  )
}

Round.propTypes = {
  roundData: PropTypes.object,
  players: PropTypes.array
}

export default Round
