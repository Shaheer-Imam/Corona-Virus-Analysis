import scrapy


class CovidSpider(scrapy.Spider):
    name = 'covid'
    allowed_domains = ['www.worldometers.info/coronavirus']
    start_urls = ['http://www.worldometers.info/coronavirus/']

    def parse(self, response):
        rows = response.xpath('(//tbody[1])[1]//td/a[@class="mt_a"]/parent::td//parent::tr')
        for row in rows:
            country = row.xpath(".//td[2]/a/text()").get()
            totalCase = row.xpath(".//td[3]/text()").get()
            totalDeath = row.xpath(".//td[5]/text()").get()
            totalRecovered = row.xpath(".//td[7]/text()").get()
            activeCase = row.xpath(".//td[9]/text()").get()
            seriousCritical = row.xpath(".//td[10]/text()").get()
            totalTest = row.xpath('.//td[13]/text()').get()
            population = row.xpath('.//td[15]/a/text()').get()

            yield {
                "CountryName": country,
                "Total Case": totalCase,
                "Total Deaths": totalDeath,
                "Total Recovered": totalRecovered,
                "Active Cases": activeCase,
                "Critical Cases": seriousCritical,
                "Total Test": totalTest,
                "Population": population
            }
