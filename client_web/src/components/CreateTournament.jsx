import React, { useEffect, useState } from 'react'
import Nav from '../components/Nav.jsx'
import PlayerRow from './PlayerRow.jsx'
import { getPlayers } from '../pages/Players.jsx'
import { useNavigate } from 'react-router-dom'

const CreateTournament = () => {
  const [tournamentName, setTournamentName] = useState('')
  const [tournamentLocation, setTournamentLocation] = useState('')
  const [tournamentRoundNumber, setTournamentRoundNumber] = useState(4)
  const [tournamentDescription, setTournamentDescription] = useState('')
  const [players, setPlayers] = useState([])
  const [selectedPlayerIDs, setSelectedPlayerIDs] = useState([])
  const [error, setError] = useState(null)
  const navigate = useNavigate()
  const [isLoaded, setIsLoaded] = useState(false)

  useEffect(() => {
    getPlayers().then(players => {
      setPlayers(players)
      setIsLoaded(true)
    }
    )
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
        name: tournamentName,
        location: tournamentLocation,
        rounds: tournamentRoundNumber,
        description: tournamentDescription,
        players_ids: selectedPlayerIDs
      })
    })

    const response = await res.json()

    if (response.status_code === 200) {
      const tournamentId = response.tournament_id
      navigate(`/tournament/${tournamentId}`)
    } else {
      setError(response.message)
    }
  }

  function handlePlayerSelection (playerID) {
    const currentSelectedIDs = [...selectedPlayerIDs]
    if (currentSelectedIDs.includes(playerID)) {
      currentSelectedIDs.splice(currentSelectedIDs.indexOf(playerID), 1)
    } else {
      currentSelectedIDs.push(playerID)
    }
    setSelectedPlayerIDs(currentSelectedIDs)
  }

  const unselectedPlayers = players.filter(
    (player) => !selectedPlayerIDs.includes(player.player_id)
  )
  const selectedPlayers = players.filter((player) =>
    selectedPlayerIDs.includes(player.player_id)
  )

  return (
    !isLoaded
      ? <p>Loading...</p>
      : <>
      <Nav />
      <h1>Create Tournament</h1>
      {error && <p>{error}</p>}
      <form className="create_tournament_form" onSubmit={handleCreateTournament}>
        <label htmlFor="tournament_name">Tournament name</label>
        <input
          type="text"
          value={tournamentName}
          onChange={(e) => setTournamentName(e.target.value)}
        />
        <label htmlFor="tournament_rounds">Tournament rounds</label>
        <input
          type="number" min={1}
          value={tournamentRoundNumber}
          onChange={(e) => setTournamentRoundNumber(e.target.value)}
        />
        <label htmlFor="tournament_location">Tournament location</label>
        <input
          type="text"
          value={tournamentLocation}
          onChange={(e) => setTournamentLocation(e.target.value)}
        />
        <label htmlFor="tournament_description">Tournament description</label>
        <input
          type="text"
          value={tournamentDescription}
          onChange={(e) => setTournamentDescription(e.target.value)}
        />
        <div className="players_list">
          <h2>Selected Players</h2>
          {selectedPlayers.map((player) => (
            <div className="tournament_player" key={`player_${player.player_id}`}>
              <input
                type="checkbox"
                checked
                onChange={() => handlePlayerSelection(player.player_id)}
              />
              <PlayerRow player={player} />
            </div>
          ))}
          <h2>Unselected Players</h2>
          {unselectedPlayers.map((player) => (
            <div className="tournament_player" key={`player_${player.player_id}`}>
              <input
                type="checkbox"
                onChange={() => handlePlayerSelection(player.player_id)}
              />
              <PlayerRow player={player} />
            </div>
          ))}
        </div>
        <button type="submit">Envoyer</button>
      </form>
    </>
  )
}

export default CreateTournament
