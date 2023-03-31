import { headers } from './utils.js'

async function createTournament (tournament) {
  const response = await fetch('http://127.0.0.1:5000/tournaments/',
    {
      headers,
      method: 'POST',
      body: JSON.stringify(tournament)
    }
  )

  return await response.json()
}

async function getTournaments (id) {
  const res = await fetch('http://127.0.0.1:5000/tournaments',
    {
      headers,
      method: 'GET'
    }
  )
  return await res.json()
}

export { createTournament, getTournaments }
