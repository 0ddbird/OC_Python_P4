import React, { useEffect, useState } from 'react'
import APIService from '../api/ApiService.js'
import { useNavigate } from 'react-router-dom'
import Player from '../components/Player.jsx'

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
  const fields = ['chess_id', 'firstName', 'lastName', 'elo']
  useEffect(() => {
    (async() => {
      const response = await APIService.getPlayers()
      if (response.ok) {
        const jsonResponse = await response.json()
        const players = jsonResponse.payload
        setPlayers(players)
        setIsLoaded(true)
      }
    })()
  }, [])

  async function handleCreateTournament(e) {
    e.preventDefault()
    const tournament = {
      name: tournamentName,
      location: tournamentLocation,
      description: tournamentDescription,
      max_rounds: tournamentRoundNumber,
      players_ids: selectedPlayerIDs
    }
    const response = await APIService.createTournament(tournament)
    if (response.ok) {
      const jsonResponse = await response.json()
      console.log(jsonResponse)
      const tournamentID = jsonResponse.payload
      navigate(`/tournaments/${tournamentID}`)
    } else setError(response.message)
  }

  function handlePlayerSelection(playerID) {
    const currentSelectedIDs = [...selectedPlayerIDs]
    if (currentSelectedIDs.includes(playerID)) currentSelectedIDs.splice(currentSelectedIDs.indexOf(playerID), 1)
    else currentSelectedIDs.push(playerID)
    setSelectedPlayerIDs(currentSelectedIDs)
  }

  const unselectedPlayers = players.filter((player) => !selectedPlayerIDs.includes(player.id))
  const selectedPlayers = players.filter((player) => selectedPlayerIDs.includes(player.id))

  return !isLoaded
    ? <p>Loading...</p>
    : <div id="create_tournament_page">

        <h1>Create tournament</h1>
        {error && <p>{error}</p>}
        <form className="create_tournament_form" onSubmit={handleCreateTournament}>
          <fieldset className="tournament_form_fields">
            <h3>Tournament details</h3>
            <label htmlFor="tournament_name">Tournament name</label>
            <input type="text" value={tournamentName} onChange={(e) => setTournamentName(e.target.value)}/>
            <label htmlFor="tournament_rounds">Tournament rounds</label>
            <input type="number" min={1} value={tournamentRoundNumber} onChange={(e) => setTournamentRoundNumber(e.target.value)}/>
            <label htmlFor="tournament_location">Tournament location</label>
            <input type="text" value={tournamentLocation} onChange={(e) => setTournamentLocation(e.target.value)}/>
            <label htmlFor="tournament_description">Tournament description</label>
            <textarea value={tournamentDescription} rows={5} onChange={(e) => setTournamentDescription(e.target.value)}></textarea>
          </fieldset>

          <div className="player_selection">
            <div className="player_selection_pool">
              <h4>Player pool ({unselectedPlayers.length})</h4>
              {unselectedPlayers.map((player) => (
                  <div className="tournament_player" key={`player_${player.id}`}>
                    <input type="checkbox" onChange={() => handlePlayerSelection(player.id)}/>
                    <Player player={player} fields={fields}/>
                  </div>
              ))}
            </div>
            <div className="player_selection_selected">
              <h4>Selected Players ({selectedPlayers.length})</h4>
              {selectedPlayers.map((player) => (
                  <div className="tournament_player" key={`player_${player.id}`}>
                    <input type="checkbox" checked onChange={() => handlePlayerSelection(player.id)}/>
                    <Player player={player} fields={fields}/>
                  </div>
              ))}
            </div>
          </div>

          <button type="submit" className="create_tournament_submit_button">Submit</button>
        </form>
      </div>
}

export default CreateTournament
