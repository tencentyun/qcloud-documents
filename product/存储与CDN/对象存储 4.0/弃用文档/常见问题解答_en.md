- When the files stored in COS are under DDoS attacks, will traffic fee be generated?
  Hotlink protection will protect files from generating traffic when under DDoS attack. For more information, refer to [Hotlink Protection Configuration](/doc/product/436/6250).

- Can I download files after the 50G free traffic of the month is used up while there is no account balance?
  Every month, you will get 50G free traffic. The extra amount is subject to tiered pricing. The bill for the current month will be generated between the 3rd and 5th day of the next month. If the bill is not settled, we will remind you via email and SMS. You need to pay the bill before the deadline; otherwise your account will be frozen. For more information, refer to instructions on how to freeze an account.

- Why does not a download URL end with a file name?
  Since the storage is set to be private, a signature is added to the accessed URL.

- What can I do if a message indicates signature mismatch when uploading?
  Check whether there are omissions in the signature you entered, and ensure that there is no unnecessary character between sign and the signature.

- What can I do if a message indicates that appid/userid does not match the signature when creating Bucket on the page?
  It may be caused by the occasional system error due to key application failure. Click on https://console.cloud.tencent.com/cos/project to assign the key automatically or contact developers to resolve the problem.

- When I upload files to COS, will folders contained in the full path of the specified files on COS server be created automatically?
  No. You need to create folders in advance.

- Is the signature required when I only upload files on the server?
  Yes. Files will be uploaded to the COS server.

- How to download a file through the download URL after the file is deleted in COS?
  After the file is deleted in COS, the deletion takes effect in COS immediately. But for each CDN node, it takes some time to synchronize the operation. You can request each time a signature with a short validity period from your service server to prevent possible data theft.

- Is user identification required when I want to get a specified file in COS? For example, can I get a file if I do not log in?
  You can set Bucket to private read and write. For more information, refer to Access Permission.

- Is there a limit to the number of Buckets?
  The maximum number of Buckets under all the projects with the same APPID is 200. However, there is no limit to the number of directories and files under a Bucket.

- Does COS support remote file uploading? For example: http:/lwww.*.com/ uploadfile/avatar.png
  Restful API in COS supports remote file uploading. Each language provides an SDK that encapsulates the Restful API.

- How to get a signature when uploading files to COS?
  When files are uploaded to COS via mobile devices, the service server needs to deploy signature service by referring to server SDK. After getting the signature from the server, the mobile device will be granted the uploading permission. In this way, the decompilation of SDK can be avoided, thus preventing any security risks arising from the disclosure of APP ID, SecretID and SecretKey. For more information, refer to Permission Control.

- Can upload be accelerated by using COS in Tencent CVM?
  Files are uploaded to COS through the private network of Tencent Cloud CVM. But COS and CVM are not located in the same data center. Uploading files through private network can protect the network stability from being affected by the fluctuation of public network can not affect network stability.

- Can COS provide statistical data?
  Yes. On Bucket Monitor Report page, you can view statistical data and trends of storage usage, traffic usage, number of requests and other dimensions of resources in the Bucket.

- Does Tencent Cloud COS support backup by users?
  Currently, COS does not support backup by users. But Tencent Cloud has automatic backup mechanism to prevent the loss of files.

- Can I bind my domain in COS?
  Yes. You can configure it through CNAME. For more information, refer to Domain Management.

- How to set CNAME address in COS?
  The default format is {bucket}-{appid}.file.myqcloud.com. You can enter your information in Bucket and appid.

- Can I set response mine-type?
  Common types can be set.

- What is the address for back-to-origin requests used for?
  For migration. Specifically, if the accessed resource does not exist in COS, it will be pulled from the address for back-to-origin requests.

- If the path for back-to-origin requests is not created in COS, will a directory be created automatically when the path is accessed?
  Yes. A directory will be automatically pulled and created for back-to-origin requests.

- Does COS support FTP uploading or can COS be used as NFS by storing all attachments of a site in it?
  Currently, COS supports FTP whitelist, but NFS has not been scheduled yet.

- How long is the maximum validity period of a signature? How to make a download URL valid permanently?
  You can set the Bucket to public,  so that files under this Bucket can be downloaded even without authentication.

- How to control COS master account's read and write permission to data of ordinary users when they upload personal data to COS through APPs?
  You can create a Bucket via an APP, set the Bucket to private read and write, and create a folder for each user ID so as to control every user's access to the folder via the APP. You need to set permission for different users at your service backend to decide whether to allocate a signature.

- What can I do if such information as APP ID, SecretID and SecretKey is disclosed?
  Create a new key to replace the previous one. For more information, refer to Permission Control - Key Management.

- Can I create or delete Bucket via COS APIs?
  Currently, you cannot work with Bucket via APIs, but only on the console.

- Can the upload be resumed from a breakpoint in COS?
  Breakpoint resume is applicable to all SDKs and the Restful APIs.

- Which algorithm of opensslcrypto is used in C++ SDK?
  HmacEncode is used to calculate a signature and SHA-1 is used to calculate the hash value of a file.

- Does Tencent Cloud COS provide APIs for the batch upload of images via H5?
  Yes. You can batch select files via H5, and then send an HTTP request through js to upload files. We provide the Restful API or the integrated SDK to support the function.

- Can I use COS SDKs and Cloud Image SDKs at the same time to store images, videos and audios?
  Yes. You can use the both at the same time. But, COS can only be used for storage and does not provide additional functions, and Cloud Image can be used to process images.


