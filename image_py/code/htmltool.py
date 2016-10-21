#! coding=utf-8

__author__ = 'ocean'

import re
import HTMLParser
import cgi
import sys
import os

# cash tag class
class htmltool:
    #del img tag, 1-7 spaces
    removeImg = re.compile('<img.*?>| {1,7}|&nbsp;')
    #del href
    removeAddr = re.compile('<a.*?>|</a>')
    #replace line to \n
    replaceLine = re.compile('<tr>|<div>|</div>|</p>')
    #replace <td> to \t
    replaceTD = re.compile('<td>')
    #replace br to \n
    replaceBR = re.compile('<br><br>|<br>')
    #del other tag
    removeExtraTag = re.compile('<.*?>')
    #del space lines
    removeNoneLine = re.compile('\n+')

    #html turn to txt
    #like this '&lt;abc&gt;' --> '<abc>'
    def html2txt(self, html):
        html_parser = HTMLParser.HTMLParser()
        txt = html_parser.unescape(html)
        return txt.strip()

    #html turn to txt
    #like this '<abc>' --> '&lt;abc&gt;'
    def txt2html(self, txt):
        html = cgi.escape(txt)
        return html.strip()

    def replace(self, x):
        x = re.sub(self.removeImg, "", x)
        x = re.sub(self.removeAddr, "", x)
        x = re.sub(self.replaceLine, "\n", x)
        x = re.sub(self.replaceTD, "\t", x)
        x = re.sub(self.replaceBR, "\n", x)
        x = re.sub(self.removeExtraTag, "", x)
        x = re.sub(self.removeNoneLine, "\n", x)
        #strip() del more no use infomation
        return x.strip()

    #get python file current path, return utf-8
    def getPyFileDir(self):
        #get python file path
        path = sys.path[0]
        # judge python file
        if os.path.isdir(path):
            return path.decode('utf-8')
        elif os.path.isfile(path):
            return os.path.dirname(path).decode('utf-8')

    #create dir
    def mkdir(self, path):
        path = path.strip()
        pathDir = self.getPyFileDir()
        print path
        print pathDir
        #unicode
        path = u'%s\\%s' % (pathDir, path)
        #is exist
        isExists = os.path.exists(path)
        #judge result
        if not isExists:
            # False
            print 'new dir [%s]\n' % (path)
            # create dir
            os.makedirs(path)
        else:
            # True
            print 'file dir [%s] is exist\n' % (path)
        os.chdir(path)
        return path
