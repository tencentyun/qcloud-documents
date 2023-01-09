## 前期准备
- 安装 postman。
- 获取腾讯云 secretId + secretKey，地址。

<table>
   <tr>
      <th width="0%" >接口名称</td>
      <th width="0%" >接口功能</td>
   </tr>
   <tr>
      <td>公有云</td>
      <td><a href="https://console.cloud.tencent.com/cam/capi">API 密钥管理</a>。</td>
   </tr>
   <tr>
      <td>私有化</td>
      <td>	
修改 Uin、AppId、EnvId、Message。登录任意 pod 里执行。
```html
 {
   curl -i -X POST \
  -H "Content-Type:application/json" \
   -d \
'{
  "Action": "CreateClient",
  "Version": "2018-06-08",
  "AppId": appId,
  "Uin": "uin",
  "EnvId": "envId",
  "Name": {
    "Message": "xxx使用"
  },
  "Type":"SERVER",
  "Platform": "SERVICE"
}' \
 'weda-idaas-mgr:8080/cloudbase.auth.v1.Mgr/AddClient'
```</td>
   </tr>
</table>

- token 获取，注意：
 - **url：**https://{envId}.ap-shanghai.tcb-api.tencentcloudapi.com
 - **access token path：** /auth/v1/token/clientCredential
 - **client Id：**secretId
 - **client secret：**secretKey




## 用户列表
调用方式：GET
接口请求域名：
```html
https://lowcode-8gm1omixe8f6360b.ap-shanghai.tcb-api.tencentcloudapi.com/weda/auth/v1/prod/describeUserList?pageNo=1&pageSize=10
```
返回格式如下：
<dx-codeblock>
:::  html
{
    "Response":{
        "RequestId":"8c34f676-e9b0-425b-9804-25c061bd1c4d",
        "Data":{
            "Total":1,
            "UserList":[
                {
                    "Email":"", // 邮箱
                    "IsLicensed":false, // 是否授权
                    "EnvId":"lowcode-8gm1omixe8f6360b", // 环境id
                    "UserExtend":"{\"createdAt\":1648556705303,\"createBy\":\"administrator\",\"updateBy\":\"administrator\",\"app_id\":\"1301962775\",\"updatedAt\":1648556705303}", // 扩展信息
                    "MainOrg":{ // 主岗部门
                        "OrgId":"a54f45296363a7e8007e4cba09020c4a",
                        "OrgName":"后台开发组",
                        "OrgIdentity":"htkfz_azpf"
                    },
                    "Orgs":[  // 兼岗部门列表
                        {
                            "OrgId":"ykfcpz_w0gi",
                            "OrgName":"产品组",
                            "OrgIdentity":"ykfcpz_w0gi"
                        }
                    ],
                    "UserDesc":"", // 用户描述
                    "Source":1, // 来源
                    "Name":"pppppppppp", // 名称
                    "Type":0, // 用户类型，0:内部用户，1:外部用户，2:匿名用户
                    "Uuid":"7dbcba575af545bd805f0b618094d006", // Idassid
                    "Phone":"", // 手机号
                    "UserId":"1508782293638291458", // weda用户id
                    "RelatedRoles":[
                        {
                            "UpdateTime":"2022-03-29T16:12:23",
                            "RoleDesc":"",
                            "EnvId":"lowcode-8gm1omixe8f6360b",
                            "RoleIdentity":"portal",
                            "Id":"1508718702063099905",
                            "Name":"企业工作台"
                        }
                    ], // 关联角色
                    "Uin":"100013962784", // uin
                    "InternalUserType":0 // 内部用户类型，1：超级管理员；0：自建用户
                }
            ]
        }
    }
}

:::
</dx-codeblock>



