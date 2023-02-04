import pythonGeneral.database.mongo as pdm
from PythonScrapeWithRequest.Libs.companyCoordinate.lib_scrapy import getDictItems

class companyCoordinatePipelines:
    def __init__(self,spider):
        self.mon = pdm.mon(initFileAddress = spider.configDir,collectionName=spider.spiderName)
    
    def processItem(self,item):
        itemsDict = getDictItems(item)
        self.mon.insertOneData(itemsDict)