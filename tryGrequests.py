__author__ = "al walker"

import grequests

# read in urls from file
with open("urls.txt") as f:
    urls = f.read().splitlines()

rs = (grequests.get(u) for u in urls)

resp = grequests.map(rs)

listresult = list(resp)

print listresult
for x in listresult:
    rurl = x.url
    rtext = x.content
    rstat = x.status_code
    rtime = x.elapsed.microseconds / 1000.
    print "+++Url -> ", rurl, " Status -> ", rstat, "  Elapsed Time -> ", rtime, "milliseconds \n"
    #    print "   Content -> ", rtext
    print "--- \n"
