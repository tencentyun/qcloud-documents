After accessing the Tencent LVB service, you need to enable the recording feature before enabling automatic stitching feature. The specific procedure is as follows:
1. Enable recording feature 
When enabling the recording feature, you need to configure the recording file type as HLS in order to use the automatic stitching feature. For more information on how to configure and enable recording feature (in LVB code mode only) via the console, please see [Cloud Recording](https://cloud.tencent.com/document/product/267/7963).
![](//mc.qcloudimg.com/static/img/f0ae825b082dac847640eb7b931eb927/image.png)
2. Configure the callback address
Configure the callback address on the console, and the LVB service backend automatically calls back the URL of recording file to your service backend.
>**Note:**
>Only for push in LVB mode can the callback address be configured on the console. For push in channel mode, you need to call the API to query the recording URL or [submit a ticket](https://console.cloud.tencent.com/workorder/category) for the Cloud LVB service backend to configure one. It is recommended to access using LVB code.

![](//mc.qcloudimg.com/static/img/b19be8058b7f29fe66eb160d6f01abb1/image.png)
3. Configure automatic stitching feature 
The automatic stitching feature and suspending time supported by automatic stitching can only be configured by the Cloud LVB service backend. To enable the automatic stitching feature, [submit a ticket](https://console.cloud.tencent.com/workorder/ Category) or contact Tencent service personnel. Tel: 4009-100-100.

  

