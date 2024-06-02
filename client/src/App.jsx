import { useEffect } from 'react'
import axios from 'axios'

function App() {
  useEffect(() => {
    async function getMoodData() {
      try {
        const { data } = await axios.get('/api/moods/')
        console.log(data)
      } catch (error) {
        console.log(error)
      }
    }
    getMoodData()
  }, [])

  return (
    <div>
      <h1>SpotiMood</h1>
      <p>Welcome to SpotiMood!</p>
    </div>
  )
}

export default App