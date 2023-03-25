import React from 'react'
import PropTypes from 'prop-types'

const PlayerRow = ({ player }) => {
  return (
      <>
        <div className="player_id">{player.player_id}</div>
        <div className="player_chess_id">{player.chess_id}</div>
        <div className="player_firstname">{player.first_name}</div>
        <div className="player_lastname">{player.last_name}</div>
        <div className="player_birthdate">{player.birthdate}</div>
        <div className="player_elo">{player.elo}</div>
      </>
  )
}

PlayerRow.propTypes = {
  player: PropTypes.object
}

export default PlayerRow
