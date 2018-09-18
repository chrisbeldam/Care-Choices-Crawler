import scrapy

from bupa.items import ExtraCareItem

class ExtraCareSpider(scrapy.Spider):
    name = "extracare"

    def start_requests(self):
        urls = []

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    
    def parse(self, response):
        item = ExtraCareItem()

        url = response.url()
        housing_name = response.xpath()
        address = response.xpath()
        telephone = response.xpath()
        cqc_id = response.xpath()
        care_provider = response.xpath()

        item['url'] = url

        if housing_name:
            item['housing_name'] = housing_name
        else:
            item['housing_name'] = 'Cannot find housing name'

        if address:
            item['address'] = address
        else:
            item['address'] = 'No address found'
        
        if telephone:
            item['telephone'] = telephone
        else:
            item['telephone'] = 'No telephone number found'
        
        if cqc_id:
            item['cqc_id'] = cqc_id
        else:
            item['cqc_id'] = 'No cqc id'

        if care_provider:
            item['care_provider'] = care_provider
        else:
            item['care_provider'] = 'No Care provider found'

        yield item
