import FormComponent from '../../subcomponents/FormComponent.jsx'
import axios from 'axios'
import { setToken } from '../../lib/auth.js'
import { useNavigate } from 'react-router-dom'

export default function Login() {
  const fields = {
    username: {
      type: 'text',
      placeholder: 'Your last name',
    },
    email: {
      type: 'email',
      placeholder: 'example@email.com',
    },
    password: {
      type: 'password',
      placeholder: '***********',
    },
  }

  const navigate = useNavigate()

  const handleLogin = async (formData) => {
  
    try {
      const response = await axios.post('api/login/', {
        username: formData.username,
        password: formData.password,
      });
      const { access } = response.data;
  
      setToken(access);
      navigate('/mood-entry');
    } catch (error) {
      console.error('Login failed:', error);
    }
  };

  return (
    <div className="form-page">
      <h2>Login</h2>
      <FormComponent request={handleLogin} fields={fields} submit="Login" />
    </div>
  )
}