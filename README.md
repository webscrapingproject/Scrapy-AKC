 # scrapy采集AKC网站犬类图片
## 1. 项目背景
具体细节请参考我的博文： https://univerone.com/post/scrapy-dogs/

## 2.使用方法
```bash
# 安装scrapy框架
conda install scrapy
# 下载项目源代码
git clone https://github.com/webscrapingproject/Scrapy-AKC.git
# 安装python依赖
cd Scrapy-AKC
pip install -r requirement.txt
# 进行爬虫
scrapy crawl images

```
图片将自动保存在Scrapy-AKC内的image文件夹里