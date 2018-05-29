### Feature Overview

With account statistics feature, data statistics based on new accounts and active accounts can be implemented. Compared with statistics based on devices, it can help developers better count users' registrations and logins.

### Acquisition of Android Account Statistics Data

Submit your own account:

```java
void StatConfig.setCustomUserId(Context ctx, String customUserId)
```

### Acquisition of iOS Account Statistics Data

Submit your own account:

```obj-c
[MTA setAccount:@"other accounts" type:AT_OTH];
```
