### 使用 C SDK 如何实现断点续传？

可以使用 [C SDK 高级上传](https://cloud.tencent.com/document/product/436/35558#.E4.B8.8A.E4.BC.A0.E5.AF.B9.E8.B1.A1.EF.BC.88.E6.96.AD.E7.82.B9.E7.BB.AD.E4.BC.A0.EF.BC.89) 接口实现断点续传功能。使用断点续传时，需设置上传控制参数为 **COS_TRUE**，例如：`clt_params = cos_create_resumable_clt_params_content(p, 0, 1, COS_TRUE, NULL)`。

