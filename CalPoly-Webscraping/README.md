# CalpolyWebscraping

- Here's a step-by-step guide for to set up a virtual environment and run your firefox driver web scraper:

### Complete Instructions to Run the Scraper

1. **Clone the Repository or Download the Files:**
   - In the terminal run the following command to clone the repo:
   - `git clone https://github.com/Castro19/CalpolyWebscraping.git`
   - Ensure you have the `scrapeAllClubs.py` file and the `requirements.txt` file in a directory on your local machine.

2. **Install Python:**

   Make sure Python is installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

3. **Install Firefox Browser:**

   Download and install Firefox from [mozilla.org](https://www.mozilla.org/firefox/new/)

4. **Install Firefox WebDriver (geckodriver):** [OPTIONAL - ONLY DO IF THIS IS NOT WORKING]

   - **On Windows:**

     - Download geckodriver from [Mozilla's GitHub](https://github.com/mozilla/geckodriver/releases)
     - Extract the downloaded file
     - Add the geckodriver location to your system's PATH environment variable
     - Or place the geckodriver.exe in your Python Scripts directory

   - **On macOS:**

     ```bash
     brew install geckodriver
     ```

   - **On Ubuntu/Debian:**
     ```bash
     sudo apt install firefox-geckodriver
     ```

5. **Open a Terminal or Command Prompt:**

   Navigate to the directory where your files are located.

6. **Create a Virtual Environment:**

   ```bash
   python3 -m venv venv
   ```

7. **Activate the Virtual Environment:**

   - **On macOS and Linux:**

     ```bash
     source venv/bin/activate
     ```

   - **On Windows:**
     ```bash
     .\venv\Scripts\activate
     ```

8. **Install Required Packages:**

   ```bash
   pip install -r requirements.txt
   ```

   Note: The `webdriver-manager` package included in the requirements will actually handle the geckodriver installation automatically, making step 4 optional. However, it's good to know how to install it manually if needed.

9. **Run the Scraper:**

   ```bash
   python scrapeAllClubs.py
   ```

10. **Deactivate the Virtual Environment (Optional):**

    ```bash
    deactivate
    ```

### Troubleshooting

If you encounter any WebDriver-related errors:

1. **Verify Firefox Installation:**

   - Make sure Firefox is properly installed
   - Check Firefox version compatibility with geckodriver

2. **Check WebDriver Installation:**

   ```python
   from selenium import webdriver
   from webdriver_manager.firefox import GeckoDriverManager

   # This line should automatically download and setup geckodriver
   driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
   ```

3. **Common Issues:**
   - If you get a "geckodriver" not found error, ensure it's in your system PATH
   - If you get permission errors on Linux/macOS, you might need to run:
     ```bash
     chmod +x /path/to/geckodriver
     ```

The `webdriver-manager` package in your script should handle most of the WebDriver setup automatically, but it's good to know the manual process in case you need to troubleshoot any issues.
