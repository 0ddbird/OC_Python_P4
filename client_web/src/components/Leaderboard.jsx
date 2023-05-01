import React from 'react'
import PropTypes from 'prop-types'

const Leaderboard = ({ players, leaderboardData }) => {
  const sortedLeaderboardData = leaderboardData
    ? leaderboardData.sort((a, b) => b[0] - a[0])
    : []

  const renderLeaderboardRow = (row) => {
    const player = players.find((player) => player.id === row[1])

    return (
        <div key={row[1]}>
          <div>Player name: {player.first_name}</div>
          <div>Score: {row[0].toFixed(1)}</div>
        </div>
    )
  }

  return (
      <>
        {sortedLeaderboardData.map((row) => renderLeaderboardRow(row))}
      </>
  )
}

Leaderboard.propTypes = {
  players: PropTypes.array,
  leaderboardData: PropTypes.array
}

export default Leaderboard
