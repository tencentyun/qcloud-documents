## 1. API Description
 
This API (CreateScreenShot) is used to acquire the URL addresses of multiple snapshots of different sizes for the specified file. Files are sorted according to the order of their IDs which correspond to snapshots at 0%, 10%, 20%, to 90% position of the time line, respectively.

Domain: vod.api.qcloud.com 

 

## 2. Input Parameters
 
<table class="t"><tbody><tr>
<th><b>Parameter Name</b></th>
<th><b>Required</b></th>
<th><b>Type</b></th>
<th><b>Description</b></th>
<tr>
<td> pullset.n.fileId
<td> Yes
<td> string
<td> File ID
</tbody></table>

 

## 3. Output Parameters
 
<table class="t"><tbody><tr>
<th><b>Parameter Name</b></th>
<th><b>Type</b></th>
<th><b>Description</b></th>
<tr>
<td> code
<td> Int
<td> Error code. 0:  Succeeded, other values:  Failed
<tr>
<td> message
<td> String
<td> Error Message
<tr>
<td> imgUrls
<td> String
<td> Returned URLs of the snapshots. Including detailed URL address, vwidth snapshot width, vheight snapshot height, ID number. The ID numbers correspond to snapshots at 0%, 10%, 20%, to 90% position of the time line, respectively.
</tbody></table>


 

## 4. Example
 
Input 1
<pre>
  https://domain/v2/index.php?Action=CreateScreenShot
 &pullset.0.fileId=16092504232103511902&pullset.0.playStatus=0&<a href="https://cloud.tencent.com/doc/api/229/6976">Common request parameters</a>
</pre>
Output 1
```

{
    "message": "", 
    "code": 0, 
    "data": {
        "list": [
            {
                "message": "", 
                "code": 1, 
                "imgUrls": [
                    {
                        "url": "http://p.qpic.cn/videoyun/0/2527_d146d44c3f0a11e5ba1c73421bba0b00_1/640", 
                        "vwidth": "640", 
                        "vheight": "360", 
                        "id": 1
                    }, 
                    {
                        "url": "http://p.qpic.cn/videoyun/0/2527_d146d44c3f0a11e5ba1c73421bba0b00_1/400", 
                        "vwidth": "400", 
                        "vheight": "300", 
                        "id": 1
                    }, 
                    {
                        "url": "http://p.qpic.cn/videoyun/0/2527_d146d44c3f0a11e5ba1c73421bba0b00_1/320", 
                        "vwidth": "320", 
                        "vheight": "180", 
                        "id": 1
                    }, 
                    {
                        "url": "http://p.qpic.cn/videoyun/0/2527_d146d44c3f0a11e5ba1c73421bba0b00_1/200", 
                        "vwidth": "200", 
                        "vheight": "150", 
                        "id": 1
                    }, 
                    {
                        "url": "http://p.qpic.cn/videoyun/0/2527_d146d44c3f0a11e5ba1c73421bba0b00_2/640", 
                        "vwidth": "640", 
                        "vheight": "360", 
                        "id": 2
                    }, 
                    {
                        "url": "http://p.qpic.cn/videoyun/0/2527_d146d44c3f0a11e5ba1c73421bba0b00_2/400", 
                        "vwidth": "400", 
                        "vheight": "300", 
                        "id": 2
                    }, 
                    {

```


