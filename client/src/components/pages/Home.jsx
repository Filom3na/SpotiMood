import React from 'react';
import { Link } from 'react-router-dom';
import '../../styles/main.scss';
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col'
import Card from 'react-bootstrap/Card'
import Carousel from 'react-bootstrap/Carousel';



function Home() {
  return (
    <div className="hero-image">
      <div className="home-container">
        <div className="title-container">
          <h1 className="title">SpotiMood</h1>
        </div>
        <div className="content-container">
          <h1>Welcome to SpotiMood</h1>
          <p className="description">
            SpotiMood is an app that helps you discover music based on your mood. Whether you're feeling happy, sad, energetic, or relaxed, SpotiMood has got you covered.
          </p>
          <Row className="feature-carousel-row">
            <Col xs={12}>
              <Card className="feature-carousel">
                <Card.Body>
                  <Carousel>
                    <Carousel.Item>
                      <div className="feature">
                        <i className="fas fa-music feature-icon"></i>
                        <h3 className="feature-title">Mood-Based Music</h3>
                        <p className="feature-description">
                          Select your current mood and let SpotiMood curate a playlist that matches your emotional state.
                        </p>
                      </div>
                    </Carousel.Item>
                    <Carousel.Item>
                      <div className="feature">
                        <i className="fas fa-list feature-icon"></i>
                        <h3 className="feature-title">Personalized Playlists</h3>
                        <p className="feature-description">
                          Create and save personalized playlists based on your favorite moods and discover new songs.
                        </p>
                      </div>
                    </Carousel.Item>
                    <Carousel.Item>
                      <div className="feature">
                        <i className="fas fa-journal-whills feature-icon"></i>
                        <h3 className="feature-title">Mood Journaling</h3>
                        <p className="feature-description">
                          Keep track of your moods and reflect on your emotional journey through the power of music.
                        </p>
                      </div>
                    </Carousel.Item>
                  </Carousel>
                </Card.Body>
              </Card>
            </Col>
          </Row>
          <div className="cta-container">
            <Link to="/register" className="cta-button">Get Started</Link>
          </div>
        </div>
      </div>
    </div>
  );
}

export default Home;