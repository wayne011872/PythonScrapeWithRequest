# Set Headers in here
HEADERS = {
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7',
    'Connection': 'keep-alive',
    'Referer': 'https://www.map.com.tw/',
    'Host': 'api.map.com.tw',
    'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'Sec-Fetch-Dest': 'script',
    'Sec-Fetch-Mode': 'no-cors',
    'Sec-Fetch-Site': 'same-site',
}
# SetDataPathHere
PATH_SETTINGS = {
    "importDir": "D:\\工業區-廠商\\工業區\\111年進出口廠商清冊\\111年進出口廠商清冊爬蟲\\座標爬蟲\\",
    "importFile": "111年生產中工廠清冊爬蟲(和工廠資料比對完).xlsx"
}
# Set Config Path Here
CONFIG_PATH = "D:\\pythonScrapy\\pythonScrapy\\config\\companyCoordinate\\"

# Set CompanyCoordinate Data Start And End Scrapy Here
DATA_START = 0
DATA_END = 10

# Set Used CompanyCoordinate Data Column Here
USE_COLUMN = ["公司名稱","統一編號","公司地址"]

# Set CompanyCoordinate CompanyName Column Here
COMNAME_COLUMN = "公司名稱"

# Set CompanyCoordinate CompanyTaxNum Column Here
COMTAXID_COLUMN = "統一編號"

# Set CompanyCoordinate CompanyAddress Column Her
COMADDR_COLUMN = "公司地址"

# Set CompanyCoordinate UrlHead Here
URLHEAD = "https://api.map.com.tw/net/GraphicsXY_TWMAP.aspx?search_class=address&searchkey=32FAFAA12E07573A06C6BAFFCC206D162C7C9D49&fun=funA&SearchWord="