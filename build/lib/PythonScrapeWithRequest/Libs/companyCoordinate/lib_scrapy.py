import pythonGeneral.dataProcessing.string as pds
def setItems(item, taxIdNum, companyName, companyLatitude, companyLongitude):
    item.taxIdNum = taxIdNum
    item.companyName = companyName
    item.latitude = companyLatitude
    item.longitude = companyLongitude
    return item

def getDictItems(item):
    longitudeRe = pds.reString(item.longitude)
    latitudeRe = pds.reString(item.latitude)
    itemDict = {}
    coordinateList = []
    coordinateList.append(float(longitudeRe.deleteSpace()))
    coordinateList.append(float(latitudeRe.deleteSpace()))
    positionDict = {}
    positionDict["type"] = "Point"
    positionDict["coordinates"] = coordinateList
    itemDict["companyName"] = pds.deleteSpace(item.companyName)
    itemDict["taxIdNum"] = pds.deleteSpace(item.taxIdNum)
    itemDict["position"] = positionDict
    return itemDict