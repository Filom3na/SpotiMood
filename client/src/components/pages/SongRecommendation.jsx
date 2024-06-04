import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { useLocation } from 'react-router-dom';
import { getToken } from '../../lib/auth';

export default function SongRecommendation() {
  const [recommendedSongs, setRecommendedSongs] = useState([]);
  const location = useLocation();
  const selectedMood = location.state?.selectedMood;

  useEffect(() => {
    fetchRecommendedSongs();
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

  return (
    <div className="song-recommendation">
      <h2>Song Recommendation</h2>
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
        <p>No recommended songs found.</p>
      )}
    </div>
  );
}