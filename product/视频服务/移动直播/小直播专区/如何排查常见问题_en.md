## 1. Signs of Incorrect Parameter Configuration at Business Backend 
### 1.1 Parameter appid or bizid 
Sign of incorrect configuration: VJs cannot push. Primary reason: Tencent Cloud refuses push requests because the generated push URLs are invalid. You can see the message "**The RTMP server actively disconnected**" in log.

![](//mc.qcloudimg.com/static/img/e3b6f9f974f561e0e3ef182580445673/image.png)

### 1.2 Push hotlink protection key 
Sign of incorrect configuration: VJs cannot push. Primary reason: An incorrect push hotlink protection key leads to incorrect txSecret because the key is used for computing txSecret. As a result, txSecret verification fails and Tencent Cloud refuses push requests. You can see the message "**The RTMP server actively disconnected**" in log.

![](//mc.qcloudimg.com/static/img/fca49e4e78c906ff27461fa8594b6d58/image.png)

### 1.3 API authentication key 
Sign of incorrect configuration: Push and playback work properly, but are not recorded in the terminal's replay list.
The replay records are generated as follows:
- After an LVB ends and is recorded, Tencent Cloud notifies Mini LVB backend through the callback URL configured in the console.
- Mini LVB backend then verifies if the callback is legal through API Authentication key. If authentication fails, no replay record will be inserted into the database.
- Otherwise, a replay record will be inserted into the tape_data table.
- If the insertion succeeds, you will see a replay record.
 
Primary reason for replay record failure: API authentication key is configured incorrectly so that callback authentication by the business backend fails.

### 1.4 COS APPID 
Sign of incorrect configuration: Uploading profile photo and video cover fails. Primary reason: COS upload request fails because the signature used for the request and issued by the business backend is incorrect. You can confirm this through "**ERROR_PROXY_APPID_USERID_NOTMATCH**" keyword in terminal's log.

![](//mc.qcloudimg.com/static/img/378e8a055f12f6aa77b2958ad1c3f149/image.png)

### 1.5 COS Bucket name 
Sign of incorrect configuration: Uploading profile photo and video cover fails. Primary reason: COS upload fails because COS Bucket, essentially a virtual disk, is specified incorrectly so that the error "Bucket not found" occurs. You can confirm this through "**ERROR_PROXY_SIGN_BUCKET_NOTMATCH**" keyword in terminal's log.
 
 ![](//mc.qcloudimg.com/static/img/92e096149bef3408c9713df93ab321ac/image.png)
 
### 1.6 Parameter COS SecretId 
 Sign of incorrect configuration: Uploading profile photo and video cover fails. Primary reason: The signature used for COS upload request is issued by the business backend. COS SecretId should be used with COS SecretKey to specify the signature key. You can confirm this through "**PROXY_AUTH_SECRETID_NOEXIST**" keyword in terminal's log.
 
 ![](//mc.qcloudimg.com/static/img/3fbfd0180fc165784c1ce30e513be5c7/image.png)
 
### 1.7 COS SecretKey 
 Sign of incorrect configuration: Uploading profile photo and video cover fails. Primary reason: COS SecretKey is incorrect so that the signature used for COS upload request and issued by the business backend fails. You can confirm this through "**ERROR_PROXY_AUTH_FAILED**" keyword in terminal's log.
 
 ![](//mc.qcloudimg.com/static/img/f1ac76d8ea4b70b883c4a45d74ee888d/image.png)

## 2. Signs of Incorrect Parameter Configuration on the Terminal (take iOS terminal as an example)
### 2.1 Parameter kTCIMSDKAppId or kTCIMSDKAccountType
Sign of incorrect configuration:Login fails.

![](//mc.qcloudimg.com/static/img/0b18fc2a7d5f7f86bbd4d56f743cee1e/image.png)

### 2.2 Parameter kTCCOSAppId or kTCCOSBucket
Sign of incorrect configuration: Uploading profile photo and video cover fails. You can see the following in the log:

![](//mc.qcloudimg.com/static/img/4192cf72b525664098fb69cd2e02ba7c/image.png)

### 2.3 Parameter kTCCOSRegion 
Sign of incorrect configuration: Uploading profile photo and video cover fails. Primary reason: kTCCOSRegion, a new parameter added in COS 4.0 to specify the location of COS data center, is set incorrectly so that the error "Bucket not found" occurs. You can see the following in the log:

![](//mc.qcloudimg.com/static/img/b023701ec5c2fe69ab35816b422afe16/image.png)

### 2.4 Parameter kHttpServerAddr 
Sign of incorrect configuration: A message of "request timeout" appear for errors occur to features such list pulling. Primary reason: The terminals fails to access correct backend service for incorrect server IP.

![](//mc.qcloudimg.com/static/img/c1ce2290019c67ae00395be67360e3d5/image.png)

## 3. Why does Replay List Pulling Fail?
For information about how the replay list is generated, please see **1.3 API authentication key**. The replay list is stored in tape_data table. When pulling fails, you can troubleshoot the following items:

![](//mc.qcloudimg.com/static/img/f28487d33a502e571737bc9c687647ac/image.png)

### 3.1 Check if the database is normal after callback
 Generally, the database runs normally as long as you don not modify backend source codes. However, if you have modified createDB script, you need to check the database status. Log is a convenient tool for troubleshooting. To enable log debugging in the backend, simply create a log directory under the live_demo_service/ directory. Check mysql_XXX.log. Modification of field attributes may cause database insertion failure.
 
### 3.2 Check if API authentication key is correct
 Make sure that the value of the API authentication key (explained above) set in the console is the same as that of CALL_BACK_KEY in OutDefine.php.
 
### 3.3 Check if callback URL is correct
 Go to "Tencent Cloud's official website" -> "Console" -> "Live Video Broadcasting" -> "Access Management" -> "LVB Code Access" -> "Access Configuration", and then check if the callback URL is correct. With an incorrect callback URL, the business backend cannot receive callback notifications from Tencent Cloud server after an LVB ends, and therefore no replay record is generated.
 
![](//mc.qcloudimg.com/static/img/61187098d48fecd3f4554d45a8503aa6/image.png)

## 4. Why does Playback List Pulling Fail?
The playback list is generatied based on the live_data table (LVB list) and tape_data table (replay list) in the database. Check if the value of **kHttpServerAddr**is correct, and if terminal network connection is normal. If both are normal, check the server.
If the server fails, after logging in to Android App, you can see a message "List pulling failed"*, and find "**HTTP Req error, error code:500**" in the logcat. For the iPhone App, you can see a message "**Internal server error**", and find **mysqli_connect failed, error:Access denied for user 'live_user'@'localhost' to database 'live'**] in the mysql_errorXXX.log file under the log directory on the backend.
Another reason is that database access failure causes API error. To confirm the error, check if the DB parameters in file cdn.route.ini under live_demo_service/conf directory are the same as the ones you specified when creating the database. PHP accesses local database through the parameters specified in cdn.route.ini. Their relationship is shown below:

![](//mc.qcloudimg.com/static/img/1a5a63e3ac06eb9eab85a0b0ed1b8879/image.png)


## 5. Why does Profile Photo and Video Cover Pulling Fail?
Sign of incorrect configuration: Uploading profile photo and video cover is successful, but downloading them fails. Primary reason: Domain name acceleration on COS version 4 is disabled by default, but a CDN address is returned for COS upload. You can enable domain acceleration to solve the problem.

![](//mc.qcloudimg.com/static/img/a2fd6cf344295b547d8d7c417142af45/image.png)

## 6. Why does Upload Fail Even If All COS Parameters are Correct?
- **Sign of incorrect configuration:** Uploading profile photo and video cover fails even if configurations of COS parameters, terminal and Mini LVB backend are correct.
- **Primary reason:** On November 2016, COS servers were upgraded, with region parameters being added. The new and old systems are independent of each other, and must be used with COS SDK of corresponding terminals. The COS service activated after November is version 4. For old version of COS, you can upgrade it to the new version by [submitting a ticket](https://console.cloud.tencent.com/workorder/category/create?level1_id=83&level2_id=84&level1_name=%E5%AD%98%E5%82%A8%E4%B8%8ECDN&level2_name=%E5%AF%B9%E8%B1%A1%E5%AD%98%E5%82%A8%20COS). Since December 30th, 2016, source code package of Mini LVB has also included COS SDK version 4 for terminals. A Bucket is essentially a virtual disk in COS. If you upload the bucket created on the old version of COS server by using new COS SDK (version 4), it will fail and the error **Bucket not exist** will occur.
- **Solution:** Create a new bucket on COS version 4 platform, and update relevant parameters of the backend and terminal COS to the new bucket.

## 7. Why does Register or Login Fail with Message "Login Fails or Register is Blocked for Security Reasons"?
Generally, this is because register operations under one network are too frequent so that the backend rejects them. You need lower register frequency.

## For Problems not Mentioned Above
Feedback to us by [submitting a ticket](https://console.cloud.tencent.com/workorder/category/create?level1_id=29&level2_id=307&level1_name=%E8%A7%86%E9%A2%91%E4%B8%8E%E9%80%9A%E4%BF%A1%E6%9C%8D%E5%8A%A1&level2_name=%E7%A7%BB%E5%8A%A8%E7%9B%B4%E6%92%ADMLVB%EF%BC%88%E5%B0%8F%E7%9B%B4%E6%92%AD%EF%BC%89).

