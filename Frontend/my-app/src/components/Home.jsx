import React, { useEffect, useState } from "react";
import httpClient from "./httpClient";
import './Home.css'; // Make sure to create this CSS file

function Home() {
    const [user, setUser] = useState(null);  // Initialize user state as null
    const [moodData, setMoodData] = useState([0, 1, 2, 3, 4, 5, 6, 7]); // Example mood data

    const logoutUser = async () => {
        try {
            await httpClient.post("http://127.0.0.1:5000/logout", {}, { withCredentials: true });
            window.location.href = "/login"; // Redirect to login after logout
        } catch (err) {
            console.error("Logout error", err);
        }
    };

    useEffect(() => {
        fetch("http://127.0.0.1:5000", {
            method: "GET",
            credentials: "include", // Ensure cookies/session info are sent
        })
        .then(response => response.json())
        .then(data => {
            if (data.error) {
                console.log("Not Authenticated");
                setUser(null);  // Explicitly set user to null if not authenticated
            } else {
                console.log("Authenticated User:", data);
                setUser(data);  // Set the authenticated user's data
            }
        })
        .catch(err => {
            console.error("Error fetching user:", err);
            setUser(null); // Handle errors by setting user to null
        });
    }, []);

    return (
        <div className="dashboard">
            <h1 className="dashboard-title">Mental Health Companion</h1>
            {user ? (
                <div className="welcome-section">
                    <h2>Welcome, {user.email}</h2>
                    <button className="logout-button" onClick={logoutUser}>Logout</button>
                </div>
            ) : (
                <div className="login-prompt">
                    <p>You are not logged in</p>
                    <div>
                        <a href="/login">
                            <button className="action-button">Login</button>
                        </a>
                        <a href="/register">
                            <button className="action-button">Register</button>
                        </a>
                    </div>
                </div>
            )}

            {/* Mood Tracker Section */}
            <div className="mood-tracker">
                <h3>How are you feeling today?</h3>
                <div className="mood-icons">
                    {/* Replace these with appropriate icons */}
                    <span role="img" aria-label="happy">😊</span>
                    <span role="img" aria-label="neutral">😐</span>
                    <span role="img" aria-label="sad">😢</span>
                </div>
                <h3>Mood Tracker</h3>
                <div className="mood-graph">
                    {/* Render mood graph here, you can use chart libraries like Chart.js or Recharts */}
                    <p>Graph Placeholder</p>
                </div>
            </div>

            {/* Daily CBT Exercise Section */}
            <div className="cbt-exercise">
                <h3>Daily CBT Exercise</h3>
                <p>Identify and challenge negative thoughts.</p>
                <button className="action-button">Continue Exercise</button>
            </div>

            {/* Quick Journal Section */}
            <div className="quick-journal">
                <h3>Quick Journal</h3>
                <textarea placeholder="What's on your mind today?" className="journal-input"></textarea>
                <button className="action-button">Save</button>
            </div>
        </div>
    );
}

export default Home;
