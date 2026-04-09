import { BrowserRouter as Router, Routes, Route, Navigate } from 'react-router-dom';
import Login from './pages/Login';

function App() {
  return (
    <Router>
      <Routes>
        {/* Redirect people going to the base URL straight to login */}
        <Route path="/" element={<Navigate to="/login" replace />} />
        
        {/* The actual login page */}
        <Route path="/login" element={<Login />} />

        {/* We will add /doctor-dashboard and /patient-portal here later */}
      </Routes>
    </Router>
  );
}

export default App;