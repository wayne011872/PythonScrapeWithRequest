import PythonScrapeWithRequest.Spiders.companyCoordinate as psc
import PythonScrapeWithRequest.pipelines as pp
import time

def main():
    companyCoordinateSpider = psc.CompanyCoordinateSpider()
    for companyCoordinateSpider.spiderCount in range(companyCoordinateSpider.startNum,companyCoordinateSpider.endNum):
        companyCoordinateSpider.start_requests()
        item = companyCoordinateSpider.parseResponse()
        companyCoordinatePipelines = pp.companyCoordinatePipelines(companyCoordinateSpider)
        companyCoordinatePipelines.processItem(item)
        time.sleep(companyCoordinateSpider.sleepTime)

main()