import React, { useContext, useEffect } from 'react'
import APIService from '../api/ApiService.js'
import { NavLink } from 'react-router-dom'
import { AppContext } from '../App.jsx'
import Player from '../components/Player.jsx'
import DeletePlayerIcon from '../assets/user-xmark-solid.svg'
import EditPlayerIcon from '../assets/user-pen-solid.svg'

const Players = () => {
  const { players, setPlayers } = useContext(AppContext)
  const fields = ['id', 'chessId', 'firstName', 'lastName', 'birthdate', 'elo']
  useEffect(() => {
    (async() => {
      const response = await APIService.getPlayers()
      if (response.ok) {
        const jsonResponse = await response.json()
        setPlayers(jsonResponse.payload)
      }
    })()
  }, [])

  async function handleDeletePlayer(e, id) {
    e.preventDefault()
    const response = await APIService.deletePlayer(id)
    if (response.ok) {
      setPlayers(players.filter((player) => player.id !== id))
    }
  }

  return (
      <>
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
                          <div key={player.id} className="player_row">
                            <Player player={player} fields={fields}/>
                            <NavLink to={`/players/${player.id}/edit`}>
                              <button className="edit_player_button">
                                <img src={EditPlayerIcon} className="edit_player_icon icon" alt="edit_player"/>
                              </button>
                            </NavLink>
                            <button onClick={(e) => handleDeletePlayer(e, player.id)} className="delete_player_button">
                              <img src={DeletePlayerIcon} className="delete_player_icon icon" alt="delete_player"/>
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
