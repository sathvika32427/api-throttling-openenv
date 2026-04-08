---
title: API Throttling OpenEnv
emoji: 🚀
colorFrom: blue
colorTo: green
sdk: docker
app_file: app.py
pinned: false
---

# API Throttling OpenEnv

This project simulates API throttling using an environment and a baseline agent.

## Overview
- Simulates API request load
- Applies throttling strategies
- Evaluates system performance using rewards

## Project Structure
- `baseline/` → Agent logic
- `env/` → Environment simulation
- `tasks/` → Request generation
- `graders/` → Evaluation logic
- `app.py` → API server (for OpenEnv validation)
- `inference.py` → Runs the agent

## How It Works
1. Requests are generated dynamically
2. Environment processes them with throttling
3. Agent decides actions
4. Rewards are calculated

## Run
The application runs automatically using Docker.

## API Endpoints
- `POST /reset` → Reset environment
- `GET /run` → Run simulation

## Final Output
The system outputs a final score based on performance.