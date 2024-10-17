import React, { useState } from 'react';
import httpClient from './httpClient'; // Your Axios instance
import './Register.css'; // Import your CSS file

const Register = () => {
    const [username, setUsername] = useState("");
    const [firstName, setFirstName] = useState("");
    const [lastName, setLastName] = useState("");
    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");

    const registerUser = async () => {
        try {
            const resp = await httpClient.post("http://127.0.0.1:5000/register", {
                username,
                first_name: firstName,
                last_name: lastName,
                email,
                password
            }, 
            {
                headers: {
                    "Content-Type": "application/json"
                }, 
                withCredentials: true // lowercase 'true'
            });

            window.location.href = "/";
            console.log(resp);
        } catch (error) {
            if (error.response && error.response.status === 401) {
                alert("Invalid Credentials");
            }
        }
    };

    const handleSubmit = (e) => {
        e.preventDefault(); // Prevent the default form submission behavior
        registerUser();
    };

    return (
        <div className="register-container">
            <form className="register-form" onSubmit={handleSubmit}>
                <h2>Register</h2>
                <div className="input-group">
                    <label>Username:</label>
                    <input
                        type='text'
                        value={username}
                        onChange={e => setUsername(e.target.value)}
                        className="input-field"
                    />
                </div>
                <div className="input-group">
                    <label>First Name:</label>
                    <input
                        type='text'
                        value={firstName}
                        onChange={e => setFirstName(e.target.value)}
                        className="input-field"
                    />
                </div>
                <div className="input-group">
                    <label>Last Name:</label>
                    <input
                        type='text'
                        value={lastName}
                        onChange={e => setLastName(e.target.value)}
                        className="input-field"
                    />
                </div>
                <div className="input-group">
                    <label>Email:</label>
                    <input
                        type='text'
                        value={email}
                        onChange={e => setEmail(e.target.value)}
                        className="input-field"
                    />
                </div>
                <div className="input-group">
                    <label>Password:</label>
                    <input
                        type='password'
                        value={password}
                        onChange={e => setPassword(e.target.value)}
                        className="input-field"
                    />
                </div>
                <button type='submit' className="submit-button">
                    Submit
                </button>
            </form>
        </div>
    );
};

export default Register;
