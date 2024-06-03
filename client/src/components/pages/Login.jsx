import FormComponent from '../../subcomponents/FormComponent.jsx'
import axios from 'axios'
import { setToken } from '../../lib/auth.js'
import { useNavigate } from 'react-router-dom'

export default function Login() {
  const fields = {
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

  async function handleLogin(formData) {
    const { data: { token } } = await axios.post('/api/login', formData)
    setToken(token)
    navigate('/mood-entry')
  }

  return (
    <div className="form-page">
      <h2>Login</h2>
      <FormComponent request={handleLogin} fields={fields} submit="Login" />
    </div>
  )
}