// import React, { useEffect } from 'react';
// import { useNavigate } from 'react-router-dom';
// import axios from 'axios';

// export default function ConnectSpotify() {
//   const navigate = useNavigate();

//   useEffect(() => {
//     const connectSpotify = async () => {
//       const params = new URLSearchParams(window.location.hash.slice(1));
//       const accessToken = params.get('access_token');
//       const state = params.get('state');
//       const error = params.get('error');

//       if (error) {
//         console.error('Spotify authorization failed:', error);
//         // Handle the error case
//       } else if (accessToken && state) {
//         try {
//           // Send the access token and state to your backend as a POST request
//           await axios.post('/api/spotify-callback/', {
//             access_token: accessToken,
//             state: state
//           });

//           // Redirect to the /mood-entry route
//           navigate('/mood-entry');
//         } catch (error) {
//           console.error('Error processing Spotify callback:', error);
//         }
//       } else {
//         // Redirect to the Spotify authorization URL
//         window.location.href = '/api/spotify-authorize/';
//       }
//     };

//     connectSpotify();
//   }, [navigate]);

//   return <div>Connecting to Spotify...</div>;
// }


import React, { useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import axios from 'axios';

export default function ConnectSpotify() {
  const navigate = useNavigate();

  useEffect(() => {
    const connectSpotify = async () => {
      const params = new URLSearchParams(window.location.search);
      const code = params.get('code');
      const state = params.get('state');
      const error = params.get('error');

      if (error) {
        console.error('Spotify authorization failed:', error);
        // Handle the error case
      } else if (code && state) {
        try {
          // Send the code and state to your backend as a GET request
          await axios.get(`/api/spotify-callback/?code=${code}&state=${state}`);

          // Redirect to the /mood-entry route
          navigate('/mood-entry');
        } catch (error) {
          console.error('Error processing Spotify callback:', error);
        }
      } else {
        // Redirect to the Spotify authorization URL
        window.location.href = '/api/spotify-authorize/';
      }
    };

    connectSpotify();
  }, [navigate]);

  return <div>Connecting to Spotify...</div>;
}
