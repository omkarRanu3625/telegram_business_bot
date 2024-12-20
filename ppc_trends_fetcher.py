import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def fetch_ppc_trends(industry, ad_type="Google Ads CTR"):
    # Set up Chrome WebDriver options
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run Chrome in headless mode for automation

    # Set the path to your WebDriver executable
    driver_path = 'C:\WebDriver\chromedriver-win64\chromedriver.exe'  # Update this with the correct path
    service = Service(driver_path)
    
    # Create a new instance of Chrome WebDriver
    driver = webdriver.Chrome(service=service, options=chrome_options)

    # Navigate to the PPC Industry Benchmarks page
    url = "https://databox.com/ppc-industry-benchmarks"
    driver.get(url)

    # Wait for the page to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//button[contains(text(), 'CTR')]")))

    try:
        # Click on the "CTR" tab to reveal different CTR options (Google Ads, Facebook Ads, LinkedIn Ads)
        ctr_tab = driver.find_element(By.XPATH, "//button[contains(text(), 'CTR')]")
        ctr_tab.click()

        # Wait for the specific ad type to be available and click on it
        ad_type_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, f"//span[contains(text(), '{ad_type}')]"))
        )
        ad_type_button.click()

        # Wait for the data to load
        time.sleep(5)

        # Scrape the data from the table for the selected industry
        rows = driver.find_elements(By.XPATH, "//table/tbody/tr")
        trends = {}
        for row in rows:
            columns = row.find_elements(By.TAG_NAME, "td")
            
            if len(columns) > 1:
                industry_name = columns[0].text.strip().lower()
                # Get the CTR value, removing extra <strong> tags
                ctr_value = columns[1].find_element(By.TAG_NAME, "strong").text.strip()
                
                if industry_name == industry.lower():
                    trends['Industry'] = industry_name.capitalize()
                    trends['CTR'] = ctr_value
                    break
        else:
            trends = f"Industry '{industry}' not found in the benchmark table for {ad_type}."

    except Exception as e:
        trends = f"An error occurred: {str(e)}"

    finally:
        # Close the browser
        driver.quit()

    return trends

# Example usage:
industry = "apparel & footwear"
trend_data = fetch_ppc_trends(industry)
print(trend_data)
