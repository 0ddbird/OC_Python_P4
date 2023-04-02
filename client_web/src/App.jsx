import React, { createContext, useState } from 'react'
import { BrowserRouter, Routes, Route } from 'react-router-dom'
import Home from './pages/Home.jsx'
import Players from './pages/Players.jsx'
import Tournaments from './pages/Tournaments.jsx'
import Reports from './pages/Reports.jsx'
import PlayerProfile from './pages/PlayerProfile.jsx'
import CreatePlayer from './pages/CreatePlayer.jsx'
import CreateTournament from './components/CreateTournament.jsx'
import Tournament from './pages/Tournament.jsx'

export const AppContext = createContext(null)

function App() {
  const [players, setPlayers] = useState(null)

  return (
    <>
      <AppContext.Provider value={{ players, setPlayers }}>
        <BrowserRouter>
          <Routes>
            <Route path="/" element={<Home />}></Route>
            <Route path="/players" element={<Players />}></Route>
            <Route path="/tournaments" element={<Tournaments />}></Route>
            <Route path="/reports" element={<Reports />}></Route>
            <Route path="/player/:id/edit" element={<PlayerProfile />}></Route>
            <Route path="/player/create" element={<CreatePlayer />}></Route>
            <Route path="/tournament/create" element={<CreateTournament />}></Route>
            <Route path="/tournament/:id" element={<Tournament />}></Route>
          </Routes>
        </BrowserRouter>
      </AppContext.Provider>
    </>
  )
}

export default App
