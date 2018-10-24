## Information Disclosure
- The automatic testing of conventional information disclosure is mainly performed on some known types of threats, for example, path information contained in the returned page, anonymous browsing directory under a directory, and automatically backed-up file contained in a file.
- Manual intervention is required for analyzing some information disclosure vulnerabilities. For example, if the returned information contains data that is highly relevant to the target system business, the disclosure of these data can lead to serious consequence. Automatic scanning tools are unable to identify such disclosure, and manual intervention is needed to discover and verify the disclosure.

## Injection Vulnerabilities
- There are a variety of injection vulnerabilities, such as: SQL injection, XPath injection, and LDAP injection.
- Different types of injection vulnerabilities are similar in how they are exploited and how they work, but the data content and user permissions stored in the backend determine the benefit that an injection vulnerability can gain.
- When testers manually test for an injection vulnerability manually, in addition to verifying whether the injection vulnerability exists, they also need to analyze to what extent the injection vulnerability produces adverse effect, and set a reasonable risk level for the injection vulnerability based on the degree of adverse effect.

## Exploitation of XSS and CSRF Vulnerabilities
- Most Web scanners identify and test for XSS and CSRF using a single method. Generally, scanners can only verify such vulnerabilities theoretically. Therefore, the security risks caused by such vulnerabilities need to be identified and evaluated manually.

## Exploitation and Test of Redirect Vulnerability
- Redirect vulnerability is often used in conjunction with other vulnerabilities. In the traditional automatic evaluation process, it is difficult to identify and completely test redirect vulnerability. The way that a redirect vulnerability is exploited and its impact can be re-evaluated and redefined through manual testing. 

## Parameter Errors
- There are many types of parameter errors. The errors that involve logic and permissions are difficult to be identified automatically with scanners. Penetration engineers are often needed for identifying and testing such errors with their extensive testing experiences. 

## Authentication Errors
- Authentication error is a multi-dimensional concept. To put it simply, it means that a user's login portal (especially the sensitive user's login portal, for example, the admin login portal) is exposed and has a risk of weak password or brute force (for example, authentication can be passed through brute force in a login page without verification code). In addition, there are some authentication errors that cannot be recognized by automation programs. For example, after a user logs in to a system, no authentication is performed on the user and the user can perform any operation in the system, or when the user changes the password, no verification is done for the original password. These vulnerabilities may lead to the unauthorized operations of ordinary users.

