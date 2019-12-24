
"""
class to use google drive 
"""
import os, io
from apiclient.http import MediaFileUpload, MediaIoBaseDownload
from apiclient import errors
class ggdrive:
    def __init__(self, namefoler = "parentfolder" ,
                            namefile = None,
                            ser = None,
                            parentIdfolder = None,
                            size = 10,
                            filepath = None,
                            mimetype = None,
                            fileId = None,
                            new_title = None,
                            new_description = None,
                            new_mime_type = None,
                            new_filename = "unname",
                            new_revision = True,
                            ):
     
        self.namefoler = namefoler 
        self.namefile = namefile 
        self.ser = ser
        self.parentIdfolder = parentIdfolder 
        self.size = size
        self.filepath = filepath
        self.mimetype = mimetype
        self.fileId = fileId
        # set new for update file for google drive 
        self.new_title = new_title
        self.new_description = new_description
        self.new_mime_type = new_mime_type
        self.new_filename = new_filename
        self.new_revision = new_revision
    # is file exsting ?
    def isfolderexst(self):
        check = False

        results = self.ser.files().list(q="name='" + self.namefoler +\
                                        "' and mimeType='application/vnd.google-apps.folder'\
                                        and trashed=false",
                                        fields="nextPageToken, files(id, name)"
                                        ).execute()

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
    def isfilerexst(self):
        check = False

        results = self.ser.files().list(q="name='" + self.namefile + "' and mimeType='image/jpeg'",
                                        fields="nextPageToken, files(id, name)"
                                        ).execute()

        items = results.get('files',[])
        try:
            for item in items:
                if item['name'] == self.namefile:
                    check = True
                    return check
        except:
            print  ("not any folder")
            check = False
            return check 
    
    # to check exiting file ? 
    def refoidifext ( self):
        
        results = self.ser.files().list(q="name='" + self.namefoler + "' \
                                        and mimeType='application/vnd.google-apps.folder'\
                                        and trashed=false",
                                        fields="nextPageToken, files(id, name)"
                                        ).execute()
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
        if self.parentIdfolder:
            body['parents'] = [{'id': 
                                self.parentIdfolder}]

        root_folder = self.ser.files().create(
                                            body = body,
                                            fields='id'
                                            ).execute()
        return root_folder.get('id')
        
    def listFiles(self):
        results = self.ser.files().list(pageSize= self.size,
                                        fields="nextPageToken,\
                                        files(id, name)"
                                        ).execute()
        items = results.get('files', [])
        if not items:
            print('No files found.')
        else:
            for item in items:
                print('{0} ({1})'.format(item['name'],
                                         item['id']))

    def uploadFile(self):
        file_metadata = {
                        'name': self.namefile,
                        'parents': [self.parentIdfolder]
                        }
        
        media = MediaFileUpload(self.filepath,
                                mimetype=self.mimetype,
                                )
                                
        file =self.ser.files().create(body=file_metadata,
                                      media_body=media,
                                      fields='id'
                                      ).execute()
        print('File ID: %s' % file.get('id'))

    #--------------------------->>>>>>>>>
    """
    if folder is not exting, it'll create with namefolder from user 
    else it'll not  create folder 
    file is exting, it'will be overriden  else it create one with namefile 
    """
    def uploadFilewithoverfolderandfile(self):
        # get folder id to create or get folder
        folderid =  self.refoidifext() if self.isfolderexst() == \
                    True else self.refoidifnotext()
        # set folder id for parent 
        print (folderid)
        self.parentIdfolder= folderid
        # get ID by name file
        newfileid = self.getIdbynamefile()
        # set id of file to fileid 
        self.fileId = newfileid
        # if exsting is upload else update 
        self.update_file() if newfileid != None else self.uploadFile()
    #<<<<<<<<<<<<-----------------------

    def uploadFilenovr(self):
        file_metadata = {
                        'name': self.namefile,
                        'parents': [self.parentIdfolder]
                        }
        
        media = MediaFileUpload(self.filepath,
                                mimetype=self.mimetype,
                                )
                                
        file =self.ser.files().create(body=file_metadata,
                                            media_body=media,
                                            fields='id').execute()
        print('File ID: %s' % file.get('id'))

    def downloadFile(self):
        request = self.ser.files().get_media(fileId=self.fileId)
        fh = io.BytesIO()
        downloader = MediaIoBaseDownload(fh, request)
        done = False
        while done is False:
            status, done = downloader.next_chunk()
            print("Download %d%%." % int(status.progress() * 100))
        
        with io.open(self.filepath,'wb') as f:
            fh.seek(0)
            f.write(fh.read())
        
    def createFolder(self):
        file_metadata = {
                        'name': self.namefoler,
                        'mimeType': 'application/vnd.google-apps.folder'
                        }
        file = self.ser.files().create(body=file_metadata,
                                            fields='id').execute()
        print ('Folder ID: %s' % file.get('id'))

    def searchFile(self,query):
        results = self.ser.files().list(
        pageSize=self.size, fields="nextPageToken, files(id, name, kind, mimeType)",
                                                            q=query).execute()
        items = results.get('files',[])
        if not items:
            print('No files found.')
        else:
            print('Files:')
            for item in items:
                print('{0} ({1})'.format(item['name'],
                                         item['id']))
    def getIdbynamefile(self):
        results = self.ser.files().list(pageSize= self.size,
                                        fields="nextPageToken, files(id, name)")\
                                        .execute()
        items = results.get('files', [])
        if not items:
            print('No files found.')
            return None
        else:
            for item in items:
                if item['name'] == self.namefile:
                    return  item['id']
                else:
                    print ("Can not file name {}".format(self.namefile))
                    return None

    # update file for existing file 
    def update_file(self):
        """Update an existing file's metadata and content.

        Args:
            service: Drive API service instance.
            file_id: ID of the file to update.
            new_title: New title for the file.
            new_description: New description for the file.
            new_mime_type: New MIME type for the file.
            new_filename: Filename of the new content to upload.
            new_revision: Whether or not to create a new revision for this file.
        Returns:
            Updated file metadata if successful, None otherwise.
        """
        try:
            # First retrieve the file from the API.
            file = self.ser.files().get(fileId = self.fileId).execute()

            # File's new metadata.
            file_metadata = {
                            'name': [self.new_filename],
                            }

            if self.isfilerexst() == True:
                media_body = MediaFileUpload(self.filepath,
                                        mimetype=self.new_mime_type,
                                        )
                # Send the request to the API.
                updated_file = self.ser.files().update(
                                                    fileId=self.fileId,
                                                    body = file_metadata,
                                                    ).execute()

            else:
                print("no file to update")

            #return updated_file
        except AttributeError as er:
            print (er)
    def uploadfoldertoggdriveover(self):
        file_metadata = {
                        'name': self.namefoler,
                        'mimeType': 'application/vnd.google-apps.folder'
                        }
        media = MediaFileUpload('files/photo.jpg',
                        mimetype='image/jpeg')
                
        file = self.ser.files().create(body=file_metadata,
                                            fields='id').execute()
        print ('Folder ID: %s' % file.get('id'))
"""
def upload_file(access_token, filename, filepath, parentID = "root"):
    query_link = 'https://www.googleapis.com/upload/drive/v3/files'
    query_params = "?uploadType=multipart"
    link = '{0}{1}'.format(query_link, query_params)
    headers = {"Authorization": "Bearer " + access_token}
    meta_data = {
        "name": filename,
        "parents": [{"id": parentID}]
                }
    files = {
        "data": ("metadata", json.dumps(meta_data), "application/json; charset=UTF-8"),
        "file": open(filepath + "\\" + filename, 'rb')
            }
    response = requests.post(link, headers=headers, files=files)
"""