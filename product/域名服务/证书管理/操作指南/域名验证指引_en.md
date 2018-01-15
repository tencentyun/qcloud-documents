When applying for a DV certificate, you can verify its ownership via the following methods:

### 1 Manual DNS Verification
Verify the domain ownership by resolving the specified DNS record. The resolution format can be specified as `host name -> TXT record -> record value`.

For example, to add a DNS record of TXT type for domain name www.domain.com that is applying for a certificate, you can put it as `www.domain.com -> TXT -> 201704262209564gw0...hj37i4xai8m7uii2a23l`:

![](https://mc.qcloudimg.com/static/img/817e158a70e3ae78741f07bec6798b38/1.png)

Operation method on Tencent Cloud DNS Console:

#### 1.1 Add domain name

Click **Add Domain Name**, enter the primary domain name `domain.com` to be resolved, and click **OK**

![](https://mc.qcloudimg.com/static/img/3c906608a8759c24cf9bd0391c74c896/1.png)

#### 1.2 Add resolution record

Click **Resolution** for the added domain name

![](https://mc.qcloudimg.com/static/img/db4edbdb57ddaee7f028e04d133c8258/3.png)

Click **Add Record**

![](https://mc.qcloudimg.com/static/img/cc84a183208a3af200f167beb40e51de/4.png)

#### 1.3 Complete adding the specified TXT record

TXT record is a way used to identify and explain the domain name:

- Select TXT as the record type
- Fill in subdomain as the host name. For example, to add resolution for `www.domain.com`, you only need to fill in `@` as the host name instead of primary domain `domain.com`
- Select **Default** as the line type
- The record value refers to the text provided by the system, and here is `201704262209564gw0...hj37i4xai8m7uii2a23l`. Note: **the complete record value must be filled in**
- Select 10 minutes (default) for TTL

![](https://mc.qcloudimg.com/static/img/f64d0c0a2e6cf265b51f6846acc7ecf5/5.png)

The added resolution is shown as follows:

![](https://mc.qcloudimg.com/static/img/063467572f5b5493db8492a8fd0ed4d1/6.png)

The system regularly checks the TXT record value of www.domain.com. If it is detected and matches with the specified value, the domain name ownership verification is completed.

### 2. Automatic DNS Verification
> Note: Only applicable to domain names that are resolved using Tencent Cloud DNS

If a domain name applying for a certificate has been resolved on the Cloud DNS platform, you can choose automatic verification.
The system automatically adds the specified DNS record for the domain name. If the record is detected and matches with the specified value, the domain name ownership verification is completed, and then the record is automatically cleared.

### 3. File Verification

#### 3.1 Create a file in the specified directory
Create a file according to the specified file directory, name, and content. For example

| File Directory | File Name | File Content |
|---------|---------|---------|
| /.well-known/pki-validation | fileauth.txt | 201608241742072yvt8bxp9jv0ycginrnnebwgy1nvwgvxtssucy39w7b20nelfa |

If the domain name applying for file verification is `example.www.domain.com`, access the URL `http://example.www.domain.com/.well-known/pki-validation/fileauth.txt` or `https://example.www.domain.com/.well-known/pki-validation/fileauth.txt` for verification.

If the domain name applying for file verification is pan domain `*.domain.com`, access the URL `http://domain.com/.well-known/pki-validation/fileauth.txt` or `https://domain.com/.well-known/pki-validation/fileauth.txt` for verification

You can obtain `201608241742072yvt8bxp9jv0ycginrnnebwgy1nvwgvxtssucy39w7b20nelfa` by accessing the URL.

> It allows http access or https access;
> File verification does not support any redirection, and directly responses to status code 200 and file content.

#### 3.2 Wait for approval
After creating the file, wait for the CA to scan and approve. After the certificate is issued, the file and directory can be cleared.

#### 3.3 The /.well-known directory cannot be created in Windows system
In Windows, you cannot create files and folders beginning with a dot (.), such as `.log` by `right-clicking -> New`, and you will be prompted to enter a file name when doing so.
You can create files and folders through a command line:

New Folder
```
mkdir .well-known
```

