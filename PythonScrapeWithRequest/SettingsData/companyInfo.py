import PythonScrapeWithRequest.Settings.companyInfo as psc


class companyInfoSettings:
    path_settings = {}

    def __init__(self):
        self.getDataPath()
        self.getSpiderName()
        self.getStartDataNum()
        self.getEndDataNum()
        self.getUsedCol()
        self.getComNameCol()
        self.getComTaxIDCol()
        self.getUrlHead()
        self.getConfigDir()
        self.getRequestHeaders()
        self.getLogSettings()
        self.getRequestSleepTime()

    def getDataPath(self):
        importDir = psc.PATH_SETTINGS.get("importDir")
        importFile = psc.PATH_SETTINGS.get("importFile")
        exportDir = psc.PATH_SETTINGS.get("exportDir")
        exportFile = psc.PATH_SETTINGS.get("exportFile")
        self.path_settings['importDir'] = importDir
        self.path_settings['importFile'] = importFile
        self.path_settings['exportDir'] = exportDir
        self.path_settings['exportFile'] = exportFile

    def getSpiderName(self):
        self.spiderName = psc.SPIDER_NAME

    def getStartDataNum(self):
        self.startDataNum = psc.DATA_START

    def getEndDataNum(self):
        self.endDataNum = psc.DATA_END

    def getUsedCol(self):
        self.usedCol = psc.USE_COLUMN

    def getComNameCol(self):
        self.comNameCol = psc.COMNAME_COLUMN

    def getComTaxIDCol(self):
        self.comTaxIdCol = psc.COMTAXID_COLUMN

    def getUrlHead(self):
        self.urlHead = psc.URLHEAD

    def getConfigDir(self):
        self.configDir = psc.CONFIG_PATH

    def getRequestHeaders(self):
        self.requestHeaders = psc.HEADERS

    def getLogSettings(self):
        self.logName = psc.LOGNAME
        self.logDir = psc.LOGDIR
        self.logLevel = psc.LOGLEVEL

    def getRequestSleepTime(self):
        self.sleepTime = psc.SLEEP_TIME
