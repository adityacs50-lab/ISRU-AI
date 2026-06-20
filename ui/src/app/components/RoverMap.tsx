'use client';
import { useEffect, useState } from 'react';

export default function RoverMap() {
  const [roverPos, setRoverPos] = useState({ x: 0, y: 0 });
  const [obstacles, setObstacles] = useState<Array<{x: number, y: number}>>([]);

  useEffect(() => {
    // Subscribe to ROS 2 topics (via WebSocket bridge)
    const ws = new WebSocket('ws://localhost:9001');
    
    ws.onmessage = (event) => {
      const data = JSON.parse(event.data);
      if (data.topic === '/rover_position') {
        setRoverPos({ x: data.x, y: data.y });
      }
      if (data.topic === '/obstacles') {
        setObstacles(prev => [...prev, { x: data.x, y: data.y }]);
      }
    };
  }, []);

  return (
    <div className="bg-gray-800 rounded-lg p-4">
      <h2 className="text-lg font-semibold mb-4 text-orange-400">🗺️ Rover Map</h2>
      <div className="relative w-full h-64 bg-gray-700 rounded overflow-hidden">
        {/* Mars terrain background */}
        <div className="absolute inset-0 bg-gradient-to-br from-orange-900 to-red-900 opacity-50" />
        
        {/* Obstacles (rocks) */}
        {obstacles.map((obs, i) => (
          <div
            key={i}
            className="absolute w-4 h-4 bg-gray-900 rounded-full"
            style={{ left: `${obs.x}px`, top: `${obs.y}px` }}
          />
        ))}
        
        {/* Rover */}
        <div
          className="absolute w-6 h-6 bg-orange-500 rounded-full border-2 border-white"
          style={{ left: `${roverPos.x}px`, top: `${roverPos.y}px` }}
        />
      </div>
      <p className="mt-2 text-sm text-gray-400">
        Position: ({roverPos.x}, {roverPos.y}) | Obstacles: {obstacles.length}
      </p>
    </div>
  );
}
