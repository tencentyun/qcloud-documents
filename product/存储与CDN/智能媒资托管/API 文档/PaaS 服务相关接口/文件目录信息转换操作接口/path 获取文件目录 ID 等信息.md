## 功能描述

用于根据 directoryID/path 获取文件目录 ID 等信息。

#### 接口说明

- 要求权限：
    - 非 acl 鉴权：admin
>?
> - 非 acl 鉴权是指当前用户对所有文件的操作权限，详情可参考 [生成访问令牌接口](https://cloud.tencent.com/document/product/1339/71159)。
> - acl 鉴权是通过共享授权接口给指定用户，以文件夹为单位授予的权限，详情可参考 [角色授权模块](https://cloud.tencent.com/document/product/1339/71014)。
>

## 请求

#### 请求示例  

POST /api/v1/directory-info/`{LibraryId}`?access_token=`{AccessToken}`&user_id=`{UserId}`

请求参数：
- LibraryId：媒体库 ID，必选参数。
- SpaceId：空间 ID，如果媒体库为单租户模式，则该参数固定为连字符(`-`)；如果媒体库为多租户模式，则必须指定该参数。
- AccessToken：访问令牌，对于公有读媒体库或租户空间，可不指定该参数，否则必须指定该参数。
- UserId：用户身份识别，当访问令牌对应的权限为管理员权限且申请访问令牌时的用户身份识别为空时用来临时指定用户身份，详情请参阅 [生成访问令牌接口](https://cloud.tencent.com/document/product/1339/71159)，可选参数。

#### 请求体

application/json

- 请求体示例
```json
{
  "directoryList": [
    {
      "spaceId": "spacexxx",
      "path": "A/B"
    },
    {
      "spaceId": "spacexxx",
      "directoryId": 123
    }
  ],
  "permission": {
    "acl": {
      "userId": 1,
      "spaceIds": ["a","b"]
    },
    "admin": [
      {"spaceIds": ["personalA"]}, 
      {"spaceTag": "team", "spaceIds": ["a"]}
    ]
  }
}

```

- 请求体字段说明：
  - directoryList
   - spaceId: 空间 ID，必填参数。
   - directoryId: 文件目录 ID，选填参数。
   - path: 文件目录路径数组，选填参数。当 directoryId 和 path 同时存在时，以 directoryId 为准。
  - permission（可选参数，不传则返回所有权限）
    - admin: 具有 admin 权限的空间集合，如果指定的 spaceIds 为空数组，表示所有空间。
    - acl: 使用 acl 检查权限的参数，spaceIds 为该用户所属的 spaceId 集合。
    - userId: 用户 ID。

## 响应

#### 响应码

获取成功，返回 HTTP 200 OK。

#### 响应体

application/json

- 响应体示例：
```json
[{
  "spaceId": "spacexxx",
  "spaceTag": "team",
  "path": ["A","B.png"],
  "type": "file",
  "directoryId": 123,
  "size": "10000",
  "modificationTime": "2021-02-01T08:21:47.000Z",
  "previewByDoc": false,
  "previewByCI": true,
  "previewAsIcon": false,
  "fileType": "image",
  "contentType": "image/png",
  "localSync": {
    "syncId": 4,
    "strategy": "local_to_cloud",
    "isSyncRootFolder": true,
    "syncUserId": "123"
  },
  "authorityList": {
    "canView": true,
    "canPreview": true,
    "canDownload": false,
    "canUpload": false,
    "canDelete": false,
    "canModify": false,
    "canAuthorize": false,
    "canShare": false
  }
}]
```
- 响应体字段说明：
    - spaceId：空间 ID。
    - spaceTag：space 标签，字符串。
    - path：文件目录路径。
    - type：文件类型。
    - directoryId：文件目录 ID。
    - size：文件目录大小。
    - modificationTime：文件最近一次被覆盖的时间。
    - previewByDoc：是否可通过 wps 预览。
    - previewByCI：是否可通过万象预览。
    - previewAsIcon：是否可用预览图做 icon。
    - fileType：文件类型：excel、powerpoint 等。
    - contentType：媒体类型。
    - authorityList 允许操作的权限。
      - canView：可查看，非必返。
      - canPreview：可预览，非必返。
      - canDownload：可下载，非必返。
      - canUpload：可上传，非必返。
      - canDelete：可删除，非必返。
      - canModify：可修改，非必返。
      - canAuthorize：可共享，非必返。
      - canShare：可分享，非必返。
    - localSync：当该文件夹是同步盘，或是同步盘的子级文件目录时，返回该字段。
      - isSyncRootFolder：当前文件夹是否为同步盘，如果是同步盘根目录返回 true，如果是同步盘子级节点，返回 false，如果不是同步盘，不返回该字段。
      - strategy：当该文件夹为同步盘时，返回同步方式，`local_to_cloud`，非必返。
      - syncId：当该文件夹为同步盘时，返回同步任务 ID。
      - syncUserId：当该文件夹为同步盘时，返回设置同步任务的 userID。
