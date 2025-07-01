
# ShadowLogin Tracker

**ShadowLogin Tracker** is a simple Python-based cybersecurity tool to detect suspicious login activity based on user behavior — such as impossible travel logins (logging in from two different countries within minutes).

---

## How It Works

The tool simulates login records (username, IP, timestamp) and checks for abnormal patterns, like:
- Same user logging in from India and then USA within 15 minutes.
- Unusual IP address switch in short time span.

> It's useful for learning about behavioral analytics in cybersecurity.

---

##  Features

Detects suspicious login sessions  
Mock IP-to-country mapping  
Built entirely with standard Python (no libraries needed)  
Beginner-friendly code  

---

##  Sample Detection Output

```
 Suspicious logins detected:
- User: Cristiano | Location changed from India to USA in 15.0 mins (2025-07-01 10:15:00 → 2025-07-01 10:30:00)
```

---

##  How to Run

```bash
python shadowlogin_tracker.py
```

Make sure Python 3 is installed. No internet or third-party libraries are required.

---

## Technologies Used

- Python 3
- `datetime` module
- Dictionary-based location logic

---

##  What I Learned

- Basics of anomaly detection in login behavior
- Writing clean Python logic to simulate cyber threats
- Simple techniques used in SIEM/SOC environments

---

## Future Ideas

- Real IP location lookup (using ipinfo.io or GeoIP)
- Email alert system
- Web-based dashboard with Flask

---

##  Author

**Prasanth K**  
Cybersecurity Enthusiast | Python Learner  

---

## License

Free to use for learning, academic, or personal cybersecurity projects.
