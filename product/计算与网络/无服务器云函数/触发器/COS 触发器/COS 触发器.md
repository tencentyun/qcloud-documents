用户可以编写 SCF 函数来处理 COS Bucket 中的对象创建和对象删除事件。COS 可将事件发布给 SCF 函数并将事件数据作为参数来调用该函数。用户可以在 COS Bucket 中添加存储桶通知配置，该配置可标识触发函数的事件类型和希望调用的函数名称等信息。

COS 触发器具有以下特点：

- **Push 模型**
COS 会监控指定的 Bucket 动作（事件类型）并调用相关函数，将事件数据推送给 SCF 函数。在推模型中使用 Bucket 通知来保存 COS 的事件源映射。
- **异步调用**
COS 始终使用异步调用类型来调用函数，结果不会返回给调用方。有关调用类型的更多信息，请参阅 [调用类型](https://cloud.tencent.com/document/product/583/9694#.E8.B0.83.E7.94.A8.E7.B1.BB.E5.9E.8B)。





## COS 触发器属性

- COS Bucket（必选）：配置的 COS Bucket，仅支持选择同地域下的 COS 存储桶。
- 事件类型（必选）：支持 “文件上传” 和 “文件删除”、以及更细粒度的上传和删除事件，具体事件类型见下表。事件类型决定了触发器何时触发云函数，例如选择 “文件上传” 时，会在该 COS Bucket 中有文件上传时触发该函数。
<table>
<thead>
<tr>
<th>事件类型</th>
<th>描述</th>
</tr>
</thead>
<tbody><tr>
<td><code>cos:ObjectCreated:*</code></td>
<td>以下提到的所有上传事件均可触发云函数。</td>
</tr>
<tr>
<td><code>cos:ObjectCreated:Put</code></td>
<td>使用 Put Object 接口创建文件时触发云函数。</td>
</tr>
<tr>
<td><code>cos:ObjectCreated:Post</code></td>
<td>使用 Post Object 接口创建文件时触发云函数。</td>
</tr>
<tr>
<td><code>cos:ObjectCreated:Copy</code></td>
<td>使用 Put Object - Copy 接口创建文件时触发云函数。</td>
</tr>
<tr>
<td><code>cos:ObjectCreated:CompleteMultipartUpload</code></td>
<td>使用 CompleteMultipartUpload 接口创建文件时触发云函数。</td>
</tr>
<tr>
<td><code>cos:ObjectCreated:Origin</code></td>
<td>通过 <a href="https://cloud.tencent.com/document/product/436/13310">COS 回源</a> 创建对象时触发云函数。</td>
</tr>
<tr>
<td><code>cos:ObjectCreated:Replication</code></td>
<td>通过跨区域复制创建对象时触发云函数。</td>
</tr>
<tr>
<td><code>cos:ObjectRemove:*</code></td>
<td>以下提到的所有删除事件均可触发云函数。</td>
</tr>
<tr>
<td><code>cos:ObjectRemove:Delete</code></td>
<td>在未开启版本管理的 Bucket 下使用 Delete Object 接口删除的 Object，或者使用 versionid 删除指定版本的 Object 时触发云函数。</td>
</tr>
<tr>
<td><code>cos:ObjectRemove:DeleteMarkerCreated</code></td>
<td>在开启或者暂停版本管理的 Bucket 下使用 Delete Object 接口删除的 Object 时触发云函数。</td>
</tr>
<tr>
<td><code>cos:ObjectRestore:Post</code></td>
<td>创建了归档恢复的任务时触发云函数。</td>
</tr>
<tr>
<td><code>cos:ObjectRestore:Completed</code></td>
<td>完成归档恢复任务时触发云函数。</td>
</tr>
</tbody></table>
- 前缀过滤（可选）：前缀过滤通常用于过滤指定目录下的文件事件。例如，前缀过滤为 `test/`，则仅 `test/` 目录下的文件事件才可以触发函数，`hello/` 目录下的文件事件不触发函数。
- 后缀过滤（可选）：后缀过滤通常用于过滤指定类型或后缀的文件事件。例如，后缀过滤为 `.jpg`，则仅 `.jpg` 结尾的文件的事件才可以触发函数，`.png` 结尾的文件事件不触发函数。

## COS 触发器使用限制

- 为了避免 COS 的事件生产投递出现错误，COS 针对每个 Bucket 的每个事件（如文件上传/文件删除等）和前后缀过滤的组合，限制同一组规则只能绑定一个可触发的函数。因此，在您创建 COS 触发器时，请不要针对同一个 COS Bucket 配置相同的规则。例如，您可以为函数 A 配置 test Bucket 的 “Created: * ” 事件触发（未配置过滤规则），那么该 test Bucket 的上传事件不能再绑定到其他函数，这些事件包含（Created:Put、Created:Post等），但是您可以为函数 B 配置 test Bucket 的 “ObjectRemove” 事件触发。

- 当使用前后缀过滤规则时，为了保证同一个 Bucket 触发事件的唯一性，需要注意同一 Bucket 无法使用重叠前缀、重叠后缀或前缀和后缀的重叠组合为相同的事件类型定义筛选规则。例如，当您给函数 A 配置了 test Bucket 的 “Created: * ” 和前缀过滤为 “Log” 的事件触发，那么该 test Bucket下就不能再创建 “Created: * ” 和前缀过滤为 “Log” 的事件触发。

- 目前 COS 触发器仅支持同地域 COS Bucket 事件触发，即广州区创建的 SCF 函数，在配置 COS 触发器时，仅支持选择广州区（华南）的 COS Bucket。如果您想要使用特定地域的 COS Bucket 事件来触发 SCF 函数，可以通过在对应地域下创建函数来实现。

- COS 触发器有 SCF 侧和 COS 侧两个维度限制：
 - SCF 侧限制：云函数仅支持单函数绑定10个 COS 触发器。 
 - COS 侧限制：单函数的相同事件和前后缀规则可以支持触发3个函数，单个 COS 存储桶可绑定的规则上限为10个。


## COS 触发器的事件消息结构

在指定的 COS Bucket 发生对象创建或对象删除事件时，会将类似以下的 JSON 格式事件数据发送给绑定的 SCF 函数。

```
{
	"Records": [{
		"cos": {
			"cosSchemaVersion": "1.0",
			"cosObject": {
				"url": "http://testpic-1253970026.cos.ap-chengdu.myqcloud.com/testfile",
				"meta": {
					"x-cos-request-id": "NWMxOWY4MGFfMjViMjU4NjRfMTUyMVxxxxxxxxx=",
					"Content-Type": "",
					"x-cos-meta-mykey": "myvalue"
				},
				"vid": "",
				"key": "/1253970026/testpic/testfile",
				"size": 1029
			},
			"cosBucket": {
				"region": "cd",
				"name": "testpic",
				"appid": "1253970026"
			},
			"cosNotificationId": "unkown"
		},
		"event": {
			"eventName": "cos:ObjectCreated:*",
			"eventVersion": "1.0",
			"eventTime": 1545205770,
			"eventSource": "qcs::cos",
			"requestParameters": {
				"requestSourceIP": "192.168.15.101",
				"requestHeaders": {
					"Authorization": "q-sign-algorithm=sha1&q-ak=xxxxxxxxxxxxxx&q-sign-time=1545205709;1545215769&q-key-time=1545205709;1545215769&q-header-list=host;x-cos-storage-class&q-url-param-list=&q-signature=xxxxxxxxxxxxxxx"
				}
			},
			"eventQueue": "qcs:0:scf:cd:appid/1253970026:default.printevent.$LATEST",
			"reservedInfo": "",
			"reqid": 179398952
		}
	}]
}
```

数据结构内容详细说明如下：

|    结构名    | 内容 |
| ---------- | --- |
| Records |  列表结构，可能有多条消息合并在列表中。 |
| event       |  记录事件信息，包括事件版本、事件源、事件名称、时间、队列信息、请求参数、请求 ID。 |
| cos | 记录事件对应的 COS 信息。 |
| cosBucket |  记录具体事件发生的 Bucket，包含 Bucket 名称、地域、所属用户 APPID。 |
| cosObject |  记录具体事件发生的对象，包含对象文件路径、大小、自定义元数据、访问 URL。  |

## 相关示例
以下为 Java 语言的 COS 触发器示例，您可参考示例进行使用：
```
https://github.com/tencentyun/scf-demo-java/blob/master/src/main/java/example/Cos.java
```


