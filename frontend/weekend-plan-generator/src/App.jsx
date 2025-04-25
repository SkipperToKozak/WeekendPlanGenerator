import React, { useState, useEffect } from "react";
import { useSearchParams } from "react-router-dom";
import FilterSection from "./FilterSection.jsx";
import ActivityList from "./components/ActivityList.jsx";

const App = () => {
  const [filters, setFilters] = useState({
    category: null,
    budget: null,
    weather: null,
  });
  const [searchTriggered, setSearchTriggered] = useState(false);
  const [searchParams, setSearchParams] = useSearchParams();

  // Odczyt filtrów z URL przy ładowaniu
  useEffect(() => {
    setFilters({
      category: searchParams.get("category") || null,
      budget: searchParams.get("budget") || null,
      weather: searchParams.get("weather") || null,
    });
  }, [searchParams]);

  const handleSearch = () => {
    const params = {};
    if (filters.category) params.category = filters.category;
    if (filters.budget) params.budget = filters.budget;
    if (filters.weather) params.weather = filters.weather;

    setSearchParams(params);
    setSearchTriggered(true);
  };

  return (
    <div className="min-h-screen bg-gray-100 p-4">
      <h1 className="text-3xl font-bold mb-6 text-center">
        Pomysły na wolny czas
      </h1>
      <FilterSection
        filters={filters}
        setFilters={setFilters}
        onSearch={handleSearch}
      />
      {searchTriggered && <ActivityList filters={filters} />}
    </div>
  );
};

export default App;
