from splinter import Browser
from bs4 import BeautifulSoup as bs
import time


def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
     executable_path = {'executable_path': 'chromedriver.exe'}
     return Browser("chrome", **executable_path, headless=False)

#Nasa Mars News
def nasa_mars_scrape():
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
    
    # Extract Paragraph text
    nasa_news_paragraph=Nasa_soup.find('div',class_='article_teaser_body').text
    
    #Store Data into a dictionary
    Nasa_mars_news={"title":nasa_news_title, "paragraph:":nasa_news_paragraph}

    # Close the browser after scraping
    browser.quit()
    #return results
    return Nasa_mars_news

#JPL Mars Image
def jpl_mars_img():
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
    featured_image_url=main_url+featured_image_url
    return featured_image_url 

