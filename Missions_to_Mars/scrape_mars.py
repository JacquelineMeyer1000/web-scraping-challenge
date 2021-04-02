# Import Dependecies 
from splinter import Browser
from bs4 import BeautifulSoup as bs
import pandas as pd 
import requests 
import time
from webdriver_manager.chrome import ChromeDriverManager

def scrape_info():
    # Set up Splinter
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    # Nasa Mars news 
    news_url = 'https://redplanetscience.com/'
    browser.visit(news_url)
    time.sleep(2)

    html = browser.html
    soup = bs(html, 'html.parser')

    news_title = soup.find('div', class_='content_title').text
    news_paragraph = soup.find('div', class_='article_teaser_body').text

    # # Mars facts url 
    # facts_url = 'https://galaxyfacts-mars.com/'

    # tables = pd.read_html(facts_url)
    # df = tables[1]
    # df.columns = ["Facts", "Value"]
    # df.set_index(["Facts"])
    # html_table = df.to_html()
    # html_table = html_table.replace("\n","")

    # mars_info['tables'] = html_table

    # # Hemispheres website  
    # hemispheres_url = 'https://marshemispheres.com/'
    # browser.visit(hemispheres_url)
    # time.sleep(2)

    # html_hemispheres = browser.html
    # soup = bs(html_hemispheres, 'html.parser')

    # results = soup.find_all('div', class_='item')
    # hiu = []

    # # Loop through the items previously stored
    # for x in results: 
    #     # Store title
    #     title = x.find('h3').text
            
    #     # Store link that leads to full image website
    #     partial_img_url = x.find('a', class_='itemLink product-item')['href']
            
    #     # Visit the link that contains the full image website 
    #     browser.visit(url + partial_img_url)
            
    #     # HTML Object of individual hemisphere information website 
    #     partial_img_html = browser.html
            
    #     # Parse HTML with Beautiful Soup for every individual hemisphere information website 
    #     soup = BeautifulSoup( partial_img_html, 'html.parser')
            
    #     # Retrieve full image source 
    #     img_url = url + soup.find('img', class_='wide-image')['src']
            
    #     # Append the retreived information into a list of dictionaries 
    #     hiu.append({"title" : title, "img_url" : img_url})

    #     mars_info['hiu'] = hiu
    
    # Create dictionary
    mars_info = {
		'news_title' : news_title,
		'news_paragraph': news_paragraph,
        # 'featured_image': feature_url,
		# 'featured_image_title': featured_image_title,
		# 'fact_table': html_table,
		# 'hemisphere_image_urls': hemisphere_image_urls,
        # 'news_url': news_url,
        # 'jpl_url': jurl,
        # 'weather_url': turl,
        # 'fact_url': murl,
        # 'hemisphere_url': mhurl,
        }
    
       
    browser.quit()
  
    # Return mars_data dictionary
    return mars_info

        