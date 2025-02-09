import React, { useState, useEffect, useContext } from 'react';
import { useNavigate } from 'react-router-dom';
import Calendar from 'react-calendar';
import 'react-calendar/dist/Calendar.css'; // Default calendar styling
import './Home.css'; // Custom styling for the calendar and page
import { AuthContext } from '../AuthContext'; // Import the AuthContext
import axios from 'axios';

const Home = () => {
  const [date, setDate] = useState(new Date()); // Selected date
  const [records, setRecords] = useState({}); // Stores records for each date
  const navigate = useNavigate();
  const { token } = useContext(AuthContext); // Access the token from context

  // Fetch cardio and training records for all dates
  useEffect(() => {
    const fetchRecords = async () => {
      try {
        if (!token) {
          console.error('No token found. User is not authenticated.');
          return;
        }
        // Fetch cardio records
        const cardioResponse = await axios.get('https://fitwithme.onrender.com/api/cardio_all/', {
          headers: { Authorization: `Bearer ${token}` }, // Include the token in the headers
        });
        const cardioData = cardioResponse.data;

        // Fetch training records
        const trainingResponse = await axios.get('https://fitwithme.onrender.com/api/training_all/', {
          headers: { Authorization: `Bearer ${token}` }, // Include the token in the headers
        });
        const trainingData = trainingResponse.data;

        // Combine records by date
        const combinedRecords = {};
        cardioData.forEach((record) => {
          const dateString = record.date;
          if (!combinedRecords[dateString]) {
            combinedRecords[dateString] = { cardio: [], training: [] };
          }
          combinedRecords[dateString].cardio.push(record);
        });
        trainingData.forEach((record) => {
          const dateString = record.date;
          if (!combinedRecords[dateString]) {
            combinedRecords[dateString] = { cardio: [], training: [] };
          }
          combinedRecords[dateString].training.push(record);
        });
        setRecords(combinedRecords);
      } catch (error) {
        console.error('Error fetching records:', error);
      }
    };
    fetchRecords();
  }, [token]);

  // Handle date click
  const handleDateClick = (value) => {
    setDate(value);
    navigate(`/day/${value.toISOString().split('T')[0]}`); // Navigate to the day's page
  };

  // Custom tile content to show muscle group and highlight recorded days
  const tileContent = ({ date, view }) => {
    if (view === 'month') {
      const dateString = date.toISOString().split('T')[0];
      const record = records[dateString];
      // Check if there are any cardio or training records for this date
      const hasRecord = record?.cardio?.length > 0 || record?.training?.length > 0;
      return (
        <div>
          {/* Show checkmark if there's a record */}
          {hasRecord && <div className="record-indicator">✔️</div>}
          {/* Show muscle group if there's a training record */}
          {(record?.training?.length > 0 && (
            <div className="training-program">
              {record.training[0].exercise.muscle_group.name } {/* Display the first muscle group */}
            </div>
          ))|| "Rest" }
        </div>
      );
    }
  };

  // Custom tile class to highlight recorded days
  const tileClassName = ({ date, view }) => {
    if (view === 'month') {
      const dateString = date.toISOString().split('T')[0];
      const record = records[dateString];
      const hasRecord = record?.cardio?.length > 0 || record?.training?.length > 0;
      // Highlight days with records
      if (hasRecord) {
        return 'recorded-day';
      }
    }
  };

  return (
    <div className="home-container">
      <h1>Fitness Tracker</h1>
      <div className="calendar-container">
        <Calendar
          onChange={handleDateClick}
          value={date}
          tileContent={tileContent}
          tileClassName={tileClassName}
        />
      </div>
    </div>
  );
};

export default Home;