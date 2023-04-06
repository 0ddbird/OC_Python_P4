class Router {
  static basePath = 'http://127.0.0.1:5000'
  static headers = {
    'Content-Type': 'application/json',
    Accept: 'application/json'
  }

  static createPlayer(body) {
    const route = {
      path: `${Router.basePath}/players`,
      method: 'POST'
    }
    return Router.makeRequest(route, body)
  }

  static getPlayers() {
    const route = {
      path: `${Router.basePath}/players`,
      method: 'GET'
    }
    return Router.makeRequest(route)
  }

  static getPlayer(id) {
    const route = {
      path: `${Router.basePath}/players/${id}`,
      method: 'GET'
    }
    return Router.makeRequest(route)
  }

  static updatePlayer(id, body) {
    const route = {
      path: `${Router.basePath}/players/${id}`,
      method: 'PUT'
    }
    return Router.makeRequest(route, body)
  }

  static deletePlayer(id) {
    const route = {
      path: `${Router.basePath}/players/${id}`,
      method: 'DELETE'
    }
    return Router.makeRequest(route)
  }

  static createTournament(tournament) {
    const route = {
      path: `${Router.basePath}/tournaments`,
      method: 'POST'
    }
    return Router.makeRequest(route, tournament)
  }

  static getTournaments() {
    const route = {
      path: `${Router.basePath}/tournaments`,
      method: 'GET'
    }
    return Router.makeRequest(route)
  }

  static getTournament(id) {
    const route = {
      path: `${Router.basePath}/tournaments/${id}`,
      method: 'GET'
    }
    return Router.makeRequest(route)
  }

  static handleNextRound(id) {
    const route = {
      path: `${Router.basePath}/tournaments/${id}/start`,
      method: 'POST'
    }
    return Router.makeRequest(route)
  }

  static makeRequest(route, body = null) {
    const options = { headers: Router.headers, method: route.method }
    if (body) options.body = JSON.stringify(body)
    return fetch(route.path, options)
  }
}

export default Router
