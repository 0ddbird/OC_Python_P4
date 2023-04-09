class ApiService {
  static basePath = 'http://127.0.0.1:5000'
  static headers = {
    'Content-Type': 'application/json',
    Accept: 'application/json'
  }

  static createPlayer(body) {
    const route = {
      path: `${ApiService.basePath}/players`,
      method: 'POST'
    }
    return ApiService.makeRequest(route, body)
  }

  static getPlayers() {
    const route = {
      path: `${ApiService.basePath}/players`,
      method: 'GET'
    }
    return ApiService.makeRequest(route)
  }

  static getPlayer(id) {
    const route = {
      path: `${ApiService.basePath}/players/${id}`,
      method: 'GET'
    }
    return ApiService.makeRequest(route)
  }

  static updatePlayer(id, body) {
    const route = {
      path: `${ApiService.basePath}/players/${id}`,
      method: 'PUT'
    }
    return ApiService.makeRequest(route, body)
  }

  static deletePlayer(id) {
    const route = {
      path: `${ApiService.basePath}/players/${id}`,
      method: 'DELETE'
    }
    return ApiService.makeRequest(route)
  }

  static createTournament(tournament) {
    const route = {
      path: `${ApiService.basePath}/tournaments`,
      method: 'POST'
    }
    return ApiService.makeRequest(route, tournament)
  }

  static getTournaments() {
    const route = {
      path: `${ApiService.basePath}/tournaments`,
      method: 'GET'
    }
    return ApiService.makeRequest(route)
  }

  static getTournament(id) {
    const route = {
      path: `${ApiService.basePath}/tournaments/${id}`,
      method: 'GET'
    }
    return ApiService.makeRequest(route)
  }

  static createRound(id) {
    const route = {
      path: `${ApiService.basePath}/tournaments/${id}`,
      method: 'POST'
    }
    console.log(route)
    return ApiService.makeRequest(route)
  }

  static getRound(id, roundNumber) {
    const route = {
      path: `${ApiService.basePath}/tournaments/${id}/${roundNumber}`,
      method: 'GET'
    }
    return ApiService.makeRequest(route)
  }

  static getGame(gameID) {
    const route = {
      path: `${ApiService.basePath}/games/${gameID}`,
      method: 'GET'
    }
    return ApiService.makeRequest(route)
  }

  static updateAllRoundGames(roundID, gamesResults) {
    const route = {
      path: `${ApiService.basePath}/rounds/${roundID}`,
      method: 'POST'
    }
    const body = { games: gamesResults }

    return ApiService.makeRequest(route, body)
  }

  static updateGame(gameID, p1Score, p2Score) {
    const route = {
      path: `${ApiService.basePath}/games/${gameID}`,
      method: 'PATCH'
    }
    const body = {
      p1_score: p1Score,
      p2_score: p2Score
    }
    return ApiService.makeRequest(route, body)
  }

  static getGamesByID(gamesIDS) {
    const route = {
      path: `${ApiService.basePath}/games/batch`,
      method: 'POST'
    }
    const body = {
      games_ids: gamesIDS
    }
    return ApiService.makeRequest(route, body)
  }

  static makeRequest(route, body = null) {
    const options = { headers: ApiService.headers, method: route.method }
    if (body) options.body = JSON.stringify(body)
    return fetch(route.path, options)
  }
}

export default ApiService
