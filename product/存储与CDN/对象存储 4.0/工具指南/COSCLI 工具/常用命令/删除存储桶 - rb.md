rb 命令用于删除存储桶。

## 命令格式
使用桶别名访问：
```plaintext
./coscli rb cos://<bucketAlias> [flag]
```

如果您希望使用桶全称访问桶，则需要额外携带 `endpoint` flag。命令格式如下：

```plaintext
./coscli rb cos://<BucketName-APPID> -e <endpoint> [flag]
```
>? 
>- 有关 bucketAlias 的说明，请参见 [下载与安装配置](https://cloud.tencent.com/document/product/436/63144#alias)。
>- 关于此命令的其他通用选项（例如切换存储桶、切换用户账号等），请参见 [通用选项](https://cloud.tencent.com/document/product/436/71763) 文档。
>

rb 命令包含以下参数：
| 参数格式  | 参数用途     | 示例                |
| --------- | ------------- | ------------------------ |
 cos://&lt;bucketAlias&gt; | 需要进行操作的存储桶别名。别名需要在配置文件中提前配置好。添加配置请参考 [修改配置文档](https://cloud.tencent.com/document/product/436/63679)  |example-alias  |
| cos://&lt;BucketName-APPID&gt; | 需要进行操作的存储桶名称  |examplebucket-1250000000  |

rb 命令包含以下可选 flag：

| flag 简写 | flag 全称     | flag 用途                |
| --------- | ------------- | ------------------------ |
| -h |  --help |   查看该命令的具体用法  |
| -r        | --region      | 存储桶地域               |

>!
>- rb 命令仅可删除空存储桶，如果您的桶中还有文件请使用 [删除文件](https://cloud.tencent.com/document/product/436/63671) 命令清空存储桶后再删除。
>- 使用 rb 命令成功删除存储桶后，推荐您在配置文件中删除该桶的信息。指令见下方操作实例。
>
## 操作示例

```plaintext
// 删除存储桶 bucket3
./coscli rb cos://bucket3-1250000000 -e cos.ap-chengdu.myqcloud.com
```

```
// 更新配置文件
./coscli config delete -a bucket3
```
