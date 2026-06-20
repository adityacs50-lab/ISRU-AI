<div align="center">

# ISRU AI

**AI Autonomy Software for Robots in Extreme Environments**

*Building the AI brain for robots that operate where humans can't — starting with mining, extending to space (Moon/Mars ISRU).*

[![YC Applicant](https://img.shields.io/badge/YC-Applicant-F26522?style=for-the-badge&logo=ycombinator&logoColor=white)](#)
[![Space-Tech](https://img.shields.io/badge/Space--Tech-🚀-000000?style=for-the-badge)](#)
[![Mining Automation](https://img.shields.io/badge/Mining_Automation-🏭-FF9900?style=for-the-badge)](#)
[![Built in India](https://img.shields.io/badge/Built_in-India_🇮🇳-FF9933?style=for-the-badge)](#)

</div>

---

## 🛑 The Problem

Operating in hazardous and extreme environments presents critical challenges that current systems fail to address:

- **Safety Risks:** Mining operations and hazardous industrial sites require human presence in life-threatening conditions.
- **Inefficiency:** Current teleoperated robots rely on constant human control, making operations slow, expensive, and dangerous due to latency and human error.
- **GPS-Denied Navigation:** Standard navigation systems fail entirely in subterranean mines, deep-sea operations, or extra-terrestrial environments where GPS is unavailable.

## 💡 The Solution

ISRU AI provides a full-stack autonomy solution designed from the ground up for extreme conditions:

- **Real-Time Obstacle Detection:** Advanced vision models enabling robots to autonomously perceive and categorize environmental hazards.
- **Dynamic Path Planning:** Real-time generation of safe, efficient trajectories across rough and unpredictable terrain.
- **GPS-Denied Autonomy:** Robust SLAM (Simultaneous Localization and Mapping) allowing seamless navigation in the most extreme, remote environments.

---

## 🎥 Demo

> **Simulated rover: obstacle detection + path planning in Mars-like terrain**

[![Watch Demo](https://img.shields.io/badge/Watch_Demo-FF0000?style=for-the-badge&logo=youtube&logoColor=white)](#)
[![Simulation Screenshots](https://img.shields.io/badge/Simulation_Screenshots-000000?style=for-the-badge&logo=github&logoColor=white)](#)

*(Placeholders for video and high-res screenshots of Gazebo simulations)*

---

## 🌍 Core Use Cases

| 🏭 Underground Mining | ☢️ Hazardous Industrial Sites | 🛰️ Space (Long-term) |
| :--- | :--- | :--- |
| **Autonomous Excavation** robots operating continuously in dangerous zones. | **Safety Inspection Rovers** for nuclear power plants, chemical spills, and oil & gas facilities. | **ISRU (In-Situ Resource Utilization)** rovers for lunar and Martian resource extraction. |
| **Safety inspection rovers** mapping subterranean tunnels. | Removing humans from disaster response and routine high-risk monitoring. | Next-generation planetary exploration without Earth-bound latency limits. |

---

## ⚙️ Tech Stack

<div align="center">

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![ROS 2](https://img.shields.io/badge/ROS_2-22314E?style=for-the-badge&logo=ros&logoColor=white)
![Gazebo](https://img.shields.io/badge/Gazebo-FF9900?style=for-the-badge&logo=gazebo&logoColor=white)
![OpenCV](https://img.shields.io/badge/OpenCV-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white)
![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white)
![Next.js](https://img.shields.io/badge/Next.js-000000?style=for-the-badge&logo=next.js&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)

*AI Coding: Claude + Cursor | Models: Vision models + LLMs for perception/planning*

</div>

---

## 🚀 Quick Start

```bash
# Clone the repository
git clone https://github.com/adityacs50-lab/ISRU-AI.git
cd ISRU-AI

# Install dependencies
pip install -r requirements.txt

# Setup ROS 2
sudo apt install ros-humble-ros-base

# Run simulation
ros2 launch isru_ai rover_simulation.launch.py

# Start dashboard
npm run dev
```

---

## 📂 Project Structure

```text
isru_ai/
├── src/
│   ├── vision/          # OpenCV obstacle detection
│   ├── path_planning/   # A* algorithm & dynamic routing
│   ├── ros2_nodes/      # ROS 2 integration & communication
│   └── control/         # Rover motor & actuator control
├── ui/                  # Next.js telemetry & monitoring dashboard
├── simulations/         # Gazebo environments (Mars, Mines)
├── docs/                # Architecture & API Documentation
└── tests/               # Test scenarios & unit tests
```

---

## 👥 Team ISRU AI

| Name | Role | Focus Area |
| :--- | :--- | :--- |
| **Aditya Shinde** | Founder / Product | Product Strategy, Vision, System Architecture |
| **Friend 1** | Computer Vision | Perception, Sensor Fusion, Object Detection |
| **Friend 2** | Path Planning | Robotics, Trajectory Generation, Navigation |
| **Friend 3** | Full-Stack/UI | Telemetry Dashboard, Cloud Infra, Next.js |

---

## 🗺️ Roadmap

| Phase | Timeline | Milestone |
| :---: | :--- | :--- |
| **Phase 1** | **Now** | **Simulated Rover MVP** — Obstacle detection + path planning. |
| **Phase 2** | **3 Months** | **Real Robot Validation** — Test on existing rover hardware. |
| **Phase 3** | **6 Months** | **Mining Pilot** — Partner with underground mining company. |
| **Phase 4** | **2 Years** | **Space Contracts** — ISRO/IN-SPACe grants, Moon/Mars missions. |

---

## 💼 Business Model

- **B2B SaaS:** Per-robot license ($5K–$20K/year depending on complexity).
- **Fleet Management Subscription:** Cloud-based telemetry, analytics, and multi-agent coordination.
- **Deployment + Support Fees:** Custom integration, mapping, and enterprise-grade SLA support.

---

## 📫 Contact

- **📧 Email:** [aditya@isruai.com](mailto:aditya@isruai.com)
- **📍 Location:** Pune, Maharashtra, India
- **🔗 X (Twitter):** [link](#)
- **🔗 LinkedIn:** [link](#)
- **🔗 GitHub:** [adityacs50-lab](https://github.com/adityacs50-lab)

---

<div align="center">

[![License](https://img.shields.io/badge/license-proprietary-red)](#)
[![YC](https://img.shields.io/badge/YC-Applicant-blue)](#)
[![Built with Python](https://img.shields.io/badge/Python-3.10+-blue)](#)
[![ROS 2](https://img.shields.io/badge/ROS_2-Humble-green)](#)

</div>
