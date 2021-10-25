IP 地理函数可用于判断 IP 地址属于内网还是外网，也可用于分析 IP 地址所属的国家、省份、城市。本文介绍 IP 地理函数的基本语法及示例。



## IP 地址函数

>?
> - 如下函数中的 KEY 参数表示日志字段（例如 ip），其值为 IP 地址；若其值为内部 IP 地址或非法字段将无法被解析，以 “NULL”或“未知”展示。
> - IP 目前仅支持 IPv4 地址，IPv6 暂不支持。
> - 基于 IP 地址分配机制的限制，IP 地址库无法100%准确涵盖所有 IP 地址的地理信息，极少部分 IP 地址可能会查询不到详细地理信息或地理信息存在错误。
> 

| 函数名称                 | 说明                                                         | 示例                                 |
| ------------------------ | ------------------------------------------------------------ | ------------------------------------ |
| ip_to_domain(KEY)        | 判断目标 IP 地址是内网地址还是外网地址。内网则返回 intranet，外网则返回 internet，非法 IP 地址则返回 invalid。 | `* | SELECT ip_to_domain(ip)`        |
| ip_to_country(KEY)       | 分析目标 IP 地址所属国家或地区。返回结果为国家或地区的中文名称。 | `* | SELECT ip_to_country(ip)`       |
| ip_to_country_code(KEY)  | 分析目标 IP 地址所属国家或地区的代码。返回结果为国家或地区的代码。 | `* | SELECT ip_to_country_code(ip)`  |
| ip_to_country_geo(KEY)   | 分析目标 IP 地址所属国家或地区的经纬度。返回结果为国家或地区的经纬度。 | `* | SELECT ip_to_country_geo(ip`)   |
| ip_to_province(KEY)      | 分析目标 IP 地址所属省份。返回结果为省份的中文名称。         | `* | SELECT ip_to_province(ip)`      |
| ip_to_province_code(KEY) | 分析目标 IP 地址所属省份的代码。返回结果为省份的行政区划代码。 | `* | SELECT ip_to_province_code(ip)` |
| ip_to_province_geo(KEY)  | 分析目标 IP 地址所属省份的经纬度。返回结果为省份的经纬度。   | `* | SELECT ip_to_province_geo(ip)`  |
| ip_to_city               | 分析目标 IP 地址所属城市。返回结果为城市的中文名称，国外城市为英文名。 | `* | SELECT ip_to_city(ip)`          |
| ip_to_city_code          | 分析目标 IP 地址所属城市的代码。返回结果为城市的行政区规划代码，暂不支持台湾省城市。 | `* | SELECT ip_to_city_code(ip)`     |
| ip_to_city_geo           | 分析目标 IP 地址所属城市的经纬度。返回结果为城市的经纬度，不支持国外城市。 | `* | SELECT ip_to_city_geo(ip)`      |
| ip_to_provider(KEY)      | 分析目标 IP 地址对应的网络运营商，返回结果为网络运营商名称。 | `* | SELECT ip_to_provider(ip)`      |

## IP 网段函数

>?
> - 如下函数中的 KEY 参数表示日志字段（例如 ip），其值为 IP 地址。
> - 其中 ip_subnet_min、ip_subnet_max、ip_subnet_range 函数中的字段值为子网掩码格式的 IP 地址（例如：192.168.1.0/24），如果字段值为通用的 IP 地址，则需要使用 cancat 函数将其转换为子网掩码格式。
> 

| 函数名                     | 说明                                                         | 示例                                         |
| -------------------------- | ------------------------------------------------------------ | -------------------------------------------- |
| ip_prefix(KEY,prefix_bits) | 获取目标 IP 地址的前缀。返回结果为子网掩码格式 IP 地址。例如192.168.1.0/24。 | `* | SELECT ip_prefix(ip,24)`                 |
| ip_subnet_min(KEY)         | 获取 IP 网段中的最小 IP 地址。返回结果为 IP 地址，例如192.168.1.0。 | `* | SELECT ip_subnet_min(concat(ip,'/24'))`  |
| ip_subnet_max(KEY)         | 获取 IP 网段中的最大 IP 地址。返回结果为 IP 地址，例如192.168.1.255。 | `* | SELECT ip_subnet_max(concat(ip,'/24'))`   |
| ip_subnet_range(KEY)       | 获取 IP 网段范围。返回结果为 Array 类型的 IP 地址，例如[[192.168.1.0, 192.168.1.255]]。 | `* | SELECT ip_subnet_range(concat(ip,'/24'))` |
|  is_subnet_of     | 判断目标 IP 地址是否在某网段内。返回结果为布尔值。 | `* | SELECT is_subnet_of('192.168.0.1/24', ip)` |
|  is_prefix_subnet_of      | 判断目标网段是否为某网段的子网。返回结果为布尔值。 | `* | SELECT is_prefix_subnet_of('192.168.0.1/24',concat(ip, '/24'))` |



## 示例

此处列举了 IP 地理函数在不同场景下的查询和分析示例。您在执行查询和分析操作后，还可以选择合适的统计图表展示查询和分析结果。

>? 如下示例中的 ip 为日志字段。
>

- 统计不是来自内网的请求总数。
```
* | SELECT count(*) AS PV where ip_to_domain(ip)!='intranet'
```
![image-20210718035932972](https://main.qcloudimg.com/raw/75f4d144392b9fe1bb15c24923667ad6.png)
- 统计请求总数 Top10的省份。
```
* | SELECT ip_to_province(ip) AS province, count(*) as PV GROUP BY province ORDER BY PV desc LIMIT 10
```
![image-20210718035905064](https://main.qcloudimg.com/raw/6a421629bcd8ca24e2e9923dc6396011.png)
![](https://main.qcloudimg.com/raw/1b4b4e09667cc6798105d183efbea2db.png)
如果上述结果中包含了内网请求，且您希望过滤这部分请求，可参考如下查询和分析语句。
```
* | SELECT ip_to_province(ip) AS province, count(*) as PV where ip_to_domain(ip)!='intranet' GROUP BY province ORDER BY PV desc LIMIT 10
```
- 统计 IP 地址的经纬度，确认客户端分布情况。
```
* | SELECT ip_to_geo(ip) AS geo, count(*) AS pv GROUP BY geo ORDER BY pv DESC
```
![image-20210718041532549](https://main.qcloudimg.com/raw/fd3381a7459d2fdfce3e425e38b8ef49.png)













