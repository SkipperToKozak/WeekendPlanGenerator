import React, { useState, useEffect } from "react";
import axios from "axios";

const ActivityList = ({ filters }) => {
  const [activities, setActivities] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchActivities = async () => {
      setLoading(true);
      try {
        // Budowanie URL z filtrami
        let url = "http://127.0.0.1:8000/activities/filtered?"; // Zakładając, że Twój backend działa na porcie 8000
        if (filters.category) url += `category=${filters.category}&`;
        if (filters.budget) url += `budget=${filters.budget}&`;
        if (filters.weather) url += `weather=${filters.weather}&`;
        if (filters.mood) url += `mood=${filters.mood}&`;
        if (filters.duration) url += `duration=${filters.duration}&`;

        // Usuwanie ostatniego '&' z URL
        url = url.slice(0, -1);

        // Wykonanie zapytania GET do backendu
        const response = await axios.get(url);
        setActivities(response.data); // Ustawienie wyników zapytania w stanie
      } catch (err) {
        setError("Nie udało się pobrać danych!");
      } finally {
        setLoading(false);
      }
    };

    fetchActivities();
  }, [filters]); // Odśwież dane, gdy filtry się zmienią

  if (loading) return <p>Ładowanie...</p>;
  if (error) return <p>{error}</p>;

  return (
    <div>
      <h2>Aktywności:</h2>
      <ul>
        {activities.length === 0 ? (
          <p>Brak aktywności spełniających te filtry.</p>
        ) : (
          activities.map((activity) => (
            <li key={activity.id}>
              {activity.title} - {activity.category}
            </li>
          ))
        )}
      </ul>
    </div>
  );
};

export default ActivityList;
