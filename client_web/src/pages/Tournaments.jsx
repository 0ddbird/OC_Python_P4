import React, { useEffect, useState } from 'react'
import { NavLink } from 'react-router-dom'
import Pen from '../assets/pen.svg'
import Router from '../router/Router.js'

const Tournaments = () => {
  const [tournaments, setTournaments] = useState(null)
  useEffect(() => {
    (async() => {
      const response = await Router.getTournaments()
      if (response.ok) {
        const jsonResponse = await response.json()
        const tournaments = jsonResponse.payload
        setTournaments(tournaments)
      }
    })()
  }, [])

  return (
      <>
        <section id="tournaments_page">
          <h1>Tournaments</h1>
          <section className="tournaments_table">
            <div className="tournaments_table_header">
              <div className="tournaments_table_header_item">ID</div>
              <div className="tournaments_table_header_item">Name</div>
              <div className="tournaments_table_header_item">Date</div>
              <div className="tournaments_table_header_item">Location</div>
              <div className="tournaments_table_header_item">Players</div>

              <div className="tournaments_table_header_item">Current Round</div>
              <div className="tournaments_table_header_item">Status</div>
              <div className="tournaments_table_header_item"></div>
            </div>
            <div className="tournaments_table_body">
              {tournaments &&
                  tournaments.map((tournament) => {
                    return (
                        <div className="tournament_row" key={tournament.tournament_id}>
                          <div className="tournaments_table_body_item">{tournament.tournament_id}</div>
                          <div className="tournaments_table_body_item">{tournament.name}</div>
                          <div className="tournaments_table_body_item">{tournament.creation_date}</div>
                          <div className="tournaments_table_body_item">{tournament.location}</div>
                          <div className="tournaments_table_body_item">{tournament.players_ids.length}</div>
                          <div className="tournaments_table_body_item">{tournament.current_round} / {tournament.max_rounds}</div>
                          <div className="tournaments_table_body_item">{tournament.status}</div>
                          <NavLink to={`/tournaments/${tournament.tournament_id}`}>
                            <img className="icon" src={Pen} alt="edit"/>
                          </NavLink>
                        </div>
                    )
                  })}
            </div>
          </section>
        </section>
      </>
  )
}

export default Tournaments
