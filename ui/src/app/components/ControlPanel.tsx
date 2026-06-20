'use client';
import { useState } from 'react';

export default function ControlPanel() {
  const [isRunning, setIsRunning] = useState(false);

  const startRover = () => {
    setIsRunning(true);
    // Send start command to ROS 2
    const ws = new WebSocket('ws://localhost:9001');
    ws.send(JSON.stringify({ command: 'start' }));
  };

  const stopRover = () => {
    setIsRunning(false);
    const ws = new WebSocket('ws://localhost:9001');
    ws.send(JSON.stringify({ command: 'stop' }));
  };

  return (
    <div className="bg-gray-800 rounded-lg p-4">
      <h2 className="text-lg font-semibold mb-4 text-purple-400">🎮 Controls</h2>
      <div className="flex gap-4">
        <button
          onClick={startRover}
          disabled={isRunning}
          className="bg-green-600 hover:bg-green-700 disabled:bg-gray-600 px-6 py-3 rounded font-semibold"
        >
          ▶️ Start
        </button>
        <button
          onClick={stopRover}
          disabled={!isRunning}
          className="bg-red-600 hover:bg-red-700 disabled:bg-gray-600 px-6 py-3 rounded font-semibold"
        >
          ⏸️ Stop
        </button>
      </div>
    </div>
  );
}
