rb 命令用于删除存储桶。

## 命令格式

```plaintext
./coscli rb cos://<BucketName-APPID> -r <Region> [flag]
```

rb 命令包含以下可选 flag：

| flag 简写 | flag 全称     | flag 用途                |
| --------- | ------------- | ------------------------ |
| 无 |  BucketName-APPID |   指定需要删除的存储桶名称，例如 examplebucket-1250000000  |
| -r        | --region      | 存储桶地域               |

>? 关于此命令的其他通用选项（例如切换存储桶、切换用户账号等），请参见 [通用选项](https://cloud.tencent.com/document/product/436/71763) 文档。
>
## 操作示例

```plaintext
// 删除存储桶 bucket3
./coscli rb cos://bucket3-1250000000 -r ap-chengdu
// 更新配置文件
./coscli config delete -a bucket3
```
