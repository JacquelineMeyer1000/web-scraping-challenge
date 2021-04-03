# Import Dependecies 
from splinter import Browser
from bs4 import BeautifulSoup as bs
import pandas as pd 
import requests 
import time
from webdriver_manager.chrome import ChromeDriverManager

def scrape():
    # Set up Splinter
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

     # Create empty dictionary
    mars_info = {}

    # Nasa Mars news 
    news_url = 'https://redplanetscience.com/'
    browser.visit(news_url)
    time.sleep(2)

    html = browser.html
    soup = bs(html, 'html.parser')

    mars_info["news_title"] = soup.find('div', class_='content_title').text
    mars_info["news_paragraph"] = soup.find('div', class_='article_teaser_body').text

    # Mars Feature Image
    url_feature_image = "https://spaceimages-mars.com/"
    browser.visit(url_feature_image)
    time.sleep(2)

    html = browser.html
    soup = bs(html, 'html.parser')
    
    img_url = soup.find('img', class_='headerimage fade-in')
    featured_image_url = str(url_feature_image) + str("image/featured/mars2.jpg")

    mars_info["featured_image_url"] = featured_image_url

    # Mars facts url 
    facts_url = 'https://galaxyfacts-mars.com/'

    tables = pd.read_html(facts_url)
    df = tables[1]
    df.columns = ["Facts", "Value"]
    df.set_index(["Facts"])
    html_table = df.to_html()
    html_table = html_table.replace("\n","")

    mars_info['tables'] = html_table

    # Hemispheres website  
    hemispheres_url = 'https://marshemispheres.com/'
    browser.visit(hemispheres_url)
    time.sleep(2)

    html_hemispheres = browser.html
    soup = bs(html_hemispheres, 'html.parser')

    results = soup.find_all('div', class_='item')
    hiu = []

    # Loop through the items previously stored
    for x in results: 
        
        title = x.find('h3').text
        partial_img_url = x.find('a', class_='itemLink product-item')['href']
        browser.visit(hemispheres_url + partial_img_url)
        partial_img_html = browser.html 
        soup = bs( partial_img_html, 'html.parser')
        img_url = hemispheres_url + soup.find('img', class_='wide-image')['src']
        hiu.append({"title" : title, "img_url" : img_url})

        mars_info['hiu'] = hiu
     
       
    browser.quit()
  
    # Return mars_data dictionary
    return mars_info

        