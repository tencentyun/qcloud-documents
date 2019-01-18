## 1. API Description
 
This API (DescribeAutoScreenShot) is used to batch acquire snapshots generated during transcoding process.

Domain:  vod.api.qcloud.com

 

## 2. Input Parameters
 

<table class="t"><tbody><tr>
<th><b>Parameter Name</b></th>
<th><b>Required</b></th>
<th><b>Type</b></th>
<th><b>Description</b></th>
<tr>
<td> fileId <td> Yes <td> Int <td> ID number of the video file
</tbody></table>

 

## 3. Output Parameters
 

<table class="t"><tbody><tr>
<th><b>Parameter Name</b></th>
<th><b>Type</b></th>
<th><b>Description</b></th>
<tr>
<td> code <td> Int <td> Error code, 0:  Succeeded, other values:  Failed
<tr>
<td> message <td> String <td> Error message
<tr>
<td> imageurls <td> Array <td> Image URL list
<tr>
<td> imageurls.id <td> Int <td> ID number
<tr>
<td> imageurls.url <td> String <td> URL address
<tr>
<td> imageurls.vheight <td> String <td> Height
<tr>
<td> imageurls.vwidth <td> String <td> Width
</tbody></table>

 

## 4. Example
 
Input
<pre>
  https://domain/v2/index.php?Action=DescribeAutoScreenShot
  &fileId=8782277315343726561
  &<a href="https://cloud.tencent.com/doc/api/229/6976">Common request parameters</a>
</pre>

Output
```

{
    "code": 0,
    "message": "",
    "imageurls": [
        {
            "id": 1,
            "url": "http:\/\/p.qpic.cn\/videoyun\/0\/1207_8d451afe8b1611e4919815f8b80b7a9a_1\/640",
            "vheight": "360",
            "vwidth": "640"
        },
        {
            "id": 1,
            "url": "http:\/\/p.qpic.cn\/videoyun\/0\/1207_8d451afe8b1611e4919815f8b80b7a9a_1\/400",
            "vheight": "300",
            "vwidth": "400"
        },
        {
            "id": 1,
            "url": "http:\/\/p.qpic.cn\/videoyun\/0\/1207_8d451afe8b1611e4919815f8b80b7a9a_1\/320",
            "vheight": "180",
            "vwidth": "320"
        },
        {
            "id": 1,
            "url": "http:\/\/p.qpic.cn\/videoyun\/0\/1207_8d451afe8b1611e4919815f8b80b7a9a_1\/200",
            "vheight": "150",
            "vwidth": "200"
        },
        {
            "id": 2,
            "url": "http:\/\/p.qpic.cn\/videoyun\/0\/1207_8d451afe8b1611e4919815f8b80b7a9a_2\/640",
            "vheight": "360",
            "vwidth": "640"
        },
        {
            "id": 2,
            "url": "http:\/\/p.qpic.cn\/videoyun\/0\/1207_8d451afe8b1611e4919815f8b80b7a9a_2\/400",
            "vheight": "300",
            "vwidth": "400"
        }
		......................................
    ]
}

```



