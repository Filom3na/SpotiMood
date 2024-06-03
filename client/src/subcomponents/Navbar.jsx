import React from 'react';
import { Link, NavLink, useLocation, useNavigate } from 'react-router-dom';
import { isLoggedIn, removeToken } from '../lib/auth'

export default function Navbar() {
  const location = useLocation();
  const navigate = useNavigate();

  function handleLogOut() {
    removeToken();
    navigate('/login');
  }

  return (
    <nav className="navbar navbar-expand-md bg-dark navbar-dark">
      <div className="container">
        <Link className="navbar-brand" to="/">SpotiMood</Link>
        <button className="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbar-collapse" aria-controls="navbar-collapse" aria-expanded="false" aria-label="Toggle navigation">
          <span className="navbar-toggler-icon"></span>
        </button>
        <div className="collapse navbar-collapse" id="navbar-collapse">
          <ul className="navbar-nav ms-auto">
            {isLoggedIn() ? (
              <>
                <li className="nav-item">
                  <NavLink className={({ isActive }) => isActive ? 'active nav-link' : 'nav-link'} to="/mood-entry">Mood Entry</NavLink>
                </li>
                <li className="nav-item">
                  <span className="nav-link" onClick={handleLogOut}>Log Out</span>
                </li>
              </>
            ) : (
              <>
                <li className="nav-item">
                  <NavLink className={({ isActive }) => isActive ? 'active nav-link' : 'nav-link'} to="/register">Register</NavLink>
                </li>
                <li className="nav-item">
                  <NavLink className={({ isActive }) => isActive ? 'active nav-link' : 'nav-link'} to="/login">Log In</NavLink>
                </li>
              </>
            )}
          </ul>
        </div>
      </div>
    </nav>
  );
}