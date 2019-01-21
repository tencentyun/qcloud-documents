IPv6-only network environment is supported by Tencent Cloud DNSPod. This has been tested and proved both inside and outside China.

## Background
Starting from June 1st, 2016, Apple required that all iOS applications submitted to App Store must support IPv6-only environment. As commonly known, IPv4 addresses are almost exhausted, and IPv6 is more efficient than IPv4, thus the transition towards IPv6 is the general trend of the Internet. However, during the process of compatibility adaption for IPv6, many developers passed their application test in their local environment but are not approved by App Store. When this happens, you should first check if the problem is caused by DNS resolution failure. So how to verify whether the DNS server responds to the resolution request from IPv6 address correctly? After establishing DNS64 environment, query with the following commands:
```
$ dig dnspod.cn aaaa
```

This is why we should verify DNS resolution: the first step for an app to access the Internet is to perform DNS resolution. When App Store verifies the app, it first accesses the DNS server, acquires the IPv6 address of iOS application server, then accesses it. If the DNS server cannot resolve domain to the IPv6 address in this step, App Store will disapprove the app even if the app passed the test in the locally established IPv6-only environment. So, choosing a domain name resolution service with both stability and compatibility is very important.

After thorough test and gated launch, Tencent Cloud DNSPod now fully supports App Store IPv6-only network environment. We already have successful cases where apps are approved by App Store, and the resolution both inside and outside China is proved to be functional.

## About How iOS Applications Support IPv6-only Environment

### All domain names in applications are connected into DNSPod
Both Tencent Cloud underlying service DNS resolution and DNSPod domain name resolution support IPv6-only to ensure that services are successfully resolved in IPv6-only environment. iOS application servers do not have to support IPv6. In IPv6-only environment, DNS64/NAT64 can translate IPv4 addresses into IPv6 addresses.

### Client modification
For example, using IP for direct access, or upgrading SDK APIs to be compatible with IPv6.

###Establishing the environment for verification
Please see [documentation on Apple official website](https://developer.apple.com/library/ios/documentation/NetworkingInternetWeb/Conceptual/NetworkingOverview/UnderstandingandPreparingfortheIPv6Transition/UnderstandingandPreparingfortheIPv6Transition.html#//apple_ref/doc/uid/TP40010220-CH213-SW1) to establish IPv6-only hotspot and test it by connecting to it with iPhone.

### Other suggestions
If it passed the test in self-built DNS64 environment but still cannot be accessed after being submitted to App Store for approval, excluding DNS support problem and accessing server port problem, there's another important reason: network quality when accessing the Internet across different countries.
DNS usually achieve GEO resolution for different regions by using IP address libraries. There is no library for IPv6, and all IPv6 addresses are resolved to default line addresses. If the default line is set as China Telecom or BGP (CAP, which goes through China Telecom by default) IP, it's very likely that you cannot access your target destination due to China Telecom's international connection quality, thus resulting in disapproval. Therefore, you are suggested to:
1. Change the default IP for the domain name of feature that is crucial for approval to China Unicom or China Mobile IP.
2. Connect the feature that is crucial for approval to DSA service in order to accelerate the international access.

