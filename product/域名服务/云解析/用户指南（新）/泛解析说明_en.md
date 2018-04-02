Pan resolution means to use wildcard `*` to match all sub-domain name. For example, in the following second-level domain name resolution:

| Host Name | Record Type | Line Type | Record Value | TTL |
|---|---|---|---|---|
| www | A | Default | 200.202.101.2 | 600 |
| bbs | A | Default | 200.202.101.2 | 600 |
| blog | A | Default | 200.202.101.2 | 600 |
| css | A | Default | 200.202.101.2 | 600 |

Sub-domain names may be more, but they are all resolved to the same IP address (even the same line), in which case the resolution can be simplified like this:

| Host Name | Record Type | Line Type | Record Value | TTL |
|---|---|---|---|---|
| * | A | Default | 200.202.101.2 | 600 |

>**Note:**
>The resolution mentioned above is only for second-level domain names. A wildcard can only be used to match sub-domain name of one level. You need to use `*.example` to match third-level domain names. The number of pan resolution levels that can be configured is different for different service packages.

| DNS Package | Pan Resolution Level |
|---|---|
| Free Package | 2 |
| Individual Professional Package | 4 |
| Enterprise Basic Package | 6 |
| Enterprise Standard Package | 8 |
| Enterprise Ultimate Package | 10 |

