>?当前页面接口为旧版 API，未来可能停止维护。容器服务 API 3.0 版本接口定义更加规范，访问时延下降显著，建议使用 [容器服务 API 3.0](https://cloud.tencent.com/document/api/457/31853)。
>
## 1. 接口描述
本接口 ( GetTagList ) 获取镜像 tag 列表。
接口请求域名：`ccr.api.qcloud.com`。

## 2. 输入参数
以下请求参数列表仅列出了接口请求参数，其它参数见 [公共请求参数](/doc/api/457/9463)（Region 参数必填）。

| 参数名称 | 描述 |类型 | 必选  | 
|---------|---------|---------|---------
| reponame   | 仓库名字 | String |是 |
| offset   | 偏移量,默认为 0 | Uint |否 |
| limit   | 返回最大数量，默认 20, 最大值 100 | Uint |否 |
| tag   | 可用于搜索的 tag 名字 | String |否 |


## 3. 输出参数
 
| 参数名称 | 描述 |类型 | 
|---------|---------|---------|
| code | 公共错误码。0 表示成功，其他值表示失败|Int | 
| codeDesc | 业务侧错误码。成功时返回 Success，错误时返回具体业务错误原因|String |
| message |  模块错误信息描述，与接口相关|String |
| reponame |  仓库名字|String |
| server |  镜像仓库域名|String |
| tagCount |  tag 数目|Int |
| tagInfo |  tag 列表，结果按 pushTime 降序排列|Object Array |

tag 字段详细说明：

| 参数名称 | 描述 |类型 | 
|---------|---------|---------|
| repo_name |  tag 对应的仓库名字|String |
| tagName |  tag 名字|String |
| tagId |  tag 的 ID|String |
| imageId |  镜像的 ID|String |
| size |  镜像大小|String |
| creationTime |  创建时间|String |
| updateTime |  更新时间|String |
| author |  镜像制作者|String |
| architecture |  CPU 架构|String |
| dockerVersion |  Docker 客户端版本|String |
| os |  操作系统|String |
| pushTime |  push 时间|String |
| sizeByte |  镜像大小，单位为字节|Int |

## 4. 示例
输入

```
  https://domain/v2/index.php?Action=GetTagList
  &reponame=test/kubetest  
  &offset=0
  &limit=20
  &tag=nginx_v1
  &其它公共参数
```
输出

```
{
    "code": 0,
    "message": "", 
    "codeDesc": "Success",
    "data": {
	    "reponame": "test/kubetest",
	    "server": "ccr.ccs.tencentyun.com",
	    "tagCount": 1,
	    "tagInfo": [
	      {
	        "repo_name": "kubetest",
	        "tagName": "nginx_v1",
	        "tagId": "sha256:5fbb3629fba1c7c875015c9cb4c27f1d9e8e92d2f027f09b6eda35ff952323a1",
	        "imageId": "sha256:146c8220814be5f07a03b0b0b1e352ce42278684266d95670bf3e11225441b70",
	        "size": "59 MB",
	        "creationTime": "2017-09-12 15:30:23 +0800 CST",
	        "updateTime": "2017-10-25 16:33:51 +0800 CST",
	        "author": "",
	        "architecture": "amd64",
	        "dockerVersion": "1.12.5",
	        "os": "linux",
	        "pushTime": "2017-09-12 15:33:39 +0800 CST",
	        "sizeByte": 59229024
	      }
	    ]
	}
}

```
