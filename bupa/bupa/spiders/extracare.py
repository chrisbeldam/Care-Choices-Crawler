import scrapy

from bupa.items import ExtraCareItem

class ExtraCareSpider(scrapy.Spider):
    name = "extracare"

    def start_requests(self):
       start_urls = ['http://www.housingcare.org/housing-care/results.aspx?ath=6&lst=re&ct=England&cn=&stp=1&sm=3&vm=list&rp=10']

       for url in start_urls:
            yield scrapy.Request(url=url, callback=self.parse_category)

    def parse_category(self, response):
        # Top Level - Open each home
        next_page_url = response.xpath('//a[@class="next"]/@href').extract_first()
        page_url = response.xpath('//div[@class="title"]/h3/a/@href').extract()  # Grab a list of the individual home page links
        for url in page_url:
            yield scrapy.Request(url, callback=self.parse_page_details)
        yield scrapy.Request(next_page_url, callback=self.parse_category)

    
    def parse_page_details(self, response):
        item = ExtraCareItem()

        url = response.url
        housing_name = response.xpath('//span[@itemprop="name"]/text()').extract_first()
        address = response.xpath('//span[@itemprop="address"]/text()').extract_first()
        telephone = response.xpath('//p[@class="call"]/strong/text()').extract_first()
        # cqc_id = response.xpath().extract_first()
        care_provider = response.xpath('//div[@class="managed-by"]/h2/span[@itemprop="name"]/text()').extract_first()

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
        
        # if cqc_id:
        #     item['cqc_id'] = cqc_id
        # else:
        #     item['cqc_id'] = 'No cqc id'

        if care_provider:
            item['care_provider'] = care_provider
        else:
            item['care_provider'] = 'No Care provider found'

        yield item
