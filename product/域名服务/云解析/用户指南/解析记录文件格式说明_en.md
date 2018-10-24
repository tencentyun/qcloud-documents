You can export resolution records in three file formats: text, chart and Zone file. Take "domain.com" as example, the result of export is as follows:

### 1. Text
Export `domain.com.txt` file, which contains:

```
Host | Type | Line | Record Value | MX Priority | TTL | Remark
@	NS	Default	f1g1ns1.dnspod.net.	0	86400
@	NS	Default	f1g1ns2.dnspod.net.	0	86400
www	A	Default	8.8.8.8	0	600
```

### 2. Chart
Export `domain.com.xls` file, which contains:

![excel](https://mc.qcloudimg.com/static/img/ad997ebafb5b6f6c0a42bdcd83e229e5/123.png)

### 3. Zone File
Zone files are domain name configuration files saved on DNS servers, which are formulated according to RFC standard documents.
Export `domain.com.zip` file, and decompress the file to acquire `domain.com.default_line.zone`. Open the zone file with text editor and see the following content:

```
; Domain: domain.com
; Exported at:2016-08-10 19:43:58 (Asia/Shanghai)
;
;      _/_/_/    _/      _/    _/_/_/  _/_/_/      _/_/    _/_/_/
;     _/    _/  _/_/    _/  _/        _/    _/  _/    _/  _/    _/
;    _/    _/  _/  _/  _/    _/_/    _/_/_/    _/    _/  _/    _/
;   _/    _/  _/    _/_/        _/  _/        _/    _/  _/    _/
;  _/_/_/    _/      _/  _/_/_/    _/          _/_/    _/_/_/
;
; This file is intended for use for informational and archival
; purposes ONLY and MUST be edited before used on a production
; DNS server.
;
; For further information, please consult the BIND documentation
; located on the following website:
;     http://www.isc.org/
;
; And RFC 1035:
;    http://www.ietf.org/rfc/rfc1035.txt
;
; If you are trying to import to your domain in DNSPod, you may
; want to visit here:
;    https://www.dnspod.cn/Batch
;
; If you need help, see the support:
;    https://support.dnspod.cn/Kb/showarticle/tsid/229/#link4
;
; Use at your own risk.
;


$ORIGIN domain.com.


; SOA record
DOMAIN.COM. 600 SOA f1g1ns1.dnspod.net. freednsadmin.dnspod.com. 1470829344 3600 180 1209600 180


; A records
www	600	IN	A	8.8.8.8


; NS records
@	86400	IN	NS	f1g1ns1.dnspod.net.
@	86400	IN	NS	f1g1ns2.dnspod.net.

```
Contents marked with `;` are annotations.

Records will be exported according to their lines if line grouping is implemented for resolution. For example:
`domain.com.default_line.zone`<br />
`domain.com.sogou.zone`

