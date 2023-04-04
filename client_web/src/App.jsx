import React, { createContext, useState } from 'react'
import { BrowserRouter, Routes, Route } from 'react-router-dom'
import Home from './pages/Home.jsx'
import Players from './pages/Players.jsx'
import Tournaments from './pages/Tournaments.jsx'
import Reports from './pages/Reports.jsx'
import UpdatePlayer from './pages/UpdatePlayer.jsx'
import CreatePlayer from './pages/CreatePlayer.jsx'
import CreateTournament from './pages/CreateTournament.jsx'
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
            <Route path="/players/:id/edit" element={<UpdatePlayer />}></Route>
            <Route path="/players/create" element={<CreatePlayer />}></Route>
            <Route path="/tournaments/create" element={<CreateTournament />}></Route>
            <Route path="/tournaments/:id" element={<Tournament />}></Route>
          </Routes>
        </BrowserRouter>
      </AppContext.Provider>
    </>
  )
}

export default App