## 用户详情
调用方式：GET
接口请求域名：
```html
https://lowcode-8gm1omixe8f6360b.ap-shanghai.tcb-api.tencentcloudapi.com/weda/auth/v1/prod/describeWedaUser?uid=1519289370670850049&source=4
```
返回格式如下：
<dx-codeblock>
:::  html
{
    "Response":{
        "RequestId":"54eefc71-a043-4256-b07f-0774535223d7",
        "Data":{
            "Email":"619393827@qq.com",
            "IsLicensed":false,
            "EnvId":"lowcode-8gm1omixe8f6360b",
            "UserExtend":"{\"createdAt\":1651061787680,\"createBy\":\"administrator\",\"updateBy\":\"administrator\",\"app_id\":\"1301962775\",\"updatedAt\":1651061787680}",
            "Orgs":[// 兼岗部门
                {
                    "OrgId":"2c9907ee625e7d880083fe003fc7ac47",
                    "OrgIdentity":"test1_3gyu",
                    "OrgName":"test1",
                    "Level":0
                }
            ],
             "MainOrg":{ // 主岗部门
                        "OrgId":"a54f45296363a7e8007e4cba09020c4a",
                        "OrgName":"后台开发组",
                        "OrgIdentity":"htkfz_azpf"
             },
            "UserDesc":"tes1",
            "Source":1,
            "Name":"jayzpjia10",
            "Type":0,
            "Uuid":"9dc91c661f0a47b4b1df7786bba26939",
            "Phone":"17611221322",
            "UserId":"1519289370670850049",
            "RelatedRoles":[
                {
                    "UpdateTime":"2022-03-29T16:12:23",
                    "RoleDesc":"",
                    "EnvId":"lowcode-8gm1omixe8f6360b",
                    "RoleIdentity":"portal",
                    "Id":"1508718702063099905",
                    "Name":"企业工作台"
                }
            ],
            "Uin":"100013962784",
            "InternalUserType":0
        }
    }
}


:::
</dx-codeblock>



## 资源鉴权
- 调用方式：POST
- 接口请求域名：
```html
https://lowcode-8gm1omixe8f6360b.ap-shanghai.tcb-api.tencentcloudapi.com/weda/auth/v1/prod/describeResourcesPermission
```
- 资源类型：
 - App 应用
 - modelApp 模型应用
 - flow 流程
 - dataSource 数据源


Body：
<dx-codeblock>
:::  html
{
    "UserInfo":{
        "Uid":28, // weda用户id
        "Source":4 // 来源4代表weda
    },
    "ResourceList":[{
        "ResourceId":"app-x74toau6-u_biao_dan_ti_jiao", 
// resourcetype：app resourceid：appid
// resourcetype：modelApp resourceid：appid
// resourcetype：flow resourceid：流程标识
// resourcetype：dataSource resourceid：数据源id
        "SubResourceId":["app-x74toau6-u_biao_dan_ti_jiao"],
// resourcetype：app subresourceid：pageid
// resourcetype：modelApp subresourceid：pageid
// resourcetype：flow subresourceid：无
// resourcetype：dataSource subresourceid：方法标识
    }],
    "AppId":"app-112", // 应用id
    "ResourceType":"app"
}

:::
</dx-codeblock>

返回Body:
<dx-codeblock>
:::  html
{
    "Response":{
        "Data":[
            {
                "ResourceId":"app-x74toau6-u_biao_dan_ti_jiao",
                "ResourceType":"app",
                "IsAccess":true
            }
        ]
    }
}
:::
</dx-codeblock>




## 数据鉴权
调用方式：POST
接口请求域名：
```html
https://lowcode-8gm1omixe8f6360b.ap-shanghai.tcb-api.tencentcloudapi.com/weda/auth/v1/prod/describeAuthStrategy
```
Body：
<dx-codeblock>
:::  html
{
    "UserInfo":{
        "Uid":28,
        "Source":1
    },
    "Resource":{
        "ResourceId":"data-6mgGUP8Q",
        "MethodIdList":[
           "wedaGetItem"
        ]
    },
   "AppId":"app-112" // 应用id
}

:::
</dx-codeblock>

