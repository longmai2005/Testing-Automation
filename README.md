# Selenium Python Test Automation Example

A test automation project using Selenium WebDriver with Python and the Page Object Model (POM) design pattern.

## Project Overview

This project demonstrates automated testing of a web application using Selenium WebDriver. It follows the Page Object Model pattern to create maintainable and reusable test code.

## Project Structure

```
selenium-python-example/
├── test_login.py           # Test cases for login functionality
├── pages/                  # Page Object Model classes
│   ├── login_page.py      # Login page object
│   └── home_page.py       # Home page object
└── README.md
```

## Features

- **Page Object Model (POM)**: Separates page elements and actions from test logic
- **Python unittest**: Uses Python's built-in unittest framework
- **Selenium WebDriver**: Automates browser interactions
- **Modular Design**: Reusable page objects for easy maintenance

## Prerequisites

- Python 3.x
- Google Chrome browser
- ChromeDriver (matching your Chrome version)

## Installation

1. Clone this repository:
```bash
git clone https://bitbucket.org/agestvn/vnuk-2025
cd selenium-python-example
```

2. Install required packages:
```bash
pip install selenium
```

## Usage

Run the test suite:
```bash
python test_login.py
```

Or using unittest:
```bash
python -m unittest test_login.py
```

Run with verbose output:
```bash
python -m unittest test_login.py -v
```

## Test Cases

### `test_login.py`
- **TestCase01**: Tests the login functionality
  - Navigates to the application home page
  - Clicks on the login link
  - Enters valid credentials
  - Verifies successful login with welcome message

## Page Objects

### `HomePage`
Represents the application's home page with methods:
- `go_to_login_page()`: Navigates to the login page
- `get_welcome_msg()`: Returns the welcome message text

### `LoginPage`
Represents the login page with methods:
- `enter_email(email)`: Enters email in the username field
- `enter_password(password)`: Enters password
- `click_login_btn()`: Clicks the login button
- `login(username, password)`: Performs complete login action

## Configuration

- **Test URL**: `http://railwayb1.somee.com/`
- **Browser**: Chrome (configured in `setUp()` method)

## Best Practices

This project demonstrates several automation best practices:
- Separation of concerns using POM pattern
- Reusable page object methods
- Clear test structure with setup and teardown
- Explicit waits (currently using temporary sleep - can be improved with WebDriverWait)
- Scroll into view before clicking elements

## Future Improvements

- [ ] Replace `sleep()` with explicit WebDriverWait
- [ ] Add configuration file for test data and URLs
- [ ] Implement logging for better debugging
- [ ] Add more test cases
- [ ] Add screenshots on test failure
- [ ] Support for multiple browsers
- [ ] Generate HTML test reports

## Contributing

Feel free to fork this project and submit pull requests for improvements.

## License

This project is for educational purposes.
