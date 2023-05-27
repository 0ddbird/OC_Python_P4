import React, { useState } from 'react'

const ReportsForm = () => {
  const [tournamentId, setTournamentId] = useState('')
  const [includeRounds, setIncludeRounds] = useState(false)
  const [includePlayers, setIncludePlayers] = useState(false)

  const handleSubmit = (event) => {
    event.preventDefault()

    const params = new URLSearchParams()

    if (includeRounds) params.append('rounds', 'true')
    if (includePlayers) params.append('players', 'true')

    let url = `http://localhost:5000/reports/tournaments/${tournamentId}`

    if (params.toString()) url += `?${params.toString()}`

    window.open(url, '_blank')
  }

  return (
      <form onSubmit={handleSubmit}>
        <label>
          Tournament ID:
          <input
              type="number"
              value={tournamentId}
              onChange={(e) => setTournamentId(e.target.value)}
              required
          />
        </label>
        <label>
          Include Rounds
          <input
              type="checkbox"
              checked={includeRounds}
              onChange={(e) => setIncludeRounds(e.target.checked)}
          />
        </label>
        <label>
          Include Players
          <input
              type="checkbox"
              checked={includePlayers}
              onChange={(e) => setIncludePlayers(e.target.checked)}
          />
        </label>
        <button type="submit">Generate Report</button>
      </form>
  )
}

export default ReportsForm
