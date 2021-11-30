版本：v1.1       
制定时间：2016.1

## **1. 内容说明**

**该文档用于指导直播码录制和截图功能用户进行相关操作**

## **2. 录制**

**接入流程**

在申请开通直播的基础上，需要申请录制所需要的点播账户权限。

开通为线下开通，功能开启和关闭均通过线下配置。即配置生效后，录制功能对该域名全部生效。故无录制开启和关闭操作。

**录制规则**

1. 1.开始推流时，即启动录制任务，直至直播结束
2. 2.录播按时间进行分片，最大大小为0.5小时；
3. 3.录播时，发生断流，则停止录播生成一个分片
4. 4.断流恢复后启动新的录播分片任务，重复1）2）3）的过程，直至整个任务结束
5. 5.录制分片请求url格式：http://（点播bizid).vod.myqcloud.com/（vid）.f0.flv

## **3. 截图**

**接入流程**

在申请开通直播的基础上，需要申请截图需要的cos平台权限，并获取cos账号信息。

开通为线下开通，功能开启和关闭均通过线下配置。即配置生效后，截图功能对该域名全部生效。故无截图开启和关闭操作。

**截图规则**

1. 开始推流时，即启动 截图任务，直至直播结束
2. 频率周期为10s，按照系统绝对时间；
3. 截图大小：分辨率300（宽）\*自适应（高）；
4. 截图对象：通过API制定的实时直播流；
5. 截图生成文件：文件名为（直播码id)\_（推流绝对时间戳）\_（任务启动时间戳）\_（截图相对时间）\_(长)\_(宽）.jpg
6. COS存放部分：
截图后，对应文件上载至COS系统；时间在15S内；
即15S内，用户可通过COS查询下载，COS账号、容量购买、下载部分由客户独立完成；
7. 图片url格式： [http://(cos\_bucketname)-(cos\_appid).file.myqcloud.com/文件名](http://(cos_bucketname)-(cos_appid).file.myqcloud.com/%E6%96%87%E4%BB%B6%E5%90%8D)

## **4. 接口形式**

接口采用http get方式实现，返回格式为json。

## **5. 接口定义**

**公共参数**

| **参数名** | **参数含义** | **类型** | **备注** | **是否必需** |
| --- | --- | --- | --- | --- |
| cmd | 业务id | int |   | Y |
| interface | 接口名 | string |   | Y |
| t | 有效截止时间戳 | int |   | Y |
| sign | 签名 | string | md5( **key** +有效截止时间戳) | Y |

**其中key为用户密钥，** 目前需要人工手动开启。

## **5.1 获取队列消息（含截图）**

**接口名：**

**Live\_Queue\_Get**

**输入说明**

| **参数名** | **参数含义** | **类型** | **备注** | **是否必需** |
| --- | --- | --- | --- | --- |
| Param.n.bid | 队列id | int | 100为截图 | Y |
| Param.ncount | 数量 | int | 取值在1~100，默认为1 | N |

**输出说明**

| **参数名** | **参数含义** | **类型** | **备注** | **其他说明** |
| --- | --- | --- | --- | --- |
| ret | 返回码 | int | 0，成功；其他值，失败 |   |
| message | 错误信息 | string | 错误描述 |   |
| output | 消息内容 | array |   |   |

**其中output部分结构为**

| **参数名** | **参数含义** | **类型** | **备注** | **其他说明** |
| --- | --- | --- | --- | --- |
| count | 数量 | string |   |   |
| data | 截图url列表 | array |   |   |

**其中data部分结构为**

| **参数名** | **参数含义** | **类型** | **备注** | **其他说明** |
| --- | --- | --- | --- | --- |
| stream\_id | 流id | string |   |   |
| pic\_url | 截图文件名 | string | 完整的url为： [http://(cos\_bucketname)](http://(cos_bucketname)-(cos_appid).file.myqcloud.com/%E6%96%87%E4%BB%B6%E5%90%8D) [-(cos\_appid).file.myqcloud.com/文件名](http://(cos_bucketname)-(cos_appid).file.myqcloud.com/%E6%96%87%E4%BB%B6%E5%90%8D) |   |

**完整的访问地址示例：**

** curl**"http://fcgi.video.qcloud.com/common\_access?cmd=3&interface=Live\_Queue\_Get&Param.n.bid=100&Param.n.count=10&t=1453279831&sign=XXXXXXXXXXXXXXXX"

## **5.2 获取录播分片**

**接口名：**

**Live\_Tape\_GetFilelist**

**输入说明**

| **参数名** | **参数含义** | **类型** | **备注** | **是否必需** |
| --- | --- | --- | --- | --- |
| Param.s.channel\_id | 直播码id | string |   | Y |
| Param.n.page\_no | 分页页码 | int | 从1开始，默认为1 | N |
| Param.n.page\_size | 分页大小 | int | 1~100，默认为10 | N |

**输出说明**

| **参数名** | **参数含义** | **类型** | **备注** | **其他说明** |
| --- | --- | --- | --- | --- |
| ret | 返回码 | int | 0，成功；其他值，失败 |   |
| message | 错误信息 | string | 错误描述 |   |
| output | 消息内容 | array |   |   |

**其中output部分结构为**

| **参数名** | **参数含义** | **类型** | **备注** | **其他说明** |
| --- | --- | --- | --- | --- |
| all\_count | 分片总个数 | int |   |   |
| file\_list | 分片文件信息 | array |   |   |

**其中file\_list部分结构为**

| **参数名** | **参数含义** | **类型** | **备注** | **其他说明** |
| --- | --- | --- | --- | --- |
| vid | 文件vid | string |   |   |
| start\_time | 分片开始时间 | string | 日期格式 |   |
| end\_time | 分片结束时间 | string | 日期格式 |   |

**完整的访问地址示例：**

** curl**"http://fcgi.video.qcloud.com/common\_access?cmd=3&interface=Live\_Tape\_GetFilelist&Param.n.channel\_id=123&t=1453279831&sign=XXXXXXXXXXXXXXXXXXXX"

## **5.3 获取频道状态**

**接口名：**

**Live\_Channel\_GetStatus**

**输入说明**

| **参数名** | **参数含义** | **类型** | **备注** | **是否必需** |
| --- | --- | --- | --- | --- |
| Param.s.channel\_id | 直播码id | string |   | Y |

**       **  **输出说明**

| **参数名** | **参数含义** | **类型** | **备注** | **其他说明** |
| --- | --- | --- | --- | --- |
| ret | 返回码 | int | 0，成功；其他值，失败 |   |
| message | 错误信息 | string | 错误描述 |   |
| output | 消息内容 | array |   |   |

**其中output部分结构为**

| **参数名** | **参数含义** | **类型** | **备注** | **其他说明** |
| --- | --- | --- | --- | --- |
| rate\_type | 码率 | int | 0-原始码率，10-普清，20-高清 |   |
| recv\_type | 接收协议 | int | 1-rtmp/flv，2-hls，3-rtmp/flv和hls |   |
| status | 状态 | int | 0-断流；1-有输入流 |   |

**完整的访问地址示例：**

**curl**"http://fcgi.video.qcloud.com/common\_access?cmd=3&interface=Live\_Channel\_GetStatus&Param.n.channel\_id=123&t=1453279831&sign=XXXXXXXXXXXX"

## **4. 鉴权**

**提供了安全机制保障，鉴权Key为32字节字符串，可通过联系客服人员进行开启和分配。**

