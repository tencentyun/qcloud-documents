TTL (Time to Live) refers to the duration for which the DNS servers in various regions cache the resolution record.

Suppose TTL is set as 10 minutes. When the DNS servers in various regions receive the resolution request of a domain name, they send requests to the authoritative server asking for resolution record and saves the record in local servers for 10 minutes. For resolution requests within 10 minutes, the records are read from the local cache, and record value is only obtained again when the cache expires. It is recommended to configure the TTL as 10 minutes in normal situations. The minimum TTL is different for different DNS service packages.

| DNS Package | Minimum TTL |
|---|---|
| Free Package | 600s |
| Individual Professional Package | 120s |
| Enterprise Basic Package | 60s |
| Enterprise Standard Package | 1s |
| Enterprise Ultimate Package | 1s |

