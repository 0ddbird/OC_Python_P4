import React from 'react'
import Background from './Background.jsx'
import Nav from './Nav.jsx'
import PropTypes from 'prop-types'
import Footer from './Footer.jsx'

const PageTemplate = ({ page }) => {
  return <>
    <Background/>
    <Nav/>
    {page}
    <Footer/>
  </>
}

PageTemplate.propTypes = {
  page: PropTypes.node
}

export default PageTemplate
