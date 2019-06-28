import scrapy
from mySpider.items import ItcastItem


class ItcastSpider(scrapy.Spider):
    name = "itcast"  # 这个爬虫的识别名称，必须是唯一的
    allowed_domains = ["itcast.cn"]  # 是搜索的域名范围，也就是爬虫的约束区域，规定爬虫只爬取这个域名下的网页，不存在的URL会被忽略。
    # 爬虫从这里开始抓取数据，所以，第一次下载的数据将会从这些urls开始。其他子URL将会从这些起始URL中继承性生成。
    start_urls = (
        'http://www.itcast.cn/channel/teacher.shtml',
    )  # 爬取的URL元祖/列表

    # def parse(self, response):
    #     filename = "teacher.html"
    #     # open(filename, 'w').write(response.body.decode('utf-8'))
    #
    #     con = response.body.decode('utf-8')
    #     file_object = open(filename, 'w', encoding='utf-8')
    #     file_object.write(con)
    #     file_object.close()

    # 解析的方法，每个初始URL完成下载后将被调用，调用的时候传入从每一个URL传回的Response对象来作为唯一参数
    def parse(self, response):
        # open("teacher.html","wb").write(response.body).close()

        # 存放老师信息的集合
        items = []

        # XPath 提取数据
        for each in response.xpath("//div[@class='li_txt']"):  # /html/body/div[1]/div[5]/div[2]/div[4]/ul/li[1]/div[2]
            # 将我们得到的数据封装到一个 `ItcastItem` 对象
            item = ItcastItem()
            # extract()方法返回的都是unicode字符串
            name = each.xpath("h3/text()").extract()
            title = each.xpath("h4/text()").extract()
            info = each.xpath("p/text()").extract()

            # xpath返回的是包含一个元素的列表
            item['name'] = name[0]
            item['title'] = title[0]
            item['info'] = info[0]

            items.append(item)

        # 直接返回最后数据

        return items


# class Opp2Spider(scrapy.Spider):
#     name = 'itcast'
#     allowed_domains = ['itcast.com']
#     start_urls = ['http://www.itcast.cn/']
#
#     def parse(self, response):
#         # 获取网站标题
#         context = response.xpath('/html/head/title/text()')
#
#         # 提取网站标题
#         title = context.extract_first()
#         print(title)
#         pass


"""
1. 新建项目:
scrapy startproject mySpider

2. 在mySpider目录下执行：
scrapy crawl itcast (它是 ItcastSpider 类的 name 属性)

3.保存数据: - scrapy保存信息的最简单的方法主要有四种，-o 输出指定格式的文件，命令如下
scrapy crawl itcast -o teachers.json
scrapy crawl itcast -o teachers.jsonlines
scrapy crawl itcast -o teachers.csv
scrapy crawl itcast -o teachers.xml
"""
