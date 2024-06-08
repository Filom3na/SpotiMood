import React from 'react'
import ReactDOM from 'react-dom/client'
import Root from './Root.jsx'
import { createBrowserRouter, RouterProvider } from 'react-router-dom'

import Home from './components/pages/Home.jsx'
import Register from './components/pages/Register.jsx'
import Login from './components/pages/Login.jsx'
import ConnectSpotify from './components/pages/ConnectSpotify.jsx'
import MoodEntry from './components/pages/MoodEntry.jsx'
import SongRecommendation from './components/pages/SongRecommendation.jsx'
import MoodJournal from './components/pages/MoodJournal.jsx'
import MoodPlaylist from './components/pages/MoodPlaylist.jsx'

import 'bootstrap/dist/css/bootstrap.min.css'
import 'bootstrap/dist/js/bootstrap.bundle.js'

// Router
const router = createBrowserRouter([
  {
    path: '/',
    element: <Root />,
    children: [
      {
        path: '',
        element: <Home />
      },
      {
        path: 'register',
        element: <Register />
      },
      {
        path: 'login',
        element: <Login />
      },
      // {
      //   path: 'connect-spotify',
      //   element: <ConnectSpotify />
      // },
      {
        path: 'mood-entry',
        element: <MoodEntry />
      },
      {
        path: 'song-recommendation',
        element: <SongRecommendation />
      },
      {
        path: 'mood-journal',
        element: <MoodJournal />
      },
      {
        path: 'mood-playlist',
        element: <MoodPlaylist />
      }
    ]
  }
])

ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <RouterProvider router={router} />
  </React.StrictMode>
)