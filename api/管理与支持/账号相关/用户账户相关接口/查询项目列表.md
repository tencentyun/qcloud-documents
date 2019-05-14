## 1. 接口描述
 
域名: account.api.qcloud.com
接口名: DescribeProject

查询项目列表。项目为一个虚拟概念，用户可以在一个账户下面建立多个项目，每个项目中管理不同的资源。

 

## 2. 输入参数
 

<table class="t"><tbody><tr>
<th><b>参数名称</b></th>
<th><b>必选</b></th>
<th><b>类型</b></th>
<th><b>描述</b></th>
<tr>
<td>  allList <td> 否 <td> Int
 <td> 传1 拉取所有项目（包括隐藏项目），不传或传0拉取显示项目


</tbody></table>

 

## 3. 输出参数
 | 参数名称 | 类型 | 描述 |
|---------|---------|---------|
| code |  Int | 错误码，0：成功，其他值：失败 |
| message |   String | 错误信息 |
| data |   Array | 返回数组 |

Data结构 

<table class="t"><tbody><tr>
<th><b>参数名称</b></th>
<th><b>类型</b></th>
<th><b>描述</b></th>
<tr>
<td> projectName <td> String <td> 项目的名称
<tr>
<td> projectId <td> String <td> 项目的ID
<tr>
<td> createTime <td> String <td> 项目的创建时间
<tr>
<td> creatorUin <td> String <td> 项目的创建人
<tr>
<td> projectInfo <td> String <td> 项目的描述
</tbody></table>

 

## 4. 示例
 
输入
<pre>
  https://account.api.qcloud.com/v2/index.php?Action=DescribeProject
  &<a href="https://cloud.tencent.com/doc/api/229/6976">公共请求参数</a>
</pre>


输出
```
{
    "code": 0,
    "message": "",
    "data": [
        {
            "projectName": "test1",
            "projectId": 1002189,
            "createTime": "2015-04-28 14:42:53",
            "creatorUin": 670569769,
	        "projectInfo": "info1"
        },  
        {
            "projectName": "test2",
            "projectId": 1002190,
            "createTime": "2015-04-28 14:42:57",
            "creatorUin": 670569769,
	        "projectInfo": "info2"
        }   
    ]
}
```

