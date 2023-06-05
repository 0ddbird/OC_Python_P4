## OpenClassrooms - Python certification - Project #4

### Installation

- Clone the project
- Create a virtual environment with `python3 -m venv venv`
- Activate the virtual environment with `source ./venv/bin/activate`
- Install the dependencies with `pip install -r requirements.txt`

### Usage

To run the server:
`cd ./backend ; flask --app main.py run`  
Once the server is started, you can access this page from your browser:
http://localhost:5000/

To run the CLI client:
`cd ./cli_client ; python -m main`

To generate the flake8 report:  
`flake8 --format=html --htmldir=<name_of_the_output_directory> --exclude <name_of_the_venv_directory>`  
ex: `flake8 --format=html --htmldir=flake8_output --exclude venv`