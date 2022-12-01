import requests
import lxml.html as html

HOME_URL = ''

XPATH_LINK_TO_ARTICLE = '//div[contains(@class, "V")]/a[contains(@class, "kicker")]/@href'
XPATH_TITLE = '//div[@class="mb-auto"]/h2/span/text()'
XPATH_SUMMARY = '//div[@class="lead"]/p/text()'
XPATH_BODY = '//div[@class="html-content"]/p[not (@class)]/text()'


def parse_home():
    try:
        response = requests.get(HOME_URL)

        if response.status_code != 200:
            raise ValueError(f'Error: {response.status_code}')

        home = response.content.decode('utf-8')
        parsed = html.fromstring(home)
        links_to_notices = parsed.xpath(XPATH_LINK_TO_ARTICLE)
        print(links_to_notices)
    except ValueError as ve:
        print(ve)


def run():
    parse_home()


if __name__ == '__main__':
    run()
