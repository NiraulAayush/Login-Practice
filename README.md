# Login-Practice: Automated Login Testing

This is a basic Selenium-Pytest framework to automate login functionality using the Page Object Model (POM) structure.

---

## 📁 Project Structure

- `data/`: Contains test data like login credentials.
- `pages/`: Contains page classes representing web pages (e.g., LoginPage).
- `tests/`: Contains test files and fixtures.
- `requirements.txt`: Lists Python dependencies.
- `README.md`: Documentation for the project.

---

## 🛠 Setup Instructions

1. **Create and activate a virtual environment (optional but recommended).**
2. **Install required packages using:**
   - `pip install -r requirements.txt`

3. **Make sure ChromeDriver is installed and matches your Chrome version.**
4. **Mark the `Login-Practice` directory as a "Sources Root" in PyCharm to fix import issues.**

---

## 🚀 Running the Tests

- Run all tests: `pytest tests/`
- Run a specific test file: `pytest tests/test_login.py`

---