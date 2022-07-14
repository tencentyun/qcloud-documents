signurl 命令用于获取某个对象的预签名 URL，可以通过此 URL 匿名访问对象。

## 命令格式

```plaintext
./coscli signurl cos://<bucketAlias>/<key> [flag]
```

>? 
>- 有关 bucketAlias 的说明，请参见 [下载与安装配置](https://cloud.tencent.com/document/product/436/63144#alias)。
>- 关于此命令的其他通用选项（例如切换存储桶、切换用户账号等），请参见 [通用选项](https://cloud.tencent.com/document/product/436/71763) 文档。
>

signurl 命令包含以下可选 flag：

| flag 简写 | flag 全称     | flag 用途                    |
| --------- | ------------- | ---------------------------- |
| -t        | --time        | 设置 URL 过期时间（默认1000s） |

## 操作示例

### 获取 bucket1 桶内 pictrue.jpg 的预签名 URL

```plaintext
./coscli signurl cos://bucket1/pictrue.jpg
```

### 获取 bucket2 桶内 pictrue.jpg 的预签名 URL，并设置 URL 的过期时间为1314秒

```plaintext
./coscli signurl cos://bucket2/pictrue.jpg --time 1314
```

