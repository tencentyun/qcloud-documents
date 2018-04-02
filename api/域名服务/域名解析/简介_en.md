Welcome to Tencent Cloud DNS!
Our Cloud DNS service is designed to provide free, smart resolution service to domain names across the entire Internet. The platform possesses massive processing capacity, flexible scalability and tight security, providing stable, safe and fast resolution service for your website. You can call the APIs discussed in this document to work with domain name resolution. Be sure to have a thorough understanding of domain name resolution products and how to use them before using these APIs.

In case of any conflict between the value or optional range of any parameter provided in "API Description" of this document and that provided on the Tencent Cloud official website, **the latter shall prevail**.

## 1. Glossary

| Term | Full Name | Description |
|---------|---------|---------|
| domain | Domain | Network name corresponding to IP address. For example, cloud.tencent.com. Its primary domain name qcloud.com is often used in API document. |
| subDomain | Sub Domain | The section apart from the primary domain name in a domain name. For example, www  |
| record | Record | Resolution record. Common records are host records (A records), canonical name records (CName records) and so on.  |


## 2. API Quick Start
You need to perform the following basic steps before using Cloud DNS:

1. Add domain name to be resolved
You can use API [DomainCreate](https://cloud.tencent.com/document/product/302/8504) to add your domain name to Tencent Cloud DNS platform.
2. Add resolution record
Once the domain name is added, you need to use API [RecordCreate](https://cloud.tencent.com/document/product/302/8516) to add a resolution record for your domain name. You can specify host name, record type, TTL, line type and record value.

## 3. Service Limits
Currently, all users can use the free version of Cloud DNS service in any situation.

