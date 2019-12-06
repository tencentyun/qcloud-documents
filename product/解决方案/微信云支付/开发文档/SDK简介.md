## 简介
云支付 SDK 对支付请求的各种参数进行打包和签名，封装了各种使用上的细节，并包含了自动重试、运行日志上传等功能，服务商使用更方便，且定位故障更快速、准确。

## SDK 接口
SDK 提供了**普通初始化**、**刷卡支付**、**扫码支付**、**查询订单**、**申请退款**、**查询退款**、**门店下载**、**订单批量下载**、**交易统计**等接口。

## 第三方支付平台
SDK 支持微信支付和支付宝。

## SDK 平台和语言
- Windows 环境下的 C++
- C
- .NET C#
- Java

## 下载地址
- [Windows 环境 C++](https://main.qcloudimg.com/raw/8b159f9a7f202d1896ac66ae6c0bf0e4.zip)：其中刷卡支付和扫码支付为异步方式，接口调用成功只代表支付提交成功，支付结果需要通过查询订单获取；取消订单、申请退款、退款查询、门店上传、门店下载接口为同步调用云支付接口。解压后包含以下两个目录：   
	- `CloudPayAPI\_SDK\_CPP\_DLL`目录，包含编译好的 dll 库，可直接使用。  
	- `CloudPayAPI\_SDK\_CPP`目录，包含源码，开发者可自行编译。  
- [C](https://main.qcloudimg.com/raw/daa50afec21c3d8c8030b783448ba10a.zip)：所有接口均为同步接口。
- [C#](https://main.qcloudimg.com/raw/b104bf696c175aeb3b712ebe1b488342.rar)：所有接口均为同步接口。
- [Java](https://tyx-cloudpay-1253256722.cos.ap-chengdu.myqcloud.com/%E5%BE%AE%E4%BF%A1%E4%BA%91%E6%94%AF%E4%BB%98_JAVA_SDK_1.6.zip)：所有接口均为同步接口。
