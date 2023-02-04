import PythonScrapeWithRequest.SettingsData.companyCoordinate as psdc
import PythonScrapeWithRequest.Model.companyCoordinate as pmc
import PythonScrapeWithRequest.Libs.companyCoordinate.lib_scrapy as ccls
import pythonGeneral.dataProcessing.pandas as pds
import pythonGeneral.log.logging as plg
import orjson
from fake_useragent import UserAgent
import requests
import random
from bs4 import BeautifulSoup
import urllib3


class CompanyCoordinateSpider:
    spiderCount = 0
    def __init__(self):
        self.setDataSettings()

    def setDataSettings(self):
        self.settingsData = psdc.companyCoordinateSettings()
        self.setMyLogging()
        self.setConfigDir()
        self.setSpiderName()
        self.setRequestHeader()
        self.setDataFrame()
        self.setStartAndEndCount()
    
    def setSpiderName(self):
        self.spiderName = self.settingsData.spiderName
        
    def setRequestSleepTime(self):
        self.sleepTime = self.settingsData.sleepTime
        delay = random.uniform(0, self.sleepTime)
        delay = float("%.1f" % delay)
        self.myLogger.logger.debug("### time is random delay: %s s###" % delay)
        self.sleepTime = delay
    
    def setMyLogging(self):
        logName = self.settingsData.logName
        logDir = self.settingsData.logDir
        logLevel = self.settingsData.logLevel
        self.myLogger = plg.myLogger(logName,logLevel,logDir)
    
    def setConfigDir(self):
        self.configDir = self.settingsData.configDir
    
    def setStartAndEndCount(self):
        self.startNum = self.settingsData.startDataNum
        self.endNum = self.settingsData.endDataNum
    
    def setDataFrame(self):
        self.myDfData = pds.df_data(self.settingsData.path_settings,self.settingsData.usedCol)
    
    def setSpiderField(self):    
        self.companyName = str(self.myDfData.df.at[self.spiderCount,self.settingsData.comNameCol])
        self.companyTaxId = str(self.myDfData.df.at[self.spiderCount,self.settingsData.comTaxIdCol])
        self.companyAddr = str(self.myDfData.df.at[self.spiderCount,self.settingsData.comAddrCol])
    
    def setRequestHeader(self):
        self.headers = self.settingsData.requestHeaders

    def setRandomUserAgent(self):
        user_agent = UserAgent()
        self.headers["user-agent"] = user_agent.random
    
    def setRequestUrl(self):
        self.requestUrl = self.settingsData.urlHead + self.companyAddr
    
    def setBeautifulSoup(self):
        self.soup = BeautifulSoup(self.res.text, "html.parser")
    
    def start_requests(self):
        self.setSpiderField()
        self.setRequestSleepTime()
        self.setRandomUserAgent()
        self.setRequestUrl()
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        self.res = requests.get(self.requestUrl, headers=self.headers, verify=False)
    
    def parseResponse(self):
        self.res.encoding = "utf-8"
        item = self.processResponseData()
        return item
        
    def processResponseData(self):
        item = pmc.companyCoordinate()
        try:
            responseData = str(self.res.text).split("(")[1]
            responseData = str(responseData).split(")")[0]
        except:
            item = ccls.setItems(item, self.companyTaxId, self.companyName, "0", "0")
            responseTextErr = "[{0}] {1} responseText 沒有或出問題".format(self.spiderCount, self.companyTaxId)
            print(responseTextErr)
            self.myLogger.logger.error(responseTextErr)
        else:
            try:
                companyLatitude = orjson.loads(responseData)["locate"]["lat"]
                companyLongitude = orjson.loads(responseData)["locate"]["lng"]
            except:
                item = ccls.setItems(item, self.companyTaxId, self.companyName, "0", "0")
                orjsonErr = "[{0}] {1} orjson loads出問題".format(self.spiderCount, self.companyTaxId)
                print(orjsonErr)
                self.myLogger.logger.error(orjsonErr)
            else:
                if companyLatitude == '0' or companyLongitude == '0':
                    item = ccls.setItems(item, self.companyTaxId, self.companyName, "0", "0")
                    noDataErr = "[{0}] {1} 經緯度資料為0".format(self.spiderCount, self.companyTaxId)
                    print(noDataErr)
                    self.myLogger.logger.warning(noDataErr)
                else:
                    item = ccls.setItems(item, self.companyTaxId, self.companyName, companyLatitude, companyLongitude)
                    dataMessage = "[{0}] taxId: {1} \nlatitude:{2} longitude:{3}".format(self.spiderCount, self.companyTaxId, companyLatitude, companyLongitude)
                    print(dataMessage)
                    self.myLogger.logger.info(dataMessage)
        return item