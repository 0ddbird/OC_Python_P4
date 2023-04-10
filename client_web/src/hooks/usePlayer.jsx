import { useEffect, useState } from 'react'
import APIService from '../api/ApiService.js'

function usePlayer(id) {
  const [player, setPlayer] = useState(null)

  useEffect(() => {
    if (id) {
      (async() => {
        const response = await APIService.getPlayer(id)
        if (response.ok) {
          const jsonResponse = await response.json()
          const playerData = jsonResponse.payload
          setPlayer({
            name: `${playerData.first_name} ${playerData.last_name}`
          })
        }
      })()
    }
  }, [id])

  return player
}

export default usePlayer
