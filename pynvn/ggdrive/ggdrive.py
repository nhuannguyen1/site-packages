
"""
class to use google drive 
"""
import os, io
from apiclient.http import MediaFileUpload, MediaIoBaseDownload
class ggdrive:
    def __init__(self, namefoler = None ,
                            namfle = None,
                            ser = None,
                            parentID = None,
                            size = 10,
                            filepath = None,
                            ):

        self.namefoler = namefoler 
        self.namfle = namfle 
        self.ser = ser
        self.parentID = parentID 
        self.size = size
        self.filepath = filepath

    # is file exsting ?
    def isfilexst(self):
        check = False

        results = self.ser.files().list(q="name='" + self.namefoler + "' and mimeType='application/vnd.google-apps.folder' and trashed=false",
                                         fields="nextPageToken, files(id, name)").execute()

        items = results.get('files',[])
        try:
            for item in items:
                if item['name'] == self.namefoler:
                    check = True
                    return check
        except:
            print  ("not any folder")
            check = False
            return check 
            
    # to check exiting file ? 
    def refoidifext ( self):
        
        results = self.ser.files().list(q="name='" + self.namefoler + "' and mimeType='application/vnd.google-apps.folder' and trashed=false",
                                         fields="nextPageToken, files(id, name)").execute()
        items = results.get('files',[])
        if not items:
            print('No files found.')
            return  None 
        else:
            for item in items:
                if item['name'] == self.namefoler:
                    return item['id'] 
                    break
                else:
                    return None

    # return folder id if exsting
    def refoidifnotext(self):
        # Create a folder on Drive, returns the newely created folders ID
        body = {
                'name': self.namefoler,
                'mimeType': "application/vnd.google-apps.folder"
                }

        # check parentID ! = None ?
        if self.parentID:
            body['parents'] = [{'id': 
                                self.parentID}]

        root_folder = self.ser.files().create(
                                            body = body,
                                            fields='id')\
                                                .execute()
        return root_folder.get('id')
        
    def listFiles(self):
        results = self.ser.files().list(
            pageSize= self.size,fields="nextPageToken, files(id, name)").execute()
        items = results.get('files', [])
        if not items:
            print('No files found.')
        else:
            print('Files:')
            for item in items:
                print('{0} ({1})'.format(item['name'], item['id']))

    def uploadFile(self,mimetype):
        file_metadata = {'name': self.namfle}
        media = MediaFileUpload(self.filepath,
                                mimetype=mimetype)
        file = self.ser.files().create(body=file_metadata,
                                            media_body=media,
                                            fields='id').execute()
        print('File ID: %s' % file.get('id'))

    def downloadFile(self,file_id):
        request = self.ser.files().get_media(fileId=file_id)
        fh = io.BytesIO()
        downloader = MediaIoBaseDownload(fh, request)
        done = False
        while done is False:
            status, done = downloader.next_chunk()
            print("Download %d%%." % int(status.progress() * 100))
        with io.open(self.filepath,'wb') as f:
            fh.seek(0)
            f.write(fh.read())

    def createFolder(self,name):
        file_metadata = {
        'name': name,
        'mimeType': 'application/vnd.google-apps.folder'
        }
        file = self.ser.files().create(body=file_metadata,
                                            fields='id').execute()
        print ('Folder ID: %s' % file.get('id'))

    def searchFile(self,size,query):
        results = self.ser.files().list(
        pageSize=size,fields="nextPageToken, files(id, name, kind, mimeType)",q=query).execute()
        items = results.get('files', [])
        if not items:
            print('No files found.')
        else:
            print('Files:')
            for item in items:
                print(item)
                print('{0} ({1})'.format(item['name'], item['id']))