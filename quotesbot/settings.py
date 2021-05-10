# Scrapy settings for quotesbot project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = "quotesbot"

SPIDER_MODULES = ["quotesbot.spiders"]
NEWSPIDER_MODULE = "quotesbot.spiders"


# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Scrapy splash settings
SPLASH_URL = "http://localhost:8050"
DOWNLOADER_MIDDLEWARES = {
    "scrapy_splash.SplashCookiesMiddleware": 723,
    "scrapy_splash.SplashMiddleware": 725,
    "scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware": 810,
}
SPIDER_MIDDLEWARES = {
    "scrapy_splash.SplashDeduplicateArgsMiddleware": 100,
    'scrapy_autounit.AutounitMiddleware': 950,
}
DUPEFILTER_CLASS = "scrapy_splash.SplashAwareDupeFilter"

# Enable this whenever updating tests for the spider
AUTOUNIT_ENABLED = False
