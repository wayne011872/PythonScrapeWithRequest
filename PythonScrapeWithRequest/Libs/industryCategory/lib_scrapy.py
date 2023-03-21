import pythonGeneral.dataProcessing.string as pds


def setItems(item, taxIdNum, companyName, category):
    item.taxIdNum = taxIdNum
    item.companyName = companyName
    item.category = category
    return item


def getCategoryUrl(soup):
    try:
        categoryData = soup.find_all('a')[4]["href"].split("=")
    except:
        print("取category url時錯誤")
    else:
        if len(categoryData) == 2:
            return categoryData[1]
    return ""

def getCategory(soup):
    categoryData = soup.select('section#menu1 label')
    if categoryData:
        categoryStr  = pds.reString(str(categoryData[0]))
        categoryStr.deleteSpace()
        categoryStr.splitChar('\n',1)
        categoryStr.substituteOneString('\r','')
        return categoryStr.processStr
    return ""

def getDictItems(item):
    itemDict = {}
    itemDict["companyName"] = pds.deleteSpace(item.companyName)
    itemDict["taxIdNum"] = pds.deleteSpace(item.taxIdNum)
    itemDict["category"] = pds.deleteSpace(item.category)
    return itemDict
