### Uploading a File

Once you have created the Bucket, you can upload local files of any types to the Bucket. Each Bucket in COS supports an unlimited number of file storage. For single file upload, the maximum supported size is 50 G; and for single file storage, the maximum supported size is 500 G.

Enter the COS console, click the name of the Bucket to which you want to upload files, and go to the "File List" page of the Bucket:

![](//mc.qcloudimg.com/static/img/79367fa2a4fe4234ccba86de6fb821cf/image.png)

Click **Upload File** on the page, then the dialog box for file uploading will pop up:

![](//mc.qcloudimg.com/static/img/30db79a56efd0c3e9bb5099c907c9849/image.png)

You can click **Upload File** or **Upload Folder** button to upload multiple local files or a folder. Dragging multiple files or folders for uploading is supported by some browsers. After the file has been selected to the list of files to be uploaded, you can still drag the file to the list area to upload it (the area below with a red frame):

![](//mc.qcloudimg.com/static/img/628aa0da6c04aad946d81398e4b2bcad/image.png)

You can also select the folder to which you want to upload files on the file list page, or create a new folder where you can upload the Object.


## Task Management

After you click **OK**, the corresponding upload tasks will be created in the task management list. Users can view the upload progress, terminate unfinished tasks, and check the reason for task failure in the task list.

![](//mc.qcloudimg.com/static/img/a1837dea59c07d1b9e327291abc51317/image.png)

Note: The maximum of 50 G for a single file is supported in the Console. Files more than 50 G will not be successfully uploaded. Besides, a folder whose name contains reserved words (please refer to the naming rule for folder creation) cannot be successfully uploaded either.


## Upload Succeeded

After a file has been successfully uploaded under the current path, the page will display a refresh reminder. Users can click **Refresh** button to get the latest file list.

![](//mc.qcloudimg.com/static/img/c4998edccdac0570019d7351ca707f5a/image.png)

## Incomplete Files and Breakpoint Resume

Files that are suspended from upload will be stored in the form of "incomplete files". Users can view the information of "incomplete files", but cannot download, modify access permission or set custom permission. When users upload the same file next time, the upload will be automatically resumed from the breakpoint without the need to perform other operations.


