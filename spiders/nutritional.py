# coding: utf-8


import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

from ..items import ProductItem


class NutritionalSpider(CrawlSpider):
    name = "nutritional"
    allowed_domains = ["tabelanutricional.com.br"]
    start_urls = (
        'http://www.tabelanutricional.com.br/alimentos/sem/carboidratos/1',
    )

    rules = (
        Rule(LinkExtractor(allow=('\/alimentos\/sem\/carboidratos\/',)), callback="parse_items", follow=True),
    )

    def parse_items(self, response):
        for product in response.css('.omega'):
            item = ProductItem()
            title = product.css("a.name")

            item['link'] = title.xpath("@href").extract()[0]
            item['name'] = title.xpath("text()").extract()[0]

            nutrient_table = product.css("table tr")
            portion = nutrient_table.xpath('th/strong/text()').extract()
            if portion:
                item['portion'] = portion[0].replace(u"porção:", "").strip()

            nutrients = {}
            for row in nutrient_table:
                data = row.select('td/text()').extract()
                if not data:
                    continue
                nutrient = data[0].lower().strip()
                nutrients[nutrient] = data[1].strip()

            item['nutrients'] = nutrients
            yield item
