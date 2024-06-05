import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { useLocation, useNavigate } from 'react-router-dom';
import { getToken } from '../../lib/auth';

export default function SongRecommendation() {
  const [recommendedSongs, setRecommendedSongs] = useState([]);
  const [username, setUsername] = useState('');
  const [moodName, setMoodName] = useState('');
  const location = useLocation();
  const selectedMood = location.state?.selectedMood;
  const navigate = useNavigate();

  useEffect(() => {
    fetchRecommendedSongs();
    fetchUserProfile();
    fetchMoodName();
  }, [selectedMood]);

  const fetchRecommendedSongs = async () => {
    try {
      const token = getToken();
      const response = await axios.get(`/api/mood-recommendations/${selectedMood}/`, {
        headers: {
          Authorization: `Bearer ${token}`,
        },
      });
      setRecommendedSongs(response.data);
    } catch (error) {
      console.error('Error fetching recommended songs:', error);
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
      setUsername(response.data.username);
    } catch (error) {
      console.error('Error fetching user profile:', error);
    }
  };

  const fetchMoodName = async () => {
    try {
      const response = await axios.get(`/api/moods/${selectedMood}/`);
      setMoodName(response.data.name);
    } catch (error) {
      console.error('Error fetching mood name:', error);
    }
  };

  const handleMoodJournalClick = () => {
    navigate('/mood-journal');
  };

  return (
    <div className="song-recommendation-wrapper">
      <div className="song-recommendation">
        <h2 className="title">Song Recommendation</h2>
        <p className="message">
          Hey {username}, we have noticed you feel {moodName}. This is a song recommendation for you:
        </p>
        {recommendedSongs.length > 0 ? (
          <ul className="song-list">
            {recommendedSongs.map((song) => (
              <li key={song.id} className="song-item">
                <div className="song-details">
                  <h3 className="song-title">{song.title}</h3>
                  <p className="song-artist">{song.artist}</p>
                </div>
                <div className="song-actions">
                  <button className="play-button">Play</button>
                  <button className="add-button">Add to Playlist</button>
                </div>
              </li>
            ))}
          </ul>
        ) : (
          <p className="no-songs">No recommended songs found.</p>
        )}
        <button className="mood-journal-button" onClick={handleMoodJournalClick}>
          Go to Mood Journal
        </button>
      </div>
    </div>
  );
}