返回 Body：
<dx-codeblock>
:::  html
{
  "Response": {
    "RequestId": "e7855de4b4ea7",
    "Data": {
      "Permission": {
        "RowPermission": {
          "Read": {
            "Type": 4,// 1:无权限;2:查看本人;3:查看本部门及下属部门;4:查看全部;5:自定义条件
            "Scope": [],// type为1和4，此内容为空，type为2，scope为userid，type为3，scope为组织架构id集合
            "Condition": [ // type为5使用，参考数据源openapi文档
                {
                    "DataSourceName":null,
                    "Key":"col1",
                    "Rel":"search", 
                    "Val":"test"
                }
            ]
          },
          "Write": {
            "Type": 2,// 1:无权限;2:查看本人;3:查看本部门及下属部门;4:查看全部;5:自定义条件
            "Scope": ["1123"],// type为1和4，此内容为空，type为2，scope为userid，type为3，scope为组织架构id集合
            "Condition": [ // type为5使用，参考数据源openapi文档
                {
                    "DataSourceName":null,
                    "Key":"col1",
                    "Rel":"search", 
                    "Val":"test"
                }
            ]
          }
        },
        "MethodPermission": [
          {
            "Name": "wedaGetRecords",
            "IsAccess": true
          }
        ],
        "ResourceId": "data-5Y9S3Wdj"
      },
      "UserId": "1528643355359150081"
    }
  }
}

:::
</dx-codeblock>




## 创建用户
调用方式：POST
接口请求域名：
```html
http://lowcode-8g84r3rnf95853d9.ap-shanghai.tcbapi.tencentcloud.com/weda/auth/v1/prod/addUser
```
Body：
<dx-codeblock>
:::  html
{
    "Uuid": "22332323", // 客户的用户ID
    "Orgs":[
        {
            "OrgId":"2c9907ee625e7d880083fe003fc7ac47",
            "OrgIdentity":"test1_3gyu"
        }
    ],//兼岗部门
    "MainOrg":{
            "OrgId": "11",
            "OrgIdentity": "11"
    },//主岗部门
    "Description":"tes1",
    "Email":"619393827@qq.com",
    "Phone":"17611221322",
    "UserExtend":"{\"extend1\":\"1\"}", // 用户数据源扩展字段，json串
    "Name":"jayzpjia10", // 必填
    "Password":"Jayzpjia1", // uuid和Email字段都不为空的情况下，密码可以为空，否则密码不为空
    "RoleIds":[
        "1508718702063099905"
    ]
}


:::
</dx-codeblock>

返回 Body：
<dx-codeblock>
:::  html
{
    "Response":{
        "RequestId":"ccc333a4-c440-4bf6-843b-5224eded9796",
        "Data":"1519289370670850049"
    }
}
:::
</dx-codeblock>







## 更新用户
调用方式：POST
接口请求域名：
```html
http://lowcode-8g84r3rnf95853d9.ap-shanghai.tcbapi.tencentcloud.com/weda/auth/v1/prod/updateUserInfoByUserId
```
Body：
<dx-codeblock>
:::  html
{
    "Orgs":[
        {
           "OrgId":"2c9907ee625e7d880083fe003fc7ac47",
            "OrgIdentity":"test1_3gyu"
        }
    ],
    "Description":"tes1",
    "Email":"619393827@qq.com",
    "Phone":"17611221322",
    "UserExtend":"",
    "Name":"jayzpjia10",
    "Password":"Jayzpjia1",
    "RoleIds":[
        "1508718702063099905"
    ],
    "UserId":"1508718702063099905" // 必填
}

:::
</dx-codeblock>
返回Body：
<dx-codeblock>
:::  html
{
    "Response":{
        "RequestId":"5417f24b-3078-408c-9f15-1b093b3a04b8",
        "Data":true
    }
}

:::
</dx-codeblock>


## 组织架构列表
调用方式：POST
接口请求域名：
```html
http://lowcode-8g84r3rnf95853d9.ap-shanghai.tcbapi.tencentcloud.com/weda/auth/v1/prod/describeOrgs
```
入参：
<dx-codeblock>
:::  html
{"PageNo":1,"PageSize":1000}

