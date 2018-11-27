from background_task import background
from scraping.flexscrapper import FlexScrapper

# should this be queued?
@background
def updateFlexForUser(userId, userToken):
    FlexScrapper(userId, userToken).getCSVAndUpdateFlex()
