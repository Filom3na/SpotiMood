import { useState } from 'react'
import { Container, FormGroup, FormLabel, FormControl } from 'react-bootstrap'
import 'bootstrap/dist/css/bootstrap.min.css'
import '../styles/main.scss'

export default function FormComponent({ submit, fields, request }) {
  const [formData, setFormData] = useState(
    Object.fromEntries(Object.entries(fields).map(([name, field]) => [name, '']))
  )
  const [error, setError] = useState('')

  async function handleSubmit(e) {
    e.preventDefault()
    console.log('Form submitted with data:', formData)
    try {
      await request(formData)
    } catch (error) {
      console.error('Error during request:', error)
      if (error.response) {
        setError(error.response.data)
      } else {
        setError('An error occurred. Please try again.')
      }
    }
  }

  const handleInputChange = (fieldName, e) => {
    const { value } = e.target
    setFormData((prevFormData) => ({
      ...prevFormData,
      [fieldName]: value,
    }))
  }

  return (
    <form onSubmit={handleSubmit}>
      <Container className="p-5 d-flex flex-column" style={{ backgroundColor: 'white', borderRadius: '8px', width: '100%', paddingTop: '20px' }}>
        {Object.entries(fields).map(([fieldName, fieldData]) => (
          <FormGroup className="mb-2" key={fieldName}>
            <FormLabel className="small-label">{fieldName}</FormLabel>
            <FormControl
              type={fieldData.type || 'text'}
              id={fieldName}
              name={fieldName}
              value={formData[fieldName] || ''}
              onChange={(e) => handleInputChange(fieldName, e)}
              placeholder={fieldData.placeholder || fieldName}
            />
          </FormGroup>
        ))}
        <button className="form-button" type="submit">{submit}</button>
      </Container>
    </form>
  )
}