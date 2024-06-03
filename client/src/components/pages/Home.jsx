import React from 'react';
import { Link } from 'react-router-dom';

function LandingPage() {
  return (
    <div className="landing-page">
      <header className="bg-dark text-white text-center py-5">
        <div className="container">
          <h1 className="display-4">SpotiMood</h1>
          <p className="lead">Discover music based on your mood</p>
        </div>
      </header>
      <main className="container my-5">
        <div className="row justify-content-center">
          <div className="col-md-6 text-center">
            <div className="cta-buttons">
              <Link to="/register" className="btn btn-primary btn-lg m-2">
                Register
              </Link>
              <Link to="/login" className="btn btn-secondary btn-lg m-2">
                Login
              </Link>
            </div>
          </div>
        </div>
        <div className="row mt-5">
          <div className="col-md-4">
            <div className="card">
              <div className="card-body">
                <h3 className="card-title">Select Your Mood</h3>
                <p className="card-text">Choose from a variety of moods to match your current emotional state.</p>
              </div>
            </div>
          </div>
          <div className="col-md-4">
            <div className="card">
              <div className="card-body">
                <h3 className="card-title">Get Song Recommendations</h3>
                <p className="card-text">Discover new songs that align with your selected mood.</p>
              </div>
            </div>
          </div>
          <div className="col-md-4">
            <div className="card">
              <div className="card-body">
                <h3 className="card-title">Create Mood Playlists</h3>
                <p className="card-text">Save your favorite songs to personalized mood playlists.</p>
              </div>
            </div>
          </div>
        </div>
      </main>
    </div>
  );
}

export default LandingPage;