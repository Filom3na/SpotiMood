import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { getToken } from '../../lib/auth';
import '../../styles/main.scss';

export default function MoodJournal() {
  const [moodEntries, setMoodEntries] = useState([]);
  const [username, setUsername] = useState('');

  useEffect(() => {
    fetchMoodEntries();
    fetchUserProfile();
  }, []);

  const fetchMoodEntries = async () => {
    try {
      const token = getToken();
      const response = await axios.get('/api/mood-entries/', {
        headers: {
          Authorization: `Bearer ${token}`,
        },
      });
      const entriesWithMoodNames = await Promise.all(
        response.data.map(async (entry) => {
          const moodName = await fetchMoodName(entry.mood);
          return { ...entry, moodName };
        })
      );
      setMoodEntries(entriesWithMoodNames);
    } catch (error) {
      console.error('Error fetching mood entries:', error);
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
      console.log(response.data);
      setUsername(response.data.username);
    } catch (error) {
      console.error('Error fetching user profile:', error);
    }
  };

  const fetchMoodName = async (moodId) => {
    try {
      const response = await axios.get(`/api/moods/${moodId}/`);
      return response.data.name;
    } catch (error) {
      console.error('Error fetching mood name:', error);
      return '';
    }
  };

  return (
    <div className="mood-journal-wrapper">
      <div className="mood-journal">
        <h2 className="title">Mood Journal</h2>
        {moodEntries.length > 0 ? (
          <ul className="mood-entry-list">
            {moodEntries.map((entry) => (
              <li key={entry.id} className="mood-entry-item">
                <div className="mood-entry-details">
                  <p className="mood-entry-text">
                    On {new Date(entry.created_at).toLocaleDateString()}, {username} was feeling{' '}
                    {entry.moodName}.
                  </p>
                  {entry.recommended_song && (
                    <p className="mood-entry-song">
                      Recommended Song: {entry.recommended_song.title} by{' '}
                      {entry.recommended_song.artist}
                    </p>
                  )}
                </div>
              </li>
            ))}
          </ul>
        ) : (
          <p className="no-entries">No mood entries found.</p>
        )}
      </div>
    </div>
  );
}