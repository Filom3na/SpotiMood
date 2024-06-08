import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { getToken } from '../../lib/auth';

const MoodPlaylist = () => {
  const [playlists, setPlaylists] = useState([]);

  useEffect(() => {
    fetchPlaylists();
  }, []);

  const fetchPlaylists = async () => {
    try {
      const token = getToken();
      const response = await axios.get('/api/mood-playlists/', {
        headers: {
          Authorization: `Bearer ${token}`,
        },
      });
      setPlaylists(response.data);
    } catch (error) {
      console.error('Error fetching playlists:', error);
    }
  };

  const associateSongsWithPlaylist = async (playlistId) => {
    try {
      const token = getToken();
      await axios.post(
        '/api/associate-songs/',
        { mood: playlistId},
        {
          headers: {
            'Content-Type': 'application/json',
            Authorization: `Bearer ${token}`,
          },
        }
      );
    } catch (error) {
      console.error('Error associating songs with playlist:', error);
    }
  };

  const handleDeletePlaylist = async (playlistId) => {
    try {
      const token = getToken();
      await axios.delete(`/api/mood-playlists/${playlistId}/`, {
        headers: {
          Authorization: `Bearer ${token}`,
        },
      });
      setPlaylists(playlists.filter((playlist) => playlist.id !== playlistId));
    } catch (error) {
      console.error('Error deleting playlist:', error);
    }
  };

  return (
    <div className="mood-playlist-container">
      <h2 className="mood-playlist-title">Mood Playlists</h2>
      {playlists.length > 0 ? (
        <ul className="mood-playlist-list">
          {playlists.map((playlist) => (
            <li key={playlist.id} className="mood-playlist-item">
              <h3 className="mood-playlist-name">
                {playlist.name} 
                {/* ({playlist.mood.name}) */}
              </h3>
              {playlist.songs && playlist.songs.length > 0 ? (
                <ul className="song-list">
                  {playlist.songs.map((song) => (
                    <li key={song.id} className="song-item">
                      <span className="song-title">{song.title}</span> - <span className="song-artist">{song.artist}</span>
                    </li>
                  ))}
                </ul>
              ) : (
                <p className="no-songs-message">No songs found for this playlist.</p>
              )}
              <button className="delete-playlist-button" onClick={() => handleDeletePlaylist(playlist.id)}>
                Delete Playlist
              </button>
            </li>
          ))}
        </ul>
      ) : (
        <p className="no-playlists-message">No playlists found.</p>
      )}
    </div>
  );
};

export default MoodPlaylist;