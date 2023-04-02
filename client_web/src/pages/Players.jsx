import React, { useContext, useEffect } from 'react'
import Nav from '../components/Nav.jsx'
import { NavLink } from 'react-router-dom'
import { AppContext } from '../App.jsx'
import PlayerRow from '../components/PlayerRow.jsx'
import DeletePlayerIcon from '../assets/user-xmark-solid.svg'
import EditPlayerIcon from '../assets/user-pen-solid.svg'
import { deletePlayer, getPlayers } from '../api/PlayerAPIServices.js'
import Background from '../components/Background.jsx'

const Players = () => {
  const { players, setPlayers } = useContext(AppContext)
  const fields = ['id', 'chessId', 'firstName', 'lastName', 'birthdate', 'elo']
  useEffect(() => {
    getPlayers().then((response) => setPlayers(response.payload))
  }, [])

  async function handleDeletePlayer(e, id) {
    e.preventDefault()
    const response = await deletePlayer(id)
    console.log(response)
    if (response.status_code === 204) {
      setPlayers(players.filter((player) => player.player_id !== id))
    }
  }

  return (
    <>
      <Background />
      <Nav />
      <div className="players_page">
        <div className="player_table_container">
          <h2 className="player_heading">Players</h2>
          <div className="player_table">
            <div className="player_table_header">
              <span className="player_table_header_cell">ID</span>
              <span className="player_table_header_cell">Chess ID</span>
              <span className="player_table_header_cell">First Name</span>
              <span className="player_table_header_cell">Last Name</span>
              <span className="player_table_header_cell">Birthdate</span>
              <span className="player_table_header_cell">Rating</span>
              <span className="player_table_header_cell"></span>
              <span className="player_table_header_cell"></span>
            </div>
            <div className="player_table_content">
              {players &&
                players.map((player) => {
                  return (
                    <div key={player.player_id} className="player_row">
                      <PlayerRow player={player} fields={fields}/>
                      <NavLink to={`/player/${player.player_id}/edit`}>
                        <button className="edit_player_button">
                          <img src={EditPlayerIcon} className="edit_player_icon icon" alt="edit_player" />
                        </button>
                      </NavLink>
                      <button onClick={(e) => handleDeletePlayer(e, player.player_id)} className="delete_player_button">
                        <img src={DeletePlayerIcon} className="delete_player_icon icon" alt="delete_player" />
                      </button>
                    </div>
                  )
                })}
            </div>
          </div>
        </div>
      </div>
    </>
  )
}

export default Players
