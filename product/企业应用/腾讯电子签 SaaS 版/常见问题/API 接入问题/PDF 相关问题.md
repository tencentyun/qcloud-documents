### 如何计算 PDF 签名位置？  
以 Adobe 阅读器为例：
1. 单击**准备表单**。
<img style="width:400px; max-width: inherit;" src="https://qcloudimg.tencent-cloud.cn/raw/7ea2975a0c3ecc619247a40aea69e562.png" />
2. 单击**添加文本域**。
<img style="width:800px; max-width: inherit;" src="https://qcloudimg.tencent-cloud.cn/raw/15a369537e611233f041055b565fcd27.png" />
>!此处仅做定位使用。
3. 单击**文本域属性** > **位置**，单位选点。
![](https://qcloudimg.tencent-cloud.cn/raw/32aaa5fbba148e5c1ffb3928c338bb34.png)
>!此时下方位置显示坐标值，注意此坐标值以页面左下角为原点。
4. 坐标计算  
ComponentPosX = 左对齐坐标39.4847 
ComponentPosY = 页面高度 - 上对齐坐标37.3135  
页面高度获取：可先将控件移至页面顶部，此时上对齐坐标值即为页面高度。
