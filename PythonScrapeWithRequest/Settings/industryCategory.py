# Set Spider Name Here
SPIDER_NAME = "industryCategory"

# Set Headers in here
HEADERS = {
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7',
    'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'Sec-Fetch-Dest': 'script',
    'Sec-Fetch-Mode': 'no-cors',
    'Sec-Fetch-Site': 'same-site',
}

# SetDataPathHere
PATH_SETTINGS = {
    "importDir": "D:\\工業區-廠商\\工業區\\111年生產中工廠+出口廠商清冊\\",
    "importFile": "111年生產中工廠+出口廠商清冊(全+去重覆+比過科學園區).xlsx"
}
# Set Config Path Here
CONFIG_PATH = "D:\\PythonScrapeWithRequest\\PythonScrapeWithRequest\\"

# Set CompanyCoordinate Data Start And End Scrapy Here
DATA_START = 472
DATA_END = 206875

# Set Request Sleep Time(Second)
SLEEP_TIME = 5

# Set Used CompanyCoordinate Data Column Here
USE_COLUMN = ["客戶名稱", "統一編號"]

# Set CompanyCoordinate CompanyName Column Here
COMNAME_COLUMN = "客戶名稱"

# Set CompanyCoordinate CompanyTaxNum Column Here
COMTAXID_COLUMN = "統一編號"

# Set CompanyCoordinate UrlHead Here
URLHEAD = "https://f.twincn.com/Lm.aspx?q="

# Set Logging Path And Name
LOGNAME = "companyInfo"
LOGDIR = "D:\\PythonScrapeWithRequest\\PythonScrapeWithRequest\\"

# Set Logging Level To Be Record | DEBUG,INFO,WARNING,ERROR,CRITICAL
LOGLEVEL = "DEBUG"
