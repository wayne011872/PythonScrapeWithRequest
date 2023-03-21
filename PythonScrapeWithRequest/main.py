import PythonScrapeWithRequest.Spiders.companyInfo as psc
import PythonScrapeWithRequest.pipelines as pp
import time

def main():
    companyInfoSpider = psc.CompanyInfoSpider()
    for companyInfoSpider.spiderCount in range(companyInfoSpider.startNum,companyInfoSpider.endNum):
        companyInfoSpider.start_requests()
        item = companyInfoSpider.parseResponse()
        companyPipe = pp.companyInfoPipelines(companyInfoSpider)
        companyPipe.processItem(item)
        time.sleep(companyInfoSpider.sleepTime)

main()