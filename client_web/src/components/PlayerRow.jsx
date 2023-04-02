import React from 'react'
import PropTypes from 'prop-types'

const PlayerRow = ({ player, fields }) => {
  return (
    <>
      { fields.includes('id') && <div className="player_id">{player.player_id}</div>}
      { fields.includes('chessId') && <div className="player_chess_id">{player.chess_id}</div>}
      { fields.includes('firstName') && <div className="player_firstname">{player.first_name}</div>}
      { fields.includes('lastName') && <div className="player_lastname">{player.last_name}</div>}
      { fields.includes('birthdate') && <div className="player_birthdate">{player.birthdate}</div>}
      { fields.includes('elo') && <div className="player_elo">{player.elo}</div>}
    </>
  )
}

PlayerRow.propTypes = {
  player: PropTypes.object,
  fields: PropTypes.array
}

export default PlayerRow
