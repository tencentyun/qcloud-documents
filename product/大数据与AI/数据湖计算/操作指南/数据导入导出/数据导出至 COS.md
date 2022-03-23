数据湖计算 DLC 支持将托管存储中的数据表或者查询任务结果的数据导出到 COS中，可将结果导出为：CSV、JSON、Parquet、Avro、ORC 格式。
>? 执行数据导出 COS 时，不仅需要数据湖 DLC 的操作权限，同时需要具备 COS 数据相关操作权限。


## 通过控制台导出
支持用户通过配置将查询结果自动保存至 COS 路径下，配置方式如下：
1. 登录 [数据湖 DLC 控制台](https://console.cloud.tencent.com/dlc)，选择服务地域，登录的账号需具有 COS 相关的权限。
2. 进入**查询分析页面**，单击**高级配置设置**对查询结果保存方式进行配置。
3. 开启全量模式，配置 COS 存储路径。
![](https://qcloudimg.tencent-cloud.cn/raw/a088d81e03c4888ae68390acb155f7bd.png)
更多导出方式可参见 [获取任务结果](https://cloud.tencent.com/document/product/1342/61872)。

## 通过 API 导出
### 接口说明
接口名：[CreateExportTask](https://cloud.tencent.com/document/api/1342/71477)，参数如下：
<table>
<thead>
<tr>
<th >参数名</th>
<th >类型</th>
<th >描述</th>
<th >是否必须</th>
</tr>
</thead>
<tbody>
<tr>
<td>InputType</td>
<td>string</td>
<td>    输入类型：目前仅支持 taskResult、lakfsStorage  </td>
<td>true</td>
</tr>
<tr>
<td>InputConf</td>
<td>[]KVPair</td>
<td>输入配置：导出任务的输入配置参数
<li>从 taskResult 导出数据：taskId（任务 Id）</li>
<li>从 lakfsStorage 导出数据：databaseName、tableName  </li>
</td>
<td>true</td>
</tr>
<tr>
<td>OutputType</td>
<td>string</td>
<td>输出类型：目前仅支持 cos  </td>
<td>true</td>
</tr>
<tr>
<td>OutputConf</td>
<td>    []KVPair</td>
<td>输出配置：导入任务的输出配置参数，如 fileType、path、以及各种文件类型各自支持的参数，具体查看下文 </td>
<td>true</td>
</tr>
</tbody>
</table>

其中 OutputConf 参数如下：
            
| 参数名 | 类型 | 描述 |  是否必须 |
|---------|---------|---------| ---------|
| fileType|     string  | 文件类型，可选csv、JSON、parquet、avro、orc  | true| 
| path  | string    | 导出地路径 | true| 
| mode  | string    | 导出模式，可选append(默认)、overwrite   | false| 
| ......    | string    | 查看下文获取具体文件类型所支持的参数    | false| 

### 导出为 CSV 数据

| 参数名 | 描述 | 默认值 |
|---------|---------|---------|
| sep | 指定单个字符分割字段和值 | , |
| encoding  | 通过给定的编码类型进行解码 | uft-8| 
| quote | 其中分隔符可以是值的一部分，设置用于转义带引号的值的单个字符    | "| 
| escape    | 设置单个字符用于在引号里面转义引号 | \| 
| header    | 是否有表头 | true| 
| compression   | 压缩格式，可选择 none, bzip2, gzip,  and deflate  | none| 

### 导出 JSON 数据

| 参数名 | 描述 | 默认值 |
|---------|---------|---------|
| encoding  | 通过给定的编码类型进行解码 | uft-8| 
| compression   | 压缩格式，可选择 none, bzip2, gzip,  and deflate  | none| 


### 导出 Parquet 数据

| 参数名 | 描述 | 默认值 |
|---------|---------|---------|
| compression   | 压缩格式，可选择 none, bzip2, gzip,  and deflate  | none| 

### 导出 Avro 数据

| 参数名 | 描述 | 默认值 |
|---------|---------|---------|
| compression   | 压缩格式，可选择 none, bzip2, gzip,  and deflate  | none| 

### 导出 ORC 数据

| 参数名 | 描述 | 默认值 |
|---------|---------|---------|
| compression   | 压缩格式，可选择 none, bzip2, gzip,  and deflate  | none| 
