import scrapy

from pep_parse.items import PepParseItem


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = ['peps.python.org']
    start_urls = ['https://peps.python.org/']

    def parse(self, response):
        all_peps = response.css(
            '#numerical-index td:nth-child(2) a[href^="/pep-"]'
        )
        for pep_link in all_peps:
            yield response.follow(pep_link, callback=self.parse_pep)

    def parse_pep(self, response):
        page_title = response.css('h1.page-title::text').get()
        splited_page_title = page_title.split(' – ')
        data = {
            'number': int(splited_page_title[0].split()[1]),
            'name': splited_page_title[1],
            'status': response.css('dt:contains("Status") + dd::text').get()
        }
        yield PepParseItem(data)
