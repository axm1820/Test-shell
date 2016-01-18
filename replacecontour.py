#!/usr/bin/python
import os
import sys
import fileinput
rootdir="/Users/akshatmishra/jama/"
for root, subFolders, files in os.walk(rootdir):
   print root
   print subFolders
   for inpfile in files:
       print inpfile
       path=os.path.join(root,inpfile)
       f=open(path,'r')
       filedata = f.read()
       print filedata
       f.close()
       newdata = filedata.replace("contour","jama")
       print newdata
       f = open(path,'w')
       print "************************"
       print "Modifying folder in "+root
       print "Modifing file "+inpfile
       print "*************************"
       f.write(newdata)
       f.close()




