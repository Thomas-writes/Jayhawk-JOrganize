#put stuff to get file name here
from pathlib import Path
import scrapy 
import csv 
import sys
from scrapy.crawler import CrawlerProcess

class TableSpider(scrapy.Spider):
    name = "table"

    def start_requests(self):
        user_url = sys.argv[1]
        urls=[user_url]
        

        for url in urls:
            yield scrapy.Request(url=url, callback = self.parse)
    
    def parse(self, response):
        matrix =[]
        headers =[]
        
        
        headers = response.css("th")
        header_text = ["".join(text.strip()) for text in headers.css("*::text").getall() if text.strip()]
        matrix.append(header_text)

        for item in response.css("tr"):
            matrix.append(item.css("td::text").getall())
        with open('scrappy/matrix.csv', "w", newline='') as file:
            writer = csv.writer(file)
            writer.writerows(matrix)

process = CrawlerProcess({
    'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
})

process.crawl(TableSpider)
process.start() # the script will block here until the crawling is finished

#my_spider = TableSpider(scrapy.Spider)
#results = my_spider.start_requests(user_url)
#results = my_spider.parse(results)
#print(results)

#def make_csv(res)

#make sure i make somethign to where the th are always in the same spot 