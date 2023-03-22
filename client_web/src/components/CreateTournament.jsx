import React, { useContext, useEffect, useState } from 'react'
import Nav from '../components/Nav.jsx'
import { AppContext } from '../App.jsx'
import { getPlayers } from '../pages/Players.jsx'
import PlayerRow from './PlayerRow.jsx'

const CreateTournament = () => {
  const [tournamentName, setTournamentName] = useState('')
  const { players, setPlayers } = useContext(AppContext)
  const [selectedPlayerIDs, setSelectedPlayerIDs] = useState([])
  useEffect(() => {
    if (!players) {
      getPlayers().then(players => {
        setPlayers(players)
      }
      )
    }
  }, [])

  async function handleCreateTournament (id) {
    const res = await fetch('http://127.0.0.1:5000/tournament/create', {
      headers: {
        'Content-Type': 'application/json',
        Accept: 'application/json'
      },
      method: 'POST',
      body: JSON.stringify({
        tournament_name: tournamentName
      })
    })

    return await res.json()
  }

  function handlePlayerSelection (e, player) {
    const currentSelectedIDs = [...selectedPlayerIDs]
    currentSelectedIDs.push(player.id)
    setSelectedPlayerIDs(currentSelectedIDs)
    console.log(setSelectedPlayerIDs())
  }

  return (
      <>
        <Nav/>
        <h1>Create Tournament</h1>
        <form className="create_tournament_form"
              onSubmit={handleCreateTournament}>
          <label htmlFor="tournament_name">Tournament name</label>
          <input type="text" value={tournamentName}
                 onChange={(e) => setTournamentName(e.target.value)}/>
          <div className="players_list">
            {
                players && players.map(player => {
                  return (
                      <div className="player" key={`player_${player.id}`}>
                        <input type="checkbox"
                               onChange={(e, player) => handlePlayerSelection(e, player)}/>
                        <PlayerRow player={player} key={player.id}/>
                      </div>

                  )
                })
            }
          </div>
          <button type="submit">Envoyer</button>
        </form>
      </>
  )
}

export default CreateTournament
