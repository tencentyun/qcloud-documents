Since November 2016, we have received feedbacks from some Google Chrome users on the prompt "Your connection is not private key connection" (error **NET::ERR_CERTIFICATE_TRANSPARENCY_REQUIRED**) when accessing HTTPS websites.

See the details below:
![](https://mc.qcloudimg.com/static/img/0fdf027303e53946698dcb377431597e/0.png)

This CT error is confirmed to be a kernel bug with Chrome versions 53 and 54, which causes the incompatibility with SSL certificates issued by Symantec CA. CT error occurs in all certificates issued by Symantec CA after June 1, 2016. Chrome handled this problem with automatic patch in the first place, and fixed this problem in version 55.

Users who can connect to Chrome's server will not be affected by this issue. But most users in China cannot access Chrome's server. It is recommended to upgrade to version 55 or above to solve this problem.

![](https://mc.qcloudimg.com/static/img/25a818d9e80a02c2b8b7c90f0e1c93df/1.png)


Details can be found in [Symantec's official announcement](https://knowledge.symantec.com/support/ssl-certificates-support/index?page=content&id=ALERT2160).

[Symantec's official statement](https://www.symantec.com/connect/blogs/chrome-53-bug-affecting-symantec-ssltls-certificates).

[Chrome's official announcement](https://bugs.chromium.org/p/chromium/issues/detail?id=664177).


In addition, this problem exists in QQ browsers using Chromium 53 kernel, but has been fixed in new versions. The users using out-of-date QQ browser versions are also recommended to upgrade to the latest version.
Details can be found in [QQ Browser's official announcement](http://bbs.browser.qq.com/thread-222732-1-1.html). 


