import React from 'react'
import ReportsForm from '../components/ReportsForm.jsx'

const Reports = () => {
  return (
      <div>
        <h1>Reports</h1>
        <a href="http://localhost:5000/reports/players" target="_blank" rel="noopener noreferrer">
          Open Player Reports
        </a>
        <a href="http://localhost:5000/reports/tournaments" target="_blank" rel="noopener noreferrer">
          Open Tournaments Reports
        </a>

        <h2>Generate Tournament Report</h2>
        <ReportsForm/>
      </div>
  )
}

export default Reports
