# Pytest Framework

## Overview
This project is a Pytest-based testing framework designed to facilitate automated end-to-end testing for web applications. The framework integrates Selenium for browser automation and Pytest-HTML for generating detailed test execution reports.

## Getting Started

### Prerequisites
- Python 3.6 or higher
- ChromeDriver

### Installation

1. Clone the repository:

   ```
   git clone <repository_url>
   cd pytest_framework
   ```

2. Set up the virtual environment and install dependencies:

   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   pip install -r requirements.txt
   ```

## Configuration
### Configuration is managed in conftest.py.

## Running Tests
To execute the tests, run the following command:

   ```
   pytest --html=reports/report.html
   ```

## Viewing Reports
After the tests have run, you can view the detailed report by opening reports/report.html in your web browser.

## Writing Tests
Tests should be written in the tests/ directory.

## Dependencies
### Dev Dependencies
pytest: Testing framework
pytest-html: HTML reporting plugin
selenium: Browser automation library
faker: Library for generating fake data

## License
This project is licensed under the ISC License.

## Author
Elmar Yusifli

## Contributing
Contributions are welcome! Please feel free to submit a Pull Request.
