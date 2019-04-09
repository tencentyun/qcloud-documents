## 1. Domain Name Statuses in whois

   When viewing whois information of a domain name, there is a "Domain Name Status" bar which shows the current status of the domain name. A domain name can have one or multiple statuses. Knowing the meanings of different statuses can help you understand the causes for them in order to take appropriate measures in time.

There are several situations: Statuses that start with "client" are initiated by registrar, and those start with "server" are initiated by CNNIC (China Internet Network Information Center).

ACTIVE (OK): Normal status. No action is required and no protection measure is configured. The "OK" status is not displayed when there is another status (this does not indicate abnormality).

INACTIVE: Domain name is not active (domain name server was not configured upon registration and domain name cannot be resolved).

**For protecting domain name registration information, the statuses listed below will appear when domain name is under certain security lock:**

client Delete Prohibited: Deletion is prohibited according to registrar configuration

server Delete Prohibited: Deletion is prohibited according to registry configuration

client Update Prohibited: Modification is prohibited according to registrar configuration (modification of domain name information is not allowed, while you can still configure or modify resolution records)

server Update Prohibited: Modification is prohibited according to registry configuration (modification of domain name information is not allowed, while you can still configure or modify resolution records)

client Transfer Prohibited: Ownership transfer is prohibited according to registrar configuration (registrar has configured that domain name cannot be transferred away)

server Transfer Prohibited: Ownership transfer is prohibited according to registry configuration (the domain name that is newly registered or newly transferred will be set to this status within 60 days, and the status will be automatically removed after 60 days.  The registry can also configure this status for domain names involved in arbitrations or law cases, and the status will be removed once the arbitration or law case closes)


**Other statuses of the prohibition for resolution or renewal:**

client Renew Prohibited: Renewal is prohibited according to registrar configuration (domain name cannot be renewed. This usually means the domain name is under arbitration or court dispute, and the owner needs to contact the registrar to identify the reason)

server Renew Prohibited: Renewal is prohibited according to registry configuration (domain name cannot be renewed. This usually means the domain name is under arbitration or court dispute, and the owner needs to contact the registrar to identify the reason)

client Hold: Resolution is suspended according to registrar configuration. Contact registrar to remove the status

server Hold: Resolution is suspended according to registry configuration (in most cases, this is because the domain name (such as ".com", ".cn", ".net") does not have identity verification completed. The status is automatically removed once identity verification is done)

pending Transfer: Domain name is being transferred

pending Verification: Domain name is being verified (if identity verification is not completed after domain name registration, the owner should submit required information within 5 days after purchasing the domain name. If verification is not completed after 5 days, the domain name will go into Server Hold status)


## 2. Domain Name Expiration Statuses

A: Within 1-45 days after a domain name expires, it will be in REGISTRAR HOLD (held by registrar) status.

B: When REGISTRAR HOLD status ends, the domain name will go into a period of redemption of 30 days, when the status will show REDEMPTION PERIOD (grace period).

C: When REDEMPTION PERIOD ends, the domain name will go into a pending deletion period of 6 days, and domain name is deleted after 6 days. When this happens, the status will show PENDING Delete (being deleted), and domain name will become open for registration again after deletion.

D: REGISTRAR/REGISTRY LOCK means the domain name is locked by registrar/registry to prevent registrar transfer after domain name has expired.



[About Tencent Cloud Resolution](https://cloud.tencent.com/document/product/302)

[About Domain Name Identity Verification](https://cloud.tencent.com/document/product/242/6707)


Should you have any other questions, [Submit Ticket](https://console.cloud.tencent.com/workorder/category/create?level1_id=16&level2_id=17&level1_name=%E5%85%B6%E4%BB%96%E6%9C%8D%E5%8A%A1&level2_name=%E5%9F%9F%E5%90%8D) for assistance.






