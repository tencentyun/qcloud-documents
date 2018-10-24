## Product Content
### Does the HTTP request threshold in the CC defense switch refer to the QPS for a single IP or QPS for the entire website?
The HTTP request threshold refers to the QPS for the entire website.
### What should the HTTP request threshold be set to?
We recommend that you set the HTTP request threshold (QPS) as 1.2 times of the business traffic volume.
## Product Implementation
### What will the system do after the CC defense is triggered?
After CC defense is triggered, the system cleans CC attacks.
### Why doesn't the added custom policy/whitelist/blacklist take effect?
They take effect only if the CC defense is enabled and the CC defense threshold is reached.
### How long will it take for CC defense to take effect?
The CC defense takes effect in real time as you enable it or modify its configuration.

