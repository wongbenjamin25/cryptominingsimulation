# Blockchain Mining Simulation Assignment

This project was developed as part of the QF4211 / DSE4211 Digital Currencies module at NUS. It simulates a blockchain mining environment where nodes compete to solve proof-of-work puzzles and build a valid blockchain.

## Overview

The goal of this assignment is to simulate the behavior of a blockchain network with multiple miners (nodes) that:
- Attempt to mine new blocks using a simplified proof-of-work algorithm
- Broadcast newly mined blocks to other nodes
- Build a local view of the blockchain
- Resolve forks by adopting the longest valid chain

## Key Features

- Implementation of the mining logic including:
  - Proof-of-work algorithm
  - Nonce discovery
  - Block propagation and chain extension
- Simulated network behavior using asynchronous communication
- Fork resolution strategy based on the longest chain rule
- Command-line configuration of mining difficulty, block interval, and network size

## Technologies Used

- Python 3.x
- asyncio (for simulating concurrent miners)
- hashlib (for block hashing)
- argparse (for CLI configuration)

## Project Structure

mining-assignment/
│
├── miner.py              # Core mining logic and block structure
├── network.py            # Simulated peer-to-peer communication
├── node.py               # Node process for mining and message handling
├── config.json           # Simulation parameters (difficulty, delay, etc.)
├── run.py                # Entry point for launching the simulation
└── README.md             # Project documentation

Parameters:
	•	--nodes: Number of miner nodes to simulate
	•	--difficulty: Mining difficulty (number of leading zeros in hash)
	•	--block-interval: Target average time between blocks (in seconds)

Learning Outcomes
	•	Gained practical understanding of how mining and consensus work in a blockchain.
	•	Learned to simulate distributed systems with asynchronous behavior.
	•	Understood the trade-offs in fork resolution and difficulty adjustment.

Author

Benjamin Wong (@wongbenjamin25)
Bachelor of Science (Hons.) in Data Science & Quantitative Finance
National University of Singapore
