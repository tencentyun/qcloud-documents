## 1. API Description

Domain name: live.api.qcloud.com
API name: DescribeQueueLog

Note: This API is used to query the queue of a screenshot and can also be used for other message queuing services.
The screenshot files are stored on COS for long-term storage. You need to activate the service before you can use this feature, and you will be charged a fee (for the storage and etc.) based on the billing mode for COS. See the [Relevant Document](http://www.qcloud.com/product/cos.html) for details.

**Note: This service must be activated separately for the queue query API**. You can submit a request through the after-sales QQ number 514025596 to activate the service. You can send the request by simply indicating that "I want to activate the LVB screenshot query queue API service" as well as the account information in the message. The service will be activated within one business day. You can also choose to perform query through COS related APIs. In this case, you do not need to activate this service separately.

## 2. Input parameters
</b></th>
<table class="t"><tbody><tr>
<th><b>Parameter name</b></th>
<th><b>Required</b></th>
<th><b>Type</b></th>
<th><b>Description</b></th>
<tr>
<td> bid
<td> Yes
<td> Int
<td> Service type, 100-screenshot.
<tr>
<td> count
<td> No
<td> Int
<td> The number of messages. The default value is 1 (value range: 1~100).
<tr>
</tbody></table>


</b></th>

## 3. Output parameters
</b></th>
<table class="t"><tbody><tr>
<th><b>Parameter name</b></th>
<th><b>Type</b></th>
<th><b>Description</b></th>
<tr>
<td> code
<td> Int
<td> Error code, 0: succeeded; other values: failed
<tr>
<td> message
<td> String
<td> Error message
<tr>
<tr>
<td> data
<td> array
<td> Message content
<tr>
<tr>

</tbody></table>


</b></th>

## 4. Example

Input 1
<pre>
http://domain/v2/index.php?Action=DescribeQueueLog&bid=100&count=5&<a href="https://www.qcloud.com/doc/api/229/6976">Public Request Parameters</a>

</pre>

Output 1
```
{

"code": 0,
    "message": "",
    "data": [
        {
            "stream_id": "2000_f3d360679eeb11e5b91fa4dcbef5e35a",
            "pic_url": "2000_f3d360679eeb11e5b91fa4dcbef5e35a_1453255801_0_146434_1280_720.jpg"
        },
        {
            "stream_id": "2000_f3d360679eeb11e5b91fa4dcbef5e35a",
            "pic_url": "2000_f3d360679eeb11e5b91fa4dcbef5e35a_1453255801_0_146444_1280_720.jpg"
        },
        {
            "stream_id": "2000_f3d360679eeb11e5b91fa4dcbef5e35a",
            "pic_url": "2000_f3d360679eeb11e5b91fa4dcbef5e35a_1453255801_0_146454_1280_720.jpg"
        },
        {
            "stream_id": "2000_f3d360679eeb11e5b91fa4dcbef5e35a",
            "pic_url": "2000_f3d360679eeb11e5b91fa4dcbef5e35a_1453255801_0_146464_1280_720.jpg"
        },
        {
            "stream_id": "2000_f3d360679eeb11e5b91fa4dcbef5e35a",
            "pic_url": "2000_f3d360679eeb11e5b91fa4dcbef5e35a_1453255801_0_146474_1280_720.jpg"
        }
    ]


}

```

The format of the URL where he screenshot file is stored is as follows:
Description of the screenshot URL
http://(cos_bucketname)-(cos_appid).file.myqcloud.com/file name
Example:
http://record1-10005041.file.myqcloud.com/2000_f3d36****eeb11e5b91fa4dcbef5e35a_1453255801_0_146324_1280_720.jpg
For details on the access method, refer to the COS [Relevant Documents](https://www.qcloud.com/document/product/430).
