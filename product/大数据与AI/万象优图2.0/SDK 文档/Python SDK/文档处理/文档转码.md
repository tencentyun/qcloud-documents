
## 简介

本文档提供关于文档预览的相关的 API 概览以及 SDK 示例代码。

| API           |    操作名  |   操作描述               |
| :--------------- | :------------------ | :--------------------- |
| [CreateDocProcessJobs](https://cloud.tencent.com/document/product/436/54056)|   提交文档预览任务        |   用于提交一个文档预览任务   |
| [DescribeDocProcessJob](https://cloud.tencent.com/document/product/436/54095) |   查询文档预览任务    |查询指定的文档预览任务 |
| [DescribeDocProcessJobs](https://cloud.tencent.com/document/product/436/54096)  |  拉取文档预览任务     |  拉取符合条件的文档预览任务   |



## 提交文档预览任务

#### 功能说明

ci_create_doc_job 接口用于提交一个文档预览任务。

#### 示例代码

```python
   response = client.ci_create_doc_job(
                    Bucket="examplebucket-1250000000",
                    QueueId='pbbbcc56b344e422da78c984be45*****',
                    InputObject='normal.pptx',
                    OutputBucket="examplebucket-1250000000",
                    OutputRegion='ap-chongqing',
                    OutputObject='/test_doc/normal/abc_${Number}.jpg',
                )
    print(response)
    return response 
```


#### 参数说明

调用 ci_create_doc_job 函数，具体请求参数如下：

| 参数名称  | 描述                                                         | 类型   | 是否必选 |
| --------- | ------------------------------------------------------------ | ------ | -------- |
| Bucket | 存储桶名称。                                 | String  | 是       |
| QueueId| 任务所在的队列 ID。                | String  | 是       |
| InputObject| 文件在 COS 上的文件路径。                | String  | 是       |
| OutputBucket| 存储结果的存储桶。                | String  | 是       |
| OutputRegion| 存储结果的存储桶的地域。                | String  | 是       |
| OutputObject| 输出文件路径。<br/>**非表格文件输出文件名需包含 ${Number} 或 ${Page} 参数。**多个输出文件，${Number} 表示序号从1开始，${Page} 表示序号与预览页码一致。<ul style="margin-bottom:0px"><li>${Number} 表示多个输出文件，序号从1开始，例如输入 abc_${Number}.jpg，预览某文件5 - 6页，则输出文件名为 abc_1.jpg，abc_2.jpg</li><li>${Page} 表示多个输出文件，序号与预览页码一致，例如输入 abc_${Page}.jpg，预览某文件5 - 6页，则输出文件名为 abc_5.jpg，abc_6.jpg。<br/>**表格文件输出路径需包含 ${SheetID} 占位符，输出文件名必须包含 ${Number} 参数。**<br>例如 `/${SheetID}/abc_${Number}.jpg`，先根据 excel 转换的表格数，生成对应数量的文件夹，再在对应的文件夹下，生成对应数量的图片文件</li>   </ul>         | String  | 是       |
| SrcType|  源数据的后缀类型，当前文档转换根据 COS 对象的后缀名来确定源数据类型，当 COS 对象没有后缀名时，可以设置该值。                | String  | 否       |
| TgtType|  转换输出目标文件类型：<br>jpg，转成 jpg 格式的图片文件。如果传入的格式未能识别，默认使用 jpg 格式。<br>png，转成 png 格式的图片文件。<br>pdf，转成 pdf 格式文件（暂不支持指定页数）。                | String  | 否       |
| StartPage|  从第 X 页开始转换。在表格文件中，一张表可能分割为多页转换，生成多张图片。StartPage 表示从指定 SheetId 的第 X 页开始转换。默认为1。                | Int  | 否       |
| EndPage|  转换至第 X 页。在表格文件中，一张表可能分割为多页转换，生成多张图片。EndPage 表示转换至指定 SheetId 的第 X 页。默认为-1，即转换全部页。                | Int  | 否       |
| SheetId|  表格文件参数，转换第 X 个表，默认为0。设置 SheetId 为0，即转换文档中全部表。                | Int  | 否       |
| PaperDirection| 表格文件转换纸张方向，0代表垂直方向，非0代表水平方向，默认为0。                | Int  | 否       |
| PaperSize|  设置纸张（画布）大小，对应信息为： `0 → A4` 、 `1 → A2` 、 `2 → A0` ，默认 A4 纸张。            | Int  | 否       |
| DocPassword|  Office 文档的打开密码，如果需要转换有密码的文档，请设置该字段。	                | String  | 否       |
| Comments|  是否隐藏批注和应用修订，默认为 0。<br>0：隐藏批注，应用修订。1：显示批注和修订。                | Int  | 否       |
| ImageParams|   转换后的图片处理参数，支持基础图片处理所有处理参数，多个处理参数可通过管道操作符分隔，从而实现在一次访问中按顺序对图片进行不同处理。                | String  | 否       |
| Quality|  生成预览图的图片质量，取值范围 [1-100]，默认值100。 例：值为100，代表生成图片质量为100%。                | Int  | 否       |
| Zoom|   预览图片的缩放参数，取值范围[10-200]， 默认值100。 例：值为200，代表图片缩放比例为200% 即放大两倍。                | Int  | 否       |
| ImageDpi|  按指定 dpi 渲染图片，该参数与 Zoom 共同作用，取值范围 96-600 ，默认值为 96。转码后的图片单边宽度需小于65500像素。                | Int  | 否       |
| PicPagination| 是否转换成单张长图，设置为 1 时，最多仅支持将 20 标准页面合成单张长图，超过可能会报错，分页范围可以通过 StartPage、EndPage 控制。默认值为 0 ，按页导出图片，TgtType="png"/"jpg" 时生效。                | Int  | 否       |

#### 返回参数说明

调用 ci_create_doc_jobs 函数，会把 api 里面的 xml 返回转换成 dict，具体返回参数可查看 [提交文档预览任务](https://cloud.tencent.com/document/product/436/54056) 文档。

## 查询文档预览任务

#### 功能说明


ci_get_doc_job 用于查询指定的文档预览任务。

#### 示例代码

```python
    response = client.ci_get_doc_job(
                    Bucket="examplebucket-1250000000",
                    JobID='d31d414c8c07811ec894cd30d17*****',
                )
    print(response)
    return response 
```

#### 参数说明

调用 ci_get_doc_job 函数，具体请求参数如下：

| 参数名称  | 描述                     | 类型   | 是否必选 |
| --------- | --------------------- | ------ | -------- |
| Bucket | 存储桶名称。          | String  | 是       |
| JobID| 任务 ID。                | String  | 是       |

#### 返回参数说明

调用 ci_get_doc_job 函数，会把 api 里面的 xml 返回转换成 dict，具体返回参数可查看 [查询文档预览任务](https://cloud.tencent.com/document/product/436/54095) 文档。



## 查询所有文档预览任务

#### 功能说明

ci_list_doc_jobs 用于查询指定的文档预览任务。

#### 示例代码

```python
    response = client.ci_list_doc_jobs(
                    Bucket="examplebucket-1250000000",
                    QueueId='pbbbcc56b344e422da78c984be45*****',
                )
    print(response)
    return response 
```

#### 参数说明

调用 ci_list_doc_jobs 函数，具体请求参数如下：

| 参数名称  | 描述               | 类型   | 是否必选 |
| --------- | ----------------- | ------ | -------- |
| Bucket | 存储桶名称。         | String  | 是       |
| QueueId| 任务所在的队列 ID。         | String  | 是       |
| StartCreationTime| 开始时间。      | String  | 否       |
| EndCreationTime| 结束时间。       | String  | 否       |
| OrderByTime| 排序方式。Desc 或者 Asc。默认为 Desc。  | String  | 否    |
| States| 拉取该状态的任务，以`,`分割，支持多状态：All、Submitted、Running、Success、Failed、Pause、Cancel。默认为 All。  | String  | 否       |
| Size| 	拉取的最大任务数。默认为10。最大为100。   | String  | 否       |
| NextToken| 请求的上下文，用于翻页。   | String  | 否       |

#### 返回参数说明

调用 ci_list_doc_jobs 函数，会把 api 里面的 xml 返回转换成 dict，具体返回参数可查看 [拉取文档预览任务](https://cloud.tencent.com/document/product/436/54096) 文档。
