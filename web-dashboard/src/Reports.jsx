import { useState } from 'react';
import { Link } from 'react-router-dom';
import api from './api';

export default function Reports() {
  const [reportImage, setReportImage] = useState(null);
  const [loading, setLoading] = useState(false);
  const [month, setMonth] = useState(10); 
  const [year, setYear] = useState(2026);

  const generateReport = async () => {
    setLoading(true);
    setReportImage(null); // Clear old image
    try {
      const response = await api.get(`/reports/generate?month=${month}&year=${year}`, {
        responseType: 'blob', 
      });
      const imageUrl = URL.createObjectURL(response.data);
      setReportImage(imageUrl);
    } catch (err) {
      console.error(err);
      alert("Failed to generate report. Make sure there is data for this month.");
    } finally {
      setLoading(false);
    }
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
          <div className="hidden md:flex gap-8 text-sm font-semibold tracking-wide">
            <a href="/dashboard" className="text-brand-gold border-b-2 border-brand-gold pb-1">Floor Plan</a>
            <a href="/reports" className="text-gray-300 hover:text-white transition pb-1">Reports</a>
            <a href="/menu" className="text-gray-300 hover:text-white transition pb-1">Menu</a>
          </div>
        </div>
      </nav>

      <div className="p-8 md:p-12 max-w-6xl mx-auto">
        <div className="mb-10">
          <h2 className="text-3xl font-serif text-brand-dark">Financial Reports</h2>
          <p className="text-gray-500 mt-1">Generate and view monthly performance charts.</p>
        </div>
        
        {/* Control Panel */}
        <div className="bg-white p-8 rounded-2xl shadow-lg border border-gray-100 mb-10 flex flex-wrap items-end gap-6">
          <div className="flex-1 min-w-[150px]">
            <label className="block text-xs font-bold uppercase tracking-widest text-gray-500 mb-2">Month</label>
            <input 
              type="number" min="1" max="12" value={month} 
              onChange={(e) => setMonth(e.target.value)}
              className="w-full px-4 py-3 bg-gray-50 border border-gray-200 rounded-xl focus:ring-2 focus:ring-brand-gold outline-none transition font-medium" 
            />
          </div>
          <div className="flex-1 min-w-[150px]">
            <label className="block text-xs font-bold uppercase tracking-widest text-gray-500 mb-2">Year</label>
            <input 
              type="number" value={year} 
              onChange={(e) => setYear(e.target.value)}
              className="w-full px-4 py-3 bg-gray-50 border border-gray-200 rounded-xl focus:ring-2 focus:ring-brand-gold outline-none transition font-medium" 
            />
          </div>
          <button 
            onClick={generateReport} 
            disabled={loading}
            className="bg-brand-dark text-white px-8 py-3 rounded-xl font-bold hover:bg-black transition shadow-lg flex items-center gap-2 disabled:opacity-50"
          >
            {loading ? 'Generating...' : 'Generate Report'}
          </button>
        </div>

        {/* Display the Generated Chart */}
        {reportImage ? (
          <div className="bg-white p-4 rounded-2xl shadow-2xl border border-gray-100 animate-fade-in">
            <img src={reportImage} alt="Monthly Report Chart" className="w-full rounded-xl" />
          </div>
        ) : (
          <div className="text-center py-20 bg-white/50 border-2 border-dashed border-gray-200 rounded-3xl">
            <span className="text-6xl text-gray-300 mb-4 block">📊</span>
            <p className="text-gray-500 text-lg">Select a month and click generate to view the report.</p>
          </div>
        )}
      </div>
    </div>
  );
}