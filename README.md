# SpotiMood: Your Mood-Based Music Companion


https://github.com/user-attachments/assets/97539e26-2c3e-4ddc-85da-ddf0d07f8f03


## Table of Contents
- [Project Overview](#project-overview)
- [Demo](#demo)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Detailed Planning Process](#detailed-planning-process)
- [Installation and Setup](#installation-and-setup)
- [API Endpoints](#api-endpoints)
- [Database Models](#database-models)
- [User Flow](#user-flow)
- [Component Structure](#component-structure)
- [Challenges and Solutions](#challenges-and-solutions)
- [Future Improvements](#future-improvements)
- [Reflections and Learnings](#reflections-and-learnings)

## Project Overview

SpotiMood is an innovative mood-based music recommendation application developed as part of the Software Engineering Immersive course at General Assembly. This full-stack project aims to bridge the gap between a user's emotional state and their music listening experience. By allowing users to select their current mood, SpotiMood provides tailored song and playlist recommendations, creating a personalized and emotionally resonant music journey.

The application was developed over a two-week sprint, showcasing the integration of a Django backend with a React frontend, and demonstrating proficiency in full-stack development, API integration, and user-centric design.

## Demo
The application is deployed on Heroku. You can explore Spotimood [here](https://spotimood-12bff2675e3a.herokuapp.com/).

## Features

1. **User Authentication**:
   - Secure registration and login system
   - JWT (JSON Web Token) based authentication for enhanced security

2. **Mood Selection and Entry**:
   - Interactive interface for users to select their current mood
   - Ability to create and store mood entries with timestamps

3. **Personalized Song Recommendations**:
   - Algorithm to match selected moods with appropriate music genres
   - Display of song recommendations based on user's mood entry

4. **User Mood Journal**:
   - Historical view of user's mood entries
   - Ability to edit or delete past mood entries

5. **Mood-Based Playlists**:
   - Creation and management of playlists associated with specific moods
   - Option to add recommended songs to mood-based playlists

6. **Responsive Design**:
   - Seamless user experience across various devices and screen sizes

7. **Data Seeding**:
   - Pre-populated database with a variety of moods, songs, and playlists for immediate user engagement

## Technologies Used

### Backend
- **Django**: Chosen for its robust ORM, built-in admin interface, and RESTful API capabilities
- **Django REST Framework**: Utilized to build a powerful and flexible API
- **PostgreSQL**: Selected as the database for its reliability and advanced features
- **Simple JWT**: Implemented for secure token-based authentication
- **Cors Headers**: Used to handle Cross-Origin Resource Sharing, allowing secure communication between frontend and backend

### Frontend
- **React**: Employed for building a dynamic and responsive user interface
- **React Router**: Utilized for seamless navigation within the single-page application
- **Axios**: Chosen for making HTTP requests to the backend API
- **SCSS**: Used for advanced styling capabilities and better code organization

### Development and Deployment Tools
- **Git & GitHub**: Employed for version control and collaborative development
- **Trello**: Utilized for project management and task tracking
- **Excalidraw**: Used for creating wireframes and visual designs
- **ERD Tool**: Employed for designing and visualizing the database schema
- **Heroku**: Selected for deploying both frontend and backend applications

## Detailed Planning Process

The planning phase of SpotiMood was crucial in laying a strong foundation for the project's development. Here's a detailed breakdown of the planning process:

1. **Conceptualization and User Stories**:
![uxflowchart](https://github.com/user-attachments/assets/8440c6df-23f1-41d5-9587-98869e99251e)

   - Brainstorming sessions to define the core concept of a mood-based music recommendation app
   - Creation of user stories to outline key functionalities from a user's perspective
   - Example user story: "As a user, I want to select my current mood so that I can receive song recommendations that match my emotional state."

3. **Trello Board Organization**:
<img width="952" alt="Screenshot 2024-09-13 at 16 24 58" src="https://github.com/user-attachments/assets/1fda45fa-376e-4857-99c0-46beac66945d">

   - Set up a Trello board with columns for "To Do", "In Progress", and "Done"
   - Created cards for each feature and user story
   - Assigned priority levels and time estimates to each task
   - Regularly updated the board throughout the development process to track progress

4. **Wireframing with Excalidraw**:
![wireframe](https://github.com/user-attachments/assets/ce0165d4-c4f7-432b-aa2c-c7b1b1eb7812)

   - Created low-fidelity wireframes for each main component of the application
   - Designed the user flow from login to mood selection and song recommendations
   - Iterated on designs based on peer and instructor feedback
   - Key wireframes included:
     - Home page layout
     - User registration and login forms
     - Mood selection interface
     - Song recommendation display
     - User mood journal view

5. **Database Schema Design (ERD)**:
![erd](https://github.com/user-attachments/assets/90ce385c-0943-4253-a0a9-6ee557677c4e)
<img width="389" alt="Screenshot 2024-09-13 at 16 24 20" src="https://github.com/user-attachments/assets/d35459d4-32f8-4e2b-ba65-0d6e4bd43fa0">

   - Utilized an ERD tool to visually map out the database structure
   - Defined relationships between models (User, Mood, MoodEntry, Song, MoodPlaylist)
   - Identified primary and foreign keys
   - Planned for scalability and future feature additions

6. **API Endpoint Planning**:
<img width="296" alt="Screenshot 2024-09-13 at 16 24 35" src="https://github.com/user-attachments/assets/50a2a29d-ab42-41fc-9e7b-962950b4c805">

   - Created a comprehensive list of required API endpoints
   - Documented HTTP methods, URL patterns, request payloads, and expected responses for each endpoint
   - Considered authentication requirements for protected routes
   - Planned for error handling and appropriate status codes

8. **Technology Stack Selection**:
   - Evaluated various technologies and frameworks
   - Chose Django for the backend due to its robustness and team familiarity
   - Selected React for the frontend to create a dynamic and responsive UI

9. **Project Timeline and Milestones**:
   - Set deadlines for completing backend setup, API development, frontend components, and integration
   - Allocated time for testing, bug fixing, and potential feature additions

This thorough planning process provided a clear roadmap for development, helping to mitigate risks and ensure a focused approach to building SpotiMood.

## Installation and Setup

To set up SpotiMood locally, follow these steps:

1. **Clone the Repository**:
   ```
   git clone https://github.com/your-username/spotimood.git
   cd spotimood
   ```

2. **Backend Setup**:
   ```
   cd backend
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   pip install -r requirements.txt
   python manage.py migrate
   python manage.py createsuperuser  # Follow prompts to create an admin user
   python manage.py runserver
   ```

3. **Frontend Setup**:
   ```
   cd ../frontend
   npm install
   npm start
   ```

4. **Environment Variables**:
   Create a `.env` file in the backend directory with the following variables:
   ```
   SECRET_KEY=your_django_secret_key
   DEBUG=True
   DATABASE_URL=your_database_url
   CORS_ALLOWED_ORIGINS=http://localhost:3000
   ```

5. **Database Seeding**:
   To populate the database with initial data, run:
   ```
   python manage.py loaddata initial_data.json
   ```

6. **Accessing the Application**:
   - Backend API will be available at `http://localhost:8000/api/`
   - Frontend will be served at `http://localhost:3000/`
   - Admin interface can be accessed at `http://localhost:8000/admin/`

## API Endpoints

SpotiMood's backend API provides the following endpoints:

1. **User Authentication**:
   - `POST /api/register/`: Register a new user
     - Payload: `{ "username": "string", "email": "string", "password": "string" }`
   - `POST /api/login/`: Authenticate and receive JWT tokens
     - Payload: `{ "username": "string", "password": "string" }`
   - `POST /api/token/refresh/`: Refresh JWT token
     - Payload: `{ "refresh": "string" }`

2. **Moods**:
   - `GET /api/moods/`: Retrieve list of available moods
   - `GET /api/moods/{id}/`: Retrieve details of a specific mood

3. **Mood Entries**:
   - `GET /api/mood-entries/`: List user's mood entries
   - `POST /api/mood-entries/`: Create a new mood entry
     - Payload: `{ "mood": int }`
   - `PUT /api/mood-entries/{id}/`: Update a specific mood entry
   - `DELETE /api/mood-entries/{id}/`: Delete a specific mood entry

4. **Song Recommendations**:
   - `GET /api/recommendations/?mood={mood_id}`: Get song recommendations based on mood

5. **Playlists**:
   - `GET /api/playlists/`: List user's playlists
   - `POST /api/playlists/`: Create a new playlist
     - Payload: `{ "name": "string", "mood": int }`
   - `PUT /api/playlists/{id}/`: Update a specific playlist
   - `DELETE /api/playlists/{id}/`: Delete a specific playlist

6. **Mood-Based Playlists**:
   - `GET /api/mood-playlists/`: List all mood-based playlists
   - `POST /api/mood-playlists/`: Create or update a mood-based playlist
     - Payload: `{ "name": "string", "spotify_playlist_id": "string", "mood": int }`

All endpoints, except for register and login, require JWT authentication.

## Database Models

SpotiMood's database schema consists of the following models:

1. **User** (extends Django's AbstractUser):
   ```python
   class User(AbstractUser):
       spotify_access_token = models.CharField(max_length=255, null=True, blank=True)
       spotify_refresh_token = models.CharField(max_length=255, null=True, blank=True)
       spotify_token_expires_at = models.DateTimeField(null=True, blank=True)
   ```

2. **Mood**:
   ```python
   class Mood(models.Model):
       name = models.CharField(max_length=100)
       genres = models.CharField(max_length=255, null=True, blank=True)
   ```

3. **MoodEntry**:
   ```python
   class MoodEntry(models.Model):
       user = models.ForeignKey(User, on_delete=models.CASCADE)
       mood = models.ForeignKey(Mood, on_delete=models.CASCADE)
       created_at = models.DateTimeField(auto_now_add=True)
   ```

4. **Song**:
   ```python
   class Song(models.Model):
       title = models.CharField(max_length=100)
       artist = models.CharField(max_length=100)
       spotify_id = models.CharField(max_length=100)
       mood = models.ForeignKey(Mood, on_delete=models.CASCADE, null=True, blank=True)
       mood_playlist = models.ForeignKey('MoodPlaylist', on_delete=models.CASCADE, null=True, blank=True)
   ```

5. **MoodPlaylist**:
   ```python
   class MoodPlaylist(models.Model):
       name = models.CharField(max_length=100)
       spotify_playlist_id = models.CharField(max_length=100)
       mood = models.ForeignKey(Mood, on_delete=models.CASCADE)
   ```

These models form the core structure of the SpotiMood application, allowing for efficient storage and retrieval of user data, moods, songs, and playlists.

## User Flow

The typical user journey through SpotiMood is as follows:

1. **Home Page**: User arrives at the landing page, which showcases the app's features and benefits.

2. **Registration/Login**: New users can register for an account, while existing users can log in.

3. **Mood Selection**: After authentication, users are presented with a mood selection interface.

4. **Mood Entry**: Upon selecting a mood, a new mood entry is created and stored in the database.

5. **Song Recommendations**: Based on the selected mood, the app displays a list of recommended songs.

6. **Playlist Creation**: Users can create a new playlist based on their current mood and add recommended songs to it.

7. **Mood Journal**: Users can view their mood history and associated playlists in the journal section.

8. **Profile Management**: Users can update their profile information and manage their account settings.

This flow ensures a seamless and intuitive experience for users to explore their moods and discover new music.

## Component Structure

The React frontend is organized into the following main components:

1. **App**: The root component that handles routing and global state.

2. **Navbar**: Provides navigation links and displays user authentication status.

3. **Home**: Landing page component introducing the app's features.

4. **Auth**: 
   - Register: Handles user registration.
   - Login: Manages user login.

5. **MoodSelection**: Displays available moods for user selection.

6. **MoodEntry**: Allows users to create a new mood entry.

7. **SongRecommendations**: Displays recommended songs based on the selected mood.

8. **Playlist**: 
   - PlaylistCreate: For creating new playlists.
   - PlaylistList: Displays user's playlists.
   - PlaylistDetail: Shows details of a specific playlist.

9. **MoodJournal**: Displays the user's mood history and associated playlists.

10. **Profile**: Allows users to view and edit their profile information.

This component structure promotes modularity and reusability throughout the application.

## Challenges and Solutions

Throughout the development of SpotiMood, several challenges were encountered and overcome:

1. **Spotify API Integration**:
   - Challenge: Implementing OAuth 2.0 flow and managing access tokens.
   - Solution: Created a custom authentication flow using Django's session middleware to store Spotify tokens securely.

2. **Mood-Based Recommendation Algorithm**:
   - Challenge: Developing an accurate system to match moods with appropriate songs.
   - Solution: Implemented a weighted genre-based algorithm, considering both user preferences and mood-genre associations.

3. **Real-Time Updates**:
   - Challenge: Ensuring playlist changes reflect immediately without full page reloads.
   - Solution: Utilized React's state management and implemented a custom hook for real-time data fetching.

4. **Performance Optimization**:
   - Challenge: Slow loading times when fetching large playlists.
   - Solution: Implemented pagination and lazy loading for playlist tracks, significantly improving load times.

5. **Cross-Origin Resource Sharing (CORS)**:
   - Challenge: Frontend unable to make requests to the backend due to CORS restrictions.
   - Solution: Properly configured Django's CORS headers, allowing specific origins to access the API.

6. **State Management**:
   - Challenge: Managing complex state across multiple components.
   - Solution: Implemented React Context API for global state management, reducing prop drilling and simplifying data flow.

These challenges provided valuable learning experiences and contributed to the robustness of the final application.

## Future Improvements

While SpotiMood has achieved its core functionality, there are several areas identified for future enhancement:

1. **Advanced Mood Analysis**: Implement natural language processing to analyze user inputs for more nuanced mood detection.

2. **Social Features**: Add the ability for users to share playlists and compare mood patterns with friends.

3. **Mood Trends and Insights**: Develop a dashboard showcasing mood trends over time and correlations with music choices.

4. **Integration with Wearables**: Connect with fitness trackers or smartwatches to gather biometric data for more accurate mood prediction.

5. **Collaborative Playlists**: Allow users to create and contribute to mood-based collaborative playlists.

6. **Offline Mode**: Implement caching strategies to enable basic app functionality without an internet connection.

7. **Voice Commands**: Integrate voice recognition for hands-free mood selection and playlist control.

8. **Personalized AI DJ**: Develop an AI system that learns user preferences and creates dynamic, mood-appropriate playlists in real-time.

These improvements would further enhance the user experience and expand the app's capabilities.

## Reflections and Learnings
Developing SpotiMood has been an invaluable learning experience, offering insights into full-stack development, API integration, and user-centric design. Here are some key reflections and learnings from the project:

Full-Stack Integration:

The project reinforced the importance of planning the integration between frontend and backend from the outset.
Learned to effectively manage state across the entire application stack, ensuring data consistency between the server and client.


API Design and Documentation:

Gained appreciation for well-documented APIs and their impact on development speed and collaboration.
Learned to design RESTful APIs with clear endpoints, consistent naming conventions, and appropriate HTTP methods.


Authentication and Security:

Deepened understanding of JWT-based authentication and its implementation in both Django and React.
Learned about the importance of secure token storage and the risks of cross-site scripting (XSS) attacks.


Database Modeling:

Improved skills in designing efficient database schemas that balance normalization with query performance.
Learned to leverage Django's ORM for complex queries and data relationships.


React Best Practices:

Enhanced understanding of React hooks and functional components.
Improved skills in managing complex state and side effects in React applications.


Error Handling and Debugging:

Developed strategies for effective error handling across the full stack.
Improved debugging skills, particularly in identifying and resolving issues in asynchronous operations.


User Experience Design:

Gained insights into creating intuitive user flows and responsive designs.
Learned the importance of user feedback in the iterative design process.


Project Management:

Improved skills in breaking down large projects into manageable tasks and setting realistic timelines.
Learned the value of daily stand-ups and regular progress tracking in maintaining project momentum.


Continuous Integration and Deployment:

Gained experience in setting up CI/CD pipelines for automated testing and deployment.
Learned about the challenges and best practices in deploying full-stack applications.


Working with External APIs:

Although full Spotify integration wasn't implemented due to time constraints, the planning process provided valuable insights into working with complex external APIs.
Learned about OAuth flows and the challenges of managing third-party access tokens.


## Conclusion
SpotiMood represents a significant milestone in my journey as a full-stack developer. While the project achieved its core functionality of providing mood-based music recommendations using seeded data, the process of planning and partial implementation of Spotify integration has laid a strong foundation for future enhancements.
The challenges faced during development, from database modeling to frontend state management, have contributed to a deeper understanding of web application architecture and best practices. The project not only showcases technical skills but also demonstrates the ability to conceptualize, plan, and execute a complex application from start to finish.
Moving forward, SpotiMood has immense potential for growth. The groundwork laid for Spotify integration can be built upon to create a fully functional, real-time music recommendation system. Additionally, the insights gained from this project will be invaluable in tackling future full-stack challenges and in continuing to grow as a developer.
