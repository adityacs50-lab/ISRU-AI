import RoverMap from './components/RoverMap';
import PathVisualizer from './components/PathVisualizer';
import Telemetry from './components/Telemetry';
import ControlPanel from './components/ControlPanel';

export default function Home() {
  return (
    <div className="min-h-screen bg-gray-900 text-white">
      {/* Header */}
      <header className="bg-gray-800 border-b border-gray-700 p-4">
        <h1 className="text-2xl font-bold text-orange-500">
          🚀 ISRU AI - Rover Autonomy Dashboard
        </h1>
        <p className="text-gray-400">Autonomous navigation in extreme environments</p>
      </header>

      {/* Main Dashboard */}
      <main className="p-6 grid grid-cols-1 md:grid-cols-2 gap-6">
        {/* Left Column */}
        <div className="space-y-6">
          <RoverMap />
          <PathVisualizer />
        </div>

        {/* Right Column */}
        <div className="space-y-6">
          <Telemetry />
          <ControlPanel />
        </div>
      </main>
    </div>
  );
}
