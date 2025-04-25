import React from "react";

const Tile = ({ label, selected, onClick }) => {
  return (
    <button
      onClick={onClick}
      className={`px-4 py-2 rounded-xl shadow text-sm font-medium transition 
        ${selected ? "bg-blue-600 text-white" : "bg-white hover:bg-blue-100"}
      `}
    >
      {label}
    </button>
  );
};

export default Tile;
