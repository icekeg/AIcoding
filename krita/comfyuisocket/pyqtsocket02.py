from PyQt5 import QtCore, QtGui, QtNetwork
import sys, json     
      
class Example:
  
    def __init__(self):    
        
        self.doRequest()
        
        
    def doRequest(self):   
        
        data = QtCore.QByteArray()
        data.append("name=Peter&")
        data.append("age=34")
    
        url = "http://127.0.0.1:8188"
        req = QtNetwork.QNetworkRequest(QtCore.QUrl(url))
        req.setHeader(QtNetwork.QNetworkRequest.ContentTypeHeader, 
            "application/x-www-form-urlencoded")
        
        self.nam = QtNetwork.QNetworkAccessManager()
        self.nam.finished.connect(self.handleResponse)
        self.nam.post(req, data)    
             
      
    def handleResponse(self, reply):

        er = reply.error()
        
        if er == QtNetwork.QNetworkReply.NoError:
    
            bytes_string = reply.readAll()
            
            json_ar = json.loads(str(bytes_string, 'utf-8'))
            data = json_ar['form']
            
            print('Name: {0}'.format(data['name']))
            print('Age: {0}'.format(data['age']))
            
            print()
            
        else:
            print("Error occurred: ", er)
            print(reply.errorString())
            
        QtCore.QCoreApplication.quit()    
        
           
app = QtCore.QCoreApplication([])
ex = Example()
sys.exit(app.exec_())