mb 命令用于创建存储桶。

## 命令格式

```plaintext
./coscli mb cos://<BucketName-APPID> -r <Region> [flag]
```

mb 命令包含以下可选 flag：

| flag 简写 | flag 全称     | flag 用途                |
| --------- | ------------- | ------------------------ |
| -h        | --help        | 输出帮助信息             |
| -c        | --config-path | 指定要使用的配置文件路径 |
| -r        | --region      | 存储桶地域               |

>! 若想在 COSCLI 中操作以 mb 命令创建的存储桶，需要在 mb 命令成功后，使用 config add 命令在配置文件中更新存储桶配置。
>

## 操作示例

```plaintext
// 创建存储桶 bucket3
./coscli mb cos://bucket3-1250000000 -r ap-chengdu
// 更新配置文件
./coscli config add -b bucket3-1250000000 -r ap-chengdu -a bucket3
// 更新后可用 cos://bucket3 访问此存储桶
```
