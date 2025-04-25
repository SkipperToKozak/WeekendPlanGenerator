import React from "react";

const ActivityList = ({ filters }) => {
  return (
    <div className="bg-white p-4 rounded-xl shadow">
      <h2 className="text-xl font-semibold mb-4">Wyniki</h2>
      <p className="text-gray-600">
        (Tutaj pojawią się aktywności na podstawie filtrów)
      </p>
      <pre className="text-sm mt-4 bg-gray-100 p-2 rounded">
        {JSON.stringify(filters, null, 2)}
      </pre>
    </div>
  );
};

export default ActivityList;
