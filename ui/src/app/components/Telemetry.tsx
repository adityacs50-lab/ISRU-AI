'use client';
import { useEffect, useState } from 'react';

export default function Telemetry() {
  const [telemetry, setTelemetry] = useState({
    speed: 0,
    distance: 0,
    battery: 100,
    status: 'Idle'
  });

  useEffect(() => {
    const ws = new WebSocket('ws://localhost:9001');
    ws.onmessage = (event) => {
      const data = JSON.parse(event.data);
      if (data.topic === '/telemetry') {
        setTelemetry(data);
      }
    };
  }, []);

  return (
    <div className="bg-gray-800 rounded-lg p-4">
      <h2 className="text-lg font-semibold mb-4 text-blue-400">📊 Telemetry</h2>
      <div className="grid grid-cols-2 gap-4">
        <div className="bg-gray-700 rounded p-3">
          <p className="text-gray-400 text-sm">Speed</p>
          <p className="text-2xl font-bold">{telemetry.speed} m/s</p>
        </div>
        <div className="bg-gray-700 rounded p-3">
          <p className="text-gray-400 text-sm">Distance</p>
          <p className="text-2xl font-bold">{telemetry.distance} m</p>
        </div>
        <div className="bg-gray-700 rounded p-3">
          <p className="text-gray-400 text-sm">Battery</p>
          <p className="text-2xl font-bold text-green-400">{telemetry.battery}%</p>
        </div>
        <div className="bg-gray-700 rounded p-3">
          <p className="text-gray-400 text-sm">Status</p>
          <p className="text-2xl font-bold text-orange-400">{telemetry.status}</p>
        </div>
      </div>
    </div>
  );
}
