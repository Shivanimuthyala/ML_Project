import time
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By

def collect_game_data(driver, writer, category):
    games = driver.find_elements(By.XPATH, "(//a[@class='Si6A0c Gy4nib'])")
    for game in games:
        game.click()
        time.sleep(10)

        Name = driver.find_element(by=By.XPATH, value="//h1[@itemprop='name']").text
        Downloads = driver.find_element(by=By.XPATH, value="//div[@class='wVqUob'][2]/div[1]").text
        phn_rating = driver.find_element(by=By.XPATH, value="//div[@class='jILTFe']").text
        phn_review = driver.find_element(by=By.XPATH, value="//div[@class='EHUI5b']").text
        phn_review_count = phn_review.split()[0]
        tab_button = driver.find_element(By.XPATH, "//div[@id='formFactor_3']")
        tab_button.click()
        time.sleep(15)
        tab_rating = driver.find_element(by=By.XPATH, value="//div[@class='jILTFe']").text
        tab_review = driver.find_element(by=By.XPATH, value="//div[@class='EHUI5b']").text
        tab_review_count = tab_review.split()[0]
        Age_group = driver.find_element(by=By.XPATH, value="//span[@itemprop='contentRating']").text

        ads = "1" if driver.find_elements(By.XPATH, "//span[contains(text(), 'Contains ads')]") else "0"
        iap = "1" if driver.find_elements(By.XPATH, "//span[contains(text(), 'In-app purchases')]") else "0"
        game_type = category
        online = "1" if driver.find_elements(By.XPATH, "//span[contains(text(), 'Online')]") else "0"
        single_player = "1" if driver.find_elements(By.XPATH, "//span[contains(text(), 'Single player')]") else "0"
        logic = "1" if driver.find_elements(By.XPATH, "//span[contains(text(), 'Logic')]") else "0"
        Realistic = "1" if driver.find_elements(By.XPATH, "//span[contains(text(), 'Realistic')]") else "0"
        stylized = "1" if driver.find_elements(By.XPATH, "//span[contains(text(), 'Stylized')]") else "0"
        cartoon = "1" if driver.find_elements(By.XPATH, "//span[contains(text(), 'Cartoon')]") else "0"
        writer.writerow([Name, Downloads, phn_rating, phn_review_count, tab_rating, tab_review_count, Age_group, ads, iap, game_type, online,
                         single_player, logic, Realistic, stylized, cartoon])
        driver.back()
        time.sleep(5)

driver = webdriver.Chrome()

with open('puzzle_games_data.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(["Game Name", "Downloads", "phone-Rating", "phone-reviews", "tab-Rating", "tab-reviews",
                     "Age Group", "Contains Ads", "In-app Purchases", "Category", "Online",
                     "Single Player", "Logic", "Realistic", "Stylized", "Cartoon"])

    driver.get("https://play.google.com/store/search?q=puzzle%20games&c=apps&hl=en&gl=US")
    time.sleep(10)
    collect_game_data(driver, writer, "Puzzle")

    driver.get("https://play.google.com/store/search?q=adventure%20games&c=apps&hl=en&gl=US")
    time.sleep(10)
    collect_game_data(driver, writer, "Adventure")

    driver.get("https://play.google.com/store/search?q=board%20games&c=apps&hl=en&gl=US")
    time.sleep(10)
    collect_game_data(driver, writer, "Board")

driver.quit()
