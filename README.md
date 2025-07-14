<img width="1818" height="879" alt="image" src="https://github.com/user-attachments/assets/1e042406-7cfb-4024-b5bc-7e3286f8d3d6" />


<img width="1840" height="882" alt="image" src="https://github.com/user-attachments/assets/b6188b7f-b1a9-4bc7-a691-8930581068a1" />



# 🧱 P2P Blockchain Simulator

A simple peer-to-peer blockchain network simulator built with **Flask (Python)** for the backend and **Next.js (TypeScript)** for the frontend. This project demonstrates basic blockchain principles like mining, transaction validation, and chain synchronization between nodes.

## 🚀 Features

- ⛏️ Proof-of-work mining algorithm  
- 📦 Blocks with hashed linkage  
- 🔁 Add/view pending transactions  
- 🌐 Register and resolve nodes (P2P network simulation)  
- 📊 Clean UI to view blockchain state  
- ⚙️ Reset blockchain functionality  

## 🧩 Tech Stack

| Layer     | Stack                      |
|-----------|----------------------------|
| Frontend  | Next.js + TypeScript       |
| Backend   | Flask (Python)             |
| Styling   | Tailwind CSS               |
| Communication | REST APIs (JSON)       |

## 📂 Project Structure

```bash
.
├── client/                 # Next.js frontend
│   ├── components/         # React components like BlockCard, TransactionForm
│   └── pages/              # Frontend pages
├── server/                 # Flask backend
│   ├── blockchain.py       # Core blockchain logic
│   └── app.py              # API endpoints
