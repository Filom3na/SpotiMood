import { Outlet } from 'react-router-dom'

import Navbar from './subcomponents/Navbar'
import Footer from './subcomponents/Footer'

export default function Root() {
  return (
    <>
      <Navbar />
      <main>
        <Outlet />
      </main>
      <Footer />
    </>
  )
}