import React from 'react'
import Nav from '../components/Nav.jsx'
import Background from '../components/Background.jsx'

const Home = () => {
  return (
      <>
        <Background/>
          <section id="hero_section">
            <Nav/>
            <div className="hero_content">
              <h1 className="home_heading">CheckMate</h1>
              <p className="home_subheading">Your chess tournament companion.</p>
              <p className="home_description">
                Checkmate helps you manage chess tournaments easily.<br/>
                Add players, create tournaments, and track results.
              </p>
            </div>
          </section>

      </>
  )
}

export default Home
