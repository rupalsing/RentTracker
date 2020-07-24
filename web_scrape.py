import os
from urllib.request import urlopen
from bs4 import BeautifulSoup
from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--incognito')
options.add_argument('--headless')

options.binary_location = os.environ.get("GOOGLE_CHROME_SHIM", None)
driver = webdriver.Chrome(chrome_options=options)

# driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver", chrome_options=options)

driver.get("www.google.com")

# quote_page = "https://www.daft.ie/westmeath/houses-for-rent/athlone/st-patricks-terrace-athlone-westmeath-2049596/"
# page = urlopen(quote_page)
# soup = BeautifulSoup(page, 'html.parser')
#
# rent = soup.select_one(
#     'body > div.PropertyDetailsPage__rootContainer > div > div.PropertyDetailsPage_'
#     '_propertyDetailsSmallContainer > div > section.Section__container.PropertyMainInformation__'
#     'noTopPadding > div.PropertyInformationCommonStyles__propertyPrice > strong').text
#
# map_ele = soup.select_one('#LaunchStreet')
# situation = str(map_ele.attrs['href']).split('viewpoint=')[1].split(',')
# latitude = situation[0]
# longitude = situation[1]
#
# title_ele = soup.select_one('body > div.PropertyDetailsPage__rootConta'
#                             'iner > div > div.PropertyDetailsPage__propertyDetailsS'
#                             'mallContainer > div > section.Section__container.Property'
#                             'MainInformation__noTopPadding > h1').text
#
# description = soup.select_one('body > div.PropertyDetailsPage__rootContainer > div > div.PropertyDet'
#                               'ailsPage__propertyDetailsSmallContainer > div > section:nth-child(5) > p').text.strip()
#
# property_overview = soup.select_one('body > div.PropertyDetailsPage__rootContainer > div > div.Propert'
#                                     'yDetailsPage__propert'
#                                     'yDetailsSmallContainer > div > section:nth-child(4) > div.PropertyOverview_'
#                                     '_propertyOverviewDetails > div:nth-child(1)').text + '\n' + \
#                     soup.select_one('body > div.PropertyDetailsPage__rootContainer > div > '
#                                     'div.PropertyDetailsPage__propertyDetailsSmallContainer > '
#                                     'div > section:nth-child(4) > div.PropertyOverview__propertyOverviewDetails > '
#                                     'div:nth-child(2)').text
#
# lease = soup.select_one('body > div.PropertyDetailsPage__rootContainer > div > '
#                         'div.PropertyDetailsPage__propertyDetailsSmallContainer > div >'
#                         ' section:nth-child(4) > div.PropertyOverview__propertyOverviewDetails >'
#                         ' div.PropertyOvervi'
#                         'ew__availability > div').text.split('Lease: ')[1]
#
# facilities = soup.select_one('body > div.PropertyDetailsPage__rootContainer > '
#                              'div > div.PropertyDetailsPage__propertyDetailsSmallContainer > '
#                              'div > section:nth-child(6) > ul')
#
# list_of_facilities = [element.text for element in facilities.select('.PropertyFacilities__iconText')]
#
# phone = soup.select_one('#property-contact-form > button.ContactForm__secondaryButton.ContactForm__baseButton')
#
# print("Title>>>")
# print(title_ele)
# print()
# print("Rent>>>")
# print(rent)
# print()
# print("Overview>>>")
# print(property_overview)
# print()
# print("Lease>>>")
# print(lease)
# print()
# print("Lat Long>>>")
# print(latitude, longitude)
# print()
# print("Description>>>")
# print(description)
# print()
# print("Facilities>>>")
# print(list_of_facilities)
# print()
