import React, { useEffect, useState } from 'react'
import Nav from '../components/Nav.jsx'
import { useNavigate, useParams } from 'react-router-dom'
import { getPlayer, updatePlayer } from '../api/PlayerAPIServices.js'
import Background from '../components/Background.jsx'

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
    getPlayer(id).then((response) => {
      const player = response.payload
      // setPlayerID(player.id)
      setFirstName(player.first_name)
      setLastName(player.last_name)
      const birthdate = new Date(player.birthdate).toISOString().slice(0, 10)
      setBirthdate(birthdate)
      setChessID(player.chess_id)
      setELO(player.elo)
    })
  }, [])

  async function handleUpdatePlayer(e) {
    e.preventDefault()

    const player = {
      chess_id: chessID,
      first_name: firstName,
      last_name: lastName,
      birthdate,
      elo: ELO
    }

    const response = await updatePlayer(id, player)
    if (response.status_code === 200) navigate('/players')
  }

  function handleFormReset() {
    setFirstName('')
    setLastName('')
    setBirthdate('')
    setChessID('')
    setELO('')
  }

  return (
    <>
      <section id="create_player_page">
        <Background />
        <Nav />
        <h1>Edit player details</h1>

        <form className="player_form" onSubmit={(e) => handleUpdatePlayer(e)}>
          <label htmlFor="first_name">First name</label>
          <input id="first_name" type="text" value={firstName} onChange={(e) => setFirstName(e.target.value)} />

          <label htmlFor="last_name">Last name</label>
          <input id="last_name" type="text" value={lastName} onChange={(e) => setLastName(e.target.value)} />

          <label htmlFor="birthdate">Birthdate</label>
          <input id="birthdate" type="date" value={birthdate} onChange={(e) => setBirthdate(e.target.value)} />

          <label htmlFor="chess_id">Chess ID</label>
          <input id="chess_id" type="text" value={chessID} onChange={(e) => setChessID(e.target.value)} />

          <label htmlFor="elo">ELO</label>
          <input id="elo" type="number" min="0" value={ELO} onChange={(e) => setELO(e.target.value)} />
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
    </>
  )
}

export default PlayerProfile
