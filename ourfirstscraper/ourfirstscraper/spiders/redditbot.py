# -*- coding: utf-8 -*-
import scrapy


class RedditbotSpider(scrapy.Spider):
    name = 'redditbot'
    allowed_domains = ['www.reddit.com/r/gameofthrones/']
    start_urls = ['http://www.reddit.com/r/gameofthrones//']

    def parse(self, response):
        titles = response.css('h2.may-blank::text').extract()
        votes = response.css('._1rZYMD_4xY3gRcSS3p8ODO::text').extract()
        time = response.css('._3jOxDPIQ0KaOWpzvSQo-1s::text').extract()
        #comments = response.css('.comments::text').extract()

        for item in zip(titles, votes, time):
            scraped_info = {
                'titles' : item[0],
                'votes' : item[1],
                'created_at' : item[2]
                #'comments' : item[3]
            }

            yield scraped_info

    
