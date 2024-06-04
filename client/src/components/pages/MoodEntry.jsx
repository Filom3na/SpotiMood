import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { useNavigate } from 'react-router-dom';
import { getToken } from '../../lib/auth';

export default function MoodEntry() {
  const [moods, setMoods] = useState([]);
  const [selectedMood, setSelectedMood] = useState('');
  const [username, setUsername] = useState('');
  const navigate = useNavigate();

  useEffect(() => {
    fetchMoods();
    fetchUserProfile();
  }, []);

  const fetchMoods = async () => {
    try {
      const response = await axios.get('/api/moods/');
      setMoods(response.data);
    } catch (error) {
      console.error('Error fetching moods:', error);
    }
  };

  const fetchUserProfile = async () => {
    try {
      const token = getToken();
      const response = await axios.get('/api/profile/', {
        headers: {
          Authorization: `Bearer ${token}`,
        },
      });
      console.log(response.data)
      setUsername(response.data.username);
    } catch (error) {
      console.error('Error fetching user profile:', error);
    }
  };

  const handleMoodChange = (e) => {
    setSelectedMood(e.target.value);
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    if (selectedMood) {
      try {
        const token = getToken();
        await axios.post(
          '/api/mood-entries/',
          { mood: selectedMood },
          {
            headers: {
              Authorization: `Bearer ${token}`,
            },
          }
        );
        navigate('/song-recommendation', { state: { selectedMood } });
      } catch (error) {
        console.error('Error creating mood entry:', error);
      }
    }
  };

  return (
    <div className="mood-entry">
      <h2 className="greeting">Hey {username}, welcome back! How are you feeling today?</h2>
      <form className="mood-form" onSubmit={handleSubmit}>
        <div className="form-group">
          <label htmlFor="mood">Select your current mood:</label>
          <select id="mood" className="mood-select" value={selectedMood} onChange={handleMoodChange}>
            <option value="">Choose a mood</option>
            {moods.map((mood) => (
              <option key={mood.id} value={mood.id}>
                {mood.name}
              </option>
            ))}
          </select>
        </div>
        <button type="submit" className="submit-button">Submit</button>
      </form>
      <p className="timestamp">Today is: {new Date().toLocaleString()}</p>
    </div>
  )
}