from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time

class Crawler:

	location_data = {}

	def __init__(self):
		self.options = Options()
		self.options.add_argument("--headless")
		self.driver = webdriver.Firefox(options=self.options)
		self.location_data["rating"] = "NA"

	def get_location_data(self):
		try:
			avg_rating = self.driver.find_element_by_class_name("aMPvhf-fI6EEc-KVuj8d")
		except:
			pass
		try:
			self.location_data["rating"] = avg_rating.text
		except:
			pass

	def scrape(self, url):
		try:
			self.driver.get(url)
		except Exception as e:
			self.driver.quit()
		time.sleep(10)
		self.get_location_data()
		self.driver.quit()
		return(self.location_data)

url = "https://www.google.com/maps/place/Mr.Fresh+Mart/@11.0475151,76.9758269,15z/data=!4m5!3m4!1s0x0:0x74469d3ffe759b5b!8m2!3d11.0475333!4d76.9743524"
x = Crawler()
print(x.scrape(url))