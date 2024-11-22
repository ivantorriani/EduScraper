from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
import json
from webdriver_manager.firefox import GeckoDriverManager
import time # Set a delat if you notice the website is blocking you are grabbing elements too quickly (before they have time to load)
import random
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

options = Options()
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")
options.headless = False

# Initialize the WebDriver with geckodriver
driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()), options=options)

# Read the hrefs to a JSON file
with open('hrefs.json', 'r') as json_file:
    hrefs = json.load(json_file)

with open('clubs.json', 'r') as file:
    clubs = json.load(file)


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 


for href in hrefs:
    
    driver.get(href)


    # General Info - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
    try:
        club_name = driver.find_element(By.CSS_SELECTOR, 'div[style*="min-height: 90px;"] h1').text
        club_description = driver.find_element(By.CSS_SELECTOR, 'div.bodyText-large.userSupplied').text

    except Exception as error:
        club_name = "N/A"
        club_description = "N/A"
    try:
        club_url = str(href)
    except Exception as error:
        club_url = "N/A"

    try:
        temp_email = driver.find_element(By.XPATH, "//div[span[@class='sr-only' and text()='Contact Email']]").text
        club_email = temp_email.split("E: ")[-1].strip()
    except Exception as error:
        club_email = "N/A"
        temp_email = "N/A"

    # Social Links - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
    links = driver.find_elements(By.XPATH, "//div/a[@href]")
    link_list = [link.get_attribute("href") for link in links]
    instagram_link = next((link for link in link_list if "instagram.com" in link), None)
    linkedin_link = next((link for link in link_list if "linkedin.com" in link), None)
    facebook_link = next((link for link in link_list if "facebook.com" in link), None)
    youtube_link = next((link for link in link_list if "youtube.com" in link), None)

    # Contact Information - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
    try: 
        contact_link_elements = driver.find_elements(By.XPATH, "//a[contains(@class, 'MuiButton-root') and contains(@aria-label, 'Contact')]")
        contact_links = [element.get_attribute('href') for element in contact_link_elements]
    except Exception as error:
        contact_link_elements = "N/A"
        contact_links = "N/A"

    #Additonal  Information - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
    try:
        download_link_element = driver.find_element(By.XPATH, "//a[contains(@aria-label, 'download')]")
        download_link = download_link_element.get_attribute('href')
    except Exception as error:
        download_link_element = "N/A"
        download_link = "N/A"

    #Events - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

    events = []

    event_names = driver.find_elements(By.CSS_SELECTOR, 'h3[style*="font-size: 1.06rem;"][style*="font-weight: 600;"][style*="max-width: 400px;"][style*="-webkit-line-clamp: 2;"]')
    event_names_text = [event.text for event in event_names] 

    event_times = driver.find_elements(By.CSS_SELECTOR, 'div[style="margin: 0px 0px 0.125rem;"]')
    event_times_text = [time.text for time in event_times]

    event_locations = driver.find_elements(By.CSS_SELECTOR, 'div[style="margin: 0px 0px 0.125rem;"] + div')
    event_locations_text = [location.text for location in event_locations]

    for name, time, location in zip(event_names_text, event_times_text, event_locations_text):

        events.append({
            "event_name": name,
            "event_time": time,
            "event_location": location
        })

    entry = {
        "club_name": str(club_name),
        "club_description": str(club_description),
        "club_url": str(club_url),

        "contact_information": { 
            "email": str(club_email)

        },

        "social_links":{
            "instagram": str(instagram_link),
            "facebook": str(facebook_link),
            "linkedin": str(linkedin_link),
            "youtube": str(youtube_link)
        },

        "join_link": str(contact_links),

        "additional_information":{
            "bylaws": str(download_link)
        },

        "events": events
            
        }

    clubs.append(entry)

with open('clubs.json', 'w') as file: 
    json.dump(clubs, file, indent = 4)
