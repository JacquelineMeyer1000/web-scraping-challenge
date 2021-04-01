# Import Dependecies 
from splinter import Browser
from bs4 import BeautifulSoup as bs
import pandas as pd 
import requests 
import time
from webdriver_manager.chrome import ChromeDriverManager

def init_browser():
    # Set up Splinter
    executable_path = {'executable_path': ChromeDriverManager().install()}
    return Browser('chrome', **executable_path, headless=False)

def scrape():

    # Empty dictionary
    mars_info = {}

    # Initialize browser 
    browser = init_browser()
    time.sleep(2)

    # HTML Object & Parse HTML with Beautiful Soup
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    # Nasa Mars news 
    news_url = 'https://redplanetscience.com/'
    browser.visit(news_url)

    news_title = soup.find('div', class_='content_title').text
    news_paragraph = soup.find('div', class_='article_teaser_body').text

    mars_info['news_title'] = news_title
    mars_info['news_paragraph'] = news_paragraph

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

        # HTML Object
        html_hemispheres = browser.html

        # Parse HTML with Beautiful Soup
        soup = BeautifulSoup(html_hemispheres, 'html.parser')

        # Retreive all items that contain mars hemispheres information
        items = soup.find_all('div', class_='item')

        # Create empty list for hemisphere urls 
        hiu = []

        # Loop through the items previously stored
        for i in items: 
            # Store title
            title = i.find('h3').text
            
            # Store link that leads to full image website
            partial_img_url = i.find('a', class_='itemLink product-item')['href']
            
            # Visit the link that contains the full image website 
            browser.visit(url + partial_img_url)
            
            # HTML Object of individual hemisphere information website 
            partial_img_html = browser.html
            
            # Parse HTML with Beautiful Soup for every individual hemisphere information website 
            soup = BeautifulSoup( partial_img_html, 'html.parser')
            
            # Retrieve full image source 
            img_url = url + soup.find('img', class_='wide-image')['src']
            
            # Append the retreived information into a list of dictionaries 
            hiu.append({"title" : title, "img_url" : img_url})

        mars_info['hiu'] = hiu
        
        # Close the browser after scraping
        browser.quit()
        
        # Return mars_data dictionary
        return mars_info

        