import { useState } from 'react';
import { Line } from 'react-chartjs-2';
import 'chart.js/auto';

const Home = () => {
  const [view, setView] = useState('dashboard'); // Controls which view to show
  const [messages, setMessages] = useState([]); // Chat messages
  const [input, setInput] = useState(''); // Chat input

  // Sample Analytics Data
  const data = {
    labels: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri'],
    datasets: [
      {
        label: 'User Activity',
        data: [12, 19, 3, 5, 2],
        backgroundColor: 'rgba(75,192,192,0.2)',
        borderColor: 'rgba(75,192,192,1)',
        borderWidth: 2,
      },
    ],
  };

  const options = {
    scales: {
      y: { beginAtZero: true },
    },
  };

  // Functions to handle navigation
  const navigate = (page) => setView(page);

  // Chat functionality
  const sendMessage = () => {
    if (input.trim()) {
      setMessages([...messages, { type: 'user', text: input }]);
      setTimeout(() => {
        setMessages((prev) => [...prev, { type: 'bot', text: `Bot response to: ${input}` }]);
      }, 1000);
      setInput('');
    }
  };

  return (
    <div style={{ display: 'flex', height: '100vh', fontFamily: 'Arial, sans-serif' }}>
      {/* Sidebar */}
      <div
        style={{
          width: '20%',
          backgroundColor: '#007bff',
          color: '#fff',
          display: 'flex',
          flexDirection: 'column',
          padding: '20px 0',
          position: 'fixed',
          height: '100%',
        }}
      >
        <div style={{ textAlign: 'center', fontSize: '1.5rem', marginBottom: '30px' }}>AI CallBot</div>
        <ul style={{ listStyle: 'none', padding: '0' }}>
          <li
            onClick={() => navigate('dashboard')}
            style={{
              padding: '15px 20px',
              cursor: 'pointer',
              backgroundColor: view === 'dashboard' ? '#0056b3' : 'transparent',
            }}
          >
            Dashboard
          </li>
          <li
            onClick={() => navigate('analytics')}
            style={{
              padding: '15px 20px',
              cursor: 'pointer',
              backgroundColor: view === 'analytics' ? '#0056b3' : 'transparent',
            }}
          >
            Analytics
          </li>
          <li
            onClick={() => navigate('settings')}
            style={{
              padding: '15px 20px',
              cursor: 'pointer',
              backgroundColor: view === 'settings' ? '#0056b3' : 'transparent',
            }}
          >
            Settings
          </li>
        </ul>
      </div>

      {/* Main Content */}
      <div style={{ marginLeft: '20%', padding: '20px', width: '80%' }}>
        {/* Dashboard View */}
        {view === 'dashboard' && (
          <>
            <h1>Conversations</h1>
            <div
              style={{
                backgroundColor: '#fff',
                padding: '20px',
                borderRadius: '10px',
                boxShadow: '0 2px 5px rgba(0, 0, 0, 0.1)',
              }}
            >
              <div
                id="messages"
                style={{
                  height: '300px',
                  overflowY: 'auto',
                  marginBottom: '10px',
                  border: '1px solid #ddd',
                  padding: '10px',
                }}
              >
                {messages.map((msg, index) => (
                  <div
                    key={index}
                    style={{
                      textAlign: msg.type === 'user' ? 'right' : 'left',
                      margin: '10px 0',
                    }}
                  >
                    <span
                      style={{
                        display: 'inline-block',
                        backgroundColor: msg.type === 'user' ? '#007bff' : '#e6e6e6',
                        color: msg.type === 'user' ? '#fff' : '#000',
                        padding: '10px',
                        borderRadius: '10px',
                      }}
                    >
                      {msg.text}
                    </span>
                  </div>
                ))}
              </div>
              <input
                type="text"
                value={input}
                onChange={(e) => setInput(e.target.value)}
                placeholder="Type a message"
                style={{ width: '80%', padding: '10px' }}
              />
              <button
                onClick={sendMessage}
                style={{
                  padding: '10px',
                  backgroundColor: '#007bff',
                  color: 'white',
                  border: 'none',
                  cursor: 'pointer',
                }}
              >
                Send
              </button>
            </div>
          </>
        )}

        {/* Analytics View */}
        {view === 'analytics' && (
          <>
            <h1>Analytics</h1>
            <div
              style={{
                backgroundColor: '#fff',
                padding: '20px',
                borderRadius: '10px',
                boxShadow: '0 2px 5px rgba(0, 0, 0, 0.1)',
              }}
            >
              <Line data={data} options={options} />
            </div>
          </>
        )}

        {/* Settings View */}
        {view === 'settings' && (
          <>
            <h1>Settings</h1>
            <ul>
              <li>
                <button onClick={() => alert('Resetting conversation...')}>Reset Conversation</button>
              </li>
              <li>
                <button onClick={() => alert('Profile settings clicked')}>Profile</button>
              </li>
              <li>
                <button onClick={() => alert('Switching accounts...')}>Switch Account</button>
              </li>
            </ul>
          </>
        )}
      </div>
    </div>
  );
};

export default Home;
