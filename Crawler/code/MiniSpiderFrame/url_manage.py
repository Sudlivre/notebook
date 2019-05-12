# encoding=utf-8


class URLManager(object):

    def __init__(self):
        self.new_urls = set()
        self.old_urls = set()

    def has_new_url(self):
        # 判断是否有未爬取的url
        return self.new_url_size() != 0

    def get_new_url(self):
        # 获取一个未爬取的链接
        new_url = self.new_urls.pop()
        # 提取之后，将其添加到已爬取的链接中
        self.old_urls.add(new_url)
        return new_url

    def add_new_url(self, url):
        # 将新链接添加到未爬取的集合中(单个链接)
        if url is None:
            return
        if url not in self.new_urls and url not in self.old_urls:
            self.new_urls.add(url)

    def add_new_urls(self, urls):
        # 将新链接添加到未爬取的集合中(集合)
        if urls is None or len(urls) == 0:
            return
        for url in urls:
            self.add_new_url(url)

    def new_url_size(self):
        # 获取未爬取的url大小
        return len(self.new_urls)

    def old_url_size(self):
        # 获取已爬取的url大小
        return len(self.old_urls)
