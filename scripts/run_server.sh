#!/bin/bash
cd ./backend || exit
flask --app main.py run --reload
