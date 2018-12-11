import scrapy
from spiders.house import JobsSpider
from scrapy.crawler import CrawlerProcess
import pandas as pd

if __name__ == "__main__":
    process = CrawlerProcess({
        'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
    })

    process.crawl(JobsSpider)
    process.start()

    housing_dataframe = pd.read_csv("/Users/ctam/craigslist/craigslist/test2.csv")
    no_duplicate_df = housing_dataframe.drop_duplicates(['Title','Price'],'first')
    no_price_df = no_duplicate_df.query("Price == 0")
    clean_df = no_duplicate_df.query("Price != 0")
    with open('/Users/ctam/craigslist/craigslist/result/no_duplicate.csv', 'a') as f:
        no_duplicate_df.to_csv(f,header=False)
    with open('/Users/ctam/craigslist/craigslist/result/no_price.csv', 'a') as f:
        no_price_df.to_csv(f,header=False)
    with open('/Users/ctam/craigslist/craigslist/result/result.csv', 'a') as f:
        clean_df.to_csv(f,header=False)

