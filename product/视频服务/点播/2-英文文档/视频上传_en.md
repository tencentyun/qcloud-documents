**What formats of videos can be uploaded and published  in Tencent Video Cloud currently?**

Videos in the following formats can be uploaded currently:
Microsoft formats: WMV, WM, ASF, ASX;
REAL formats: RM, RMVB, RA, RAM;
MPEG formats: MPG, MPEG, MPE, VOB, DAT;
Other formats: MOV, 3GP, MP4, MP4V, M4V, MKV, AVI, FLV, F4V
Videos in MP4 and HLS can be published currently.



 **How do I upload a file? Can I resume uploading from a breakpoint?**

You can upload a file by the following methods:
1. Upload from PCs or servers: You can use APIs or the console to 1) upload a local file or 2) pull a file from URL origin server.
2. Upload from mobile devices: You can upload a file from mobile devices to Tencent Cloud. Please refer to [JS Example](http://video.qcloud.com/sdk/upload.html).

Upload on the console:

Currently, breakpoint resume is supported for uploading through Web. (You can continue uploading the same local file in the same location within two days after a page is closed or the load is suspended.) To ensure the compatibility, [Chrome browser](http://xiazai.sogou.com/detail/34/8/6262355089742005676.html?e=1970) is recommended for uploading.

Upload through APIs:

For local file uploading, please refer to the description of API [MultipartUploadVodFile](http://cloud.tencent.com/doc/api/257/%E8%A7%86%E9%A2%91%E4%B8%8A%E4%BC%A0)
and [related Python/Java/PHP/JS examples](http://cloud.tencent.com/doc/api/257/%E8%A7%86%E9%A2%91%E4%B8%8A%E4%BC%A0#5.其他代码示例) 
For URL pulling, please refer to the description of API [MultiPullVodFile](http://cloud.tencent.com/doc/api/257/URL%E6%8B%89%E5%8F%96%E8%A7%86%E9%A2%91%E4%B8%8A%E4%BC%A0)

**How do I upload a massive number of videos?**

We use an upload queue to ensure that videos can be uploaded in sequence. If you have any further demands, for example, uploading a video with an ultra-large size up to several TBs or even a few PBs, please contact our sales department.

 **How long will it take for a user to watch the video after uploading?**

The lead time for the uploaded video varies depending on the video duration and transcoding rate.

**Can customers who use our APP or visit our web page upload videos directly?**

Currently, videos cannot be uploaded through APP and SDK or by enabling web APIs. Therefore, end users (not Tencent Cloud video service users) cannot upload videos directly.
