import React, { useState } from 'react';
import httpClient from './httpClient'; // Your Axios instance
import './Login.css'; // Import your CSS file

const Login = () => {
    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");

    const logInUser = async () => {
        try {
            const resp = await httpClient.post("http://localhost:5000/login", {
                email,
                password
            });
            window.location.href = "/";
        } catch (error) {
            if (error.response && error.response.status === 401) {
                alert("Invalid credentials");
            }
        }
    };

    return (
        <div className="login-container">
            <form className="login-form">
                <h2>Login</h2>
                <div className="input-group">
                    <label>Email:</label>
                    <input
                        type='text'
                        value={email}
                        onChange={(e) => setEmail(e.target.value)}
                        className="input-field"
                    />
                </div>
                <div className="input-group">
                    <label>Password:</label>
                    <input
                        type='password'
                        value={password}
                        onChange={(e) => setPassword(e.target.value)}
                        className="input-field"
                    />
                </div>
                <button type='button' className="submit-button" onClick={logInUser}>
                    Submit
                </button>
            </form>
        </div>
    );
};

export default Login;
