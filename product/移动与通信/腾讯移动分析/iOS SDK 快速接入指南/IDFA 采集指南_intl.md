### Integration Procedure
Step 1: [Download Standard SDK](http://mta.qq.com/mta/ctr_index/download).
Step 2: Decompress the downloaded SDK package, and then link libidfa.a and AdSupport.framework to the project, as shown below:
![](//mc.qcloudimg.com/static/img/b8a7a99fa2186b796a2dce35f3c3cf4b/image.png)
### Notes

MTA SDK can collect IDFA (identifier for advertising) information of iOS users. IDFA is a more versatile and accurate method to mark users. It is widely used in cross-App data cross-analysis scenarios such as accurate advertising performance statistics, App traffic exchange, and data exchange cooperation.
Theoretically, IDFA can be used only after an advertising SDK is integrated. If you want to collect IDFA without using any ads, do the followings to get approved by Appstore: 
![](//mc.qcloudimg.com/static/img/a54bb121e7b4e66ca8aaf1c48f260f6e/image.png)
1. Check the "serve advertisements within the app" option for the in-App advertising service as needed, which is suitable for scenarios where ads are integrated within the App.
2. Check the "Attribute this app installation to a previously served advertisement" option for tracking and counting the number of installations brought by ads.
3. Check the "Attribute an action taken within this app to a previously served advertisement" option for tracking and counting user behaviors after installation via ads.
4. Check the confirmation option of "Limit Ad Tracking setting in iOS".

If you still failed to be approved by Appstore due to IDFA collection, you are advised to integrate an ad or use the MTA Basic Edition. If you also need to collect the h5 page data in the App, follow [hybird App ios Instructions](https://cloud.tencent.com/document/product/549/12900) for integration.
