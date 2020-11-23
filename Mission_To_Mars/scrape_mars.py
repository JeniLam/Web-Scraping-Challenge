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
    main_url = 'https://astrogeology.usgs.gov'
    mars_hemis_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(mars_hemis_url)
    html = browser.html
    soup = bs(html, 'html.parser')
    imgs_titles = soup.find_all('div', class_="item")
    hem_title_image_urls = []
    main_url = 'https://astrogeology.usgs.gov'
    # https://www.w3schools.com/python/trypython.asp?filename=demo_ref_string_replace
    for item in imgs_titles:
    #get titles
        title = item.find('h3').text
        title = title.replace('Enhanced', "")
        
        
        # get link that leads to full res image
        start_url=item.find('a', class_='itemLink product-item')['href']
        
        
        #go to individual mars hemisphere page
        browser.visit(main_url + start_url)
    #     https://splinter.readthedocs.io/en/latest/matchers.html
        browser.is_element_present_by_css('.downloads',wait_time = 5)
        
        #now at individual hemisphere page to grap full res image
        image_html = browser.html
        
        #parse with BeautifulSoup
        soup = bs(image_html,'html.parser')
        
        #get full res image source
        fullRes_image = soup.find('div', class_='downloads')
        fullRes_url = fullRes_image.find('li').find('a')['href']
        

        #append into a list of dictionaries
        hemImageUrl_dict = {}
        hemImageUrl_dict['title'] = title
        hemImageUrl_dict['fullResImg_url'] = fullRes_url
        hem_title_image_urls.append(hemImageUrl_dict)


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