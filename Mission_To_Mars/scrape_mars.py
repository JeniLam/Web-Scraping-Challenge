from splinter import Browser
from bs4 import BeautifulSoup as bs
from webdriver_manager.chrome import ChromeDriverManager

def init_browser():
    executable_path = {"executable_path": ChromeDriverManager().install()}
    return Browser("chrome", **executable_path, headless=False)

def scrape():
    browser=init_browser()
    mars_dict{}
    ## Mars News
    mars_news_url = 'https://mars.nasa.gov/news/'
    browser.visit(mars_news_url)
    html = browser.html
    soup = bs(html, 'html.parser')

    # Retriece all elements that contain news title
    news = soup.find_all('div', class_='list_text')

    # use news variable to get the latest news
    latest_news = news [0]

    # grab title and paragraph text
    latest_news_title = latest_news.find('div', class_='content_title').text
    latest_news_paragraph = latest_news.find('div', class_="article_teaser_body").text

    ## JPL Mars Space Images
    jpl_img_url ='https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(jpl_img_url)
    jpl_img_url ='https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(jpl_img_url)
    image_url = soup.find('section', class_='main_feature').a['data-fancybox-href']
    featured_image_url = 'https://www.jpl.nasa.gov/' + image_url

    ## Mars Facts
    mars_facts_url = 'https://space-facts.com/mars'
    mars_facts_table = pd.read_html(mars_facts_url)

    # convert to dataframe
    mars_facts_df = mars_facts_table[0]
    mars_facts_df = mars_facts_df.rename(columns={0:"Mars Profile", 1 : " "})

    # reset index to first column
    mars_facts_df = mars_facts_df.set_index('Mars Profile')

    # Convert df to html
    mars_facts_html = mars_facts_df.to_html()

    # Strip unwanted newlines to cleanup table
    mars_facts_html.replace('\n', '')

    ## Mars Hemispheres


    mars_dict ={
        "Latest News Title" : latest_news_title,
        "Latest News Paragraph": latest_news_paragraph,
        "Featured Image URL": featured_image_url,
        "Mars Fact Table": mars_facts_html,
    }

    # Close the browser after scraping
    browser.quit()
    
     # Return results
    return mars_dict