## OpenClassrooms - Python certification - Project #4

### Installation

- Clone the project
- Create a virtual environment with `python3 -m venv venv`
- Activate the virtual environment with `source ./venv/bin/activate`
- Install the dependencies with `pip install -r requirements.txt`

### Usage

To run the server:
`cd ./backend ; flask --app main.py run --reload`
TODO: servir l'app react dans un dossier statique web/ par Flask
To run the web client:
`cd ./web_client ; yarn start`

To run the CLI client:

`cd ./cli_client ; python -m main`

### Project status

v1 is functionnal

### Improvements

- CLI client : UX improvements to update a tournament
- CLI client : autorun Flask server from client
- Web client : UI improvements to the Tournament page
- Jinja templates : CSS layout 

