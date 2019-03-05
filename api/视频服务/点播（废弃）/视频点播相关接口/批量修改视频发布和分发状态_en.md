## 1. API Description
 
This API (MultiSetVodPlayStatus) is used to modify file publish status, and the status which indicates whether the file has been delivered to CDN.

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
<td> File
<tr>
<td> pullset.n.playStatus
<td> Yes
<td> int
<td> File status, 0: Paused. 1: Resumed
<tr>
<td> pullset.n.isPushCDN
<td> Yes
<td> int
<td> Whether to publish to CDN. 0: Do not publish. 1: Publish
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
</tbody></table>

 

## 4. Example
 
Input 1
<pre>
  https://domain/v2/index.php?Action=MultiSetVodPlayStatus&pullset.0.fi
 leId=16092504232103511902&pullset.0.playStatu=s0&pullset.0.isPush=CDN
 0&<a href="https://cloud.tencent.com/doc/api/229/6976">Common request parameters</a>
</pre>
Output 1
```

{
    "code" : 0,
    "message" : "",
}

```


