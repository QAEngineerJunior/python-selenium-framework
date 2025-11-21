# Python Selenium Automation Framework

A fully featured, professional-grade **Selenium Test Automation Framework** built with:

- **Python 3**
- **Selenium 4**
- **Pytest**
- **Page Object Model (POM)**
- **Cross-browser support (Chrome, Firefox, Edge)**
- **Multi-environment config (dev, stage, prod)**
- **Logging system**
- **HTML reports**
- **Automatic screenshots on failure**
- **Parallel execution**
- **CI/CD integration with GitHub Actions**

This repo is a complete showcase of QA Automation Engineering skills and can be used as a template for production-quality automated UI testing.

---

## 🚀 Features

### ✔ Page Object Model (POM)
Clean separation between Pages, Tests, Utilities, and Config files.

### ✔ Cross-Browser Support
Run tests on:
- Chrome
- Firefox
- Edge

### ✔ Multi-environment Support
Run against:
- dev
- stage
- prod  
(using `--env` flag)

### ✔ Automatic Screenshots on Test Failures
All failures automatically save screenshots into `/screenshots` and are embedded in the HTML report.

### ✔ Logging System
Every test action is logged into `/logs` with timestamps.

### ✔ HTML Reports
Pytest generates full standalone HTML reports in `/reports`.

### ✔ Parallel Test Execution
Run tests across multiple CPU cores using `pytest-xdist`.

### ✔ GitHub Actions CI/CD
A complete workflow automatically runs your Selenium tests in the cloud using headless Chrome.

---

## 🧱 Project Structure

python-selenium-framework/
│
├── config/
│ ├── environments.json
│ └── settings.py
│
├── pages/
│ ├── base_page.py
│ ├── login_page.py
│ ├── products_page.py
│ └── checkout_page.py
│
├── tests/
│ ├── test_cart.py
│ ├── test_checkout.py
│ ├── test_invalid_login.py
│ ├── test_locked_user.py
│ └── test_login_variations.py
│
├── utils/
│ ├── browser.py
│ ├── logger.py
│ ├── screenshots.py
│ └── data_loader.py
│
├── reports/
├── logs/
├── screenshots/
│
├── .github/
│ └── workflows/
│ └── selenium_tests.yml
│
├── pytest.ini
├── requirements.txt
└── README.md




---

## 🏁 How to Run Tests Locally

### Install dependencies:

pip install -r requirements.txt


### Run all tests:

pytest -v


### Run tests in parallel:

pytest -n auto


### Run on Chrome, Firefox, or Edge:

pytest --browser=chrome
pytest --browser=firefox
pytest --browser=edge


### Run against an environment:

pytest --env=dev
pytest --env=stage
pytest --env=prod


---

## 📸 Example Screenshot on Failure

Screenshots are saved in `/screenshots` automatically.  
They also appear inside the HTML report generated on each run.

---

## 📊 HTML Reports

Reports are generated here: reports/report.html


They contain:

- Test results
- Execution times
- Embedded screenshots
- Metadata
- Fail reasons

---

## 🤖 CI/CD – GitHub Actions

This project includes a GitHub Actions workflow: .github/workflows/selenium_tests.yml


The pipeline:

- Runs tests automatically on every push
- Uses Python 3.10 on Ubuntu
- Runs headless Chrome
- Uploads HTML report & screenshots as artifacts

---

## 🛠 Technologies Used

| Tool | Purpose |
|------|---------|
| Python | Main language |
| Selenium 4 | Browser automation |
| Pytest | Test execution |
| WebDriver Manager | Automatic Chrome driver |
| Page Object Model | Clean architecture |
| GitHub Actions | CI/CD pipeline |
| Chrome / Firefox / Edge | Cross-browser support |

---

## 👤 Author

**GitHub:** [@tripperry](https://github.com/tripperry)

---






