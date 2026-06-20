'use client';
import { useEffect, useState } from 'react';

export default function PathVisualizer() {
  const [path, setPath] = useState<Array<{x: number, y: number}>>([]);

  useEffect(() => {
    const ws = new WebSocket('ws://localhost:9001');
    ws.onmessage = (event) => {
      const data = JSON.parse(event.data);
      if (data.topic === '/planned_path') {
        setPath(data.points);
      }
    };
  }, []);

  return (
    <div className="bg-gray-800 rounded-lg p-4">
      <h2 className="text-lg font-semibold mb-4 text-green-400">🛣️ Planned Path</h2>
      <div className="relative w-full h-64 bg-gray-700 rounded overflow-hidden">
        <div className="absolute inset-0 bg-gradient-to-br from-orange-900 to-red-900 opacity-50" />
        
        {/* Path line */}
        {path.length > 0 && (
          <svg className="absolute inset-0 w-full h-full">
            <polyline
              points={path.map(p => `${p.x},${p.y}`).join(' ')}
              stroke="#22c55e"
              strokeWidth="2"
              fill="none"
            />
          </svg>
        )}
      </div>
      <p className="mt-2 text-sm text-gray-400">
        Path length: {path.length} points
      </p>
    </div>
  );
}
