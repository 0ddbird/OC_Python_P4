#!/bin/bash

gnome-terminal --working-directory=backend/ --command="bash -c 'flask --app
main.py run --reload'" &
gnome-terminal --working-directory=client_web/ --command="bash -c 'yarn start'" &
