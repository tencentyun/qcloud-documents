## Overview

Tencent Cloud VOD provides __Referer hotlink protection__ and __URL timestamp hotlink protection__ (also known as __Key hotlink protection__ because key is needed for encryption) to prevent your video playback URLs from being used maliciously. Referer hotlink protection set filtering policy by configuring the value of the Referer field in the user's HTTP Request Header to restrict access to sources. URL timestamp hotlink protection generates playback URLs with specified expiration dates and encrypted information in real time and allows users to determine whether to enable the trial mode (a limited length of a video is allowed to be viewed) to effectively protect the video content.  

By default, both of the two VOD hotlink protection features are disabled. If you want to enable them, log in to the VOD console, select “”Global Configuration” in the left menu bar, click the “Domain Name Configuration" tab, and click "Hotlink Protection Settings" on the right of the domain name you want to set.

![Alt text](https://mc.qcloudimg.com/static/img/93efd0bf99ed0e50fdc4ca224906fdad/image.png "Figure: VOD Console Hotlink Protection Settings")

You can see the settings of Referer hotlink protection and Key hotlink protection. Click "Edit" to enable or disable the corresponding hotlink protection settings.  

![Alt text](https://mc.qcloudimg.com/static/img/6af09bb6465c17f8ad1098a3e786e38a/image.png "Figure: Details of VOD Console Hotlink Protection Settings")

## 1 Referer Hotlink Protection
### 1.1 Configuration Description

![Alt text](https://mc.qcloudimg.com/static/img/d9c289d7a0f2b1cb89ba03f7f268c687/image.png "Figure: Referer Whitelist Settings")

#### Configuring Referer blacklist/whitelist 

Select "Blacklist" or "Whitelist" in **Select an Object** and enter the blacklist or whitelist in the box below. The entered domain name or IP should not include http: // or https: //.  

If you select "Yes" for **Whether to allow Referer to be left empty**, it means that an HTTP request header without the field of Referer is allowed (For example, you can access by directly entering the URL in the browser's address bar) or the value of Referer is empty for access. If you select "No", it means that Referer is not allowed to be left empty.

#### Must-Know Facts About Whitelist

* If the Referer field of a request matches the string set for the whitelist, the requested information is returned normally.

* If the Referer field of a request does not match the string set for the whitelist, the 403 status code is returned.
  
#### Must-Know Facts About Blacklist

* If the Referer field of a request matches the string set for the blacklist, the 403 status code is returned.

* If the Referer field of a request does not match the string set for the blacklist, the requested information is returned normally.

#### Note

- Use the new Tencent Cloud domain `https://console.cloud.tencent.com` to log in to the VOD console.

- Referer blacklist and whitelist are not compatible with each other. You can only enable either of them at the same time.

- You can add a maximum of 10 entries for the hotlink protection feature, separated by line breaks (one entry per line).

- Hotlink protection supports the "domain name/IP" rule (prefix match). For example, if `www.abc.com` is set in the list, `www.abc.com/123` and `www.abc.com.cn` will be considered to match the list; if "127.0.0.1" is set in the list, "127.0.0.1/123" will be considered to match the list.

- Hotlink protection supports the use of wildcard. If `*.qq.com` is set in the list, `www.qq.com` and `a.qq.com` will be considered to match the list.

- If you need to preview the video on the VOD console,

- If your browser has Flash Player enabled, make sure that requests from the domain name `\* qq.com` are accessible. That is, if you set a whitelist, add `\* qq.com` to the whitelist; if you set a blacklist, make sure that `\* qq.com` is not in the blacklist.
- Otherwise, make sure that the domain `\*.cloud.tencent.com` is accessible. That is, if you set a whitelist, add `\*.cloud.tencent.com` to the whitelist; if you set a blacklist, make sure that `\*.cloud.tencent.com*` is not in the blacklist.

## 2 URL Timestamp Hotlink Protection 

### 2.1 Business Processes of Hotlink Protection

![Alt text](https://mc.qcloudimg.com/static/img/78dc2e06c3df8ed6adb2b71a7a035471/image.png "Figure: Business Processes of Hotlink Protection") 

#### Process Description  

1. The video requestor requests the playback URL from the user server.

2. The user server generates an encrypted playback URL using the hotlink protection key and algorithm and returns it to the video requestor.

3. The video requestor initiates the request using the encrypted playback URL obtained in step 2.

4. Tencent Cloud verifies the validity of the encrypted playback URL and responds. Extract the hotlink protection parameters such as expiration timestamp from the encrypted playback URL obtained in step 3. If the value of the expiration time parameter is greater than the local time, the 403 status code is returned. Otherwise, locally work out the hotlink protection signature string based on the user-defined hotlink protection key and algorithm, and compare it with the hotlink protection signature carried in request. If both of the signatures are identical, the video is returned. Otherwise, the 403 status code is returned.

### 2.2 Types of Hotlink Protection  

Tencent Cloud VOD provides the following types of URL timestamp hotlink protection:

1. Common hotlink protection (with "ts"): When the video wrapper format is HLS, Tencent Cloud conducts hotlink protection inspection to both "m3u8" and "ts" files.

2. Common hotlink protection (without "ts"): When the video wrapper format is HLS, Tencent Cloud conducts hotlink protection inspection to only "m3u8" files.

3. Hotlink protection with trial mode (with "ts"): You must specify the video trial duration. The types of files that support trial are "ts", "mp4", and "flv". For now, the VOD console does not support such hotlink protection. You can submit a ticket to have it configured at the backend of Tencent Cloud.

4. Hotlink protection with trial mode (without "ts"): You must specify the video trial duration. The types of files that support trial are "m3u8", "mp4", and "flv".  

The above 1, 2 and 4 respectively correspond to the "Hotlink Protection Format" drop-down list in the VOD console.

![Alt text](https://mc.qcloudimg.com/static/img/d75b05eb433c84b2c89fb64a3ef15afd/image.png "Figure: Key Hotlink Protection Format")

As the hotlink protection with trial mode has a trial parameter, its signature computing method is different from that of the common hotlink protection. However, 1 and 2 share the same hotlink protection computing method and 3 and 4 share the same as well. 

#### Notes  

When you enable the URL timestamp hotlink protection, Tencent Cloud VOD conducts hotlink protection inspection to the media files in the following formats: mp4, m3u8, flv, aac, mov, wmv, avi, mp3, rmvb, mkv, mpg, 3gp, webm, m4v, asf, f4v, wav, mpeg, vob, rm, wma, dat and m4a. "ts" is subject to the type of hotlink protection, as shown in the following table. 

__Hotlink Protection Inspection Table__   

Hotlink protection type | Whether to inspect "ts" hotlink protection
--- | --- |
Common hotlink protection (without "ts") | No
Common hotlink protection (with "ts") | Yes
Hotlink protection with trial mode (with "ts") | Yes
Hotlink protection with trial mode (without "ts") | Yes

#### Note  

In the past, APIs SimpleConcatHls and SimpleClipHls were used for VOD (Now, SimpleConcatHls is discarded and replaced by ConcatVideo). HLS playback URLs (m3u8) generated by these two APIs cannot be inspected by the hotlink protection with ts.  

m3u8 files can be normally played only when the m3u8 index files and the "ts" file are located in the same directory. (When the "ts" file in the "m3u8" is requested in Tencent Cloud, the parameters of the hotlink protection and "m3u8" should be identical. That is, the implicit "dir" should be consistent.) As the "m3u8" and "ts" files generated by SimpleConcatHls (discarded, replaced by ConcatVideo) and SimpleClipHls are not in the same directory, these "m3u8" files cannot be normally played after the hotlink protection that requires inspecting "ts" (excluding the common hotlink protection without "ts") is enabled. Therefore, you should evaluate the result before enabling the hotlink protection that requires inspecting "ts".  

For now, APIs ConcatVideo and SimpleClipHls in the <a href="https://cloud.tencent.com/document/product/266/7788">List of Server APIs</a> at Tencent Cloud VOD website have solved such problem. "m3u8" and "ts" files are generated in the same directory and can pass the "ts" inspection.
 

### 2.3 Algorithms for Generating Encrypted Playback URLs

#### Description of Hotlink Protection Parameters 

Parameter | Required | Type | Description | Note
---| --- | --- | --- | --- |
dir | Yes | String | Contains URL path, file name is not included | Implicit parameter 
t | Yes | String | Encrypted URL timeout timestamp, converted to a hexadecimal lower case string. Tencent Cloud CDN server determines whether the URL is valid based on time | It is recommended that the hotlink protection validity not exceed the total duration of the video.
us | Yes | String | The unique identity request, which strengthens the uniqueness of the URL | It is recommended to be as random as possible 
exper | No | Integer | Trial duration, in seconds, decimal | A required parameter for hotlink protection with trial mode. 0 indicates trial mode is disabled and a complete video is played. The trial duration of "mp4" and "ts" cannot be longer than the duration of the original video. Otherwise, an error occurs. 
sign | Yes | String | Signature string | Computing method varies depending on common hotlink protection and hotlink protection with trial mode, as shown below. 
  
Hotlink protection type | Computing method for signature string
--- | --- |
Common hotlink protection | sign = md5 x (KEY + dir + t + us) 
Hotlink protection with trial mode | sign = md5 x (KEY + dir + t + exper + us) 

KEY is the one you set in the VOD console and must be kept properly. If it is disclosed, disable and then re-enable the key hotlink protection in the VOD console, set a new key, and change the hotlink protection algorithm. Note: After change of the hotlink protection key, you need to generate new playback URLs accordingly because the previous ones will become invalid.    

![Alt text](https://mc.qcloudimg.com/static/img/f1c89ca986f70728f128975d873a5e74/image.png "Figure: The Key of Key Hotlink Protection")

The hotlink protection key shall 

* Not exceed 50 characters.

* Not contain Chinese characters or Chinese special characters.

* Not contain the English character "@".

#### Common hotlink protection

Assume that the hotlink protection key is a string of "abcTEST", the specified expiration time is "2017/6/21 13:2:1" (UNIX timestamp is 1498021321, equal to 5949fdc9 after it is converted to a hexadecimal string. That is, t = 5949fdc9). "us" is "test_user", and the original playback URL of the video file is   
```
http://test.vod2.myqcloud.com/a/c/b.m3u8
```  

The parameter list of the encrypted playback URL is as follows:
```
t=5949fdc9&us=test_user&sign=xxx
```  
Parameters "t", "us", and "sign" should be combined strictly as per the above order and no other parameters can be added among them. You can add other parameters before "t" or after "sign".  
Here, the implicit parameter dir = /a/c/. Therefore, the signature is as follows:  
```
sign = md5(KEY+dir+t+us) = md5(abcTEST/a/c/5949fdc9test_user) = 989778d1e86e8acc105cfeca65aa6460
```

The final encrypted playback URL is:
```
http://test.vod2.myqcloud.com/a/c/b.m3u8?t=5949fdc9&us=test_user&sign=989778d1e86e8acc105cfeca65aa6460
```
 
#### Hotlink protection with trial mode

Assume that the hotlink protection key is a string "abcTEST", the specified expiration time is "2017/6/21 13:2:1" (UNIX timestamp is 1498021321, equal to 5949fdc9 after it is converted to a hexadecimal string. That is, t = 5949fdc9). "us" is "test_user", the specified trial duration is 300 seconds (exper =300), and the original playback URL of the video file is  
```
http://test.vod2.myqcloud.com/a/c/b.m3u8
```  

The parameter list of the encrypted playback URL is as follows:
```
t=5949fdc9&exper=300&us=test_user&sign=xxx
```
Parameters "t", "exper", "us", and "sign" should be combined strictly as per the above order and no other parameters can be added among them. You can add other parameters before "t" or after "sign".
Here, the implicit parameter dir = /a/c/. Therefore, the signature is as follows:
```
sign = md5(KEY+dir+t+exper+us) = md5(abcTEST/a/c/5949fdc9300test_user) = 4454808ca6d980bffa3793193d300083
```
 
The final encrypted playback URL is:
```
http://test.vod2.myqcloud.com/a/c/b.m3u8?t=5949fdc9&exper=300&us=test_user&sign=4454808ca6d980bffa3793193d300083
```

#### Note

The following shows the results returned by Tencent Cloud VOD for different formats of videos with different trial durations:

Video format | Trial duration = 0 | Trial duration < Video duration | Trial duration > Video duration
--- | --- | --- | --- |
m3u8 | Complete video | Trial duration | Complete video
mp4 | Complete video | Trial duration | HTTP error status code
flv | Complete video | Trial duration | Complete video
ts | Complete video | Trial duration | HTTP error status code

__Advice__: For playback URLs not supporting trial, set "exper" to 0, and do not specify "trial duration > video duration".

### 2.4 Tencent Cloud Authentication Logic

After you enable the URL timestamp hotlink protection, all the files under the corresponding domain are protected by the hotlink protection mechanism. When someone request to access a file under the domain, Tencent Cloud authenticates the URL to be accessed to determine whether the request is valid. The authentication logic is as follows:

1. If the format of the URL parameter and the enabled hotlink protection type does not match, the video cannot be played.
2. If the parameter "t" of the URL expires, the video cannot be played.
3. Extract the parameter of URL and calculate "sign" based on the hotlink protection type and key. If the calculated result is inconsistent with the value of "sign" of the URL, the video cannot be played.
4. The video can be played.

## 3. Notes

 1. You cannot use the VOD player to play videos once the Referer hotlink protection or URL timestamp hotlink protection is enabled.

 2. If you have released relevant static codes including URLs and player codes before enabling the URL timestamp hotlink protection, the static codes will become unavailable after the function is enabled. You can access video files only through URLs generated dynamically.

 3. Referer and URL timestamp hotlink protection can be enabled at the same time and both of them take effect. In such case, videos can be played only when the access source conforms to the rules of the blacklist & whitelist and the URL is verified by the timestamp hotlink protection.

 4. If the URL failed to pass the hotlink protection verification, it returns to the 403 page by default.

 5. It takes five to fifteen minutes for the Referer hotlink protection or URL timestamp to be enabled or disabled on Tencent Cloud.

