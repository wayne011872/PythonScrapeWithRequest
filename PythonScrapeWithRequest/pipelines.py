import pythonGeneral.database.mongo as pdm
import PythonScrapeWithRequest.Libs.companyCoordinate.lib_scrapy as pccl
import PythonScrapeWithRequest.Libs.companyInfo.lib_scrapy as pcil
import PythonScrapeWithRequest.Libs.industryCategory.lib_scrapy as plil

class companyCoordinatePipelines:
    def __init__(self,spider):
        self.mon = pdm.mon(initFileAddress = spider.configDir,collectionName=spider.spiderName)
    
    def processItem(self,item):
        itemsDict = pccl.getDictItems(item)
        self.mon.insertOneData(itemsDict)
        

class companyInfoPipelines:
    def __init__(self, spider):
        self.mon = pdm.mon(initFileAddress=spider.configDir,collectionName=spider.spiderName)

    def processItem(self, item):
        itemsDict = pcil.getDictItems(item)
        self.mon.insertOneData(itemsDict)
        
class categoryPipelines:
    def __init__(self, spider):
        self.mon = pdm.mon(initFileAddress=spider.configDir,collectionName=spider.spiderName)

    def processItem(self, item):
        itemsDict = plil.getDictItems(item)
        self.mon.insertOneData(itemsDict)
