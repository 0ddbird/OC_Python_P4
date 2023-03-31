import { headers } from './utils.js'

async function createPlayer (player) {
  const response = await fetch('http://127.0.0.1:5000/players',
    {
      headers,
      method: 'POST',
      body: JSON.stringify(player)
    }
  )
  return await response.json()
}

async function getPlayers () {
  const response = await fetch('http://127.0.0.1:5000/players',
    {
      headers,
      method: 'GET'
    }
  )
  return await response.json()
}

async function getPlayer (id) {
  const response = await fetch(`http://127.0.0.1:5000/players/${id}`,
    {
      headers,
      method: 'GET'
    }
  )
  return await response.json()
}

async function updatePlayer (id, player) {
  const response = await fetch(`http://127.0.0.1:5000/players/${id}`,
    {
      headers,
      method: 'PUT',
      body: JSON.stringify(player)
    }
  )
  return await response.json()
}

async function deletePlayer (id) {
  const response = await fetch(`http://127.0.0.1:5000/players/${id}`,
    {
      headers,
      method: 'DELETE'
    }
  )
  return await response.json()
}

export { createPlayer, getPlayer, getPlayers, updatePlayer, deletePlayer }
