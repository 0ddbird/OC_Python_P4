import React from 'react'
import PropTypes from 'prop-types'
import PlayerRow from './PlayerRow.jsx'

const PlayersTable = ({ players }) => {
  return (
      <div>
        {
          players.map(player => <PlayerRow player={player} key={player.player_id}/>)
        }
      </div>
  )
}

PlayersTable.propTypes = {
  players: PropTypes.array
}

export default PlayersTable
