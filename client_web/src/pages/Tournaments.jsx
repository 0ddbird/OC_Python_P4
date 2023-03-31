import React, { useEffect, useState } from 'react'
import Nav from '../components/Nav.jsx'
import { NavLink } from 'react-router-dom'
import { getTournaments } from '../api/TournamentsAPIServices.js'
import Background from '../components/Background.jsx'

const Tournaments = () => {
  const [tournaments, setTournaments] = useState(null)
  useEffect(() => {
    getTournaments().then(response => setTournaments(response.payload)
    )
  }, [])

  return (
      <>
        <Background/>
        <Nav/>
        <h1>Tournaments</h1>
        <NavLink to="/tournament/create">Create tournament</NavLink>
        <section className="tournaments_table">
          <div className="tournaments_table_header">
            <div className="tournaments_table_header_item">ID</div>
            <div className="tournaments_table_header_item">Name</div>
            <div className="tournaments_table_header_item">Date</div>
            <div className="tournaments_table_header_item">Location</div>
            <div className="tournaments_table_header_item">Number of players</div>
            <div className="tournaments_table_header_item">Max Rounds</div>
            <div className="tournaments_table_header_item">Current Rounds</div>
            <div className="tournaments_table_header_item">Status</div>
            <div className="tournaments_table_header_item">Edit</div>
          </div>
          <div className="tournaments_table_body">
            {
              tournaments && tournaments.map(tournament => {
                return (
                    <div className="tournament_row" key={tournament.tournament_id}>
                      <div className="tournaments_table_body_item">{tournament.tournament_id}</div>
                      <div className="tournaments_table_body_item">{tournament.name}</div>
                      <div className="tournaments_table_body_item">{tournament.creation_date}</div>
                      <div className="tournaments_table_body_item">{tournament.location}</div>
                      <div className="tournaments_table_body_item">{tournament.players_ids.length}</div>
                      <div className="tournaments_table_body_item">{tournament.max_rounds}</div>
                      <div className="tournaments_table_body_item">{tournament.current_round}</div>
                      <div className="tournaments_table_body_item">{tournament.status}</div>
                      <NavLink to={`/tournament/${tournament.tournament_id}`}>Edit</NavLink>
                    </div>
                )
              })
            }
          </div>
        </section>
      </>
  )
}

export default Tournaments