:::
</dx-codeblock>

返回格式如下：
<dx-codeblock>
:::  html
{
    "Response":{
        "RequestId":"7a6991cd-e826-4595-bdee-f87666d8f6e4",
        "Data":{
            "DataList":[
                {
                    "DataId":"16db756f6269fdce0068ab835373f72f",
                    "DataRecord":"{\"
\":\"部门1\",\"createdAt\":1651113422190,\"createBy\":\"administrator\",\"depth\":4,\"departmentParentCode\":\"test1_3gyu\",\"updateBy\":\"administrator\",\"departmentCode\":\"bm1_ymmi\",\"_id\":\"16db756f6269fdce0068ab835373f72f\",\"updatedAt\":1651113422190}"
                }
            ],
            "Total":1
        }
    }
}
:::
</dx-codeblock>


## 创建组织架构
调用方式：POST
接口请求域名：
```html
http://lowcode-8g84r3rnf95853d9.ap-shanghai.tcbapi.tencentcloud.com/weda/auth/v1/prod/addOrg
```
Body：
<dx-codeblock>
:::  html
{"OrgData":"{\"_id\":\"addtest1_1234\",\"departmentCode\":\"addtest1_1234\",\"departmentName\":\"addtest1\",\"departmentParentCode\":\"\"}"}


:::
</dx-codeblock>

返回 Body：
<dx-codeblock>
:::  html
{
    "Response": {
        "RequestId": "3be32d4eead71",
        "Data": "f6e08a646295f54b05faedfd24735047"
    }
}

:::
</dx-codeblock>



## 更新组织架构
调用方式：POST
接口请求域名：
```html
http://lowcode-8g84r3rnf95853d9.ap-shanghai.tcbapi.tencentcloud.com/weda/auth/v1/prod/updateOrg
```
Body：
<dx-codeblock>
:::  html
{"OrgData":"{\"departmentCode\":\"addtest31\",\"departmentName\":\"addtest11\",\"departmentParentCode\":\"\",\"_id\":\"addtest1_1234\"}"}

:::
</dx-codeblock>

返回 Body：
<dx-codeblock>
:::  html
{
    "Response": {
        "RequestId": "7aca5faad264b",
        "Data": 1
    }
}

:::
</dx-codeblock>


## 删除组织架构
调用方式：POST
接口请求域名：
```html
http://lowcode-8g84r3rnf95853d9.ap-shanghai.tcbapi.tencentcloud.com/weda/auth/v1/prod/deleteOrg
```
入参：
<dx-codeblock>
:::  html
{"OrgId":"684266796295f1260452b9d903645019"}

:::
</dx-codeblock>

返回 Body：
<dx-codeblock>
:::  html
{
    "Response": {
        "RequestId": "ebac17009f6e1",
        "Data": 1
    }
}
:::
</dx-codeblock>






## 角色列表
调用方式：POST
接口请求域名：
```html
http://lowcode-8g84r3rnf95853d9.ap-shanghai.tcbapi.tencentcloud.com/weda/auth/v1/prod/describeRoelList
```
入参：
<dx-codeblock>
:::  html
{"PageNo":1,"PageSize":10}


:::
</dx-codeblock>

返回格式如下：
<dx-codeblock>
:::  html
{
    "Response": {
        "RequestId": "bb88e8e2e8286",
        "Data": {
            "Total": 17,
            "RoleList": [
                {
                    "Name": "1", // 角色名称
                    "RoleIdentity": "1", // 角色标识
                    "UpdateTime": "2022-05-24T14:35:40", // 更新时间
                    "Id": 1528933366865600513, // 角色id
                    "ParentRoleId": null,
                    "ChildRoleId": null,
                    "EnvIdentity": null,
                    "RoleDesc": "1", // 角色描述
                    "EnvId": "lowcode-8gm1omixe8f6360b", // 环境id
                    "IsReleased": true // 是否发布
                }
            ]
        }
    }
}

:::
</dx-codeblock>


