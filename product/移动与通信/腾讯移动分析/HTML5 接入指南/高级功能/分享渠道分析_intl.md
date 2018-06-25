### Description
Calculate the proportion of H5 light App page shared to WeChat Moments, WeChat Friends, Mobile QQ, Microblog and other platforms. You can also implement second-level drill-down.
### Application Scenarios
- Calculate the proportion of destinations of data sharing.
- Implement second-level drill-down after calculating the sharing proportion.
- Calculate the proportion of return visits after the page is shared to various platforms, and analyze the quality of each platform (conversion rate of sharing channel).

### Tips on Usage

Execute the sharing code in the "success" method returned by the js sdk call method of WeChat, Sina, QQ. If the page is shared for the first time and the second-level drill-down is required, the parameter CKTAG=mtah5_share needs to be added in the sharing link. Here is an example of a first-level sharing channel ID:

```
wx.onMenuShareTimeline({
    title: '', // Sharing title
    link: '', // Sharing link. CKTAG=mta_share.wechat_moments needs to be added in the URL if second-level drill-down is required.
    imgUrl: '', // Sharing icon
    success: function () { 
        // The callback function to be executed after user confirms sharing
        MtaH5.clickShare('wechat_moments');  // Add h5 sharing code here
    },
    cancel: function () { 
        // The callback function to be executed after user cancels sharing
    }
});
```
### Notes
1. Second-level drill-down cannot be implemented if the adtag parameter has been added.
2. "mta js sdk" must be embedded in the page.
3. If the custom event tracking is not enabled when adding code, you need to enable it on the console, and then update the new mta h5 and report js.
