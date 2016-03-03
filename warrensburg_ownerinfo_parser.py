import re
import csv
from collections import Counter
class AddressParser:
    def __init__(self):
        self.addressLines = []
        self.addressList = []
        self.f = None
        self.recIdRgx = re.compile('^\*+\s(.*?)\s.*$')
        self.addrListClean = []
        self.entry_sizes = []
        self.entry_size_table = {}
        self.rec_size_freq = ()
        self.listOfAddresses = []
        self.addressFields = [] 
    def isRecHeader(self,line):
        recStart = re.compile('\*{103}\s\d+.*')
        if recStart.match(line):
            return True
        else:
            return False
    def parseFile(self, filename):
        state = 'START'
        recStart = re.compile('\*{103}\s\d+.*') 
        self.f = None
        self.f = open(filename, 'r')
        for line in self.f:
            line.replace("\r\n","")
            line.replace('\t','        ')
            # print "At state " + state + " w/Current line: " + line
            if state == 'START' and self.isRecHeader(line):
                state = 'CONTENT'
                # print "Found new record, switching from START to CONTENT."
                self.addressLines = []
                self.addressLines.append(self.extractId(line))
                self.addressLines.append(line)
            elif state == 'CONTENT' and not self.isRecHeader(line):
                # print "\tNo delimiter; adding line to addressLines."
                self.addressLines.append(line)
            elif state == 'CONTENT' and  self.isRecHeader(line):
                # print "\tDelimiter encountered. adding addressLines to addressList, changing to START."
                state = 'START'
                self.addressList.append(self.addressLines)
                self.addressLines = []
                self.addressLines.append(self.extractId(line))
                self.addressLines.append(line)
            elif state == 'START' and not self.isRecHeader(line):
                # print "\tNo delimiter: adding line and changing to CONTENT"
                state = 'CONTENT'
                self.addressLines.append(line)
            else:
                print "No valid state for given line."
        self.removeNonEntries()
    def extractId(self,line):
        match = self.recIdRgx.match(line)
        if match is None:
            print "possible error, returning generic record id."
            return "NO_REC_ID"
        else:
            return self.recIdRgx.match(line).group(1)
    def removeNonEntries(self):
        for i, entry in enumerate(self.addressList):
            print "Checking for district summary at index ", str(i)
            if len(entry) > 2:
                if entry[1] == '':
		    del(self.addressList[i])
        print "District summaries deleted."
    def split_addr(self,addresses): 
        new_addresses = [] 
        for addr in addresses: 
            if len(addr) > 2: 
                m = re.search('^(\d+\s)(.*)$', addr[1]) 
                if m: 
                    num = m.group(1) 
                    street = m.group(2) 
                    addr.append(num) 
                    addr.append(street) 
                    new_addresses.append(addr) 
                    addr = []
                else: 
                    num = 'NN'
                    entity = addr[1]
                    addr.append(num)
                    addr.append(entity)
                    new_addresses.append(addr)
            else: 
                new_addresses.append(addr.append('missing')) 
        return new_addresses
    def write_to_csv(self,filename,addresses):
        with open(filename, 'wb') as csvfile:
            csvwriter = csv.writer(csvfile, delimiter=',',
                            quotechar='"', quoting=csv.QUOTE_MINIMAL)
            for addr in addresses:
               csvwriter.writerow(addr)
    def deleteIfAboveSize(self, n):
        for i, entry in enumerate(self.addressList):
            if len(entry) > n:
                print "Deleting record " + str(i) + "as greater than length " + str(n)
                del self.addressList[i]
        print "Complete."
    def deleteBadRecs(self):
        for i, entry in enumerate(self.addressList):
            print entry[0]
            if entry[0] == '' or entry[0] == 'NO_REC_ID' or entry[0] == '*':
                del self.addressList[i]

# create function to slice by character count... 
        return line[31:59].strip()
    def getOwnerInfo(self):
        recIdRgx = re.compile('\d+\.\d+.*')
        propertyData = [] 
        properties = []
        for index in range(0,len(
        for entry in self.addressList:
            recId = entry[0]
            propertyData.append(recId)
            if recIdRgx.match(recId):
                propertyData.append(entry[3])
                propertyData.append(entry[4]))
                propertyData.append(entry[5]))
                propertyData.append(entry[6]))
                propertyData.append(entry[7]
                properties.append(propertyData)
                propertyData = []
        return properties
    def extractOwnerFields(self):
        pass
