## 1. Steps for File Release
Step 1. Uploading/Updating CDN files via SVN
For details on how to use SVN, refer to How to Use SVN on Windows or How to Use SVN on Linux.
When using SVN, you need to enter the SVN library path, as well as the user name and password, which can be viewed in the CDN "File Release" page of the Console, as shown below:
![](https://mccdn.qcloud.com/static/img/56f91c137833a1667c82a1b9aecc6b0b/image.png)

Step 2. Validating files to each CDN server
On the CDN "File Release" page, click the "Validate CDN File" button, and the new uploaded file will be synchronized to each CDN server within 5 minutes.

Simplified steps for file release:
![](https://mccdn.qcloud.com/static/img/625b3e88e1bac241fe7bcd619618c406/image.png)
Step 1. Setting the "Auto validate" function
If the developer can guarantee the correctness and validity of the files uploaded to the CDN server, the function can be firstly set as "Enabled" on the CDN "File Release" page.


Step 2. Uploading/updating CDN files via SVN
Any changes to the files on SVN will be automatically synchronized to the CDN server nodes. Thus, there's no need to click on the "Validate CDN File" button after each update.
Note: Any file changes on the SVN before the "Auto validate" function is enabled will not be automatically synchronized. If you want to synchronize, click the "Validate CDN File" button.

## 2. Access the released files on CDN
The files released on CDN can be accessed by using the URL address given on the CDN "File Release" page.
![](https://mccdn.qcloud.com/static/img/7f4bda0577446fa6e2ce4eb5888df912/image.png)

For example:
Your account of Cloud Services is 1251000013. Using the SVN client, create the img directory at https://cdn.yun.qq.com/1251000013 and upload the file CVM.png to the img directory. After the CVM.png file is validated, the image can be accessed by using the following CDN public network address:
`http://1251000013.cdn.myqcloud.com/1251000013/img/CVM.png`
