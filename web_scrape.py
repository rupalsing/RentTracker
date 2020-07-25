import os
import time
from bs4 import BeautifulSoup
from selenium import webdriver

options = webdriver.ChromeOptions()
# options.add_argument('--ignore-certificate-errors')
# options.add_argument('--incognito')
# options.add_argument('--headless')
# options.add_argument('--disable-gpu')
# options.add_argument('--no-sandbox')

# options.binary_location = os.environ.get("GOOGLE_CHROME_BIN", None)
# driver = webdriver.Chrome(chrome_options=options)


driver = webdriver.Chrome("./chromedriver", options=options)


def load_page(url):
    driver.get(url)


def get_source():
    return driver.page_source


def load_page_and_get_source(url):
    load_page(url)
    return get_source()


def click_button_and_refresh_soup(button_selector):
    global soup
    for i in driver.find_elements_by_css_selector(button_selector):
        i.click()
    soup = BeautifulSoup(get_source(), 'html.parser')


# quote_page = "https://www.daft.ie/westmeath/houses-for-rent/athlone/st-patricks-terrace-athlone-westmeath-2049596/"
quote_page = "https://www.daft.ie/westmeath/apartments-for-rent/athlone/kilmacoo-lane-dublin-road-athlone-westmeath-2034037/"
soup = BeautifulSoup(load_page_and_get_source(quote_page), 'html.parser')

rent = soup.select_one(
    'body > div.PropertyDetailsPage__rootContainer > div > div.PropertyDetailsPage_'
    '_propertyDetailsSmallContainer > div > section.Section__container.PropertyMainInformation__'
    'noTopPadding > div.PropertyInformationCommonStyles__propertyPrice > strong').text

map_ele = soup.select_one('#LaunchStreet')
situation = str(map_ele.attrs['href']).split('viewpoint=')[1].split(',')
latitude = situation[0]
longitude = situation[1]

title_ele = soup.select_one('body > div.PropertyDetailsPage__rootConta'
                            'iner > div > div.PropertyDetailsPage__propertyDetailsS'
                            'mallContainer > div > section.Section__container.Property'
                            'MainInformation__noTopPadding > h1').text

description = soup.select_one('body > div.PropertyDetailsPage__rootContainer > div > div.PropertyDet'
                              'ailsPage__propertyDetailsSmallContainer > div > section:nth-child(5) > p').text.strip()

property_overview = soup.select_one('body > div.PropertyDetailsPage__rootContainer > div > div.Propert'
                                    'yDetailsPage__propert'
                                    'yDetailsSmallContainer > div > section:nth-child(4) > div.PropertyOverview_'
                                    '_propertyOverviewDetails > div:nth-child(1)').text + '\n' + \
                    soup.select_one('body > div.PropertyDetailsPage__rootContainer > div > '
                                    'div.PropertyDetailsPage__propertyDetailsSmallContainer > '
                                    'div > section:nth-child(4) > div.PropertyOverview__propertyOverviewDetails > '
                                    'div:nth-child(2)').text

lease = soup.select_one('body > div.PropertyDetailsPage__rootContainer > div > '
                        'div.PropertyDetailsPage__propertyDetailsSmallContainer > div >'
                        ' section:nth-child(4) > div.PropertyOverview__propertyOverviewDetails >'
                        ' div.PropertyOvervi'
                        'ew__availability > div').text.split('Lease: ')[1]

facilities = soup.select_one('body > div.PropertyDetailsPage__rootContainer > '
                             'div > div.PropertyDetailsPage__propertyDetailsSmallContainer > '
                             'div > section:nth-child(6) > ul')

list_of_facilities = [element.text for element in facilities.select('.PropertyFacilities__iconText')]

click_button_and_refresh_soup('#property-contact-form > button.Contact'
                              'Form__secondaryButton.ContactForm__baseButton')

phone = [ele.text.split("Call ")[1] for ele in soup.select('#property-contact-form > b'
                                                           'utton.ContactForm__secondaryButton.Cont'
                                                           'actForm__baseButton')]

print("Title>>>")
print(title_ele)
print()
print("Rent>>>")
print(rent)
print()
print("Overview>>>")
print(property_overview)
print()
print("Lease>>>")
print(lease)
print()
print("Lat Long>>>")
print(latitude, longitude)
print()
print("Description>>>")
print(description)
print()
print("Facilities>>>")
print(list_of_facilities)
print()
print("Phone>>>")
print(phone)
print()

driver.close()
