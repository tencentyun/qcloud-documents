rb 命令用于删除存储桶。

## 命令格式

```plaintext
./coscli rb cos://<BucketName-APPID> -r <Region> [flag]
```

rb 命令包含以下可选 flag：

| flag 简写 | flag 全称     | flag 用途                |
| --------- | ------------- | ------------------------ |
| -h        | --help        | 输出帮助信息             |
| -c        | --config-path | 指定要使用的配置文件路径 |
| -r        | --region      | 存储桶地域               |

## 操作示例

```plaintext
// 删除存储桶 bucket3
./coscli rb cos://bucket3-1250000000 -r ap-chengdu
// 更新配置文件
./coscli config delete -a bucket3
```
