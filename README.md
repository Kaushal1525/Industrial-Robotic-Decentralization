
# Decentralized Swarm Task Allocation and Collaborative Recovery System

## Overview

This project demonstrates a decentralized multi-robot task allocation and collaborative recovery system developed using Python. The simulation models a swarm of autonomous mobile robots operating within a shared environment where robots independently select tasks, execute missions, detect failures, and collaboratively recover unfinished work.

Unlike centralized fleet management systems, this implementation allows robots to make local decisions based on task priority, distance, and workload. When a robot fails during task execution, the swarm automatically identifies an available replacement robot to continue the mission without centralized supervision.

The project illustrates important concepts in swarm robotics, distributed artificial intelligence, collaborative autonomous systems, and industrial automation.

---

## Features

- Decentralized task allocation
- Autonomous task selection
- Priority-aware task assignment
- Robot motion simulation
- Dynamic workload management
- Robot failure simulation
- Collaborative task recovery
- Autonomous task reassignment
- Multi-robot coordination
- Decision cycle monitoring

---

## Technologies Used

- Python 3
- Math
- Random
- Time

---

## Project Structure

```text
Decentralized-Swarm-Task-Allocation/
│
├── swarm_task_allocation.py
├── README.md
└── requirements.txt
```

---

## Installation

### Clone the repository

```bash
git clone https://github.com/Kaushal1525/Decentralized-Swarm-Task-Allocation.git
```

### Navigate to the project directory

```bash
cd Decentralized-Swarm-Task-Allocation
```

No external libraries are required.

Run the simulation using:

```bash
python swarm_task_allocation.py
```

---

## Working Principle

The simulation executes repeated collaborative decision cycles.

During each cycle:

1. Display the current state of every robot.
2. Identify all available tasks.
3. Allow idle robots to independently evaluate nearby tasks.
4. Assign tasks based on distance and priority.
5. Simulate robot failures.
6. Detect interrupted missions.
7. Search for available helper robots.
8. Select the most suitable replacement robot.
9. Reassign unfinished tasks.
10. Continue robot movement until task completion.

---

## Robot Model

Each robot maintains the following attributes:

- Robot ID
- Current position
- Velocity
- Assigned task
- Workload
- Failure status

Robots move toward assigned task locations while continuously updating their positions.

---

## Task Model

Each task includes:

- Task identifier
- Target coordinates
- Priority level
- Assigned robot
- Completion status

Tasks remain available until successfully completed.

---

## Autonomous Task Allocation

Idle robots independently search for available tasks.

Task selection considers:

- Distance to the task
- Task priority
- Current task ownership

The robot selects the most suitable unassigned task based on a simple cost function.

---

## Robot Failure Simulation

The simulation randomly introduces robot failures during execution.

When a failure occurs:

- The robot stops operating.
- Its assigned task becomes interrupted.
- The swarm initiates collaborative recovery.

---

## Collaborative Recovery

The recovery process consists of:

1. Detecting robot failure.
2. Identifying all available robots.
3. Evaluating candidate robots based on:
   - Distance to the unfinished task
   - Current workload
4. Selecting the best replacement robot.
5. Reassigning the interrupted task.
6. Continuing mission execution.

This decentralized mechanism enables continuous operation without relying on a permanent central controller.

---

## Motion Model

Robots navigate toward assigned task locations using a simple velocity-based movement model.

The simulation includes:

- Position updates
- Velocity updates
- Speed limiting
- Task completion detection

---

## Decision Cycle Workflow

```text
Initialize Robots and Tasks
            │
            ▼
Display Robot Dashboard
            │
            ▼
Autonomous Task Selection
            │
            ▼
Task Assignment
            │
            ▼
Robot Motion
            │
            ▼
Failure Detection
            │
            ▼
Available Robot Search
            │
            ▼
Task Reassignment
            │
            ▼
Mission Continuation
            │
            ▼
Task Completion
```

---

## Applications

- Swarm Robotics
- Warehouse Automation
- Autonomous Mobile Robots
- Smart Manufacturing
- Logistics Automation
- Fleet Coordination
- Distributed Artificial Intelligence
- Industrial Robotics
- Multi-Agent Systems
- Autonomous Systems Research
- Search and Rescue Robotics
- Smart Factory Automation

---

## Future Enhancements

- Conflict-Based Search (CBS)
- Multi-robot path planning
- Adaptive swarm intelligence
- Reinforcement learning
- Dynamic obstacle avoidance
- Battery management system
- ROS 2 integration
- Gazebo simulation
- Digital twin visualization
- Task scheduling optimization
- Inter-robot communication
- Distributed consensus algorithms
- Real robot deployment
- Warehouse digital simulation

---

## Requirements

- Python 3.8 or later

---

## Dependencies

This project uses only Python's standard library.

- math
- random
- time

---

## Author

Kaushal Reddy

AI & Autonomous Systems Engineer

GitHub: https://github.com/Kaushal1525
````
