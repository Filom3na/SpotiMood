import FormComponent from '../../subcomponents/FormComponent'
import axios from 'axios'
import { useNavigate } from 'react-router-dom'
import '../../styles/main.scss'


export default function Register() {
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
    confirmPassword: {
      type: 'password',
      placeholder: '***********',
    },
  }

  const navigate = useNavigate()

  const handleRegistration = async (formData) => {
    try {
      const response = await axios.post('api/register/', formData);
      console.log('Registration successful:', response.data);
      navigate('/login')
    } catch (error) {
      console.error('Registration failed:', error)
    }
  }

  return (
    <div className="form-page">
      <h2 style={{ textAlign: 'center' }}><span style={{ fontWeight: '500', fontSize: '50px' }}>Register</span></h2>
      <FormComponent request={handleRegistration} fields={fields} submit="Register" />
    </div>
  )
}