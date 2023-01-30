abort 命令用于清理分块上传过程中产生的文件碎片。

## 命令格式
使用桶别名访问：
```plaintext
./coscli abort cos://<bucketAlias>[/prefix/] [flag]
```

如果您希望使用桶全称访问桶，则需要额外携带 `endpoint` flag。命令格式如下：

```plaintext
./coscli abort cos://<bucket-name>[/prefix/] -e <endpoint> [flag]
```

>? 
>- 有关 bucketAlias 的说明，请参见 [下载与安装配置](https://cloud.tencent.com/document/product/436/63144#alias)。
>- 关于此命令的其他通用选项（例如切换存储桶、切换用户账号等），请参见 [通用选项](https://cloud.tencent.com/document/product/436/71763) 文档。
>

abort 命令包含以下参数：
| 参数格式  | 参数用途     | 示例                |
| --------- | ------------- | ------------------------ |
 cos://&lt;bucketAlias&gt; | 需要进行操作的存储桶别名。别名需要在配置文件中提前配置好。添加配置请参考 [修改配置文档](https://cloud.tencent.com/document/product/436/63679)  |example-alias  |
| cos://&lt;BucketName-APPID&gt; | 需要进行操作的存储桶名称  |examplebucket-1250000000  |
| /prefix/          | 可选参数。指定某一文件夹 | /picture/ |


abort 命令包含以下可选 flag：

| flag 简写 | flag 全称     | flag 用途                |
| --------- | ------------- | ------------------------ |
| -h |  --help |   查看该命令的具体用法  |
|     无      | --include     | 包含特定模式的文件       |
|     无      | --exclude     | 排除特定模式的文件       |

## 操作示例

### 清除 bucket1 桶内的所有文件碎片

```plaintext
./coscli abort cos://bucket1
```

### 清除 bucket1 桶内 pictrue 文件夹下的所有碎片

```plaintext
./coscli abort cos://bucket1/pictrue/
```
