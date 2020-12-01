## 功能描述
DescribeProjects 用于查找项目。

## 请求
### 请求实例

```shell
GET /project HTTP/1.1
Host: iss.<Region>.myqcloud.com
Date: <GMT Date>
Authorization: <Auth String>
Content-Length: <length>
Content-Type: application/xml

```

>? Authorization: Auth String （详情请查阅 [请求签名](https://cloud.tencent.com/document/product/1344/50456) 文档）。


### 请求头
#### 公共头部
该请求操作的实现使用公共请求头，了解公共请求头详情请参见 [公共请求头部](https://cloud.tencent.com/document/product/1344/50451) 文档。
#### 非公共头部
该请求操作无特殊的请求头部信息。

### 请求体
该请求的请求体为空。

#### 请求参数
参数的具体内容如下：

|节点名称（关键字）|父节点     |描述                    |   类型    |   必选    |
|:---           |:--       |:--                    |   :--     |   :--    |
| ids           | 无        | 项目 ID, 以,符号分割字符串  | String     |否|
| name          | 无        | 项目名称前缀              | String     |否|
| pageNumber    | 无        | 第几页                   | Integer     |否|
| pageSize      | 无        | 每页个数                 | Integer     |否|

## 响应
### 响应头

#### 公共响应头
该响应包含公共响应头，了解公共响应头详情请参见 [公共响应头部]( https://cloud.tencent.com/document/product/1344/50452) 文档。
#### 特有响应头
该响应无特殊的响应头。

### 响应体
该响应体返回为 **application/xml** 数据，包含完整节点数据的内容展示如下：

``` shell
<Response>
    <TotalCount>1</TotalCount>
    <PageNumber>1</PageNumber>
    <PageSize>10</PageSize>
    <ProjectList>
        <Name>ProjectName</Name>
        <Desc>ProjectDesc</Desc>
        <ProjectId>pj1460606b9752148c4ab182f55163ba7cd</ProjectId>
        <Status>Active</Status>
        <Mode>HTTP</Mode>
        <Bucket>
            <Region>ap-beijing</Region>
            <BucketId>bucket-1250000000</BucketId>
            <Prefix>/iss</Prefix>
        </Bucket>
        <ServiceConf>
            <Notify></Notify>
        </ServiceConf>
        <TemplateList>
            <TemplateId></TemplateId>
            <Tag></Tag>
            <Name></Name>
            <Status></Status>
            <Output>
                <Region>ap-beijing</Region>
                <Bucket>abc-1250000000</Bucket>
                <Object>snapshot-${Number}.jpg</Object>
            </Output>
            <Notify></Notify>
        </TemplateList>
        <TemplateList>
            <TemplateId></TemplateId>
            <Tag></Tag>
            <Name></Name>
            <Status></Status>
            <Output>
                <Region>ap-beijing</Region>
                <Bucket>abc-1250000000</Bucket>
                <Object>snapshot-${Number}.jpg</Object>
            </Output>
            <Notify></Notify>
        </TemplateList>
        <CreateTime>2020-08-05T11:35:24+0800</CreateTime>
        <UpdateTime>2020-08-31T16:15:20+0800</UpdateTime>
    </ProjectList>
</Response>
```

具体的数据内容如下：

| 节点名称（关键字） | 父节点 | 描述           | 类型      |
| :----------------- | :----- | :------------- | :-------- |
| Response           | 无     | 保存结果的容器 | Container |

Container 节点 Response 的内容：

| 节点名称（关键字） | 父节点   | 描述                           | 类型      |
| :----------------- | :------- | :----------------------------- | :-------- |
| TotalCount         | Response | 项目总数                       | Int       |
| PageNumber         | Response | 当前页数，同请求中的 pageNumber | Int       |
| PageSize           | Response | 每页个数，同请求中的 pageSize   | Int       |
| ProjectList        | Response | 项目数组                       | Container |

Container 节点 ProjectList 的内容：

| 节点名称（关键字） | 父节点                | 描述                                                         | 类型      |
| :----------------- | :-------------------- | :----------------------------------------------------------- | :-------- |
| ProjectId          | Response.ProjectList | 项目 ID                                                      | String    |
| Name               | Response.ProjectList | 项目名字                                                     | String    |
| Desc               | Response.ProjectList | 项目描述                                                     | String    |
| Mode               | Response.ProjectList | 接入类型                                                     | String    |
| Status             | Response.ProjectList | 项目状态                                                     | String    |
| UpdateTime         | Response.ProjectList | 更新时间                                                     | String    |
| CreateTime         | Response.ProjectList | 创建时间                                                     | String    |
| Bucket             | Response.ProjectList | 参考更新项目接口的 Bucket 参数 | Container |
| ServiceConf        | Response.ProjectList | 参考更新项目接口的服务配置 | Container |
| TemplateList       | Response.ProjectList | 参考更新项目接口的模板列表 | Container |

Container 节点 ServiceConf 的内容：

| 节点名称（关键字） | 父节点                | 描述                                                         | 类型      |
| :----------------- | :-------------------- | :----------------------------------------------------------- | :-------- |
| Notify      | Response.ProjectList.ServiceConf | 服务配置回调                                               | String    |

Container 节点 TemplateList 的内容：

| 节点名称（关键字） | 父节点                | 描述                                                         | 类型      |
| :----------------- | :-------------------- | :----------------------------------------------------------- | :-------- |
| TemplateId      | Response.ProjectList.TemplateList | 模板 ID                                               | String    |
| Tag             | Response.ProjectList.TemplateList | 模板类型                                               | String    |
| Name            | Response.ProjectList.TemplateList | 模板名称                                               | String    |
| Status          | Response.ProjectList.TemplateList | 模板状态                                               | String    |
| Notify          | Response.ProjectList.TemplateList | 模板回调                                                | String    |
| Output          | Response.ProjectList.TemplateList | 模板输出                                                | Container    |


Container 节点 Output 的内容：

| 节点名称（关键字） | 父节点                   | 描述                                                         | 类型   | 必选 |
| ------------------ | ------------------------ | ------------------------------------------------------------ | ------ | ---- |
| Region             | Response.ProjectList.TemplateList.Output | 存储桶的园区                                   | String | 是   |
| Bucket             | Response.ProjectList.TemplateList.Output | 存储结果的存储桶                                | String | 是   |
| Object             | Response.ProjectList.TemplateList.Output | 结果文件的名字                                  | String | 是   |

### 错误码

该请求无特有错误信息，常见的错误信息请参见 [错误码](https://cloud.tencent.com/document/product/1344/50457) 文档。

## 实际案例

### 按照模板 ID 维度查询
#### 请求


```shell
GET /project?ids=pj1460606b9752148c4ab182f55163ba7cd,B,C HTTP/1.1
Authorization:q-sign-algorithm=sha1&q-ak=AKIDZfbOAo7cllgPvF9cXFrJD0**********&q-sign-time=1497530202;1497610202&q-key-time=1497530202;1497610202&q-header-list=&q-url-param-list=&q-signature=28e9a4986df11bed0255e97ff90500557e0e****
Host: iss.ap-beijing.myqcloud.com
Content-Length: 0
Content-Type: application/xml

```

#### 响应

```shell
HTTP/1.1 200 OK
Content-Type: application/xml
Content-Length: 100
Connection: keep-alive
Date: Thu, 15 Jun 2017 12:37:29 GMT
Server: tencent-iss
x-iss-request-id: NTk0MjdmODlfMjQ4OGY3XzYzYzhfMjc=

<Response>
    <ProjectList>
        <Name>ProjectName</Name>
        <Desc>ProjectDesc</Desc>
        <ProjectId>pj1460606b9752148c4ab182f55163ba7cd</ProjectId>
        <Status>Active</Status>
        <Mode>HTTP</Mode>
        <Bucket>
            <Region>ap-beijing</Region>
            <BucketId>bucket-1250000000</BucketId>
            <Prefix>/iss</Prefix>
        </Bucket>
        <ServiceConf>
            <Notify></Notify>
        </ServiceConf>
        <TemplateList>
            <TemplateId></TemplateId>
            <Tag></Tag>
            <Name></Name>
            <Status></Status>
            <Output>
                <Region>ap-beijing</Region>
                <Bucket>abc-1250000000</Bucket>
                <Object>snapshot-${Number}.jpg</Object>
            </Output>
            <Notify></Notify>
        </TemplateList>
        <TemplateList>
            <TemplateId></TemplateId>
            <Tag></Tag>
            <Name></Name>
            <Status></Status>
            <Output>
                <Region>ap-beijing</Region>
                <Bucket>abc-1250000000</Bucket>
                <Object>snapshot-${Number}.jpg</Object>
            </Output>
            <Notify></Notify>
        </TemplateList>
        <CreateTime>2020-08-05T11:35:24+0800</CreateTime>
        <UpdateTime>2020-08-31T16:15:20+0800</UpdateTime>
    </ProjectList>
    <NonExistProjectIds>
        <ProjectId>B</ProjectId>
        <ProjectId>C</ProjectId>
    </NonExistProjectIds>
</Response>
```

### 按照分页列表维度查询
#### 请求

```shell
GET /project?pageSize=10&pageNumber=1 HTTP/1.1
Authorization:q-sign-algorithm=sha1&q-ak=AKIDZfbOAo7cllgPvF9cXFrJD0**********&q-sign-time=1497530202;1497610202&q-key-time=1497530202;1497610202&q-header-list=&q-url-param-list=&q-signature=28e9a4986df11bed0255e97ff90500557e0e****
Host:iss.ap-beijing.myqcloud.com
Content-Length: 0
Content-Type: application/xml

```

#### 响应

```shell
HTTP/1.1 200 OK
Content-Type: application/xml
Content-Length: 100
Connection: keep-alive
Date: Thu, 15 Jun 2017 12:37:29 GMT
Server: tencent-iss
x-iss-request-id: NTk0MjdmODlfMjQ4OGY3XzYzYzhfMjc=

<Response>
    <TotalCount>1</TotalCount>
    <PageNumber>1</PageNumber>
    <PageSize>10</PageSize>
    <ProjectList>
        <Name>ProjectName</Name>
        <Desc>ProjectDesc</Desc>
        <ProjectId>pj1460606b9752148c4ab182f55163ba7cd</ProjectId>
        <Status>Paused</Status>
        <Mode>HTTP</Mode>
        <Bucket>
            <Region>ap-beijing</Region>
            <BucketId>bucket-1250000000</BucketId>
            <Prefix>/iss</Prefix>
        </Bucket>
        <ServiceConf>
            <Notify></Notify>
        </ServiceConf>
        <TemplateList>
            <TemplateId>t1460606b9752148c4ab182f55163ba7cd</TemplateId>
            <Tag>Snapshot</Tag>
            <Name></Name>
            <Status>On</Status>
            <Output>
                <Region>ap-beijing</Region>
                <Bucket>abc-1250000000</Bucket>
                <Object>snapshot-${Number}.jpg</Object>
                <Count>4</Count>
            </Output>
            <Notify></Notify>
        </TemplateList>
        <TemplateList>
            <TemplateId>t1460606b9752148c4ab182f55163ba7cd</TemplateId>
            <Tag>Snapshot</Tag>
            <Name></Name>
            <Status>On</Status>
            <Output>
                <Region>ap-beijing</Region>
                <Bucket>abc-1250000000</Bucket>
                <Object>snapshot-${Number}.jpg</Object>
                <Count>4</Count>
            </Output>
            <Notify></Notify>
        </TemplateList>
        <CreateTime>2020-08-05T11:35:24+0800</CreateTime>
        <UpdateTime>2020-08-31T16:15:20+0800</UpdateTime>
    </ProjectList>
</Response>
```
