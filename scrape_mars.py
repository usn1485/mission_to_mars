from splinter import Browser
from bs4 import BeautifulSoup as bs
import pandas as pd


def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
     executable_path = {'executable_path': 'chromedriver.exe'}
     browser = Browser('chrome', **executable_path, headless=False)
     return browser

mars_data= {}
def mars_news_scrape():
     browser = init_browser()
    #Visit Nasa News url  using splinter module

     Nasa_url = 'https://mars.nasa.gov/news/'
     browser.visit(Nasa_url)
     #create HTMl Object
     html = browser.html
     #parse HTML with beautiful soup
     Nasa_soup = bs(html, 'html.parser')

     # Extract title text
     nasa_news_title = Nasa_soup.find('div',class_='content_title').find('a').text
     print(f"title {nasa_news_title}")
     mars_data['nasa_news_title']=nasa_news_title
     # Extract Paragraph text
     nasa_news_paragraph=Nasa_soup.find('div',class_='article_teaser_body').text
     mars_data['nasa_news_paragraph'] = nasa_news_paragraph
     #print(nasa_news_paragraph)
     print(f"paragraph {nasa_news_paragraph}")

     return mars_data
     
def img_scrape():
     browser = init_browser()
     #Visit Nasa's JPL Mars Space url  using splinter module
     jplNasa_url='https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
     browser.visit(jplNasa_url)
     #create HTML object
     html = browser.html
     soup = bs(html, 'html.parser')

     #get base Nasa link
     main_url ='https://www.jpl.nasa.gov'
     #get image url from the soup object.
     featured_image_url = soup.find('article')['style'].replace('background-image: url(','').replace(');', '')[1:-1]

     #Create one full image url link
     full_image_url=main_url+featured_image_url
     mars_data['full_image_url']= full_image_url
     print(full_image_url )     

     return mars_data


def mars_weather():
     browser = init_browser()
     #Visit the Mars Weather twitter account
     Tweet_url='https://twitter.com/marswxreport?lang=en'
     # Retrieve page with the requests module
     browser.visit(Tweet_url)
     #create HTML object
     html=browser.html
     twit_soup=bs(html,'html.parser')

     # Extract title text
     mars_data['mars_weather'] = twit_soup.find('p',class_='TweetTextSize').text
     #print('mars_weather = '+ mars_weather.text)
     return mars_data

def mars_facts():
     # Visit the Mars Facts webpage
     mars_facts_url='https://space-facts.com/mars/'
     mars_fact_table=pd.read_html(mars_facts_url)

     #Create Dataframe to store table data
     df = mars_fact_table[0]
     df.columns = ['Mars-Earth Comparison', 'Mars', 'Earth']
     mars_facts = df.to_html()
     mars_data['mars_facts'] = mars_facts
     return mars_data


def mars_hem():

     browser = init_browser()
     # Visit the Mars Facts webpage
    # Visit the USGS Astrogeology site
     USGS_url="https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
     short_url="https://astrogeology.usgs.gov"

     browser.visit(USGS_url)
     html = browser.html
     soup = bs(html, 'html.parser')
     main_url = soup.find_all('div', class_='item')
     
     hemisphere_img_urls=[]      
     for x in main_url:
          title = x.find('h3').text
          url = x.find('a')['href']
          hem_img_url= short_url+url
          #print(hem_img_url)
          browser.visit(hem_img_url)
          html = browser.html
          soup = bs(html, 'html.parser')
          hemisphere_img_original= soup.find('div',class_='downloads')
          hemisphere_img_url=hemisphere_img_original.find('a')['href']
          
          print(hemisphere_img_url)
          img_data=dict({'title':title, 'img_url':hemisphere_img_url})
          hemisphere_img_urls.append(img_data)
     mars_data['hemisphere_img_urls']=hemisphere_img_urls
     return mars_data