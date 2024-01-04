#from krita import *
#Krita.instance().action("ten_brushes").trigger()
#Krita.instance().action("ten_scripts").trigger()
#Krita.instance().action("color_space").trigger()
#Krita.instance().action("python_scripter").trigger()
#doc = Krita.instance().createDocument(100, 100, "Doc1", "RGBA", "U8", "", 120.0)
#Krita.instance().activeWindow().addView(doc)
#!/usr/bin/python3
# -*- coding: utf-8 -*-
from PyQt5 import  QtNetwork
from PyQt5.QtCore import QCoreApplication, QUrl
import sys
            
class Example:
  
    def __init__(self):    
        
        self.doRequest()
        
        
    def doRequest(self):   
    
        url = "http://127.0.0.1:8188"
        req = QtNetwork.QNetworkRequest(QUrl(url))
        
        self.nam = QtNetwork.QNetworkAccessManager()
        self.nam.finished.connect(self.handleResponse)
        self.nam.get(req)    
             
      
    def handleResponse(self, reply):

        er = reply.error()
        
        if er == QtNetwork.QNetworkReply.NoError:
    
            bytes_string = reply.readAll()
            print("ooo")
            print(str(bytes_string, 'utf-8'))
            
        else:
            print("Error occured: ", er)
            print(reply.errorString())
            
        QCoreApplication.quit()    
        

app = QCoreApplication([])
ex = Example()
sys.exit(app.exec_())
