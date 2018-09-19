### Description
Channel Analytics can analyze the source of scenarios and entry paths to enter Mini Programs, and perform parameter drill-down. With Channel Analytics, you can understand the effects of promotion and optimization of each channel scenario and differentiation of entrance interfaces. Parameter drill-down can be used to analyze the effect of the same source in different locations. More analysis effects can be obtained based on users' own Mini Programs.
![](//mc.qcloudimg.com/static/img/aadf83407d11c2aca48452e54044bdbe/image.jpg)
## Instructions 
1. Pass options in the onLaunch method, and then pass the options parameter to the lauchOpts parameter to report the channel-related information:

```java
onLaunch: function(options){
  
mta.App.init({
       
 "appID":"********",
       
  "lauchOpts":options,
   
 });
 
}
```
2. Add the _mta_ref_id parameter to the path to calculate the value of this parameter for channel parameter drill-down analysis. For example: `pages/detail/detail?id=5363928&_mta_ref_id=channel_id`
>**Note:**
>Channel parameter drill-down analysis is optional. "_mta_ref_id" is an English character, and the statistical effect will be affected if it is a special character. The scenario value is officially defined by WeChat Mini Program.

If you have any questions or suggestions, please contact dtsupport@tencent.com.
