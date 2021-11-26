#bs4 is a python module, which is famously used for parsing the text as HTML and
#  then perfroming the actions and finding specific HTML tags with
#  a particular class/id, or listing out all the li tags inside the ul tags

#Selenium is used to interact with the webpage.
#It is famously used for automation testing,
#such as testing funcionality of a wedsite (login/out/.....) ,can also be used 
# to interact with the page such as clicking a button....

# import the desired modules
from selenium import webdriver # selenium opens the webpage in a browser
from bs4 import BeautifulSoup
import time #to make our code sleep for some time , so that the web page could load properly before we start scraping
import csv # export the data that we scrape into csv


START_URL = "https://exoplanets.nasa.gov/exoplanet-catalog/" 
browser = webdriver.Chrome(executable_path=r"C:\Users\monika\Desktop\python\class127\chromedriver")
browser.get(START_URL)
time.sleep(10)
def scrape():
    headers = ["name", "light_years_from_earth", "planet_mass", "stellar_magnitude", "discovery_date"]
    planet_data = []
    for i in range(0, 428):
        soup = BeautifulSoup(browser.page_source, "html.parser")
        #Earlier , the chrome window we opened with the selenium, 
        # we named it as browser . now we r creating a beautifulSoup object
        #  where we are passing the browser's page source and 
        # asking our bs4 to use html parsing in it, which means 
        # it will read the page as an HTML
        for ul_tag in soup.find_all("ul", attrs={"class", "exoplanet"}):
            #next we are creating a for loop to iterate over all the
            #  ul tags inside meaning that it will find all the ul tags 
            # with class exoplanet
            li_tags = ul_tag.find_all("li")
            # now all we have to do is to iterate over these li tags and 
            # fetch the data,create a temporary list and then finally 
            # append that list into the planet_data list that we created earlier.
            # lets inspect the li tags a bit deeper.
            temp_list = []
            for index, li_tag in enumerate(li_tags):
                if index == 0:
                    temp_list.append(li_tag.find_all("a")[0].contents[0])
                else:
                    try:
                        temp_list.append(li_tag.contents[0])
                    except:
                        temp_list.append("")
            planet_data.append(temp_list)
        browser.find_element_by_xpath('/html/body/div[2]/div/div[3]/section[2]/div/section[2]/div/div/article/div/div[2]/footer/div/div/div/nav/span[2]/a').click()
    with open("test.csv", "w") as f:
        csvwriter = csv.writer(f)
        csvwriter.writerow(headers)
        csvwriter.writerows(planet_data)
scrape()