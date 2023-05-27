import React, { useEffect, useState } from 'react'
import { NavLink } from 'react-router-dom'
import Pen from '../assets/pen.svg'
import APIService from '../api/ApiService.js'

const Tournaments = () => {
  const [tournaments, setTournaments] = useState(null)
  useEffect(() => {
    (async() => {
      const response = await APIService.getTournaments()
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
              <div className="tournaments_table_header_item">Rounds</div>
              <div className="tournaments_table_header_item">Status</div>
              <div className="tournaments_table_header_item"></div>
            </div>
            <div className="tournaments_table_body">
              {tournaments &&
                  tournaments.map((tournament) => {
                    return (
                        <div className="tournament_row" key={tournament.id}>
                          <div className="tournaments_table_body_item">{tournament.id}</div>
                          <div className="tournaments_table_body_item">{tournament.name}</div>
                          <div className="tournaments_table_body_item">{tournament.start_datetime}</div>
                          <div className="tournaments_table_body_item">{tournament.location}</div>
                          <div className="tournaments_table_body_item">{tournament.current_round} / {tournament.max_rounds}</div>
                          <div className="tournaments_table_body_item">{tournament.status}</div>
                          <NavLink to={`/tournaments/${tournament.id}`}>
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
