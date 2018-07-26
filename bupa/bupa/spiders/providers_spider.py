import scrapy
from bupa.items import BupaItem
import w3lib

class ProviderSpider(scrapy.Spider):
    name = "providers"

    def start_requests(self):
        urls = [
            'https://www.bupa.co.uk/care-services/care-homes/woodend-cheshire',
            'https://www.bupa.co.uk/care-services/care-homes/warren-lodge-ashford',
            'https://www.bupa.co.uk/care-services/care-homes/the-springs-malvern',
            'https://www.bupa.co.uk/care-services/care-homes/the-sidcup-sidcup',
            'https://www.bupa.co.uk/care-services/care-homes/the-links-dorset',
            'https://www.bupa.co.uk/care-services/care-homes/the-kensington-london',
            'https://www.bupa.co.uk/care-services/care-homes/the-highgate-london',
            'https://www.bupa.co.uk/care-services/care-homes/the-donnington-newbury',
            'https://www.bupa.co.uk/care-services/care-homes/thatcham-court-berkshire',
            'https://www.bupa.co.uk/care-services/care-homes/tenterden-house-st-albans',
            'https://www.bupa.co.uk/care-services/care-homes/tadworth-grove-surrey',
            'https://www.bupa.co.uk/care-services/care-homes/staplehurst-manor-kent',
            'https://www.bupa.co.uk/care-services/care-homes/stamford-london',
            'https://www.bupa.co.uk/care-services/care-homes/st-marys-luton',
            'https://www.bupa.co.uk/care-services/care-homes/st-georges-surrey',
            'https://www.bupa.co.uk/care-services/care-homes/shockerwick-house-bath',
            'https://www.bupa.co.uk/care-services/care-homes/puttenham-hill-house-guildford',
            'https://www.bupa.co.uk/care-services/care-homes/pendean-house-west-sussex',
            'https://www.bupa.co.uk/care-services/care-homes/pebble-mill-birmingham',
            'https://www.bupa.co.uk/care-services/care-homes/parkside-reading',
            'https://www.bupa.co.uk/care-services/care-homes/mount-hall-macclesfield',
            'https://www.bupa.co.uk/care-services/care-homes/middlesex-manor-wembley',
            'https://www.bupa.co.uk/care-services/care-homes/maypole-southampton',
            'https://www.bupa.co.uk/care-services/care-homes/manor-court-southall',
            'https://www.bupa.co.uk/care-services/care-homes/manley-court-london',
            'https://www.bupa.co.uk/care-services/care-homes/lynton-hall-surrey',
            'https://www.bupa.co.uk/care-services/care-homes/leominster-leominster',
            'https://www.bupa.co.uk/care-services/care-homes/knights-grove-southampton',
            'https://www.bupa.co.uk/care-services/care-homes/hutton-village-essex',
            'https://www.bupa.co.uk/care-services/care-homes/holyport-lodge-maidenhead',
            'https://www.bupa.co.uk/care-services/care-homes/heathgrove-lodge-london',
            'https://www.bupa.co.uk/care-services/care-homes/heathbrook-house-stoke-heath',
            'https://www.bupa.co.uk/care-services/care-homes/havering-court-romford',
            'https://www.bupa.co.uk/care-services/care-homes/harts-house-woodford-green',
            'https://www.bupa.co.uk/care-services/care-homes/hadley-lawns-barnet',
            'https://www.bupa.co.uk/care-services/care-homes/erskine-hall-northwood',
            'https://www.bupa.co.uk/care-services/care-homes/brunswick-court-watford',
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
            'https://www.bupa.co.uk/care-services/care-homes/sunnyview-house-leeds',	
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
            'https://www.bupa.co.uk/care-services/care-homes/clare-house-uxbridge',
            'https://www.bupa.co.uk/care-services/care-homes/collingwood-grange-camberley',
            'https://www.bupa.co.uk/care-services/care-homes/colonia-court-colchester',
            'https://www.bupa.co.uk/care-services/care-homes/cottenham-court-cambridge',
            'https://www.bupa.co.uk/care-services/care-homes/croft-house-essex',
            'https://www.bupa.co.uk/care-services/care-homes/dene-place-surrey',
            'https://www.bupa.co.uk/care-services/care-homes/east-dean-grange-east-sussex',
            'https://www.bupa.co.uk/care-services/care-homes/queensmount-bournemouth',
            'https://www.bupa.co.uk/care-services/care-homes/red-court-surrey',

        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
    
    def parse(self, response):
        item = BupaItem()

        home_title = response.xpath('//div[@class="pad"]/div/div/h1/text()').extract_first()

        if home_title:
            item['home_title'] = home_title
        else:
            home_title = "No Home Title Found"
            item['home_title'] = home_title

        item['url'] = response.url

        description_p = response.xpath('//div[@class="col w-95"]/p/text()') # Description inside a paragraph tag
        description_n = response.xpath('//div[@class="col w-95"]/text()') # Description not inside paragraph tag
        description_b = response.xpath('//div[@class="body-content"]/div/p[2]/text()') # Description in body class
        description_a = response.xpath('//div[@class="body-content"]/div/div/text()') # Description in body + 2 divs
        description_c = response.xpath('//div[@class="body-content"]/div/div/p/text()') # Description in body + 2 divs + p

        if "Hill House" in home_title:
            description = response.xpath('//div[@class="col w-95"]/p/text()').extract()
            item['description'] = description
        else:
            if description_p:
                description = response.xpath('//div[@class="col w-95"]/p/text()').extract_first()
                item['description'] = description
            elif description_n:
                description = response.xpath('//div[@class="col w-95"]/text()[2]').extract()
                item['description'] = description
            elif description_b:
                description = response.xpath('//div[@class="body-content"]/div/p[2]/text()').extract_first()
                item['description'] = description 
            elif description_a:
                description = response.xpath('//div[@class="body-content"]/div/div/text()').extract()
                item['description'] = description
            elif description_c:
                description = response.xpath('//div[@class="body-content"]/div/div/p/text()').extract_first()
                item['description'] = description
            else:
                description = "No Description Found"
                item['description'] = description
        
        yield item