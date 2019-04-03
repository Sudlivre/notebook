# JavaScript渲染服务Splash

> Splash是一个JavaScript渲染服务。它是一个带有HTTP API的轻量级Web浏览器，使用Twisted和QT5在Python 3中实现。QT反应器用于使服务完全异步，允许通过QT主循环利用webkit并发。

**功能：**

- 异步方式处理多个网页渲染过程
- 获取渲染后的页面的源代码或者截图
- 通过关闭图片渲染或者使用Adblock规则来加快页面渲染速度
- 可执行特定的JavaScript脚本
- 可通过Lua脚本来控制页面渲染过程
- 获取渲染的详细信息并通过HAR（HTTP Archive）格式呈现



#### 安装Splash

安装docker使用官方文档[**https://www.docker.com/get-started**](https://www.docker.com/get-started)

安装Splash并启动服务`docker run -p 8050:8050 scrapinghub/splash`

然后就可以使用其接口实现一些动态页面的抓取。同时可以对接Scrapy框架。



#### Splash API调用

 **render.html**

此接口用于获取JavaScript渲染页面的HTML代码

```python
import requests
 
 
def splash_render(url):
    splash_url = "http://192.168.99.100:8050/render.html"
 
    args = {
        "url": url,
        "timeout": 5,
        "image": 0
    }
 
    response = requests.get(splash_url, params=args)
    return response.text
 
 
if __name__ == '__main__':
    url = "https://www.baidu.com"
    html = splash_render(url)
    print(html)
```

- **args参数**
  url: 需要渲染的页面地址
  timeout: 超时时间
  proxy：代理
  wait：等待渲染时间
  images: 是否下载，默认1（下载）
  js_source: 渲染页面前执行的js代码

**详情：https://splash.readthedocs.io/en/stable/api.html#render-html**

 **execute**

可以通过此接口实现与Lua脚本的对接。

```python
import requests
from urllib.parse import quote
 
 
# Lua脚本
lua = '''
function main(splash, args)
    local treat = require("treat")
    local response = splash:http_get("http://httpbin.org/get")
    return {
        html = treat.as_string(response.body),
        url=response.url,
        status=response.status
    }
end
'''
 
url = 'http://192.168.99.100:8050/execute?lua_source=' + quote(lua)
response = requests.get(url)
print(response.text)
```



#### Scrapy对接Splash

**settings.py中增加以下配置**

```python
SPIDER_MIDDLEWARES = {
    'scrapy_splash.SplashDeduplicateArgsMiddleware': 100,
}
 
DOWNLOADER_MIDDLEWARES = {
    'scrapy_splash.SplashCookiesMiddleware': 723,
    'scrapy_splash.SplashMiddleware': 725,
    'scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware': 810
}
# Splash服务启动的地址
SPLASH_URL = 'http://192.168.99.100:8050'
 
DUPEFILTER_CLASS = 'scrapy_splash.SplashAwareDupeFilter'
HTTPCACHE_STORAGE = 'scrapy_splash.SplashAwareFSCacheStorage'
```

**spider中使用SplashRequest**

```python
from scrapy import Spider, Request
from urllib.parse import quote
from scrapysplashtest.items import ProductItem
from scrapy_splash import SplashRequest
 
script = """
function main(splash, args)
  splash.images_enabled = false
  assert(splash:go(args.url))
  assert(splash:wait(args.wait))
  js = string.format("document.querySelector('#mainsrp-pager div.form > input').value=%d;document.querySelector('#mainsrp-pager div.form > span.btn.J_Submit').click()", args.page)
  splash:evaljs(js)
  assert(splash:wait(args.wait))
  return splash:html()
end
"""
 
 
class TaobaoSpider(Spider):
    name = 'taobao'
    allowed_domains = ['www.taobao.com']
    base_url = 'https://s.taobao.com/search?q='
    
    def start_requests(self):
        for keyword in self.settings.get('KEYWORDS'):
            for page in range(1, self.settings.get('MAX_PAGE') + 1):
                url = self.base_url + quote(keyword)
                yield SplashRequest(url, callback=self.parse, endpoint='execute',
                                    args={'lua_source': script, 'page': page, 'wait': 7})
```

