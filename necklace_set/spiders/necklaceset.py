import scrapy
from scrapy.selector import Selector


class NecklacesetSpider(scrapy.Spider):
    name = 'necklaceset'
    allowed_domains = ['www.houseofindya.com/zyra/necklace-sets/cat']
    start_urls = ['https://www.houseofindya.com/zyra/necklace-sets/cat/']

    def parse(self, response, **kwargs):
        # get all jewel list store in ul tag
        jewel_list = response.xpath('//div[@class="catgList"]/ul[@id="JsonProductList"]/li')
        for i,jewel in enumerate(jewel_list):
            jewel_dict = dict()
            # change jewel data to new Selector
            jewel = Selector(text=jewel.get())
            jewel_name = jewel.xpath("//li").attrib['data-name']
            jewel_price = jewel.xpath("//li").attrib['data-price']
            jewel_discount = jewel.css('span::text').get()
            jewel_image1 = jewel.xpath("//img").attrib['onmouseout'].split("=")[1]
            jewel_image2 = jewel.xpath("//img").attrib['onmouseover'].split("=")[1]

            jewel_dict["Description"] = jewel_name
            jewel_dict["Price"] = jewel_price
            jewel_dict["Image1"] =  jewel_image1
            jewel_dict["Image2"] = jewel_image2

            yield jewel_dict
