"use client";
import { useState, useEffect } from "react";
import axios from "axios";

export default function Home() {
    const [message, setMessage] = useState("Chargement...");

    useEffect(() => {
        axios.get("http://127.0.0.1:8000/")
            .then(response => setMessage(response.data.message))
            .catch(error => setMessage("Erreur de connexion au backend"));
    }, []);

    return (
        <div style={{ textAlign: "center", marginTop: "50px" }}>
            <h1>AI Trade Optimizer</h1>
            <p>{message}</p>
        </div>
    );
}
