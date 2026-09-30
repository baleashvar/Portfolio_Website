import React, { useState } from 'react';
import { Alert, Button, Card, CardContent } from '@mui/material';
import CloseIcon from '@mui/icons-material/Close';
import ArrowBackIcon from '@mui/icons-material/ArrowBack';
import { useNavigate } from 'react-router-dom';
import { useForm } from 'react-hook-form';
import { zodResolver } from '@hookform/resolvers/zod';
import { z } from 'zod';
import './Department.css';

const departmentSchema = z.object({
  departmentName: z.string().trim().min(2, 'DepartmentName is required!').max(30, 'DepartmentName cannot exceed 30 characters'),
});

const Department = () => {
  const [responseMessage, setResponseMessage] = useState('');
  const backendURL = 'http://localhost:8000/department/';
  const navigate = useNavigate();

  const { register, handleSubmit, formState: { errors } } = useForm({
    resolver: zodResolver(departmentSchema)
  });

  const onSubmit = async (data) => {
    try {
      const accessToken = localStorage.getItem('accessToken');
      const response = await fetch(backendURL, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': accessToken
        },
        body: JSON.stringify(data),
      });

      if (response.ok) {
        const data = await response.json();
        setResponseMessage(data.message);
      } else {
        const errorData = await response.json();
        setResponseMessage(errorData.message);
      }
    } catch (error) {
      console.error('Error submitting department:', error);
      setResponseMessage('Error submitting department');
    }
  };

  const handleCloseAlert = () => {
    setResponseMessage('');
  };

  return (
    <React.Fragment>
      <div className="back-button-container">
        <Button className="back-button" type='submit' onClick={() => navigate('/admin/dashboard')}
          style={{ color: '#16A085', textTransform: 'none', fontWeight: 'bold', fontSize:'x-large' }} >
          <ArrowBackIcon />Back
        </Button>
      </div>
      <Card className="department-card">
        <CardContent>
          {responseMessage && (
            <Alert
              className="custom-alert"
              severity={responseMessage.includes('Success') ? 'success' : 'error' }
              action={
                <Button color="inherit" size="small" onClick={handleCloseAlert}>
                  <CloseIcon />
                </Button>
              }
            >
              {responseMessage}
            </Alert>
          )}
          <h2>Add Department</h2>
          <form onSubmit={handleSubmit(onSubmit)}>
            <label htmlFor="departmentInput">Department Name</label>
            <input
              className='department-text'
              type="text"
              id="departmentInput"
              {...register('departmentName')}
              placeholder="Enter Department Name"
            />
            {errors.departmentName && <p className="department-error-message">{errors.departmentName.message}</p>}
            <button className='department-button' type="submit">Submit</button>

          </form>
        </CardContent>
      </Card>
    </React.Fragment>
  );
};

export default Department;