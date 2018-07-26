import scrapy
from bupa.items import BupaItem
import w3lib

class ProviderSpider(scrapy.Spider):
    name = "providers"

    def start_requests(self):
        urls = [
            'https://www.bupa.co.uk/care-services/care-homes/southlands-harrogate',
            'https://www.bupa.co.uk/care-services/care-homes/greenhill-powys',
            'https://www.bupa.co.uk/care-services/care-homes/heathland-court-wimbledon',	
            'https://www.bupa.co.uk/care-services/care-homes/hill-house-elstree',	
            'https://www.bupa.co.uk/care-services/care-homes/nairn-house-enfield',	
            'https://www.bupa.co.uk/care-services/care-homes/amberley-court-birmingham',	
            'https://www.bupa.co.uk/care-services/care-homes/ashley-house-gloucestershire',	
            'https://www.bupa.co.uk/care-services/care-homes/aylesham-court-leicester',
            'https://www.bupa.co.uk/care-services/care-homes/eastbury-manor-guildford',	
            'https://www.bupa.co.uk/care-services/care-homes/the-lawns-chelmsford',
            'https://www.bupa.co.uk/care-services/care-homes/the-manor-house-wirral',	
            'https://www.bupa.co.uk/care-services/care-homes/chilton-meadows-stowmarket',	
            'https://www.bupa.co.uk/care-services/care-homes/copper-beech-uckfield',	
            'https://www.bupa.co.uk/care-services/care-homes/druid-stoke-bristol',	
            'https://www.bupa.co.uk/care-services/care-homes/beacher-hall-reading',	
            'https://www.bupa.co.uk/care-services/care-homes/brookview-cheshire',	
            'https://www.bupa.co.uk/care-services/care-homes/westcombe-park-london',	
            'https://www.bupa.co.uk/care-services/care-homes/eglantine-villa-dartford',	
            'https://www.bupa.co.uk/care-services/care-homes/elm-grove-cirencester',	
            'https://www.bupa.co.uk/care-services/care-homes/hatfield-peverel-chelmsford',		
            'https://www.bupa.co.uk/care-services/care-homes/the-mellowes-gillingham',		
            'https://www.bupa.co.uk/care-services/care-homes/trowbridge-oaks-trowbridge',		
            'https://www.bupa.co.uk/care-services/care-homes/wilmington-manor-dartford',		
            'https://www.bupa.co.uk/care-services/care-homes/fountains-lodge-nursing-and-residential-home-tunbridge-wells',		
            'https://www.bupa.co.uk/care-services/care-homes/dean-wood-brighton',		
            'https://www.bupa.co.uk/care-services/care-homes/waverley-grange-farnham',		
            'https://www.bupa.co.uk/care-services/care-homes/crossley-house-bradford',		
            'https://www.bupa.co.uk/care-services/care-homes/edmund-house-scunthorpe',		
            'https://www.bupa.co.uk/care-services/care-homes/hazelmere-house-wilmslow',		
            'https://www.bupa.co.uk/care-services/care-homes/heol-don-cardiff',		
            'https://www.bupa.co.uk/care-services/care-homes/premier-court-hertfordshire',		
            'https://www.bupa.co.uk/care-services/care-homes/prestemede-powys',		
            'https://www.bupa.co.uk/care-services/care-homes/sandhills-court-scunthorpe',		
            'https://www.bupa.co.uk/care-services/care-homes/sunnyview-house-leeds	',	
            'https://www.bupa.co.uk/care-services/care-homes/the-arkley-barnet',		
            'https://www.bupa.co.uk/care-services/care-homes/the-lindsay-dorset',		
            'https://www.bupa.co.uk/care-services/care-homes/wykebeck-court-leeds',		
            'https://www.bupa.co.uk/care-services/care-homes/wylesfield-powys',		
            'https://www.bupa.co.uk/care-services/care-homes/alveston-leys-stratford-upon-avon',		
            'https://www.bupa.co.uk/care-services/care-homes/abbotsleigh-mews-kent',		
            'https://www.bupa.co.uk/care-services/care-homes/arbrook-house-surrey',		
            'https://www.bupa.co.uk/care-services/care-homes/ardenlea-grove-solihull',		
            'https://www.bupa.co.uk/care-services/care-homes/argyles-newbury',		
            'https://www.bupa.co.uk/care-services/care-homes/ashby-court-leicestershire',		
            'https://www.bupa.co.uk/care-services/care-homes/ashley-park-surrey',			
            'https://www.bupa.co.uk/care-services/care-homes/the-priory-shirley',		
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
    
    def parse(self, response):
        item = BupaItem()
        item['url'] = response.url
        item['home_title'] = response.xpath('//div[@class="pad"]/div/div/h1/text()').extract_first()

        description_p = response.xpath('//div[@class="col w-95"]/p/text()') # Description inside a paragraph tag
        description_n = response.xpath('//div[@class="col w-95"]/text()') # Description not inside paragraph tag

        if description_p:
            description = response.xpath('//div[@class="col w-95"]/p/text()').extract_first()
            item['description'] = description
        elif description_n:
            description = response.xpath('//div[@class="col w-95"]/text()[2]').extract()
            item['description'] = description
       
        yield item