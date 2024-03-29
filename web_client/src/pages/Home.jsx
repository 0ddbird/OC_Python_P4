import React from 'react'
import Logo from '../assets/chess-solid.svg'

const Home = () => {
  return (
      <>
        <section id="hero_section">
          <div className="hero_content">
            <img src={Logo} alt="logo" className="home_logo"/>
            <h1 className="home_heading">CheckMate</h1>
            <p className="home_subheading">Your chess tournament assistant.</p>
            <p className="home_description">
              Checkmate helps you manage chess tournaments easily.
              <br/>
              Add players, create tournaments, and track results.
            </p>
          </div>
        </section>
      </>
  )
}

export default Home
