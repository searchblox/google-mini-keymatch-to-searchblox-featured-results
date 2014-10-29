__author__ = 'epalmer'

# open the downloaded csv file (from the google mini) in excel
# save as tab separated file and name it googlemini.tsv
# run this program

import os
def main():
    print os.path.dirname(os.path.realpath(__file__))
    infile = os.path.dirname(os.path.realpath(__file__)) + "/files/googlemini.txt"
    outfile = os.path.dirname(os.path.realpath(__file__)) + "/files/outfile.txt"
    print outfile
    urls = dict()
    titles = dict()
    keywords = dict()
    keywords = dict()
    with open(infile, 'rU') as f:
        lineNo = 0
        for line in f:
            lineNo = lineNo + 1
            # uncomment this next line if the program dies
            #print lineNo
            piece = line.strip().split("\t")
            urls[piece[2]] = ""
            titles[piece[2]]=piece[3]
            if piece[2] in keywords.keys():
                keywords[piece[2]].append(piece[0])
            else:
                temp = list()
                temp.append(piece[0])
                keywords[piece[2]] = temp

    startDate = '01/Jan/2014'
    endDate = '01/Jan/2024'
    header = ['startDate', 'keywords', 'status', 'imageUrl', 'expiryDate',
              'useDates', 'type', 'url', 'keywordsFieldType', 'expiryCount',
              'title', 'priority', 'description', 'keywordsUrl']
    headerStr = ('| ').join(header)
    print "Processed ",len(urls), " unique Urls"

    rows = list()
    rows.append(headerStr)
    for key in urls:
        row = list()
        row.append(startDate)
        row.append(','.join(keywords[key]))
        row.append('active')
        row.append('<nil>')
        row.append(endDate)
        row.append('true')
        row.append('TEXT')
        row.append(key)
        row.append('STRING')
        row.append('-1')
        row.append(titles[key])
        row.append('A')
        row.append('<nil>')
        row.append('<nil>')
        rows.append('| '.join(row))

    outfilePtr = open(outfile, 'w')
    for row in rows:
        outfilePtr.write(row)
        outfilePtr.write("\n")
    outfilePtr.close()
if __name__ == '__main__':
    main()