## Fully Automated Stock Trading Bot
A high-performance, fully automated stock trading bot built in Python that executes real-time trades based on technical indicators and market data. Designed for intraday equity trading, the system detects high-probability buy/sell signals and places trades with built-in risk management — no manual intervention required.

## Why I Built This
I've always been curious about the intersection of finance, data, and automation. This project combines all three — built from scratch to challenge myself and create a system that could operate independently like a human trader, but with more speed, discipline, and precision.

## System Architecture 

![Trading Bot Demo](https://media.licdn.com/dms/image/v2/D4D22AQHQNQo7i6qiYQ/feedshare-shrink_1280/feedshare-shrink_1280/0/1722856132867?e=1746057600&v=beta&t=NQ8SEUvgVf1-QwvpWIPp0PRiV0SSF59UpWoLSO_Fekc)


## Features

📡 Real-time market feed via WebSockets

⚙️ Strategy engine using RSI, Moving Averages, and Stochastic RSI

💾 Fast signal storage and inter-process communication with Redis

🧠 Intelligent signal throttling to avoid duplicate triggers

📊 Trade history and signal logging using MySQL

🔁 Auto Stop Loss and Target handling

🏦 Broker integration for live order execution

📈 Scalable architecture to support multiple stocks & intervals

🛠️ Tech Stack
Category	Tools/Tech
Language	Python
Databases	Redis (real-time), MySQL (persistent logs)
Data Feed	Kotak Securities WebSocket API
Libraries	pandas, numpy, ta-lib, redis-py, sqlalchemy
Broker API	Secure integration for order placement
Platform	Linux, cron jobs for continuous execution


## Performance
📈 Tested on real market data with live trades executed.

✅ Automatically handles SL/Target exits — no manual action needed.

⚡ Optimized for low-latency and high-frequency signal processing.


## 💼 What I Learned
Building robust, low-latency systems

Real-time data handling using WebSockets

Clean architectural design using modular programming

Importance of risk management in trading systems

Integration of multiple systems (Redis, SQL, Broker APIs)




📬 Let's Connect
I'm passionate about fintech, algo trading, and scalable backend systems.
If you're hiring or just want to connect, feel free to reach out on [LinkedIn](https://www.linkedin.com/in/vaibhav-mokale-b50504217/) or [email](mokalevaibhav@gmail.com) me.












## 🔒 License

This project is proprietary. Unauthorized use is prohibited. Contact the author for permission.
