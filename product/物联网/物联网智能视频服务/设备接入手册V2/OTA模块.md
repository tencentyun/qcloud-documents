## 功能介绍

本模块用于将设备端实现 OTA 功能，当设备有新功能或者需要修复漏洞时，设备可以通过 OTA 服务快速的进行固件升级。

## 使用流程

固件升级的过程中，通过 MQTT 实现与云端的信令交互，上报本地固件版本号，等待云端下发升级指令，并上报升级状态。在拿到固件的 URL 地址之后，会通过 HTTP 下载固件。

>! SDK 会在用户提供的固件下载目录下面创建包含固件版本号的**.bin**文件，某些平台对文件名的长度有限制，因此在云端控制台创建固件版本号不宜太长。

```
iv_ota_init          //提供本地固件版本及下载路径，开始OTA流程
    |
iv_ota_firmware_update_cb // 固件下载完成之后，收到回调，开始更新固件
    |
iv_ota_update_progress // 更新固件过程中通过该函数上报结果
    |
iv_ota_exit          // 更新成功或出现异常，都需要停止OTA模块运行
```

## 接口简介

接口函数声明请参考 **iv_ota.h**，具体内容请 [单击此处](https://cloud.tencent.com/apply/p/ozpml9a5po) 进行 SDK 获取。

## 操作流程

设备的升级流程如下所示：
![OTA 时序图](https://main.qcloudimg.com/raw/a2f10ab90959a23b1675201b1e2311e0.jpg)

1. 设备上报当前版本号。
   当执行**iv_ota_init**之后，SDK会启动单独的 OTA 任务线程，并通过 MQTT 协议进行版本号的上报，消息为 json 格式，内容如下：
```json
{
	"type": "report_version",
	"report":{
    	"version": "0.1"
	}
}
// type：消息类型
// version：上报的版本号
```
2. 然后您可以在控制台上传固件。
   具体控制台操作指引，可以参考 [固件升级](https://cloud.tencent.com/document/product/1131/56756)
3. 在控制台将指定的设备升级到指定的版本。
4. 触发固件升级操作后，设备端 SDK 会收到固件升级的消息，内容如下：
``` json
{
    "file_size": 708482,
    "md5sum": "36eb59511****14a631463a37a9322a2",
    "type": "update_firmware",
    "url": "https://ota-1255858890.cos.ap-guangzhou.myqcloud.com",
    "version": "0.2"
}
// type：消息类型为update_firmware
// version：升级版本
// url：下载固件的url
// md5asum：固件的MD5值
// file_size：固件大小，单位为字节
```
5. 设备端 SDK 在收到固件升级的消息后，会根据 URL 下载固件，下载的过程中设备 SDK 会不断的上报下载进度，上报的内容如下： 
```json
{
    "type": "report_progress",
    "report":{
        "progress":{
               "state":"downloading",
          	   "percent":"10",
               "result_code":"0",
               "result_msg":""
        },
        "version": "0.2"
    }
}
// type：消息类型
// state：状态为正在下载中
// percent：当前下载进度，百分比
```
6. 当设备端 SDK 下载完固件并校验 MD5 正确之后，会通过回调**iv_ota_firmware_update_cb**通知使用者，并告知固件地址及相关信息。
   使用者在开始更新固件之前，需要通过 **iv_ota_update_progress** 来触发 SDK 上报一条开始升级的消息，内容如下：

```json
{
    "type": "report_progress",
    "report":{
        "progress":{
               "state":"burning",
               "result_code":"0",
               "result_msg":""
        },
        "version": "0.2"
    }
}
// type：消息类型
// state：状态为烧制中
```
7. 设备固件升级完成后，再通过 **iv_ota_update_progress** 来触发 SDK 上报升级成功消息，内容如下：
```json
{
	"type": "report_progress",
	"report":{
		"progress":{
       		"state":"done",
       		"result_code":"0",
       		"result_msg":""
		},
		"version": "0.2"
	}
}
// type：消息类型
// state：状态为已完成
```
>!在下载固件或升级固件的过程中，如果失败，同样通过**iv_ota_update_progress**来触发 SDK 上报升级失败消息，内容如下：
>
```json
{
	"type": "report_progress",
	"report":{
		"progress":{
       		"state":"fail",
       		"result_code":"-1",
       		"result_msg":"time_out"
		},
		"version": "0.2"
	}
}
// state：状态为失败
// result_code：错误码，-1：下载超时；-2：文件不存在；-3：签名过期；-4:MD5不匹配；-5：更新固件失败
// result_msg：错误消息
```
8. 当固件升级结束之后，或者发生异常需要退出的时候，需要调用 **iv_ota_exit** 退出 OTA 模块，否则会循环上报版本并进行 OTA 过程。

## OTA断点续传

物联网设备有部分场景处于弱网环境，在这个场景下连接会不稳定，固件下载会中断的情况出现。如果每次都从0偏移开始下载固件，则弱网环境有可能一直无法完成全部固件下载，因此固件的断点续传功能特别必要。

断点续传就是从文件上次中断的地方开始重新下载或上传，要实现断点续传的功能，需要设备端记录固件下载的中断位置，同时记录下载固件的md5、文件大小、版本信息。

平台针对 OTA 中断的场景，设备侧 report 设备的版本，如果上报的版本号与要升级的目标版本号不一致，则平台会再次下发固件升级消息，设备获取到升级的目标固件的信息与本地记录的中断的固件信息比较，确定为同一固件后，基于断点继续下载。

目前 SDK 会在用户提供的固件下载路径下，创建 json 文件实现记录描述，如果固件下载路径下除了 bin 固件文件，还存在一个文本文件，则说明固件下载还未完成，在固件下载完成并校验无误之后，SDK 会自动删除文本描述文件。

带断点续传的 OTA 升级流程如下，弱网环境下第3步到第6步有可能会多次执行，没有执行第7步，执行第3步，设备端都会收到第4步的消息。

![OTA 断点续传时序图](https://main.qcloudimg.com/raw/5d17e84352b59ea448fb95824ea53e6d.jpg)
