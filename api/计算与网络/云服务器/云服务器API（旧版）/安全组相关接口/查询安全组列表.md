>? **当前页面接口为旧版 API，未来可能停止维护，目前不展示在左侧导航。云服务器 API 3.0 版本接口定义更加规范，访问时延下降显著，建议使用 <a href="https://cloud.tencent.com/document/api/213/15689" target="_blank">云服务器 API 3.0</a>。**
>

## 1. 接口描述
 
本接口（DescribeSecurityGroupEx）用于根据多种索引查询一个或多个安全组的基本信息。
接口请求域名：<font style="color:red">dfw.api.qcloud.com</font>
 

## 2. 输入参数
 
以下请求参数列表仅列出了接口请求参数，正式调用时需要加上公共请求参数，见公共请求参数页面。其中，此接口的 Action 字段为 DescribeSecurityGroupEx。
<table class="t"><tbody><tr>
<th><b>参数名称</b></th>
<th><b>必选</b></th>
<th><b>类型</b></th>
<th><b>描述</b></th>
<tr>
<td> projectId <td> 否 <td> Int <td> 项目 Id，不传返回所有项目的安全组列表
<tr>
<td> sgId <td> 否 <td> String <td> 按 sgId 过滤结果，仅支持精确过滤
<tr>
<td> sgName <td> 否 <td> String <td> 按 sgName 过滤结果，支持模糊过滤
<tr>
<td> offset <td> 否 <td> Int <td> 初始的页偏移量，默认为 0。在将来的 V3 版中会改成行偏移量。目前建议使用 offsetLine。
<tr>
<tr>
<td> offsetLine <td> 否 <td> Int <td> 初始的行偏移量，默认为 0。不能与 offset 同时传入。
<tr>
<td> limit <td> 否 <td> Int <td> 每页行数，默认为 20。
</tbody></table>

 

## 3. 输出参数
 

| 参数名称 | 类型 | 描述 |
|---------|---------|---------|
| code |  Int | 错误码， 0：成功，其他值：失败 |
| message |   String | 错误信息 |
| data.totalNum |   Int | 开发商安全组总数 |
| data.detail | Array | 返回的数据结构|

detail结构
<table class="t"><tbody><tr>
<th><b>参数名称</b></th>
<th><b>类型</b></th>
<th><b>描述</b></th>
<tr>
<td> detail.n.sgId <td> String <td> 安全组 Id
<tr>
<td> detail.n.sgName <td> String <td> 安全组名
<tr>
<td> detail.n.sgRemark <td> String <td> 安全组备注
<tr>
<td> detail.n.createTime <td> String <td> 安全组创建时间
<tr>
<td> detail.n.projectId <td> Int <td> 项目 Id
<tr>
<td> detail.n.beAssociateCount <td> Int <td> 被安全组引用个数
</tbody></table>

 ## 4. 错误码表
 <table class="t"><tbody><tr>
<th><b>错误码数值</b></th>
<th><b>原因</b></th>
<tr>

<td> 7000 <td> 安全组后台异常
</tbody></table>


## 5. 示例
 
输入
<pre>

  https://dfw.api.qcloud.com/v2/index.php?Action=DescribeSecurityGroupEx
  &<<a href="https://cloud.tencent.com/doc/api/229/6976">公共请求参数</a>>

</pre>

输出
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
             "sgName": "示例安全组",
             "sgRemark": "",
             "createTime": "2015-10-15 17:12:17",
             "projectId": 1003744,
             "beAssociateCount": 0
         },
         {
             "sgId": "sg-ooa41c4o",
             "sgName": "示例安全组",
             "sgRemark": "",
             "createTime": "2015-09-11 16:12:28",
             "projectId": 1002110,
             "beAssociateCount": 0
         },
         {
             "sgId": "sg-7tk6qery",
             "sgName": "示例安全组",
             "sgRemark": "",
             "createTime": "2015-10-15 17:12:13",
             "projectId": 1003774,
             "beAssociateCount": 0
         },
         {
             "sgId": "sg-cqovl1fw",
             "sgName": "示例安全组",
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
             "sgName": "一二三四五六七八九十_-...12345",
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

