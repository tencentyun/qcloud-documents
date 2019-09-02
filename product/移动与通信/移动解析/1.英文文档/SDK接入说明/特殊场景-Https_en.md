This document describes HTTPS scenarios of HttpDNS

### Code for iOS

#### Principle
To verify a certificate, replace IP with the original domain name, and then proceed with the verification.

#### Demo
Take the API NSURLConnection as an example

```
#pragma mark - NSURLConnectionDelegate

- (BOOL)evaluateServerTrust:(SecTrustRef)serverTrust
                  forDomain:(NSString *)domain
{
    /*
     * Create a certificate verification policy
     */
    NSMutableArray *policies = [NSMutableArray array];
    if (domain) {
        [policies addObject:(__bridge_transfer id)SecPolicyCreateSSL(true, (__bridge CFStringRef)domain)];
    } else {
        [policies addObject:(__bridge_transfer id)SecPolicyCreateBasicX509()];
    }

    /*
     * Bind the verification policy to the certificate at the server end
     */
    SecTrustSetPolicies(serverTrust, (__bridge CFArrayRef)policies);

    /*
     * Evaluate whether the current serverTrust is trustable
     * It is officially recommended that if result = kSecTrustResultUnspecified/kSecTrustResultProceed, 
     * the verification of serverTrust can be successful, https://developer.apple.com/library/ios/technotes/tn2232/_index.html
     * For more information about SecTrustResultType, please see SecTrust.h
     */
    SecTrustResultType result;
    SecTrustEvaluate(serverTrust, &result);

    return (result == kSecTrustResultUnspecified || result == kSecTrustResultProceed);
}

- (void)connection:(NSURLConnection *)connection willSendRequestForAuthenticationChallenge:(NSURLAuthenticationChallenge *)challenge
{
    if (!challenge) {
        return;
    }

    /*
     * If HTTPDNS is used, the host in URL is set to IP, and you can acquire the actual domain name from HTTP header.
     */
    NSString* host = [[self.request allHTTPHeaderFields] objectForKey:@"Host"];
    if (!host) {
        host = self.request.URL.host;
    }

    /*
     * Determine whether the authentication method of challenge is NSURLAuthenticationMethodServerTrust (this authentication process is initiated in HTTPS mode)
     * Perform the default network request process if the authentication method is not configured.
     */
    if ([challenge.protectionSpace.authenticationMethod isEqualToString:NSURLAuthenticationMethodServerTrust])
    {
        if ([self evaluateServerTrust:challenge.protectionSpace.serverTrust forDomain:host]) {
            /*
             * After verification, you need to construct a NSURLCredential and send it to the initiator
             */
            NSURLCredential *credential = [NSURLCredential credentialForTrust:challenge.protectionSpace.serverTrust];
            [[challenge sender] useCredential:credential forAuthenticationChallenge:challenge];
        } else {
            /*
             * Verification failed. Cancel this verification process
             */
            [[challenge sender] cancelAuthenticationChallenge:challenge];
        }
    } else {
        /*
         * For other verification methods, directly proceed with the verification
         */
        [[challenge sender] continueWithoutCredentialForAuthenticationChallenge:challenge];
    }
}
```

