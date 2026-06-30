#!/usr/bin/env python3
import os
import requests
from datetime import datetime
import pytz

GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')
GITHUB_USERNAME = os.getenv('GITHUB_USERNAME', 'ShreyanshMishra1202')

HEADERS = {
    'Authorization': f'token {GITHUB_TOKEN}',
    'Accept': 'application/vnd.github.v3+json'
}

def get_user_stats():
    """Fetch user statistics from GitHub API"""
    try:
        url = f'https://api.github.com/users/{GITHUB_USERNAME}'
        response = requests.get(url, headers=HEADERS)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching user stats: {e}")
        return {}

def get_repos_stats():
    """Fetch repository statistics"""
    try:
        url = f'https://api.github.com/users/{GITHUB_USERNAME}/repos'
        params = {'sort': 'stars', 'direction': 'desc', 'per_page': 100}
        response = requests.get(url, headers=HEADERS, params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching repos: {e}")
        return []

def get_total_stars(repos):
    """Calculate total stars across all repositories"""
    return sum(repo.get('stargazers_count', 0) for repo in repos)

def get_total_forks(repos):
    """Calculate total forks across all repositories"""
    return sum(repo.get('forks_count', 0) for repo in repos)

def get_update_time():
    """Get current time in IST"""
    ist = pytz.timezone('Asia/Kolkata')
    return datetime.now(ist).strftime('%Y-%m-%d %H:%M:%S IST')

def generate_readme():
    """Generate the README content with dynamic stats"""
    user_stats = get_user_stats()
    repos = get_repos_stats()
    
    total_stars = get_total_stars(repos)
    total_forks = get_total_forks(repos)
    public_repos = user_stats.get('public_repos', 0)
    followers = user_stats.get('followers', 0)
    following = user_stats.get('following', 0)
    update_time = get_update_time()
    
    readme_content = f"""# 👋 Hi, I'm Shreyansh Mishra

<div align="center">

### Aspiring Software Engineer | Full Stack MERN Developer | GATE CSE Aspirant

[![GitHub followers](https://img.shields.io/github/followers/ShreyanshMishra1202?label=Follow&style=social)](https://github.com/ShreyanshMishra1202)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=flat&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/shreyansh-mishra-cse/)
[![Email](https://img.shields.io/badge/Email-D14836?style=flat&logo=gmail&logoColor=white)](mailto:shreyanshmishra1202@gmail.com)
[![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat&logo=github&logoColor=white)](https://github.com/ShreyanshMishra1202)

</div>

---

## 🚀 About Me

I am a **B.Tech Computer Science student** with a strong interest in software development, problem-solving, and system design. I have **3+ years of academic and project-based programming experience** building full-stack web applications using MERN and MySQL. Alongside development, I am actively preparing for **GATE CSE** and continuously improving my data structures, algorithms, and computer science fundamentals.

I combine **strong software development skills** with **deep computer science fundamentals** and **competitive exam preparation**. My focus on full-stack development, problem-solving, and continuous learning helps me build practical solutions while maintaining a solid theoretical foundation.

- 💻 **Specialized in:** Full Stack MERN Development & Backend (Spring Boot)
- 🔍 **Expertise in:** Building scalable REST APIs & web applications
- 📚 **Currently Learning:** GATE CSE topics (OS, DBMS, CN, TOC, Algorithms)
- 🎯 **Passion:** Writing clean, maintainable, and efficient code
- 🤝 **Always Open:** To collaboration, learning, and knowledge sharing

---

## 📊 Live GitHub Statistics

<div align="center">

| Metric | Count |
|--------|-------|
| 📚 Public Repositories | {public_repos} |
| ⭐ Total Stars | {total_stars} |
| 🍴 Total Forks | {total_forks} |
| 👥 Followers | {followers} |
| 🔗 Following | {following} |

**Last Updated:** `{update_time}` ⏰

</div>

---

## 📊 GitHub Activity

[![Activity Graph](https://github-readme-activity-graph.vercel.app/graph?username=ShreyanshMishra1202&theme=github-dark&bg_color=0d1117&color=58a6ff&line=30363d&point=58a6ff&area=true)](https://github.com/ShreyanshMishra1202)

---

## 📈 GitHub Statistics

<div align="center">

[![GitHub Stats](https://github-readme-stats-sigma-five.vercel.app/api?username=ShreyanshMishra1202&show_icons=true&theme=dark&bg_color=0d1117&title_color=58a6ff&text_color=c9d1d9&icon_color=58a6ff&cache_seconds=3600)](https://github.com/ShreyanshMishra1202)

[![Top Languages](https://github-readme-stats-sigma-five.vercel.app/api/top-langs/?username=ShreyanshMishra1202&layout=compact&theme=dark&bg_color=0d1117&title_color=58a6ff&text_color=c9d1d9&cache_seconds=3600)](https://github.com/ShreyanshMishra1202)

</div>

---

## 🛠️ Tech Stack

### Languages
![Java](https://img.shields.io/badge/Java-ED8B00?style=for-the-badge&logo=openjdk&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)
![C](https://img.shields.io/badge/C-00599C?style=for-the-badge&logo=c&logoColor=white)
![SQL](https://img.shields.io/badge/SQL-CC2927?style=for-the-badge&logo=microsoft-sql-server&logoColor=white)

### Frontend
![React.js](https://img.shields.io/badge/React-61DAFB?style=for-the-badge&logo=react&logoColor=black)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)
![Bootstrap](https://img.shields.io/badge/Bootstrap-7952B3?style=for-the-badge&logo=bootstrap&logoColor=white)
![Vite](https://img.shields.io/badge/Vite-646CFF?style=for-the-badge&logo=vite&logoColor=white)

### Backend
![Spring Boot](https://img.shields.io/badge/Spring_Boot-6DB33F?style=for-the-badge&logo=spring-boot&logoColor=white)
![REST APIs](https://img.shields.io/badge/REST_APIs-FF6B6B?style=for-the-badge&logo=api&logoColor=white)
![Hibernate](https://img.shields.io/badge/Hibernate-59666C?style=for-the-badge&logo=hibernate&logoColor=white)
![JPA](https://img.shields.io/badge/JPA-FF6B6B?style=for-the-badge&logo=java&logoColor=white)

### Databases
![MySQL](https://img.shields.io/badge/MySQL-005C84?style=for-the-badge&logo=mysql&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-336791?style=for-the-badge&logo=postgresql&logoColor=white)
![H2](https://img.shields.io/badge/H2_Database-003D82?style=for-the-badge&logo=database&logoColor=white)

### Tools & Platforms
![Git](https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)
![Maven](https://img.shields.io/badge/Maven-C71A36?style=for-the-badge&logo=apache-maven&logoColor=white)
![Postman](https://img.shields.io/badge/Postman-FF6C37?style=for-the-badge&logo=postman&logoColor=white)
![VS Code](https://img.shields.io/badge/VS_Code-007ACC?style=for-the-badge&logo=visualstudiocode&logoColor=white)
![IntelliJ IDEA](https://img.shields.io/badge/IntelliJ_IDEA-000000?style=for-the-badge&logo=intellij-idea&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-F37726?style=for-the-badge&logo=jupyter&logoColor=white)

---

## 🏆 Key Achievements & Certifications

- 🥉 **3rd Prize Winner in College Hackathon** — ₹2000 Cash Prize
- 🎓 **Meta Front-End Developer Professional Certificate** — Meta (Coursera)
- 📊 **TCS NQT Qualified** — Score: 84% (Very Good)
- 🏅 **NPTEL Software Engineering Certification** — Successfully Completed
- 🗣️ **Participant in Youth Parliament** — Active Community Engagement
- 💪 **3+ Years of Consistent Programming Experience** — Academic & Project-based

---

## 📂 Featured Projects

### 1. **E-Commerce Web Application** | [Frontend](https://github.com/ShreyanshMishra1202/Ecommerce-frontend) | [Backend](https://github.com/ShreyanshMishra1202/E-commerceProject)

A full-stack e-commerce platform featuring comprehensive product management, user authentication, secure shopping cart functionality, and RESTful APIs with complete CRUD operations.

- **Tech Stack:** React.js, Spring Boot, Java, MySQL/H2, Bootstrap
- **Key Features:** 
  - Product catalog with filtering & search
  - User authentication & authorization
  - Shopping cart & order management
  - Admin dashboard for product management
  - RESTful API design with proper error handling

---

### 2. **Road Accident Data Analysis** | [View Project](https://github.com/ShreyanshMishra1202)

Performed comprehensive exploratory data analysis on road accident datasets to identify trends, accident-prone regions, and key contributing factors using advanced data visualization techniques.

- **Tech Stack:** Python, Pandas, NumPy, Matplotlib, Seaborn
- **Key Features:**
  - Statistical analysis & trend identification
  - Geospatial visualization of accidents
  - Factor analysis & correlation studies
  - Data cleaning & preprocessing
  - Actionable insights generation

---

### 3. **House Price Prediction System** | [View Project](https://github.com/ShreyanshMishra1202)

Built a machine learning model to predict house prices using historical housing data, regression techniques, and feature engineering for accurate price forecasting.

- **Tech Stack:** Python, Scikit-learn, Pandas, NumPy, Matplotlib
- **Key Features:**
  - Data preprocessing & feature engineering
  - Multiple regression models implementation
  - Model evaluation & performance metrics
  - Visualization of predictions vs actual values
  - Hyperparameter tuning

---

## 📚 What I'm Currently Learning

- 🎓 **GATE CSE Preparation** — Operating Systems, DBMS, Computer Networks, TOC, Advanced Algorithms
- 🔧 **Spring Boot & Backend Development** — Advanced patterns, microservices concepts
- 💾 **Advanced SQL & Database Systems** — Query optimization, indexing, normalization
- 🏗️ **System Design & Architecture** — Scalable application design principles

---

## 💡 Skills & Expertise

### Software Development
- ✅ Full Stack Web Development (MERN + Spring Boot)
- ✅ RESTful API Design & Development
- ✅ Database Design & SQL Optimization
- ✅ Object-Oriented Programming & Design Patterns
- ✅ Version Control & Git Workflows

### Problem Solving
- 🎯 Data Structures & Algorithms
- 🎯 Competitive Programming (Java, Python, C)
- 🎯 System Design & Architecture
- 🎯 Debugging & Troubleshooting
- 🎯 Code Optimization & Performance

### Tools & Methodologies
- 🛠️ Agile Development Practices
- 🛠️ API Testing (Postman)
- 🛠️ Build Tools (Maven)
- 🛠️ IDE Proficiency (VS Code, IntelliJ IDEA)
- 🛠️ Documentation & Clean Code Principles

---

## 🎯 Career Aspirations

My goal is to become a proficient **Software Engineer** who can:
- Design and develop scalable, production-ready applications
- Contribute to open-source projects
- Master full-stack development from frontend to backend
- Excel in GATE CSE and secure opportunities in top tech companies
- Solve complex real-world problems through innovative software solutions

---

## 📞 Let's Connect!

<div align="center">

[📧 Email](mailto:shreyanshmishra1202@gmail.com) • 
[💼 LinkedIn](https://www.linkedin.com/in/shreyansh-mishra-cse/) • 
[💻 GitHub](https://github.com/ShreyanshMishra1202) • 
[🐙 Open to Opportunities](mailto:shreyanshmishra1202@gmail.com)

**Feel free to reach out for collaborations, internships, or just to connect!**

</div>

---

## 💬 Fun Facts

- 🎮 I love solving algorithmic challenges on LeetCode & HackerRank
- 🌍 Passionate about open-source contributions & community learning
- ☕ Coffee-driven developer with a love for debugging
- 📖 Always reading tech blogs, documentation, and CS fundamentals
- 🚀 Excited about building projects that make a real-world impact

---

## 📊 Contribution Streak

<div align="center">

[![GitHub Streak](https://github-readme-streak-stats.herokuapp.com/?user=ShreyanshMishra1202&theme=dark&background=0d1117&ring=58a6ff&fire=58a6ff&currStreakNum=c9d1d9&currStreakLabel=58a6ff&sideNums=c9d1d9&sideLabels=c9d1d9&dates=c9d1d9)](https://github.com/ShreyanshMishra1202)

</div>

---

<div align="center">

### ⭐ If you find my work interesting, don't forget to leave a star on my repositories!

**"Code is like humor. When you have to explain it, it's bad." – Cory House**

![Profile Views](https://komarev.com/ghpvc/?username=ShreyanshMishra1202&color=0077B5)

</div>
"""
    
    return readme_content

if __name__ == '__main__':
    readme = generate_readme()
    with open('README.md', 'w', encoding='utf-8') as f:
        f.write(readme)
    print("✅ README.md updated successfully!")
