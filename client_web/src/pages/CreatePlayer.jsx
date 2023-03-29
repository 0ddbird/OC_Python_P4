import React, { useState } from 'react'
import Nav from '../components/Nav.jsx'
import { useNavigate } from 'react-router-dom'

const CreatePlayer = () => {
  const [firstName, setFirstName] = useState('')
  const [lastName, setLastName] = useState('')
  const [birthdate, setBirthdate] = useState('')
  const [chessID, setChessID] = useState('')
  const [ELO, setELO] = useState('')
  const navigate = useNavigate()

  async function handleFormSubmit (e) {
    e.preventDefault()
    const res = await fetch('http://127.0.0.1:5000/player/create', {
      headers: {
        'Content-Type': 'application/json',
        Accept: 'application/json'
      },
      method: 'POST',
      body: JSON.stringify({
        chess_id: chessID,
        first_name: firstName,
        last_name: lastName,
        birthdate,
        elo: ELO
      })
    })
    const response = await res.json()
    if (response.status_code === 201) {
      navigate('/players')
    }
  }

  return (
      <>
        <Nav/>
        <form className="player_form" onSubmit={(e) => handleFormSubmit(e)}>
          <label htmlFor="first_name">First name</label>
          <input id="first_name" type="text" value={firstName}
                 onChange={(e) => setFirstName(e.target.value)}/>

          <label htmlFor="last_name">Last name</label>
          <input id="last_name" type="text" value={lastName}
                 onChange={(e) => setLastName(e.target.value)}/>

          <label htmlFor="birthdate">Birthdate</label>
          <input id="birthdate" type="date" value={birthdate}
                 onChange={(e) => setBirthdate(e.target.value)}/>

          <label htmlFor="chess_id">Chess ID</label>
          <input id="chess_id" type="text" value={chessID}
                 onChange={(e) => setChessID(e.target.value)}/>

          <label htmlFor="elo">ELO</label>
          <input id="elo" type="number" min="0" value={ELO}
                 onChange={(e) => setELO(e.target.value)}/>
          <button type="submit">Valider les changements</button>
        </form>
      </>
  )
}

export default CreatePlayer
