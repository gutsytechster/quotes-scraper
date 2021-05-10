# Quotes Scraper
A quote spider to scrape quotes from [quotes.toscrape.com/js/](https://quotes.toscrape.com/js/)

## Setup
1. Create and activate a virtual environment(this is super important!)
    ```
    $ python -m venv scraper-env
    $ source scraper-env/bin/activate
    ```
2. Install dependencies
    ```
    (scraper-env)$ pip install -r requirements.txt
    ```
    For development environment, use `requirements-dev.txt` instead
    ```
    (scraper-env)$ pip install -r requirements-dev.txt
    ```
3. Start `splash` browser
    - Pull docker image for splash
        ```
        docker pull scrapinghub/splash
        ```
    - Run docker service for splash
        ```
        docker run -p 8050:8050 scrapinghub/splash up
        ```
3. Run spider
    ```
    (scraper-env)$ scrapy crawl quotes
    ```
    If you want to save the output to a file, use `-o` option
    ```
    (scraper-env)$ scrapy crawl quotes -o quotes.json
    ```

## Details

- The spider goes through each quotes pages, crawling through the link to next page.
- To identify specific CSS selector, inspect the HTML via browser inspector and fetch quote details from each page.
- The website is rendered dynamically by executing the JavaScript code. Hence, Splash is used here to execute the JavaScript to get the resulting HTML.
- The spider fetches the following details corresponding to each quote
    - Quote Text
    - Quote author
    - Tags
- The data is kept in JSON format using the command above in [`quotes.json`](https://github.com/gutsytechster/quotes-scraper/blob/main/quotes.json) file.
