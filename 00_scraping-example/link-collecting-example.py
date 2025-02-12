import os
from utils import utils

file_path = "00_scraping-example"
resource_name =  "link-collecting-example"
url = 'https://github.com/mwaskom/seaborn-data/tree/master'
file_types = ('.txt', '.csv')

if __name__ == '__main__':
    # Create logger
    logger = utils.create_logger(file_path=file_path, resource_name=resource_name)
    # Set up soup object to parse text; can toggle dynamic=True, headless=False options to see Selenium functionality
    soup = utils.set_up_soup(url=url, logger=logger)
    # Download all files linked in `href` tags that end in `file_types`
    utils.download_files(logger=logger, soup=soup, file_path=file_path, url=url, file_types=file_types)