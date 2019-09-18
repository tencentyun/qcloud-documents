>?当前页面接口为旧版 API，未来可能停止维护。容器服务 API 3.0 版本接口定义更加规范，访问时延下降显著，建议使用 [容器服务 API 3.0](https://cloud.tencent.com/document/api/457/31853)。
>
## 接口描述
本接口（GetRepositoryList）用于查询 TencentHub 公共仓库列表（包括官方的和用户公开的）。
接口请求域名：

````
ccr.api.qcloud.com
````

## 输入参数
以下请求参数列表仅列出了接口请求参数，其它参数见 [公共请求参数](/doc/api/457/9463)。

| 参数名称 | 描述 |类型 | 必选  |
|---------|---------|---------|---------|
| offset   | 偏移量，默认 0 | Uint |否 |
| limit   | 返回最大数量，默认 20, 最大值 100 | Uint |否 |
| reponame   | 要查询的仓库名字。不填则列出所有仓库，否则按此名字进行精确查询 | String |否 |
| orderby   | 排序条件,不填则随机排序。<br>official：按是否是官方镜像排序<br>pullCount：按下载次数排序 | String |否 |
| order   | 升序还是降序，默认是 desc，还可以选择 asc | String |否 |

## 输出参数

| 参数名称 | 描述 |类型 |
|---------|---------|---------|
| code | 公共错误码。0 表示成功，其他值表示失败|Int |
| codeDesc | 业务侧错误码。成功时返回 Success，错误时返回具体业务错误原因|String |
| message |  模块错误信息描述，与接口相关|String |
| repoInfo |  镜像信息|Object Array |

仓库信息字段：

| 参数名称 | 描述 |类型 |
|---------|---------|---------|
| reponame |  仓库名字|String |
| repotype | 仓库类型。<br>QCLOUD HUB：腾讯云仓库<br>DOCKER HUB：DockerHub 镜像 |String |
| tagCount |  tag数目|Int |
| public |  是否公开。1：公开，0：私有|Int |
| isUserFavor |  是否被用户收藏。true：是，false：否|Bool |
| isQcloudOfficial |  是否是腾讯云官方仓库。true：是，false：否|Bool |
| favorCount |  被所有用户收藏次数|Int |
| pullCount |  拉取次数|Int |
| description |  描述内容|String |
| creationTime |  创建时间|String |
| updateTime |  更新时间|String |

## 示例
### 输入

```
  https://domain/v2/index.php?Action=TencentHub
  &offset=0
  &limit=20
  &其它公共参数
```
### 输出

```
{
    "code": 0,
    "message": "", 
    "codeDesc": "Success",
    "data": {
		"totalCount": 1,
	    "privilegeFiltered": false,
	    "repoInfo": [
	      {
	        "reponame": "test/kubetest",
	        "repotype": "QCLOUD HUB",
	        "tagCount": 2,
	        "public": 0,
	        "isUserFavor": false,
	        "isQcloudOfficial": false,
	        "favorCount": 0,
	        "pullCount": 5137,
	        "description": "",
	        "creationTime": "2017-09-12 13:02:58",
	        "updateTime": "2018-02-28 14:26:06"
	      }
	   ]
	}
}

```
