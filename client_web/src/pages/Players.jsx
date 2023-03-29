import React, { useContext, useEffect } from 'react'
import Nav from '../components/Nav.jsx'
import { NavLink } from 'react-router-dom'
import { AppContext } from '../App.jsx'
import PlayerRow from '../components/PlayerRow.jsx'
import DeletePlayerIcon from '../assets/user-xmark-solid.svg'
import EditPlayerIcon from '../assets/user-pen-solid.svg'

export async function getPlayers () {
  const res = await fetch('http://127.0.0.1:5000/players', {
    headers: {
      'Content-Type': 'application/json',
      Accept: 'application/json'
    },
    method: 'GET'
  })
  return await res.json()
}

const Players = () => {
  const { players, setPlayers } = useContext(AppContext)

  useEffect(() => {
    getPlayers().then(players => {
      setPlayers(players)
    }
    )
  }, [])

  async function handleDeletePlayer (e, id) {
    const res = await fetch(`http://127.0.0.1:5000/player/${id}/delete`, {
      headers: {
        'Content-Type': 'application/json',
        Accept: 'application/json'
      },
      method: 'DELETE',
      body: JSON.stringify({ chess_id: id }
      )
    })
    return await res.json()
  }

  return (
      <>
        <Nav/>
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
              <span className="player_table_header_cell">Edit</span>
              <span className="player_table_header_cell">Delete</span>
            </div>
            <div className="player_table_content">
              {
              players && players.map(
                player => {
                  return (
                      <div key={player.player_id} className="player_row">
                        <PlayerRow player={player} />
                        <NavLink to={`/player/${player.player_id}`}>
                          <button className="edit_player_button">
                            <img src={EditPlayerIcon} className="edit_player_icon icon" alt="edit_player"/>
                          </button>
                        </NavLink>
                        <button onClick={(e) => handleDeletePlayer(e, player.player_id)} className="delete_player_button">
                          <img src={DeletePlayerIcon} className="delete_player_icon icon" alt="delete_player"/>
                        </button>
                      </div>

                  )
                }
              )
            }
            </div>

          </div>
          <NavLink to="/player/create">Add new player</NavLink>
        </div>
      </>
  )
}

export default Players
