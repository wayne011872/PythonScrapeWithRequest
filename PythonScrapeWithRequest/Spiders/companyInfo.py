import PythonScrapeWithRequest.SettingsData.companyInfo as psci
import PythonScrapeWithRequest.Model.companyInfo as pmc
import PythonScrapeWithRequest.Libs.companyInfo.lib_scrapy as ccls
import pythonGeneral.dataProcessing.pandas as pds
import pythonGeneral.log.logging as plg
from fake_useragent import UserAgent
import requests
import random
from bs4 import BeautifulSoup
import urllib3


class CompanyInfoSpider:
    spiderCount = 0

    def __init__(self):
        self.setDataSettings()

    def setDataSettings(self):
        self.settingsData = psci.companyInfoSettings()
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
        self.myLogger = plg.myLogger(logName, logLevel, logDir)

    def setConfigDir(self):
        self.configDir = self.settingsData.configDir

    def setStartAndEndCount(self):
        self.startNum = self.settingsData.startDataNum
        self.endNum = self.settingsData.endDataNum

    def setDataFrame(self):
        self.myDfData = pds.df_data(
            self.settingsData.path_settings, self.settingsData.usedCol)

    def setSpiderField(self):
        self.companyName = str(
            self.myDfData.df.at[self.spiderCount, self.settingsData.comNameCol])
        self.companyTaxId = str(
            self.myDfData.df.at[self.spiderCount, self.settingsData.comTaxIdCol])

    def setRequestHeader(self):
        self.headers = self.settingsData.requestHeaders

    def setRandomUserAgent(self):
        user_agent = UserAgent()
        self.headers["user-agent"] = user_agent.random

    def setRequestUrl(self):
        self.requestUrl = self.settingsData.urlHead + str(self.companyTaxId).zfill(8)

    def setBeautifulSoup(self):
        self.soup = BeautifulSoup(self.res.text, "html.parser")

    def start_requests(self):
        self.setSpiderField()
        self.setRequestSleepTime()
        self.setRandomUserAgent()
        self.setRequestUrl()
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        try:
            self.res = requests.get(
                self.requestUrl, headers=self.headers, verify=False)
            self.res.encoding = "utf-8"
        except:
            requestErr = "[{0}] {1} Request不到或出問題".format(
                self.spiderCount, self.companyTaxId)
            print(requestErr)
            self.myLogger.logger.error(requestErr)

    def parseResponse(self):
        item = self.processResponseData()
        return item

    def processResponseData(self):
        item = pmc.companyInfo()
        try:
            soup = BeautifulSoup(self.res.text, "html.parser")
        except:
            item = ccls.setItems(item, self.companyTaxId,self.companyName, "","", "","","")
            responseTextErr = "[{0}] {1} responseText 沒有或出問題".format(
                self.spiderCount, self.companyTaxId)
            print(responseTextErr)
            self.myLogger.logger.error(responseTextErr)
        else:
            try:
                phone = ccls.getTWCompanyPhoneNum(soup)
                # responsibleName = ccls.getTWCompanyResponsibleName(soup)
                companyAddress = ccls.getTWCompanyAddress(soup)
                capitalAmount = ccls.getTWCompanyCapital(soup)
                email = ccls.getTWCompanyEmail(soup)
                website = ccls.getTWCompanyWeb(soup)
            except:
                item = ccls.setItems(
                    item, self.companyTaxId, self.companyName, "","", "","","")
                orjsonErr = "[{0}] {1} orjson loads出問題".format(
                    self.spiderCount, self.companyTaxId)
                print(orjsonErr)
                self.myLogger.logger.error(orjsonErr)
            else:
                item = ccls.setItems(
                        item, self.companyTaxId, self.companyName, phone,capitalAmount, email, website,companyAddress)
                dataMessage = "[{0}] taxId: {1} \ncapitalAmount:{2}\nemail:{3}\nwebsite:{4}\nphone:{5}\ncompanyAddress:{6}".format(
                    self.spiderCount, self.companyTaxId, capitalAmount, email, website,phone,companyAddress)
                print(dataMessage)
                self.myLogger.logger.info(dataMessage)
        return item
