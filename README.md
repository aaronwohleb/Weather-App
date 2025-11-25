# Secure-By-Design Weather App

A Python Flask application built to demonstrate Application Security (AppSec) principles within a modern CI/CD pipeline.

This project was developed to practice "Shifting Left"—integrating security scanning and secret management directly into the development lifecycle rather than treating it as an afterthought.

## Key Features

* **Live Weather Data:** Fetches real-time data using the OpenWeatherMap API.

* **Secure Secret Management:** Uses `python-dotenv` for local development and GitHub Secrets for CI/CD, ensuring API keys are never hardcoded or exposed in version control.

* **Automated CI/CD Pipeline:** A GitHub Actions workflow that builds, tests, and scans every commit.

* **Software Composition Analysis (SCA):** Uses `pip-audit` to check dependencies for known CVEs (vulnerabilities).

* **Static Application Security Testing (SAST):** Uses `Bandit` to scan the codebase for security flaws (e.g., hardcoded secrets, debug modes).

## Security Tools & Workflow

This project implements a **DevSecOps** approach:

1.  **Push to Main:** Code changes trigger the GitHub Actions pipeline.
2.  **Automated Testing:** `pytest` runs to ensure functionality doesn't break.
3.  **Vulnerability Scanning:**
    * **pip-audit** checks `requirements.txt` against known vulnerability databases.
    * **Bandit** scans `app.py` for Python-specific security risks (like `debug=True` or weak cryptography).
4.  **Gated Deployment:** If any security check fails, the pipeline fails, preventing insecure code from merging.

## How to Run Locally

### Prerequisites

* Python 3.13+
* An API Key from [OpenWeatherMap](https://openweathermap.org/) (Free)

### 1. Clone & Setup

```bash
git clone [https://github.com/YOUR_USERNAME/secure-weather-app.git](https://github.com/YOUR_USERNAME/secure-weather-app.git)
cd secure-weather-app
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure Secrets
Create a .env file in the root directory (this file is .gitignored to prevent leaks).

```bash
# .env file content
WEATHER_API_KEY=your_actual_api_key_here
```

4. Run the App

```bash
python app.py
```

Visit ``` http://127.0.0.1:5000 ``` in your browser.

## Incident Response Scenario
During development, a configuration error temporarily exposed the .env file to git tracking.

### Remediation Steps Taken:

1.  **Detection:** Alerted by GitGuardian / manual review.

2.  **Containment:** Revoked the compromised API Key immediately via the provider.

3.  **Eradication:** Removed the file from Git history using ```git rm --cached .env``` and updated ```.gitignore.```

4.  **Recovery:** Generated a new API key and injected it via GitHub Secrets.

## Project Structure
```
├── .github/workflows/   # CI/CD Pipeline definition (secure-pipeline.yml)
├── templates/           # HTML Frontend
├── .gitignore           # Security rules for git
├── app.py               # Main Flask Application
├── requirements.txt     # Dependencies
└── test_app.py          # Automated Tests
```
