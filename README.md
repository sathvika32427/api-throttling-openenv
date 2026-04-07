\# API Throttling OpenEnv



\## Overview

This project implements a real-world reinforcement learning environment that simulates API request handling under server capacity constraints.



The agent must decide whether to:

\- Accept a request

\- Delay a request

\- Reject a request



The goal is to maximize reward while avoiding overload and minimizing latency.



\---



\## Why this matters

Modern backend systems must handle millions of requests efficiently. Poor handling leads to:

\- Server crashes

\- High latency

\- SLA violations



This environment simulates these real-world challenges.



\---



\## Environment Details



\### Observation Space

\- current\_load → current system load

\- capacity → max server capacity

\- time → timestep

\- next\_request:

&#x20; - type: premium / normal / spam

&#x20; - load: resource usage

&#x20; - latency: waiting time



\---



\### Action Space

| Action | Meaning |

|--------|--------|

| 0 | Reject |

| 1 | Delay |

| 2 | Accept |



\---



\## Tasks



| Task | Difficulty | Description |

|------|----------|-------------|

| Easy | Low | High capacity, fewer requests |

| Medium | Medium | Balanced |

| Hard | High | Heavy load, limited capacity |



\---



\## Reward System



\- Accept premium → high reward

\- Accept normal → moderate reward

\- Reject spam → high reward

\- Overload → penalty

\- High latency → penalty (SLA violation)



\---



\## Run the baseline agent



```bash

python -m baseline.run\_agent

