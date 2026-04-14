import { useState, useEffect } from 'react'
import axios from 'axios'
import { Activity, Users, Database, Server } from 'lucide-react'
import './App.css'

interface User {
  ID: number
  name: string
  email: string
}

function App() {
  const [ping, setPing] = useState<{ message: string; status: string } | null>(null)
  const [users, setUsers] = useState<User[]>([])
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    const fetchData = async () => {
      try {
        const pingRes = await axios.get('http://localhost:8081/ping')
        setPing(pingRes.data)

        const usersRes = await axios.get('http://localhost:8081/api/users')
        setUsers(usersRes.data)
      } catch (error) {
        console.error('Failed to fetch data:', error)
      } finally {
        setLoading(false)
      }
    }

    fetchData()
  }, [])

  return (
    <div className="dashboard">
      <header>
        <h1><Activity size={32} /> Agentic Template Dashboard</h1>
        <p>Go + React + MySQL Full Stack</p>
      </header>

      <main>
        <div className="stats-grid">
          <div className="stat-card">
            <div className="stat-icon"><Server /></div>
            <div className="stat-info">
              <h3>Backend Status</h3>
              <p className={ping?.status === 'healthy' ? 'status-ok' : 'status-err'}>
                {ping?.status || 'Offline'}
              </p>
            </div>
          </div>

          <div className="stat-card">
            <div className="stat-icon"><Database /></div>
            <div className="stat-info">
              <h3>Database</h3>
              <p>MySQL 8.0</p>
            </div>
          </div>

          <div className="stat-card">
            <div className="stat-icon"><Users /></div>
            <div className="stat-info">
              <h3>Users</h3>
              <p>{users.length} Registered</p>
            </div>
          </div>
        </div>

        <section className="user-list">
          <h2><Users /> User Directory</h2>
          {loading ? (
            <p>Loading components...</p>
          ) : (
            <table>
              <thead>
                <tr>
                  <th>ID</th>
                  <th>Name</th>
                  <th>Email</th>
                </tr>
              </thead>
              <tbody>
                {users.length > 0 ? (
                  users.map((user) => (
                    <tr key={user.ID}>
                      <td>{user.ID}</td>
                      <td>{user.name}</td>
                      <td>{user.email}</td>
                    </tr>
                  ))
                ) : (
                  <tr>
                    <td colSpan={3} className="empty-msg">No users found. Connect DB to see results.</td>
                  </tr>
                )}
              </tbody>
            </table>
          )}
        </section>
      </main>
    </div>
  )
}

export default App
