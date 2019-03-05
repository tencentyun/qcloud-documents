## 1. What if the backend configuration parameters are incorrect?
### 1.1 appid or bizid 
The main indication is that the VJ push always fails. The main reason is that the generated push address is invalid, and Tencent Cloud rejects the push request. In the log, you can see the message **RTMP server actively disconnects**.

![](//mc.qcloudimg.com/static/img/e3b6f9f974f561e0e3ef182580445673/image.png)

### 1.2 Push hotlink protection key 
The main indication is that the LVB push always fails. The main reason is that the push hotlink protection key involves in the txSecret computing. And push hotlink protection key error leads to txSecret error, eventually resulting in the txSecret verification failure from the server, and Tencent Cloud rejects the request. In the log, you can see the message **RTMP server actively disconnects**.

![](//mc.qcloudimg.com/static/img/fca49e4e78c906ff27461fa8594b6d58/image.png)

### 1.3  API authentication key 
The main indication is that the push playback is normal, but it does not appear in the playback list of the terminal.
Generation process of playback record:
- At the end of the LVB, Tencent Cloud completes the recording and notifies the mini LVB backend using the callback URL configured on the console.
- The mini LVB backend verifies the validity of the callback via API authentication key. If the verification fails, the playback record will not be inserted in the database.
- If the callback passes the verification, a playback record will be written to the tape_data table.
- You can only have a playback record after the record is written to the database successfully.
 
The main reason is that the configuration of the API authentication key is incorrect, and it leads to the callback authentication failure in the service backend, thus no playback record is generated.

### 1.4  COS APPID 
The main indication is the upload failure of profile photo and cover. The main reason is that the signature used by the COS upload request is issued by the business backend. Due to the signature error, the COS upload request fails. This can be confirmed by the terminal's log keyword "**ERROR_PROXY_APPID_USERID_NOTMATCH**".

![](//mc.qcloudimg.com/static/img/378e8a055f12f6aa77b2958ad1c3f149/image.png)

### 1.5  COS bucket name 
The main indication is the upload failure of profile photo and cover. The main reason is that the COS bucket can be considered as a virtual disk, and the COS upload fails if the disk is specified incorrectly, and the error "Bucket cannot be found" will be prompted. This can be confirmed by the terminal's log keyword "**ERROR_PROXY_SIGN_BUCKET_NOTMATCH**".
 
 ![](//mc.qcloudimg.com/static/img/92e096149bef3408c9713df93ab321ac/image.png)
 
### 1.6 COS SecretId 
 The main indication is the upload failure of profile photo and cover. The main reason is that the signature used by the COS upload request is issued by the business backend. COS SecretId is used to specify the key used by the signature. It must be paired with the COS SecretKey. This can be confirmed by the terminal's log keyword "**PROXY_AUTH_SECRETID_NOEXIST**".
 
 ![](//mc.qcloudimg.com/static/img/3fbfd0180fc165784c1ce30e513be5c7/image.png)
 
### 1.7  COS SecretKey 
 The main indication is the upload failure of profile photo and cover. The main reason is that the signature used by the COS upload request is issued by the business backend. The COS SecretKey error causes the signature failure. This can be confirmed by the terminal's log keyword "**ERROR_PROXY_AUTH_FAILED**".
 
 ![](//mc.qcloudimg.com/static/img/f1ac76d8ea4b70b883c4a45d74ee888d/image.png)

## 2. What if the terminal (taking IOS as an example) parameters are incorrect?
### 2.1 kTCIMSDKAppId or kTCIMSDKAccountType
The main indication is login failure.

![](//mc.qcloudimg.com/static/img/0b18fc2a7d5f7f86bbd4d56f743cee1e/image.png)

### 2.2 kTCCOSAppId or kTCCOSBucket
The main indication is the upload failure of profile photo or cover. The log is shown as follows:

![](//mc.qcloudimg.com/static/img/4192cf72b525664098fb69cd2e02ba7c/image.png)

### 2.3 kTCCOSRegion 
The main indication is the upload failure of profile photo or cover. The main reason is that kTCCOSRegion is a new parameter of COS 4.0, which is used to specify the location of the COS data center, and if it is configured incorrectly, it prompts that the bucket cannot be found. The log is shown as follows:

![](//mc.qcloudimg.com/static/img/b023701ec5c2fe69ab35816b422afe16/image.png)

### 2.4 kHttpServerAddr 
The main indication is that related features such as pulling list are exceptional, and it prompts that the request times out. The main reason is that the terminal does not access the correct backend service due to the incorrect server address.

![](//mc.qcloudimg.com/static/img/c1ce2290019c67ae00395be67360e3d5/image.png)

## 3. Why do I fail to pull the playback list?
The generation process of playback list is described in **1.3  API Authentication Key**. The playback list is stored in the data table tape_data. Pull failure causes can be checked from the following aspects.

![](//mc.qcloudimg.com/static/img/f28487d33a502e571737bc9c687647ac/image.png)

### 3.1 Whether the database write operation after callback is normal
 Generally, if you do not change our backend source code, there will be no problem. If you have changed the createDB script, then it is necessary to check here. Log is a good tool for troubleshooting. To enable log debugging at the backend is simply to create a log directory under the live_demo_service/ directory. Check mysql_XXXX.log. Failure of the database inserting operation may be caused by field attribute modification.
 
### 3.2 Whether the API authentication key is correct
 Make sure that the value of CALL_BACK_KEY in OutDefine.php is the same as the console API authentication key. Its role has been explained above.
 
### 3.3 Whether callback URL is configured correctly
 Check whether the callback URL is correctly entered in Tencent Cloud Official Website -> Console -> LVB -> Access Management -> LVB Code Access -> Access Configuration. If it is incorrect, the business backend will not receive a callback notification from Tencent Cloud Server after the LVB ends, and no playback record will be generated.
 
![](//mc.qcloudimg.com/static/img/61187098d48fecd3f4554d45a8503aa6/image.png)

## 4. Why do I fail to pull the playback list?
It is generated mainly based on the live_data (LVB list) and tape_data (playback list) of the database. Make sure **kHttpServerAddr** is entered correctly if the terminal network is normal. You can check the server.
After the App is logged in on Android, if it prompts a failure of list pull, you can see the message "**HTTP Req error, error code:500**" in logcat. Similarly, after the App is logged in on iPhone, it prompts **internal server error**. Open the mysql_errorxxxxxxxx.log in the backend log directory, and you can see the message **mysqli_connect failed, error:Access denied for user 'live_user'@'localhost' to database 'live'**].
The API failure is caused by database access failure. The confirmation method is to open the cdn.route.ini file in the live_demo_service/conf directory, and ensure that the DB parameters are the same as those you specified when creating the database. PHP accesses the local database via the parameters specified by cdn.route.ini. The mapping relationship is shown as in the figure:

![](//mc.qcloudimg.com/static/img/1a5a63e3ac06eb9eab85a0b0ed1b8879/image.png)


## 5. Why do I fail to pull the profile photo or cover?
The main indication is that the profile photo or the cover are successfully uploaded, but I failed to download them. The main reason is that the domain name acceleration of COSv4 is disabled by default. The COS upload returns the address of CDN. You can set the domain name acceleration to solve the problem.

![](//mc.qcloudimg.com/static/img/a2fd6cf344295b547d8d7c417142af45/image.png)

## 6. Why does the upload still fail with the COS parameters configured correctly?
- **Main indication**: COS parameters, terminal and mini LVB backend settings are correct, but the upload of the profile photo and cover still fails.
- **Main reason**: In November 2016, the COS server was upgraded with the region parameter added. The new system and the old one are completely independent and need to be used in combination with the cos sdk version of the corresponding terminal. All newly activated COS services use cos sdk v4. For old versions of COS, you can [submit a ticket](https://console.cloud.tencent.com/workorder/category/create?level1_id=83&level2_id=84&level1_name=%E5%AD%98%E5%82%A8%E4%B8%8ECDN&level2_name=%E5%AF%B9%E8%B1%A1%E5%AD%98%E5%82%A8%20COS) to apply to switch it to the new COS version. From December 30, 2016, mini LVB source code package is also equipped with the terminal cos sdk v4 version. A bucket can be considered as a virtual disk in the COS. The upload of a bucket created in the old version of COS server using the new version of cos sdk v4 will fail, with the error **bucket notexist** prompted.
- **The solution** is to create a bucket on the cos v4 platform, and update backend and terminal COS related parameters to those of the new bucket.

## 7. Why does it prompt "Login failed. Registration operation is rejected for security reason." during registration or login?
Generally, this is because that the registration operations are too frequent on the same network, and the backend rejected the request. Reduce the registration frequency.

## What if other problems that are not in the list?
You can [submit a ticket](https://console.cloud.tencent.com/workorder/category/create?level1_id=29&level2_id=307&level1_name=%E8%A7%86%E9%A2%91%E4%B8%8E%E9%80%9A%E4%BF%A1%E6%9C%8D%E5%8A%A1&level2_name=%E7%A7%BB%E5%8A%A8%E7%9B%B4%E6%92%ADMLVB%EF%BC%88%E5%B0%8F%E7%9B%B4%E6%92%AD%EF%BC%89) to contact us.

