## 1. API Description
 
This API (DescribeSecurityGroupEx) is used to query the basic information of one or more security groups based on multiple indexes.
Domain name for API request: <font style="color:red">dfw.api.qcloud.com</font>
 

## 2. Input Parameters
 
The following request parameter list only provides API request parameters. Common request parameters are also needed when the API is called. For more information, please see Common Request Parameters page. The Action field for this API is DescribeSecurityGroupEx.
<table class="t"><tbody><tr>
<th><b>Parameter Name</b></th>
<th><b>Required</b></th>
<th><b>Type</b></th>
<th><b>Description</b></th>
<tr>
<td> projectId <td> No <td> Int <td> Project ID. If it is left empty, all the security group lists under the project are returned.
<tr>
<td> sgId <td> No <td> String <td> Filter results by sgId. Only exact filtering is supported.
<tr>
<td> sgName <td> No <td> String <td> Filter results by sgName. Fuzzy filtering is supported.
<tr>
<td> offset <td> No <td> Int <td> Offset of initial page. Default is 0. In V3 version, offset of initial line will be used. "offsetLine" is recommended for now.
<tr>
<tr>
<td> offsetLine <td> No <td> Int <td> Offset of initial line. Default is 0. It cannot be passed along with offset at the same time.
<tr>
<td> limit <td> No <td> Int <td> Number of lines per page. Default is 20.
</tbody></table>

 

## 3. Output Parameters
 

| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Error code. 0: Successful; other values: Failed |
| message | String | Error message |
| data.totalNum | Int | Total number of developer's security groups |
| data.detail | Array | Returned data structure |

`detail` is composed as follows
<table class="t"><tbody><tr>
<th><b>Parameter Name</b></th>
<th><b>Type</b></th>
<th><b>Description</b></th>
<tr>
<td> detail.n.sgId <td> String <td> Security group Id
<tr>
<td> detail.n.sgName <td> String <td> Security group name
<tr>
<td> detail.n.sgRemark <td> String <td> Security group remarks
<tr>
<td> detail.n.createTime <td> String <td> Creation time of security group
<tr>
<td> detail.n.projectId <td> Int <td> Project Id
<tr>
<td> detail.n.beAssociateCount <td> Int <td> Number of referenced security groups
</tbody></table>

## 4. Error Codes
 <table class="t"><tbody><tr>
<th><b>Error Code Value</b></th>
<th><b>Reason</b></th>
<tr>

<td> 7000 <td> Security group backend exception
</tbody></table>


## 5. Example
 
Input
<pre>

  https://dfw.api.qcloud.com/v2/index.php?Action=DescribeSecurityGroupEx
  &<<a href="https://cloud.tencent.com/doc/api/229/6976">Common request parameters</a>>

</pre>

Output
```

{
    "code": 0,
    "message": "",
    "data":{
     "totalNum":50,
     "detail": [
         {
             "sgId": "sg-k3tjgics",
             "sgName": "test",
             "sgRemark": "",
             "createTime": "2015-05-20 16:07:58",
             "projectId": 1002207,
             "beAssociateCount": 0
         },
         {
             "sgId": "sg-56p1yd1o",
             "sgName": "Sample security group",
             "sgRemark": "",
             "createTime": "2015-10-15 17:12:17",
             "projectId": 1003744,
             "beAssociateCount": 0
         },
         {
             "sgId": "sg-ooa41c4o",
             "sgName": "Sample security group",
             "sgRemark": "",
             "createTime": "2015-09-11 16:12:28",
             "projectId": 1002110,
             "beAssociateCount": 0
         },
         {
             "sgId": "sg-7tk6qery",
             "sgName": "Sample security group",
             "sgRemark": "",
             "createTime": "2015-10-15 17:12:13",
             "projectId": 1003774,
             "beAssociateCount": 0
         },
         {
             "sgId": "sg-cqovl1fw",
             "sgName": "Sample security group",
             "sgRemark": "",
             "createTime": "2015-05-22 19:15:38",
             "projectId": 1002443,
             "beAssociateCount": 0
         },
         {
             "sgId": "sg-exnsygsm",
             "sgName": "test1",
             "sgRemark": "",
             "createTime": "2015-08-25 17:07:25",
             "projectId": 0,
             "beAssociateCount": 0
         },
         {
             "sgId": "sg-9g8qfrwi",
             "sgName": "1-10_-...12345",
             "sgRemark": "",
             "createTime": "2015-08-25 17:07:47",
             "projectId": 0,
             "beAssociateCount": 0
         },
         {
             "sgId": "sg-gte8a2ys",
             "sgName": "694949",
             "sgRemark": "",
             "createTime": "2015-05-25 15:48:24",
             "projectId": 1002026,
             "beAssociateCount": 0
         },
         {
             "sgId": "sg-fdn9vtdy",
             "sgName": "314294",
             "sgRemark": "",
             "createTime": "2015-05-25 15:42:13",
             "projectId": 1002026,
             "beAssociateCount": 0
         },
         {
             "sgId": "sg-p837l8ko",
             "sgName": "532215",
             "sgRemark": "",
             "createTime": "2015-05-25 13:27:12",
             "projectId": 1002026,
             "beAssociateCount": 0
         },
         {
             "sgId": "sg-de37xrpo",
             "sgName": "740402",
             "sgRemark": "",
             "createTime": "2015-05-25 13:27:13",
             "projectId": 1002026,
             "beAssociateCount": 0,
             "version": 0
         },
         {
             "sgId": "sg-bvdaobny",
             "sgName": "427637",
             "sgRemark": "",
             "createTime": "2015-05-25 13:25:53",
             "projectId": 1002026,
             "beAssociateCount": 0,
             "version": 0
         },
         {
             "sgId": "sg-kqj119xe",
             "sgName": "795911",
             "sgRemark": "",
             "createTime": "2015-05-25 13:26:22",
             "projectId": 1002026,
             "beAssociateCount": 0,
             "version": 0
         }
     ]
   }
}

```


