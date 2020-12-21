import dropbox
class UploadFiles:
    def __init__(self,access_token):
        self.access_token=access_token
    def upload(self,file_from,file_to):
        dbx = dropbox.Dropbox(self.access_token)
        with open(file_from,"rb") as file1:
            dbx.files_upload(file1.read(),file_to)

def main():
    file_from=input("Enter File Location: ")
    file_to = input("Enter File Destination in Dropbox: ")
    access_token="DSPohvfxDEsAAAAAAAAAAZ4WxKMJWxHs8b0c7u7WAyU69KJJf8d8kGk_RYWDY8RB"
    uploadFiles= UploadFiles(access_token)
    uploadFiles.upload(file_from,file_to)
main()