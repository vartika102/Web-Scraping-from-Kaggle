# -*- coding: utf-8 -*-
import scrapy
import json

class KaggleSpider(scrapy.Spider):
    name = 'kaggle'
    allowed_domains = ['www.kaggle.com/competitions']
    start_urls = ['https://www.kaggle.com/competitions']

    def parse(self, response):
        data = json.loads((
            response
            .css(r"script:contains('Kaggle.State.push({\"')")
            .re_first(r'Kaggle.State.push\((.+?)\);')
        ))

        for group in data['fullCompetitionGroups']:
            if group['totalCompetitions'] > 0:
                for competition in group['competitions']:
                    if 'computer vision' in competition['competitionDescription'].lower() and 'getting started' in competition['hostSegmentTitle'].lower():
                        
                        yield {
                            'title': competition['competitionTitle'],
                            'description': competition['competitionDescription'],
                            'reward': competition['rewardDisplay'],
                            'totalteams': competition['totalTeams'],
                        }
