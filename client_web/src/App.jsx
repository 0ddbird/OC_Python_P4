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
import PageTemplate from './layout/Page.jsx'
import Round from './components/Round.jsx'

export const AppContext = createContext(null)

function App() {
  const [players, setPlayers] = useState(null)

  return (
      <>
        <AppContext.Provider value={{ players, setPlayers }}>
          <BrowserRouter>
            <Routes>
              <Route
                  path="/"
                  element={<PageTemplate page={<Home/>}/>}>
              </Route>
              <Route
                  path="/players"
                  element={<PageTemplate page={<Players/>}/>}>
              </Route>
              <Route
                  path="/tournaments"
                  element={<PageTemplate page={<Tournaments/>}/>}>
              </Route>
              <Route
                  path="/reports"
                  element={<PageTemplate page={<Reports/>}/>}>
              </Route>
              <Route
                  path="/players/:id/edit"
                  element={<PageTemplate page={<UpdatePlayer/>}/>}>
              </Route>
              <Route
                  path="/players/create"
                  element={<PageTemplate page={<CreatePlayer/>}/>}>
              </Route>
              <Route
                  path="/tournaments/create"
                  element={<PageTemplate page={<CreateTournament/>}/>}>
              </Route>
              <Route
                  path="/tournaments/:id"
                  element={<PageTemplate page={<Tournament/>}/>}>
              </Route>
              <Route
                  path="/tournaments/:tournamentID/:roundNumber"
                  element={<PageTemplate page={<Round/>}/>}>
              </Route>
            </Routes>
          </BrowserRouter>
        </AppContext.Provider>
      </>
  )
}

export default App
