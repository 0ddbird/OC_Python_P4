import React, { useEffect, useState } from 'react'
import Nav from '../components/Nav.jsx'
import { useNavigate, useParams } from 'react-router-dom'

async function getPlayer (id) {
  const res = await fetch(`http://127.0.0.1:5000/player/${id}`, {
    headers: {
      'Content-Type': 'application/json',
      Accept: 'application/json'
    },
    method: 'GET'
  })
  return await res.json()
}

const PlayerProfile = () => {
  // const [playerID, setPlayerID] = useState('')
  const [firstName, setFirstName] = useState('')
  const [lastName, setLastName] = useState('')
  const [birthdate, setBirthdate] = useState('')
  const [chessID, setChessID] = useState('')
  const [ELO, setELO] = useState('')

  const { id } = useParams()
  const navigate = useNavigate()

  useEffect(() => {
    getPlayer(id).then(player => {
      // setPlayerID(player.id)
      setFirstName(player.first_name)
      setLastName(player.last_name)
      const birthdate = new Date(player.birthdate).toISOString().slice(0, 10)
      setBirthdate(birthdate)
      setChessID(player.chess_id)
      setELO(player.elo)
    })
  }, [])

  async function handleFormSubmit (e) {
    e.preventDefault()
    const res = await fetch(`http://127.0.0.1:5000/player/${id}/update`, {
      headers: {
        'Content-Type': 'application/json',
        Accept: 'application/json'
      },
      method: 'PUT',
      body: JSON.stringify(
        {
          chess_id: chessID,
          first_name: firstName,
          last_name: lastName,
          birthdate,
          elo: ELO
        }
      )
    })
    const response = await res.json()
    if (response.status_code === 200) navigate('/players')
  }

  return (
      <>
        <Nav/>
        <form className="player_form" onSubmit={(e) => handleFormSubmit(e)}>
          <label htmlFor="first_name"></label>
          <input id="first_name" type="text" value={firstName}
                 onChange={(e) => setFirstName(e.target.value)}/>

          <label htmlFor="last_name"></label>
          <input id="last_name" type="text" value={lastName}
                 onChange={(e) => setLastName(e.target.value)}/>

          <label htmlFor="birthdate"></label>
          <input id="birthdate" type="date" value={birthdate}
                 onChange={(e) => setBirthdate(e.target.value)}/>

          <label htmlFor="chess_id"></label>
          <input id="chess_id" type="text" value={chessID}
                 onChange={(e) => setChessID(e.target.value)}/>

          <label htmlFor="elo"></label>
          <input id="elo" type="number" min="0" value={ELO}
                 onChange={(e) => setELO(e.target.value)}/>
          <button type="submit">Valider les changements</button>
        </form>
      </>
  )
}

export default PlayerProfile
