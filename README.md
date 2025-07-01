# 🕵️‍♂️ ShadowLogin Tracker

**ShadowLogin Tracker** is a simple Python tool I built to spot suspicious login activity. It works by comparing the time and location of each login to detect cases where a user seems to log in from two far-apart places within a short time — something that's likely impossible.

> Example: If someone logs in from India and then the US within 15 minutes, the tool flags it.

---

## 👀 What It Does
- Tracks user login data (username, IP, timestamp)
- Uses mock IP-to-country mapping
- Detects "impossible travel" logins and prints alerts

---

## 💻 How to Run It

```bash
python shadowlogin_tracker.py


## Technologies Used
Python 3

datetime module

Dictionary-based location logic

What I Learned
Basics of anomaly detection in login behavior

Writing clean Python logic to simulate cyber threats

Simple techniques used in SIEM/SOC environments

Future Ideas
Real IP location lookup (using ipinfo.io or GeoIP)

Email alert system

Web-based dashboard with Flask

Author
Prasanth K
Cybersecurity Enthusiast | Python Learner
Built for learning and showcasing beginner-level detection logic.

License
Free to use for learning, academic, or personal cybersecurity projects.
