### 使用 C SDK 如何实现断点续传？

可以使用 [C SDK 高级上传](https://cloud.tencent.com/document/product/436/35558#.E4.B8.8A.E4.BC.A0.E5.AF.B9.E8.B1.A1.EF.BC.88.E6.96.AD.E7.82.B9.E7.BB.AD.E4.BC.A0.EF.BC.89) 接口实现断点续传功能。使用断点续传时，需设置上传控制参数为 **COS_TRUE**，例如：`clt_params = cos_create_resumable_clt_params_content(p, 0, 1, COS_TRUE, NULL)`。

### 使用 C SDK 出现HttpIOError错误

在sdk使用过程中发现任何一个接口都没法正常使用，且没法返回requestid，抓包分析发现http请求都没有发送出去，并结合如下的日志情况：<br>
transport failure curl code:1 error:Unsupported protocol<br>
status->code: -996<br>
status->error_code: HttpIoError<br>
status->error_msg: Unsupported protocol<br>
status->req_id:<br>
出现这种情况的问题为：使用了https协议，但是libcurl库却不支持https协议，可能的原因是libcurl编译时没有使能openssl库或版本不匹配。<br>
解决方法：检查运行环境，重新安装libcurl库(源码编译安装需要使能ssl)或更新openssl库。