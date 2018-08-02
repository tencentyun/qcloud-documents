## 为什么提供 SDK
- 云支付SDK对支付请求的各种参数进行打包和签名，封装了各种使用上的细节，并包含了自动重试，运行日志上传等功能，服务商使用更方便，且定位故障更快速和准确。

## SDK 提供了哪些接口
- SDK提供了**普通初始化**、**刷卡支付**、**扫码支付**、**查询订单**、**申请退款**、**查询退款**、**门店下载**，**订单批量下载**，**交易统计**等接口。

## SDK 支持的第三方支付平台
- SDK支持微信支付和支付宝。

## SDK 平台和语言
- Windows 环境下的 C++。
- C。
- .NET C#。
- JAVA。

## 下载地址
- [windows环境C++](https://main.qcloudimg.com/raw/f2897de4f46e1e774fdc45bc31c51e46.zip)，其中刷卡支付和扫码支付为异步方式，接口调用成功只代表支付提交成功，支付结果需要通过查询订单得到；取消订单、申请退款、退款查询、门店上传、门店下载接口为同步调用云支付接口；解压后包含两个目录：   
&radic;&nbsp;&nbsp;&nbsp;CloudPayAPI\_SDK\_CPP\_DLL目录，包含编译好的dll库，可直接使用。  
&radic;&nbsp;&nbsp;&nbsp;CloudPayAPI\_SDK\_CPP目录，包含源码，开发者可自行编译。  
- [C](https://main.qcloudimg.com/raw/daa50afec21c3d8c8030b783448ba10a.zip)，所有接口均为同步接口。
- [C#](https://main.qcloudimg.com/raw/5466c7694032a4b73331537002fc52b8.zip)，所有接口均为同步接口。
- [JAVA](https://main.qcloudimg.com/raw/c865fea31d32d60ab8553a13c3aeca6a.jar)，所有接口均为同步接口。

