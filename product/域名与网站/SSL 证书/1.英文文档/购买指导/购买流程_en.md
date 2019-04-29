### 1. Select a Certificate Brand and Model

Now, Tencent Cloud provides three brands of SSL certificates for sale, as show below:
#### 1.1 Symantec
Symantec, the world's largest information security service producer and provider and the most authoritative digital certification authority, offers a wide range of content and network security solutions to businesses, individual users and service providers. 93% of the Global 500 choose VeriSign SSL digital certificates. Symantec acquired VeriSign in August 2010, and since then has provided the verification services of VeriSign. In April 2012, Symantec changed VeriSign's product name and brand logo.

#### 1.2 GeoTrust
GeoTrust, the world's second-largest digital certification authority (CA) and a leader in identity verification and trust certification, provides state-of-the-art technologies that enable organizations and companies of all sizes to deploy SSL digital certificates securely and cost-effectively and achieve a wide range of identity verification. GeoTrust was founded in 2001, and by 2006, it has accounted for 25% of the global market share. VeriSign acquired GeoTrust with USD 125 million in May 2006/September 2006, which is now also a cost-effective SSL certificate brand of Symantec.

From a technical point of view, the differences between Symantec (formerly VeriSign) and GeoTrust are as shown below:
1. Symantec (supporting RSA, DSA and ECC) is superior to Geotrust (supporting RSA and DSA) on algorithm;
2. Symantec is superior to Geotrust on compatibility; Symantec is compatible with all browsers on the market, and also shows the best compatibility for mobiles;
3. Symantec is superior to Geotrust on OCSP response;
4. Symantec is superior to Geotrust on CA security. As an internationally renowned security vendor, Symantec provides the number one CA security in the world;
5. In addition to encrypted transfer, Symantec certificates provide malware scanning and vulnerability assessment features;
6. A maximum of USD 1.75 million in certificate commercial insurance compensation is provided by Symantec, while the number of GeoTrust is USD 1.5 million.

#### 1.3 TrustAsia
TrustAsia, the brand of Yashu Information Technology (Shanghai) Co., Ltd in the field of information security, is a platinum partner of Symantec. TrustAsia specializes in providing businesses with all network security services including digital certificates. And TrustAsia SSL certificates are issued by the Symantec root certificates.

#### 1.4 Brand Differences
Certificates of different brands vary on browser address bar, encryption level, and guaranteed compensation. The most important difference lies in root certificates. For example, a Geotrust wildcard certificate is issued by Geotrust root certificate, while a Symantec wildcard certificate is issued by Symantec root certificate which is compatible with all browsers on the market and also supports mobiles best. TrustAsia wildcard certificate is also a root certificate of Symantec, but as a Domain Validation (DV) certificate, it does not contain company information, so its price is more favorable.

For more information, refer to parameters comparison provided on the official website.
![](https://mc.qcloudimg.com/static/img/50fea1790cd696773c7f049f441da9f4/1.png)

### 2. Select the Number of Supported Domains

#### 2.1 Single Domain Name
A single-domain name certificate can be bound to only one domain name, which can be a second-level domain name like example.domain.com, a third-level domain name like example.example.domain.com, or a first-level domain name like domain.com. **But all subdomains under the first-level domain name are not supported**. Up to 100 levels of domain name can be supported.


> Note: An SSL certificate bound to domain name `www.domain.com` (subdomain is www) supports first-level domain name domain.com.


#### 2.2 Multiple Domain names
A Multi-domain names certificate can be bound to multiple domain names (up to 100 domain names).
> The price of Symantec multi-domain certificates are calculated based on the number of domains.
> A GeoTrust multi-domain certificate supports five domain names by default and additional domain names are priced separately.

![](https://mc.qcloudimg.com/static/img/c0ce741398ffc55def1264e681879e82/2.png)

#### 2.3 Wildcard Domain Name
Only one wildcard domain name with only one wildcard can be bound, such as \*.domain.com, \*.example.domain.com (up to 100 levels). Multi-wildcard domain name like \*.\*.domain.com is not supported.

> Note: An SSL certificate bound to domain name \*.domain.com (must be a second-level wildcard domain name) support first-levels domain name domain.com.

![](https://mc.qcloudimg.com/static/img/0603883a1efcc18bec5bc6db5a097434/3.png)

### 3. Select Certificate Validity

The validity of OV certificates is up to 3 years, EV certificates up to 2 years, and DV certificates only 1 year.
The price is 15% off for 2-year certificates, and 25% off for 3-year certificates (see the prices published on the official website).

### 4. Payment

After selecting the brand, model, supported domain name, and certificate validity, you can submit the order and proceed with the payment process.


### 5. Submit Application

After purchasing a certificate, you need to submit approval materials in [SSL Certificate Management Console](https://console.cloud.tencent.com/ssl) for certificate application. The certificate will be issued upon approval by the CA. For more information, see [application process for paid certificates](https://cloud.tencent.com/document/product/400/10257)

