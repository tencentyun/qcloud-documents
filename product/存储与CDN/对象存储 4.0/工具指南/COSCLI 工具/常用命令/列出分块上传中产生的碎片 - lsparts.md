lsparts 命令列出分块上传中产生的文件碎片。
>! 关于分块上传的更多信息，请参见 [分块上传](https://cloud.tencent.com/document/product/436/14112)。

## 命令格式
使用桶别名访问：
```plaintext
./coscli lsparts cos://<bucketAlias>[/prefix/] [flag]
```

如果您希望使用桶全称访问桶，则需要额外携带 `endpoint` flag。命令格式如下：

```plaintext
./coscli lsparts cos://<bucket-name>[/prefix/] -e <endpoint> [flag]
```

>? 
>- 有关 bucketAlias 的说明，请参见 [下载与安装配置](https://cloud.tencent.com/document/product/436/63144#alias)。
>- 关于此命令的其他通用选项（例如切换存储桶、切换用户账号等），请参见 [通用选项](https://cloud.tencent.com/document/product/436/71763) 文档。
>

lsparts 命令包含以下参数：
| 参数格式  | 参数用途     | 示例                |
| --------- | ------------- | ------------------------ |
 cos://&lt;bucketAlias&gt; | 需要进行操作的存储桶别名。别名需要在配置文件中提前配置好。添加配置请参考 [修改配置文档](https://cloud.tencent.com/document/product/436/63679)  |example-alias  |
| cos://&lt;BucketName-APPID&gt; | 需要进行操作的存储桶名称  |examplebucket-1250000000  |
| /prefix/          | 可选参数。指定某一文件夹 | /picture/ |

lsparts 命令包含以下可选 flag：

| flag 简写 | flag 全称     | flag 用途                    |
| --------- | ------------- | ---------------------------- |
| -h |  --help |   查看该命令的具体用法  |
|     无      | --include     | 包含特定模式的文件           |
|     无      | --exclude     | 排除特定模式的文件           |
|     无      | --limit       | 指定列出的最大数量（0 - 1000） |


## 操作示例

### 列出 bucket1 桶内的所有文件碎片

```plaintext
./coscli lsparts cos://bucket1
```

返回的结果示例如下，输出的信息包括：对象键（对象在存储桶中的唯一标识），分块上传的 ID，分块上传的起始时间，桶内碎片总数量。

```
      KEY      |              UPLOAD ID              |      INITIATE TIME
---------------+-------------------------------------+----------------------------
    test.txt   | 1671191183635d2b71b1d68a0********** | 2022-01-01T00:00:00.000Z
---------------+-------------------------------------+----------------------------
                                                                TOTAL: 1
                                                      ----------------------------
```

### 列出 bucket1 桶内 pictrue 文件夹下的所有碎片

```plaintext
./coscli lsparts cos://bucket1/pictrue/
```
