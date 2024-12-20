import React, { useState, useEffect } from "react";
import { getGuestsList } from "../services/GusetListService"; // Import the service to fetch data
import "../style/GuestsList.css";

const GuestsList = () => {
    const [guests, setGuests] = useState([]);

    // Mapping function for translating status
    const translateStatus = (status) => {
        switch (status) {
            case "come":
                return "מגיע";
            case "not come":
                return "לא מגיע";
            case "not know":
                return "לא יודע";
            default:
                return status;
        }
    };

    // Fetch the list of guests when the component mounts
    useEffect(() => {
        const fetchGuests = async () => {
            try {
                const data = await getGuestsList();
                setGuests(data);
            } catch (error) {
                console.error("Error fetching guests:", error);
            }
        };
        fetchGuests();
    }, []);

    return (
        <div>
            <h1>רשימת מוזמנים</h1>
            <table border="1">
                <thead>
                    <tr>
                        <th>כמות</th>
                        <th>מגיע או לא</th>
                        <th>מספר טלפון</th>
                        <th>שם משפחה</th>
                        <th>שם פרטי</th>
                    </tr>
                </thead>
                <tbody>
                    {guests.map((guest, index) => (
                        <tr key={index}>
                            <td>{guest.how_much}</td>
                            <td>{translateStatus(guest.status)}</td> {/* Translating the status here */}
                            <td>{guest.phone}</td>
                            <td>{guest.last_name}</td>
                            <td>{guest.first_name}</td>
                        </tr>
                    ))}
                </tbody>
            </table>
        </div>
    );
};

export default GuestsList;
