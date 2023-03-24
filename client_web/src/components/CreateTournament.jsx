import React, { useContext, useEffect, useState } from 'react'
import { AppContext } from '../App.jsx'
import Nav from '../components/Nav.jsx'
import PlayerRow from './PlayerRow.jsx'
import { getPlayers } from '../pages/Players.jsx'

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

  async function handleCreateTournament (e) {
    e.preventDefault()
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

  function handlePlayerSelection (e, playerID) {
    const currentSelectedIDs = [...selectedPlayerIDs]
    if (currentSelectedIDs.includes(playerID)) {
      currentSelectedIDs.splice(currentSelectedIDs.indexOf(playerID), 1)
    } else {
      currentSelectedIDs.push(playerID)
    }
    setSelectedPlayerIDs(currentSelectedIDs)
    console.log(setSelectedPlayerIDs)
  }

  return (
      <>
        <Nav/>
        <h1>Create Tournament</h1>
        <form className="create_tournament_form"
              onSubmit={(e) => handleCreateTournament(e)}>
          <label htmlFor="tournament_name">Tournament name</label>
          <input type="text" value={tournamentName}
                 onChange={(e) => setTournamentName(e.target.value)}/>
          <div className="players_list">
            {
                players && players.map(player => {
                  return (
                      <div className="player" key={`player_${player.id}`}>
                        <input type="checkbox"
                               onChange={(e) => handlePlayerSelection(player.id)}/>
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
