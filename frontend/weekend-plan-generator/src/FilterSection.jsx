import React from "react";
import Tile from "./components/Tile";

const categories = ["sports", "culture", "relax", "travels"];
const budgets = ["low", "medium", "high", "any"];
const weatherOptions = ["sunny", "rainy", "interior", "any"];

const FilterSection = ({ filters, setFilters, onSearch }) => {
  const handleFilterClick = (type, value) => {
    setFilters((prev) => ({
      ...prev,
      [type]: prev[type] === value ? null : value, // toggle
    }));
  };

  return (
    <div className="grid gap-4 mb-8">
      <div>
        <h2 className="text-xl font-semibold mb-2">Kategoria</h2>
        <div className="flex gap-2 flex-wrap">
          {categories.map((cat) => (
            <Tile
              key={cat}
              label={cat}
              selected={filters.category === cat}
              onClick={() => handleFilterClick("category", cat)}
            />
          ))}
        </div>
      </div>

      <div>
        <h2 className="text-xl font-semibold mb-2">Budżet</h2>
        <div className="flex gap-2 flex-wrap">
          {budgets.map((b) => (
            <Tile
              key={b}
              label={b}
              selected={filters.budget === b}
              onClick={() => handleFilterClick("budget", b)}
            />
          ))}
        </div>
      </div>

      <div>
        <h2 className="text-xl font-semibold mb-2">Pogoda</h2>
        <div className="flex gap-2 flex-wrap">
          {weatherOptions.map((w) => (
            <Tile
              key={w}
              label={w}
              selected={filters.weather === w}
              onClick={() => handleFilterClick("weather", w)}
            />
          ))}
        </div>
      </div>

      <div className="mt-4">
        <button
          onClick={onSearch}
          className="bg-blue-600 text-white px-6 py-2 rounded-xl shadow hover:bg-blue-700 transition"
        >
          Szukaj
        </button>
      </div>
    </div>
  );
};

export default FilterSection;
