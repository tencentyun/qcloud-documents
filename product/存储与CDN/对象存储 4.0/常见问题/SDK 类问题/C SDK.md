### 使用 C SDK 如何实现断点续传？

可以使用 [C SDK 高级上传](https://cloud.tencent.com/document/product/436/35558#.E4.B8.8A.E4.BC.A0.E5.AF.B9.E8.B1.A1.EF.BC.88.E6.96.AD.E7.82.B9.E7.BB.AD.E4.BC.A0.EF.BC.89) 接口实现断点续传功能。使用断点续传时，需设置上传控制参数为 **COS_TRUE**，例如：`clt_params = cos_create_resumable_clt_params_content(p, 0, 1, COS_TRUE, NULL)`。

### 使用 C SDK 出现 HttpIOError 错误？

在 SDK 使用过程中发现任何一个接口都没法正常使用，且没法返回 requestid，抓包分析发现 HTTP 请求都没有发送出去。结合如下的日志情况：
```
transport failure curl code:1 error:Unsupported protocol
status->code: -996
status->error_code: HttpIoError
status->error_msg: Unsupported protocol
status->req_id:
```

发现出现这种情况的原因为：使用了 HTTPS 协议，但是 libcurl 库却不支持 HTTPS 协议。从而导致 libcurl 编译时没有使用 openssl 库或版本不匹配。
**解决方法**：检查运行环境，重新安装 libcurl 库（源码编译安装需要使能 SSL）或更新 openssl 库。
