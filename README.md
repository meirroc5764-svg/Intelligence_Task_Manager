# Intelligence Task Manager 
This program distributes agents and missions, both among themselves and individually.

## project model  
intelligence-task-manager/
├── database/
│   ├── db_connection.py
│   ├── agent_db.py
│   └── mission_db.py
├── README.md
├── requirements.txt
└── .gitignore

#### database name = Intelligence_db

#### the project have two tabels
1. agents
2. missions

#### and three class
1. DBconnection:\
with 3 methods

2. AgentDB:\
with 9 methods

3. MissionDB:\
with 11 methods

## structur tabels

### agents table structur
-------------------------------
#### id: INT, AUTO_INCREMENT, PRIMARY KEY
-- number, is not repeated, it is done automatically, it is not created for users

#### name: VARCHAR(50),NOT NULL
-- name, up to 50 characters, field cannot be empty

#### specialty: VARCHAR(50), NOT NULL
-- specialty, no more than 50 characters, field cannot be empty

#### is_active: BOOLEAN, DEFAULT:TRUE
-- Whether the agent is active can only be true or false, with true being the default value.

#### completed_missions: INT, DEFAULT:0
-- 	Number of completed missions, number, default 0

#### failed_missions: INT, DEFAULT:0
-- Number of failed missions, number, default 0

#### agent_rank: VARCHAR(50), ENUM( Junior/ Senior/ Commander)
-- Agent rank, up to 50 characters, must be one of the proposed variants (Junior/Senior/Commander)

----------------------------------
### missions table structur

#### id: INT, AUTO_INCREMENT, PRAIMARY KEY
--  number, is not repeated, it is done automatically, it is not created for users

#### title: VARCHAR(50), NOT NULL
-- mission name, up to 50 characters, field cannot be empty

#### description: TEXT, NOT NULL
-- detailed description of the mission, text, fields cannot be empty

#### location: VARCHAR(50),NOT NULL
-- Mission location, from , no more than 50 characters, field cannot be empty

#### difficulty: INT, NOT NULL
-- mission difficulty, number, fields cannot be empty

#### importance: INT, NOT NULL
-- mission importance, number, fields cannot be empty

#### status: VARCHAR(50), DEFAULT:NEW
-- Mission status, no more than 50 characters. When created, the status is "new" \
if the task has been assigned to an agent, the status changes to "ASSIGNED" \
if it is in progress, the status is "IN_PROGRESS" \
if the mission was successful, the status is "COMPLETED" \
if the mission failed, the status is "FAILED" \
if the mission was canceled, the status is "CANCELLED"

#### risk_level: VARCHAR(50), NOT NULL
-- Mission risk level, no more than 50 characters, cannot be empty, calculated automatically for non-users.
Calculation formula: "difficulty * 2 + importance = risk_level" \
The risk level is determined by the number: \
0-9 = "LOW" \
10-17 = "MEDIUM" \
18-24 = "HIGH" \
25+ = "CRITICAL" 

#### assigned_agent_id: INT, DEFAULT:NULL
-- The mission's affiliation with an agent, number, is empty by default until linked to a specific agent; when linked, the agent's personal ID number is recorded.

------------------------------------

## the class

### class DBConnection

#### 1. method: get_connection()
-- Returns an active connection to MySQL

#### 2. method: create_database()
-- Creates Intelligence_db if it does not exist.

#### 3. method: create_tables()
-- Creates both tables if they do not exist.

-------------------
### class AgentDB

#### 1. method: create_agent(data)
-- Creates a new agent and returns the agent object.

#### 2. method: get_all_agents()
-- Returns a list of all agents

#### 3. method: get_agent_by_id(id)
-- Returns one agent by ID, or None

#### 4. method: update_agent(id, data)
-- UPDATE for the entire row (cannot change id)

#### 5. method: deactivate_agent(id)
-- Sets agent inactive status

#### 6. method: increment_completed(id)
-- Updates the number of tasks completed.

#### 7. method: increment_failed(id)
-- Updates the number of failed tasks

#### 8. method: get_agent_performance(id)
-- Returns a dictionary with these keys completed, failed, total, success_rate
(success_rate - what percentage of tasks completed successfully out of the total)

#### 9. method: count_active_agents()
-- Returns the number of active agents.

---------------------------
### class MissionDB

#### 1. method: create_mission(data)
-- Creates a new task and returns the entire object.

#### 2. method: get_all_missions()
-- Returns all tasks.

#### 3. method: get_mission_by_id(id)
-- Returns one task by ID, or None.

#### 4. method: assign_mission(m_id, a_id)
-- Assigning a task to an agent

#### 5. method: update_mission_status(id, status)
-- Used for any status change.

#### 6. method: get_open_missions_by_agent(id)
-- 	Returns agent ASSIGNED/IN_PROGRESS tasks.

#### 7. method: count_all_missions()
-- Total tasks.

#### 8. method: count_by_status(status)
-- Counting by a certain status

#### 9. method: count_open_missions()
-- Open task counter

#### 10. method: count_critical_missions()
-- CRITICAL task counter.

#### 11. method: get_top_agent()
-- The agent with the highest completed_missions.

----------------------------------------
## System rules — the 10 rules relevant to the data layer
### 1
rank must be Junior / Senior / Commander — any other value throws an error. 
### 2
difficulty and importance must be between 1 and 10 — otherwise an error. 
### 3
risk_level is calculated automatically when creating a task — the user does not submit it. 
### 4
An agent with is_active=False cannot accept tasks. 
### 5
An agent cannot have more than 3 open tasks (ASSIGNED / IN_PROGRESS) at the same time. 
### 6 
If risk_level=CRITICAL — only an agent with the Commander rank can accept the task. 
### 7 
Only a task with the status NEW can be assigned. After assignment: status=ASSIGNED. 
### 8 
Only a task with the status ASSIGNED can be started. After: status=IN_PROGRESS. 
### 9 
Only a task with the status IN_PROGRESS can be finished and changed to failed or completed. 
### 10 
Only a task with the status NEW or ASSIGNED can be canceled — otherwise an error. 

-----------------------------------
## Running instructions

open cmd and enter:

docker run -d --name intelligence-mysql -e MYSQL_ROOT_PASSWORD=1234 \
-e MYSQL_DATABASE=Intelligence_db -p 3306:3306 mysql:8.0

after open git 
https://github.com/meirroc5764-svg/Intelligence_Task_Manager

and take a kod \
open a vs kod and run a main 