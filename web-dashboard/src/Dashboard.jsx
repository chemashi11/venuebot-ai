import { useState, useEffect } from 'react';
import { useNavigate, Link } from 'react-router-dom';
import api from './api';

export default function Dashboard() {
  const [resources, setResources] = useState([]);
  const navigate = useNavigate();

  useEffect(() => {
    fetchResources();
  }, []);

  const fetchResources = async () => {
    try {
      const res = await api.get('/resources/');
      setResources(res.data);
    } catch (err) {
      console.error("Failed to fetch resources", err);
      if (err.response?.status === 401) {
        navigate('/');
      }
    }
  };

  const handleLogout = () => {
    localStorage.removeItem('token');
    window.location.href = '/';
  };

  return (
    <div className="min-h-screen">
      {/* Premium Navbar */}
      <nav className="bg-brand-dark text-white px-8 py-5 flex justify-between items-center shadow-2xl sticky top-0 z-50">
        <div className="flex items-center gap-10">
          <div className="flex items-center gap-3">
            <span className="text-3xl">🍽️</span>
            <h1 className="text-2xl font-serif font-bold tracking-wider text-brand-gold">VenueBot AI</h1>
          </div>
        </div>
        <div className="hidden md:flex gap-8 text-sm font-semibold tracking-wide">
          <a href="/dashboard" className="text-brand-gold border-b-2 border-brand-gold pb-1">Floor Plan</a>
          <a href="/reports" className="text-gray-300 hover:text-white transition pb-1">Reports</a>
          <a href="/menu" className="text-gray-300 hover:text-white transition pb-1">Menu</a>
        </div>
        <div className="flex items-center gap-6">
          <div className="flex items-center gap-3 bg-white/10 px-4 py-2 rounded-full border border-white/20">
            <div className="w-8 h-8 rounded-full bg-brand-gold text-brand-dark flex items-center justify-center font-bold">M</div>
            <span className="text-sm font-medium hidden sm:block">Manager</span>
          </div>
          <button 
            onClick={handleLogout} 
            className="text-gray-300 hover:text-red-400 transition text-sm font-semibold"
          >
            Logout
          </button>
        </div>
      </nav>

      <div className="p-8 md:p-12 max-w-7xl mx-auto">
        {/* Header Section */}
        <div className="mb-10">
          <h2 className="text-3xl font-serif text-brand-dark">Good evening, Manager.</h2>
          <p className="text-gray-500 mt-1">Here is what's happening at your venue today.</p>
        </div>

        {/* Stats Row */}
        <div className="grid grid-cols-1 md:grid-cols-3 gap-6 mb-12">
          <div className="bg-white p-8 rounded-2xl shadow-lg shadow-gray-200/50 border border-gray-100 hover:-translate-y-1 transition duration-300">
            <div className="flex justify-between items-start">
              <div>
                <p className="text-gray-400 text-xs font-bold uppercase tracking-widest mb-2">Total Bookings</p>
                <p className="text-4xl font-bold text-brand-dark">142</p>
              </div>
              <span className="text-3xl bg-yellow-50 p-3 rounded-xl">📅</span>
            </div>
          </div>
          
          <div className="bg-white p-8 rounded-2xl shadow-lg shadow-gray-200/50 border border-gray-100 hover:-translate-y-1 transition duration-300">
            <div className="flex justify-between items-start">
              <div>
                <p className="text-gray-400 text-xs font-bold uppercase tracking-widest mb-2">Monthly Revenue</p>
                <p className="text-4xl font-bold text-brand-dark">$4,250</p>
              </div>
              <span className="text-3xl bg-green-50 p-3 rounded-xl">💰</span>
            </div>
          </div>

          <div className="bg-white p-8 rounded-2xl shadow-lg shadow-gray-200/50 border border-gray-100 hover:-translate-y-1 transition duration-300">
            <div className="flex justify-between items-start">
              <div>
                <p className="text-gray-400 text-xs font-bold uppercase tracking-widest mb-2">Active Alarms</p>
                <p className="text-4xl font-bold text-brand-dark">0</p>
              </div>
              <span className="text-3xl bg-red-50 p-3 rounded-xl">🔔</span>
            </div>
          </div>
        </div>

        {/* Live Floor Plan */}
        <div className="flex justify-between items-end mb-6">
          <h2 className="text-2xl font-serif text-brand-dark">Live Floor Plan</h2>
          <p className="text-sm text-gray-500 font-medium">Click a card to manage</p>
        </div>
        
        <div className="grid grid-cols-1 md:grid-cols-3 lg:grid-cols-4 gap-8">
          {resources.map((res) => (
            <div 
              key={res.id} 
              className={`group p-8 rounded-3xl shadow-md border-2 transition-all duration-300 hover:-translate-y-2 hover:shadow-xl cursor-pointer relative overflow-hidden
                ${res.type === 'hall' ? 'bg-gradient-to-br from-red-50 to-orange-50 border-red-100' : 
                  res.type === 'study_spot' ? 'bg-gradient-to-br from-green-50 to-emerald-50 border-green-100' : 
                  'bg-gradient-to-br from-yellow-50 to-amber-50 border-yellow-100'}`}
            >
              {/* Decorative background circle */}
              <div className="absolute -right-6 -top-6 w-24 h-24 bg-white/40 rounded-full group-hover:scale-150 transition-transform duration-500"></div>
              
              <div className="relative z-10 flex flex-col items-center text-center">
                <span className="text-5xl mb-4 group-hover:scale-110 transition-transform duration-300">
                  {res.type === 'hall' ? '🎉' : res.type === 'study_spot' ? '📚' : '🍽️'}
                </span>
                <h3 className="font-serif font-bold text-xl text-brand-dark mb-1">{res.name}</h3>
                <p className="text-sm text-gray-500 capitalize mb-4 font-medium">{res.type.replace('_', ' ')}</p>
                <span className="text-xs bg-white px-4 py-2 rounded-full shadow-sm text-gray-700 font-bold tracking-wide border border-gray-100">
                  Capacity: {res.capacity}
                </span>
              </div>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
}