import { useState, useEffect } from 'react'
import './App.css'

function App() {
  const [message, setMessage] = useState('')
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState('')

  useEffect(() => {
    fetchWelcome()
  }, [])

  const fetchWelcome = async () => {
    try {
      setLoading(true)
      const response = await fetch('/api/welcome')
      const data = await response.json()
      setMessage(data.message)
    } catch (err) {
      setError('Failed to fetch welcome message')
      console.error(err)
    } finally {
      setLoading(false)
    }
  }

  return (
    <div className="app">
      <header className="header">
        <h1>🚀 BrandSpark AI</h1>
        <p className="subtitle">AI-Powered Marketing System</p>
      </header>

      <main className="main">
        <div className="card">
          <h2>Welcome to BrandSpark AI</h2>
          {loading && <p>Loading...</p>}
          {error && <p className="error">{error}</p>}
          {message && <p className="message">{message}</p>}
          <button onClick={fetchWelcome} className="btn">Refresh Message</button>
        </div>
      </main>

      <footer className="footer">
        <p>Built with React, Vite, and Flask</p>
      </footer>
    </div>
  )
}

export default App
