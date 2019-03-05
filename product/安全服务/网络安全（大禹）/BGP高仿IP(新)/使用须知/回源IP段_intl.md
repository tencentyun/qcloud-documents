## What is Origin-pull IP?
Origin-pull IP refers to the IP used by the high defense IP cluster to forward business traffic to your origin server.

## Why should the origin-pull IP range be opened?
After you activate the High Defense IP service, all your business traffic first flows through the high defense IP cluster, and the cluster forwards the cleaned traffic to your origin server. To avoid business traffic loss caused by blocking or speed limiting of high defense origin-pull IP, you need to add the high defense origin-pull IP ranges to the whitelist of your origin server firewall or other server security defense software.

## What are the origin-pull IP ranges?
The origin-pull IP ranges of High Defense IP are:
`119.29.255.0/24`
`123.207.76.0/24`
`123.207.177.0/24`
`123.207.212.0/24`
`139.199.114.0/24`
`139.199.120.0/24`
`111.231.80.0/24`

