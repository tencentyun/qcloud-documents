Certificates sold on Tencent Cloud official website are compatible with the mainstream browser versions. Here is the detailed compatibility test report:

| Browser | Symantec EV Type	| GeoTrust EV Type	| Symantec OV Type	| GeoTrust OV Type	| TrustAsia G5 DV Type	| GeoTrust DV Type	|
|---|---|---|---|---|---|---|
| IE6 (SHA2 patched)	| Supported	| Supported	| Supported	| Supported	| Supported	| Supported |
| IE (8+) 	| Supported	| Supported	| Supported	| Supported	| Supported	| Supported |
| QQ browser (9.5.1/9.5.2)	| CT error	| CT error	| CT error	| CT error	| CT error	| CT error |
| QQ browser (7+)	| Supported	| Supported	| Supported	| Supported	| Supported	| Supported |
| Baidu browser (6+)	| Supported	| Supported	| Supported	| Supported	| Supported	| Supported |
| Maxthon browser (4.4+)	| Supported	| Supported	| Supported	| Supported	| Supported	| Supported |
| 360 browser (8.1)	| Supported	| Supported	| Supported	| Supported	| Supported	| Supported |
| 360 browser (6+)	| Supported	| Supported	| Supported	| Supported	| Supported	| Supported |
| UC browser (5+)	| Supported	| Supported	| Supported	| Supported	| Supported	| Supported |
| Sogou browser (6+)	| Supported	| Supported	| Supported	| Supported	| Supported	| Supported |
| CM browser (3+)	| Supported	| Supported	| Supported	| Supported	| Supported	| Supported |
| 2345 browser (7.1+)	| Supported	| Supported	| Supported	| Supported	| Supported	| Supported |
| ChromePlus browser (2+)	| Supported	| Supported	| Supported	| Supported	| Supported	| Supported |
| TheWorld browser (3.6+)	| Supported	| Supported	| Supported	| Supported	| Supported	| Supported |
| Opera browser (34+)	| Supported	| Supported	| Supported	| Supported	| Supported	| Supported |
| Safari browser (5+)	| Supported	| Supported	| Supported	| Supported	| Supported	| Supported |
| Edge browser	| Supported	| Supported	| Supported	| Supported	| Supported	| Supported |
| Firefox browser (25+)	| Supported	| Supported	| Supported	| Supported	| Supported	| Supported |
| Chrome browser (53/54)	| CT error	| CT error	| CT error	| CT error	| CT error	| CT error |
| Chrome browser (46+)	| Supported	| Supported	| Supported	| Supported	| Supported	| Supported |

Note:
Certificate Transparency (CT) is a policy of Google Chrome that monitors and verifies HTTPS certificates. Due to a kernel bug of Chrome 53/54, CT error occurs in all certificates issued by Symantec CA after June 1, 2016. Chrome handles this problem with automatic patch at the first place, and fixed this problem in version 55. Users who can connect to Chrome's server will not be affected by this issue. But most users in China cannot access Chrome's server, therefore, it is recommended to upgrade to version 55+ to solve this problem. And QQ browser using kernel of Chromium 53/54 version is also affected.
Click [here](https://cloud.tencent.com/document/product/400/8562) to check specific issues and announcements.

