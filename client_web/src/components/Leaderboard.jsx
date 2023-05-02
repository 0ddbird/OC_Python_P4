import React from 'react'
import PropTypes from 'prop-types'

const Leaderboard = ({ players, leaderboardData }) => {
  const sortedLeaderboardData = leaderboardData
    ? leaderboardData.sort((a, b) => b[0] - a[0])
    : []

  const PlayerRow = (row) => {
    const player = players.find((player) => player.id === row[1])

    return (
        <div className="player_row" key={row[1]}>
          <div>{row[0].toFixed(1)}</div>
          <div>{player.first_name} {player.last_name}</div>
        </div>
    )
  }

  return (
      <div id="leaderboard">
        <h2>Leaderboard</h2>
        {sortedLeaderboardData.map((row) => PlayerRow(row))}
      </div>
  )
}

Leaderboard.propTypes = {
  players: PropTypes.array,
  leaderboardData: PropTypes.array
}

export default Leaderboard
