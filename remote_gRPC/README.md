# 📡 Distributed Systems Workshop  
## Client-Server Communication Patterns (gRPC / RMI)

## 📖 Overview
This project implements a distributed client-server system that manages student information for a course. The system exposes remote services that allow clients to query student data such as grades, group assignments, and evaluations.

The communication between client and server is implemented using remote procedure calls (RPC) through either:
- gRPC, or
- Java RMI (Remote Method Invocation)

---

## 🎯 Objectives
- Design and implement a remote server object
- Expose remote methods/services
- Develop a client application that consumes these services
- Test the system across at least two different machines

---

## ⚙️ Features / Services

### 1. 📊 Get Student Average (Notas)
- **Input:** Student's first name or last name  
- **Output:** Average grade based on:
  - Quiz 1
  - Taller 1  

---

### 2. 👥 Get Student Group (Grupo)
- **Input:** Student's last name  
- **Output:** Group assignment (e.g., GRT 1, GRT 2, etc.)

---

### 3. 📝 Get Evaluations (Evaluaciones)
- **Input:** None  
- **Output:** List of evaluations conducted so far:
  - Quiz 1
  - Taller 1  

---

## 🗂️ Dataset

| Last Name | First Name | Group | Quiz 1 | Taller 1 |
|----------|-----------|--------|--------|----------|
| Perez | Maria | GRT 1 | 4.5 | 4.0 |
| Montealegre | José | GRT 1 | 4.25 | 4.0 |
| Sanchez Burbano | Juan | GRT 2 | 5.0 | 4.5 |
| Tellez Vallejo | Mariana | GRT 2 | 5.0 | 4.5 |
| Castiblanco | Miguel | GRT 3 | 5.0 | 4.4 |
| Ospina | Thamara | GRT 3 | 5.0 | 4.4 |
| Berrizbeitia | Pedro | GRT 4 | 4.75 | 0.0 |
| Morales | Samira | GRT 4 | 4.9 | 3.0 |
| Sarmiento | Thomas Alberto | GRT 5 | 4.5 | 4.0 |
| Montenegro | Lucía | GRT 5 | 0.0 | 4.0 |
| Madrigal | Luz Juan | GRT 5 | 4.5 | 4.0 |
| Morales Sanchez | Nicolas | GRT 6 | 5.0 | 2.8 |
| Bohorquez | Daniela | GRT 7 | 4.8 | 2.3 |
| Diaz Sanjuan | Mariana | GRT 7 | 4.8 | 2.3 |
| Parrado Cruz | Alejandro | GRT 8 | 4.9 | 4.3 |
| Vargas Fonseca | Silvestre | GRT 8 | 4.9 | 4.3 |
| Araque Rojas | Juliana | GRT 9 | 5.0 | 0.0 |
| Quintero | Juan Ignacio | GRT 9 | 0.0 | 3.0 |
| Jimenez | Mónica | GRT 9 | 5.0 | 3.0 |

---

## 🏗️ System Architecture
Client  --->  Remote Calls  --->  Server 
            (gRPC / RMI)
            
- The server hosts the student data and implements remote methods
- The client sends requests and receives responses
- Communication happens over the network using RPC

---

## 🚀 How to Run

### 1. Run the Server
py server.py

### 2. Run the Server
py client.py

---

## Test Remote Methods
1. Consultar promedio notas
2. Consultar grupo
3. Consultar evaluaciones (quiz y taller)

---

## 🌐 Distributed Testing
The system was tested on:

- Two separate machines
- Connected over a network
- Verifying remote communication and response handling

---

## 🛠️ Technologies Used
- Programming Language: Python
- RPC Framework: gRPC
- Networking: TCP/IP

---

## 👥 Team Members
- Juan Felipe Gómez López
- Sebastian Gaibor
- David Beltrán Gómez