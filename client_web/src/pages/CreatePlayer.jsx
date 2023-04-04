import React, { useState } from 'react'
import Router from '../router/Router.js'
import { useNavigate } from 'react-router-dom'

const CreatePlayer = () => {
  const [firstName, setFirstName] = useState('')
  const [lastName, setLastName] = useState('')
  const [birthdate, setBirthdate] = useState('')
  const [chessID, setChessID] = useState('')
  const [ELO, setELO] = useState('')
  const navigate = useNavigate()

  async function handleFormSubmit(e) {
    e.preventDefault()
    const player = {
      chess_id: chessID,
      first_name: firstName,
      last_name: lastName,
      birthdate,
      elo: ELO
    }
    const response = await Router.createPlayer(player)
    if (response.ok) navigate('/players')
  }

  function handleFormReset() {
    setFirstName('')
    setLastName('')
    setBirthdate('')
    setChessID('')
    setELO('')
  }

  return (
      <section id="create_player_page">

        <h1>Create new player</h1>

        <form className="player_form" onSubmit={(e) => handleFormSubmit(e)}>
          <label htmlFor="first_name">First name</label>
          <input id="first_name" type="text" value={firstName} onChange={(e) => setFirstName(e.target.value)}/>

          <label htmlFor="last_name">Last name</label>
          <input id="last_name" type="text" value={lastName} onChange={(e) => setLastName(e.target.value)}/>

          <label htmlFor="birthdate">Birthdate</label>
          <input id="birthdate" type="date" value={birthdate} onChange={(e) => setBirthdate(e.target.value)}/>

          <label htmlFor="chess_id">Chess ID</label>
          <input id="chess_id" type="text" value={chessID} onChange={(e) => setChessID(e.target.value)}/>

          <label htmlFor="elo">ELO</label>
          <input id="elo" type="number" min="0" value={ELO} onChange={(e) => setELO(e.target.value)}/>
          <div className="player_form_button-container">
            <button className="reset-button" onClick={handleFormReset}>
              Reset
            </button>
            <button className="submit-button" type="submit">
              Submit
            </button>
          </div>
        </form>
      </section>
  )
}

export default CreatePlayer
