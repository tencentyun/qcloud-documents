mb 命令用于创建存储桶。

## 命令格式

```plaintext
./coscli mb cos://<BucketName-APPID> -e <endpoint> [flag]
```

>! 使用 mb 命令创建存储桶，需要携带全局 flag `-e` 或 `--endpoint` 指定存储桶所在地域。

mb 命令包含以下参数：

| 参数格式  | 参数用途     | 示例                |
| --------- | ------------- | ------------------------ |
| cos://&lt;BucketName-APPID&gt; | 用于自定义存储桶名称  |cos://examplebucket-1250000000  |


mb 命令包含以下可选 flag：

| flag 简写 | flag 全称     | flag 用途                |
| --------- | ------------- | ------------------------ |
| -h |  --help |   查看该命令的具体用法  |
| -r        | --region      | 存储桶地域               |

>! 
>- 使用 mb 命令成功创建存储桶后，推荐您在配置文件中新增该桶的信息，方便后续使用桶别名快速操作。具体命令用法，可参见下方操作示例。
>- 关于此命令的其他通用选项（例如切换存储桶、切换用户账号等），请参见 [通用选项](https://cloud.tencent.com/document/product/436/71763) 文档。
>

## 操作示例

```plaintext
// 创建存储桶 bucket3
./coscli mb cos://bucket3-1250000000 -e cos.ap-chengdu.myqcloud.com
```

如果您希望为刚创建的存储桶配置别名，需要使用以下命令更新配置文件：

```plaintext
// 更新配置文件
./coscli config add -b bucket3-1250000000 -e cos.ap-chengdu.myqcloud.com -a bucket3
// 更新后可用 cos://bucket3 访问此存储桶
```
