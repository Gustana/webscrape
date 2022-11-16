from scrape import prepareWebDriver
from scrape import loopThroughPaggination
from pandas import DataFrame

brandToScrape = (
    ('scarlet_review', 'https://www.tokopedia.com/scarlettwhite/review'),
    ('wardah_review', 'https://www.tokopedia.com/wardah-official/review'),
    ('mustika_review', 'https://www.tokopedia.com/mustika-ratu/review')
)

for brand in brandToScrape:

    driver = prepareWebDriver(brand[1])

    list = []

    loopThroughPaggination(list, driver)

    df = DataFrame(columns=['comment', 'rating'], data=list)
    df.to_csv(brand[0], mode='w+')