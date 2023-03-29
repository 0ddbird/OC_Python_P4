Start-Process pwsh -ArgumentList '-NoExit','-Command','cd backend/ ; flask
--app main.py run --reload'
Start-Process pwsh -ArgumentList '-NoExit','-Command','cd client_web/ ; yarn start'
