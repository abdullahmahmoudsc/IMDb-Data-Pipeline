from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd
driver = webdriver.Edge()
driver.get("https://www.imdb.com/chart/top/?ref_=hm_nv_menu")

time.sleep(20)

movie_Name = driver.find_elements(
    By.XPATH,
    '//ul/div/a[@class="ipc-title-link-wrapper"]'
)
movie_Year = driver.find_elements(
    By.XPATH,
    '//div[contains(@class, "cli-title-metadata")]//li[1]'
)
movie_Runtime = driver.find_elements(
    By.XPATH,
    '//div[contains(@class, "cli-title-metadata")]//li[2]'
)
movie_Rate = driver.find_elements(
    By.XPATH,
    '//span[@class="ipc-rating-star ipc-rating-star--base ipc-rating-star--imdb ratingGroup--imdb-rating"]/span[@class = "ipc-rating-star--rating"]'
)

movie_Votes = driver.find_elements(
    By.XPATH,
    '//span[@class="ipc-rating-star--voteCount"]'
)
movie_Name = [movie.text for movie in movie_Name]
movie_Year = [movie.text for movie in movie_Year]
movie_Runtime = [movie.text for movie in movie_Runtime]
movie_Rate = [movie.text for movie in movie_Rate]
movie_Votes = [movie.text for movie in movie_Votes]

data = {
    "Name": movie_Name,
    "Year": movie_Year,
    "Runtime": movie_Runtime,
    "Rate": movie_Rate,
    "Votes": movie_Votes
}

df = pd.DataFrame(data)

print(df.head())
df.to_csv("data/imdb_raw.csv", index=False)