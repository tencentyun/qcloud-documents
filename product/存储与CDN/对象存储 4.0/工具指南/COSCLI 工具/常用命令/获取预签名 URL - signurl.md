signurl 命令用于获取某个对象的预签名 URL，可以通过此 URL 匿名访问对象。

## 命令格式
使用桶别名访问：
```plaintext
./coscli signurl cos://<bucketAlias>/<key> [flag]
```

如果您希望使用桶全称访问桶，则需要额外携带 `endpoint` flag。命令格式如下：

```plaintext
./coscli signurl cos://<BucketName-APPID>/<key> -e <endpoint> [flag]
```

>? 
>- 有关 bucketAlias 的说明，请参见 [下载与安装配置](https://cloud.tencent.com/document/product/436/63144#alias)。
>- 关于此命令的其他通用选项（例如切换存储桶、切换用户账号等），请参见 [通用选项](https://cloud.tencent.com/document/product/436/71763) 文档。
>

signurl 命令包含以下参数：

| 参数格式          | 参数用途       | 示例                 |
| ----------------- | -------------- | -------------------- |
 cos://&lt;bucketAlias&gt;/&lt;key&gt; | 使用存储桶别名指定桶中的对象。桶别名需要在配置文件中提前配置好。添加配置请参考 [修改配置文档](https://cloud.tencent.com/document/product/436/63679)  |example-alias/test.txt  |
| cos://&lt;BucketName-APPID&gt;/&lt;key&gt; | 使用存储桶名称指定桶中的对象  |examplebucket-1250000000/test.txt  |


signurl 命令包含以下可选 flag：

| flag 简写 | flag 全称     | flag 用途                    |
| --------- | ------------- | ---------------------------- |
| -h |  --help |   查看该命令的具体用法  |
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

