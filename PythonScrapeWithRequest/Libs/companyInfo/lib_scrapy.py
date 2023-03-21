import pythonGeneral.dataProcessing.string as pds
import re


def setItems(item, taxIdNum, companyName, phone, capitalAmount, email, website, companyAddress):
    item.taxIdNum = taxIdNum
    item.companyName = companyName
    item.phone = phone
    item.capitalAmount = capitalAmount
    item.email = email
    item.website = website
    # item.responsibleName = responsibleName
    item.companyAddress = companyAddress
    return item

def getTWCompanyResponsibleName(soup):
    responsibleName = soup.find_all('p', {'class': 'lead wow fadeIn'})
    splitbrs  = str(responsibleName[0]).split('<br/>')
    for splitbr in splitbrs:
        if ('代表人' in splitbr):
            res = str(re.findall('代表人 (..*)', splitbr))
            print(type(res))
            return res
    return ""
def getTWCompanyAddress(soup):
    address = soup.find_all('p', {'class': 'lead wow fadeIn'})
    splitbrs = str(address[0]).split('<br/>')
    for splitbr in splitbrs:
        if ('市' in splitbr):
            add = str(splitbr)
            return add
    return ""
def getTWCompanyPhoneNum(soup):
    phonenums = soup.find_all('p', {'class': 'lead wow fadeIn'})
    splitbrs = str(phonenums[0]).split('<br/>')
    for splitbr in splitbrs:
        if ('電話' in splitbr):
            phonenum = str(re.findall('電話 :(..*)', splitbr))
            phosub = re.sub('\D', '', phonenum)
            phone = pds.reString(phosub)
            try:
                phone.processPhoneNum("台北")
                return phone.getProcessString()
            except:
                return ""
    return ""
def getTWCompanyCapital(soup):
    capitalData = soup.find_all('table', {'id': 'basic-data'})
    if capitalData:
        capitalDatum = str(capitalData).split("<tr>")
        for d in capitalDatum:
            if '資本總額(元)' in d:
                data = d.split('<td>')
                if len(data) > 2:
                    capitalData = data[2].split('</td>')
                    if len(capitalData) > 1:
                        return re.sub('\D', '', str(capitalData[0]))
    return ""

def getTWCompanyEmail(soup):
    emailData = soup.find_all('table', {'id': 'basic-data'})
    if emailData:
        emailDatum = str(emailData).split("<tr>")
        for d in emailDatum:
            if 'Mail' in d:
                data = d.split('<td>')
                if len(data) > 2:
                    mailData = data[2].split('</td>')
                    if len(mailData) > 1:
                        return mailData[0]
    return ""

def getTWCompanyWeb(soup):
    webData = soup.find_all('table', {'id': 'basic-data'})
    if webData:
        webDatum = str(webData).split("<tr>")
        for d in webDatum:
            if '網址' in d:
                data = d.split('<td>')
                if len(data) > 2:
                    webData = data[2].split('</td>')
                    if len(webData) > 1:
                        return webData[0]
    return ""

def getDictItems(item):
    itemDict = {}
    itemDict["companyName"] = pds.deleteSpace(item.companyName)
    itemDict["taxIdNum"] = pds.deleteSpace(item.taxIdNum)
    itemDict["capitalAmount"] = pds.deleteSpace(item.capitalAmount)
    # itemDict["responsibleName"] = pds.deleteSpace(item.responsibleName)
    itemDict["companyAddress"] = pds.deleteSpace(item.companyAddress)
    itemDict["phone"] = pds.deleteSpace(item.phone)
    itemDict["email"] = pds.deleteSpace(item.email)
    itemDict["website"] = pds.deleteSpace(item.website)
    return itemDict