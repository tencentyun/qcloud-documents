


### DescribeDBPrice 	查询数据库价格

```python
#!/usr/bin/python
# -*- coding: utf-8 -*-

# 引入云API入口模块
from tencentcloud.common import credential
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.cdb.v20170320 import cdb_client, models

try:
    # 实例化一个认证对象，入参需要传入腾讯云账户secretId，secretKey
    cred = credential.Credential("AKIDrY4UwCdhewLbhdG7f2DmDT4eFftKtWIz", "eGl4KUSEsmaFiyEKFID0bzFKNFvPh2EE")

    #实例化要请求产品(以cdb为例)的client对象
    client = cdb_client.CdbClient(cred, "ap-guangzhou")

    #实例化一个请求对象:req = models.ModifyInstanceParamRequest()
    req = models.DescribeDBPriceRequest()  
    req.Zone = "ap-guangzhou-3"
    req.GoodsNum = 1
    req.Memory =2000
    req.Volume =1000
    req.PayType = 'PRE_PAID'
    req.Period=1

    
    # 通过client对象调用想要访问的接口，需要传入请求对象
    resp = client.DescribeDBPrice(req)

    # 输出json格式的字符串回包
    print(resp.to_json_string())
except TencentCloudSDKException as err:
    print(err)
    
```



### DeleteBackup	|	删除云数据库备份

```python
#!/usr/bin/python
# -*- coding: utf-8 -*-

# 引入云API入口模块
from tencentcloud.common import credential
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.cdb.v20170320 import cdb_client, models

try:
    # 实例化一个认证对象，入参需要传入腾讯云账户secretId，secretKey
    cred = credential.Credential("AKIDrY4UwCdhewLbhdG7f2DmDT4eFftKtWIz", "eGl4KUSEsmaFiyEKFID0bzFKNFvPh2EE")

    #实例化要请求产品(以cdb为例)的client对象
    client = cdb_client.CdbClient(cred, "ap-shanghai")

    #实例化一个请求对象:req = models.ModifyInstanceParamRequest()
    req = models.DeleteBackupRequest()  
    req.InstanceId = "cdb-7ghaiocc"
    req.BackupId = 105119782

    
    # 通过client对象调用想要访问的接口，需要传入请求对象
    resp = client.DeleteBackup(req)

    # 输出json格式的字符串回包
    print(resp.to_json_string())
except TencentCloudSDKException as err:
    print(err)
```
### DescribeBackupConfig	|	查询云数据库备份配置信息

```python
#!/usr/bin/python
# -*- coding: utf-8 -*-

# 引入云API入口模块

from tencentcloud.common import credential
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.cdb.v20170320 import cdb_client, models

try:
    # 实例化一个认证对象，入参需要传入腾讯云账户secretId，secretKey
    cred = credential.Credential("AKIDrY4UwCdhewLbhdG7f2DmDT4eFftKtWIz", "eGl4KUSEsmaFiyEKFID0bzFKNFvPh2EE")

    #实例化要请求产品(以cdb为例)的client对象
    client = cdb_client.CdbClient(cred, "ap-shanghai")

    #实例化一个请求对象:req = models.ModifyInstanceParamRequest()
    req = models.DescribeBackupConfigRequest()
    req.InstanceId = "cdb-7ghaiocc"

    print req
    # 通过client对象调用想要访问的接口，需要传入请求对象
    resp = client.DescribeBackupConfig(req)

    # 输出json格式的字符串回包
    print(resp.to_json_string())
except TencentCloudSDKException as err:
    print(err)
```

### DescribeBackupDatabases	|	查询备份数据库列表

```python
#!/usr/bin/python
# -*- coding: utf-8 -*-

# 引入云API入口模块
import logging
import traceback
from tencentcloud.common import credential
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.cdb.v20170320 import cdb_client, models

try:
    # 实例化一个认证对象，入参需要传入腾讯云账户secretId，secretKey
    cred = credential.Credential("AKIDrY4UwCdhewLbhdG7f2DmDT4eFftKtWIz", "eGl4KUSEsmaFiyEKFID0bzFKNFvPh2EE")

    #实例化要请求产品(以cdb为例)的client对象
    client = cdb_client.CdbClient(cred, "ap-shanghai")

    #实例化一个请求对象:req = models.ModifyInstanceParamRequest()
    req = models.DescribeBackupDatabasesRequest()
    req.InstanceId = "cdb-7ghaiocc"
    req.StartTime = "2018-08-02 15:19:19"

    print req
    # 通过client对象调用想要访问的接口，需要传入请求对象
    resp = client.DescribeBackupDatabases(req)

    # 输出json格式的字符串回包
    print(resp.to_json_string())
except TencentCloudSDKException as err:
    msg = traceback.format_exc() # 方式1  
    print (msg) 
```

### DescribeBackupTables	|	查询指定数据库的备份数据表

```python
#!/usr/bin/python
# -*- coding: utf-8 -*-

# 引入云API入口模块

from tencentcloud.common import credential
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.cdb.v20170320 import cdb_client, models

try:
    # 实例化一个认证对象，入参需要传入腾讯云账户secretId，secretKey
    cred = credential.Credential("AKIDrY4UwCdhewLbhdG7f2DmDT4eFftKtWIz", "eGl4KUSEsmaFiyEKFID0bzFKNFvPh2EE")

    #实例化要请求产品(以cdb为例)的client对象
    client = cdb_client.CdbClient(cred, "ap-shanghai")

    #实例化一个请求对象:req = models.ModifyInstanceParamRequest()
    req = models.DescribeBackupTablesRequest()
    req.InstanceId = "cdb-7ghaiocc"
    req.StartTime = "2018-08-02 15:19:19"
    req.DatabaseName ="sissi"


    # 通过client对象调用想要访问的接口，需要传入请求对象
    resp = client.DescribeBackupTables(req)

    # 输出json格式的字符串回包
    print(resp.to_json_string())
except TencentCloudSDKException as err:
    print(err)
```

### DescribeBackups	|	查询备份日志

```python
#!/usr/bin/python
# -*- coding: utf-8 -*-

# 引入云API入口模块

from tencentcloud.common import credential
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.cdb.v20170320 import cdb_client, models

try:
    # 实例化一个认证对象，入参需要传入腾讯云账户secretId，secretKey
    cred = credential.Credential("AKIDrY4UwCdhewLbhdG7f2DmDT4eFftKtWIz", "eGl4KUSEsmaFiyEKFID0bzFKNFvPh2EE")

    #实例化要请求产品(以cdb为例)的client对象
    client = cdb_client.CdbClient(cred, "ap-shanghai")

    #实例化一个请求对象:req = models.ModifyInstanceParamRequest()
    req = models.DescribeBackupsRequest()
    req.InstanceId = "cdb-7ghaiocc"
     
    # 通过client对象调用想要访问的接口，需要传入请求对象
    resp = client.DescribeBackups(req)
    print resp

    # 输出json格式的字符串回包
    print(resp.to_json_string())
except TencentCloudSDKException as err:
    print(err)
```

### DescribeSlowLogs	|	查询慢查询日志

```python
#!/usr/bin/python
# -*- coding: utf-8 -*-

# 引入云API入口模块

from tencentcloud.common import credential
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.cdb.v20170320 import cdb_client, models

try:
    # 实例化一个认证对象，入参需要传入腾讯云账户secretId，secretKey
    cred = credential.Credential("AKIDrY4UwCdhewLbhdG7f2DmDT4eFftKtWIz", "eGl4KUSEsmaFiyEKFID0bzFKNFvPh2EE")

    #实例化要请求产品(以cdb为例)的client对象
    client = cdb_client.CdbClient(cred, "ap-shanghai")

    #实例化一个请求对象:req = models.ModifyInstanceParamRequest()
    req = models.DescribeSlowLogsRequest()
    req.InstanceId = "cdb-7ghaiocc"

    # 通过client对象调用想要访问的接口，需要传入请求对象
    resp = client.DescribeSlowLogs(req)

    # 输出json格式的字符串回包
    print(resp.to_json_string())
except TencentCloudSDKException as err:
    print(err)
```

### ModifyBackupConfig	|	修改数据库备份配置

```python
#!/usr/bin/python
# -*- coding: utf-8 -*-

# 引入云API入口模块

from tencentcloud.common import credential
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.cdb.v20170320 import cdb_client, models

try:
    # 实例化一个认证对象，入参需要传入腾讯云账户secretId，secretKey
    cred = credential.Credential("AKIDrY4UwCdhewLbhdG7f2DmDT4eFftKtWIz", "eGl4KUSEsmaFiyEKFID0bzFKNFvPh2EE")

    #实例化要请求产品(以cdb为例)的client对象
    client = cdb_client.CdbClient(cred, "ap-shanghai")

    #实例化一个请求对象:req = models.ModifyInstanceParamRequest()
    req = models.ModifyBackupConfigRequest()
    req.InstanceId = "cdb-1y6g3zj8"
    req.ExpireDays = 10
    req.StartTime = "06:00-10:00"
    req.BackupMethod = "logical"
    print req


    # 通过client对象调用想要访问的接口，需要传入请求对象
    resp = client.ModifyBackupConfig(req)

    # 输出json格式的字符串回包
    print(resp.to_json_string())
except TencentCloudSDKException as err:
    print(err)
```

### CloseWanService	|	关闭实例外网访问

```python
#!/usr/bin/python
# -*- coding: utf-8 -*-

# 引入云API入口模块

from tencentcloud.common import credential
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.cdb.v20170320 import cdb_client, models

try:
    # 实例化一个认证对象，入参需要传入腾讯云账户secretId，secretKey
    cred = credential.Credential("AKIDrY4UwCdhewLbhdG7f2DmDT4eFftKtWIz", "eGl4KUSEsmaFiyEKFID0bzFKNFvPh2EE")

    #实例化要请求产品(以cdb为例)的client对象
    client = cdb_client.CdbClient(cred, "ap-shanghai")

    #实例化一个请求对象:req = models.ModifyInstanceParamRequest()
    req = models.CloseWanServiceRequest()
    req.InstanceId = "cdb-1y6g3zj8"

    # 通过client对象调用想要访问的接口，需要传入请求对象
    resp = client.CloseWanService(req)

    # 输出json格式的字符串回包
    print(resp.to_json_string())
except TencentCloudSDKException as err:
    print(err)
```

### OpenWanService	|	开通实例外网访问

```python
#!/usr/bin/python
# -*- coding: utf-8 -*-

# 引入云API入口模块

from tencentcloud.common import credential
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.cdb.v20170320 import cdb_client, models

try:
    # 实例化一个认证对象，入参需要传入腾讯云账户secretId，secretKey
    cred = credential.Credential("AKIDrY4UwCdhewLbhdG7f2DmDT4eFftKtWIz", "eGl4KUSEsmaFiyEKFID0bzFKNFvPh2EE")

    #实例化要请求产品(以cdb为例)的client对象
    client = cdb_client.CdbClient(cred, "ap-shanghai")

    #实例化一个请求对象:req = models.ModifyInstanceParamRequest()
    req = models.OpenWanServiceRequest()
    req.InstanceId = "cdb-1y6g3zj8"

    # 通过client对象调用想要访问的接口，需要传入请求对象
    resp = client.OpenWanService(req)

    # 输出json格式的字符串回包
    print(resp.to_json_string())
except TencentCloudSDKException as err:
    print(err)
```

### CreateDBInstanceHour	|	创建云数据库实例（按量计费）

```python
'''小时计费要冻结金额，需要账号有钱，如果账号余额为0，则不能购买'''
#!/usr/bin/python
# -*- coding: utf-8 -*-

# 引入云API入口模块
import logging
import traceback
from tencentcloud.common import credential
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.cdb.v20170320 import cdb_client, models

try:
    # 实例化一个认证对象，入参需要传入腾讯云账户secretId，secretKey
    cred = credential.Credential("AKIDrY4UwCdhewLbhdG7f2DmDT4eFftKtWIz", "eGl4KUSEsmaFiyEKFID0bzFKNFvPh2EE")

    #实例化要请求产品(以cdb为例)的client对象
    client = cdb_client.CdbClient(cred, "ap-beijing")

    #实例化一个请求对象:req = models.ModifyInstanceParamRequest()
    req = models.CreateDBInstanceHourRequest()
    req.EngineVersion = "5.6"
    req.Zone = "ap-beijing-3"
    req.ProjectId = 0
    req.GoodsNum = 1
    req.Memory = 1000
    req.Volume = 50
    req.InstanceRole = "master"
    req.Port =3311
    req.Password = "CDB@Qcloud"
    req.ParamList = [{"name":"max_connections","value":"1000"},{"name":"lower_case_table_names","value":"1"}]
    req.ProtectMode = 1
    req.SlaveZone = "ap-beijing-3"
    req.InstanceName = "oneday1"
    req.AutoRenewFlag = 0


    # 通过client对象调用想要访问的接口，需要传入请求对象
    resp = client.CreateDBInstanceHour(req)

    # 输出json格式的字符串回包
    print(resp.to_json_string())
except TencentCloudSDKException as err:
    msg = traceback.format_exc() # 方式1  
    print (msg) 
```

### DescribeDBInstanceCharset	|	查询云数据库实例的字符集

```python
#!/usr/bin/python
# -*- coding: utf-8 -*-

# 引入云API入口模块

from tencentcloud.common import credential
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.cdb.v20170320 import cdb_client, models

try:
    # 实例化一个认证对象，入参需要传入腾讯云账户secretId，secretKey
    cred = credential.Credential("AKIDrY4UwCdhewLbhdG7f2DmDT4eFftKtWIz", "eGl4KUSEsmaFiyEKFID0bzFKNFvPh2EE")

    #实例化要请求产品(以cdb为例)的client对象
    client = cdb_client.CdbClient(cred, "ap-shanghai")

    #实例化一个请求对象:req = models.ModifyInstanceParamRequest()
    req = models.DescribeDBInstanceCharsetRequest()
    req.InstanceId = "cdb-1y6g3zj8"

    # 通过client对象调用想要访问的接口，需要传入请求对象
    resp = client.DescribeDBInstanceCharset(req)

    # 输出json格式的字符串回包
    print(resp.to_json_string())
except TencentCloudSDKException as err:
    print(err)
```

### DescribeDBInstanceConfig	|	查询云数据库实例的配置信息

```python
#!/usr/bin/python
# -*- coding: utf-8 -*-

# 引入云API入口模块

from tencentcloud.common import credential
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.cdb.v20170320 import cdb_client, models

try:
    # 实例化一个认证对象，入参需要传入腾讯云账户secretId，secretKey
    cred = credential.Credential("AKIDrY4UwCdhewLbhdG7f2DmDT4eFftKtWIz", "eGl4KUSEsmaFiyEKFID0bzFKNFvPh2EE")

    #实例化要请求产品(以cdb为例)的client对象
    client = cdb_client.CdbClient(cred, "ap-shanghai")

    #实例化一个请求对象:req = models.ModifyInstanceParamRequest()
    req = models.DescribeDBInstanceConfigRequest()
    req.InstanceId = "cdb-1y6g3zj8"


    # 通过client对象调用想要访问的接口，需要传入请求对象
    resp = client.DescribeDBInstanceConfig(req)

    # 输出json格式的字符串回包
    print(resp.to_json_string())
except TencentCloudSDKException as err:
    print(err)

```

### DescribeDBInstanceGTID	|	查询云数据实例的GTID是否开通

```python
#!/usr/bin/python
# -*- coding: utf-8 -*-

# 引入云API入口模块

from tencentcloud.common import credential
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.cdb.v20170320 import cdb_client, models

try:
    # 实例化一个认证对象，入参需要传入腾讯云账户secretId，secretKey
    cred = credential.Credential("AKIDrY4UwCdhewLbhdG7f2DmDT4eFftKtWIz", "eGl4KUSEsmaFiyEKFID0bzFKNFvPh2EE")

    #实例化要请求产品(以cdb为例)的client对象
    client = cdb_client.CdbClient(cred, "ap-shanghai")

    #实例化一个请求对象:req = models.ModifyInstanceParamRequest()
    req = models.DescribeDBInstanceGTIDRequest()
    req.InstanceId = "cdb-1y6g3zj8"

    # 通过client对象调用想要访问的接口，需要传入请求对象
    resp = client.DescribeDBInstanceGTID(req)

    # 输出json格式的字符串回包
    print(resp.to_json_string())
except TencentCloudSDKException as err:
    print(err)
```

### DescribeDBInstanceRebootTime	|查询云数据库实例的预期重启时间

```python
#!/usr/bin/python
# -*- coding: utf-8 -*-

# 引入云API入口模块

from tencentcloud.common import credential
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.cdb.v20170320 import cdb_client, models

try:
    # 实例化一个认证对象，入参需要传入腾讯云账户secretId，secretKey
    cred = credential.Credential("AKIDrY4UwCdhewLbhdG7f2DmDT4eFftKtWIz", "eGl4KUSEsmaFiyEKFID0bzFKNFvPh2EE")

    #实例化要请求产品(以cdb为例)的client对象
    client = cdb_client.CdbClient(cred, "ap-shanghai")

    #实例化一个请求对象:req = models.ModifyInstanceParamRequest()
    req = models.DescribeDBInstanceRebootTimeRequest()
    req.InstanceIds = ["cdb-1y6g3zj8"]

    # 通过client对象调用想要访问的接口，需要传入请求对象
    resp = client.DescribeDBInstanceRebootTime(req)

    # 输出json格式的字符串回包
    print(resp.to_json_string())
except TencentCloudSDKException as err:
    print(err)
```

### DescribeDBInstances	|	查询实例列表

```python
#!/usr/bin/python
# -*- coding: utf-8 -*-

# 引入云API入口模块
import logging
import traceback
from tencentcloud.common import credential
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.cdb.v20170320 import cdb_client, models

try:
    # 实例化一个认证对象，入参需要传入腾讯云账户secretId，secretKey
    cred = credential.Credential("AKIDrY4UwCdhewLbhdG7f2DmDT4eFftKtWIz", "eGl4KUSEsmaFiyEKFID0bzFKNFvPh2EE")

    #实例化要请求产品(以cdb为例)的client对象
    client = cdb_client.CdbClient(cred, "ap-shanghai")

    #实例化一个请求对象:req = models.ModifyInstanceParamRequest()
    req = models.DescribeDBInstancesRequest()
    req.EngineVersions = ["5.6"]
    req.OrderBy = "instanceId"
    req.InstanceIds = ["cdb-1j8lumf6"]


    # 通过client对象调用想要访问的接口，需要传入请求对象
    resp = client.DescribeDBInstances(req)

    # 输出json格式的字符串回包
    print(resp.to_json_string())
except TencentCloudSDKException as err:
        msg = traceback.format_exc() # 方式1  
        print (msg) 
```

### DescribeDBSwitchRecords	|	查询云数据库切换记录

```python
#!/usr/bin/python
# -*- coding: utf-8 -*-

# 引入云API入口模块

from tencentcloud.common import credential
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.cdb.v20170320 import cdb_client, models

try:
    # 实例化一个认证对象，入参需要传入腾讯云账户secretId，secretKey
    cred = credential.Credential("AKIDrY4UwCdhewLbhdG7f2DmDT4eFftKtWIz", "eGl4KUSEsmaFiyEKFID0bzFKNFvPh2EE")

    #实例化要请求产品(以cdb为例)的client对象
    client = cdb_client.CdbClient(cred, "ap-beijing")

    #实例化一个请求对象:req = models.ModifyInstanceParamRequest()
    req = models.DescribeDBSwitchRecordsRequest()
    req.InstanceId = "cdb-ogwxsm0f"


    # 通过client对象调用想要访问的接口，需要传入请求对象
    resp = client.DescribeDBSwitchRecords(req)

    # 输出json格式的字符串回包
    print(resp.to_json_string())
except TencentCloudSDKException as err:
    print(err)
```

### IsolateDBInstance	|	隔离云数据库实例

```python

#!/usr/bin/python
# -*- coding: utf-8 -*-
'''只能用于按量计费，随时隔离，不支持包年包月实例。'''
# 引入云API入口模块
import logging
import traceback
from tencentcloud.common import credential
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.cdb.v20170320 import cdb_client, models

try:
    # 实例化一个认证对象，入参需要传入腾讯云账户secretId，secretKey
    cred = credential.Credential("AKIDrY4UwCdhewLbhdG7f2DmDT4eFftKtWIz", "eGl4KUSEsmaFiyEKFID0bzFKNFvPh2EE")

    #实例化要请求产品(以cdb为例)的client对象
    client = cdb_client.CdbClient(cred, "ap-beijing")

    #实例化一个请求对象:req = models.ModifyInstanceParamRequest()
    req = models.IsolateDBInstanceRequest()
    req.InstanceId = "cdb-ogwxsm0f"

    # 通过client对象调用想要访问的接口，需要传入请求对象
    resp = client.IsolateDBInstance(req)

    # 输出json格式的字符串回包
    print(resp.to_json_string())
except TencentCloudSDKException as err:
    msg = traceback.format_exc() # 方式1  
    print (msg) 
```

### ModifyDBInstanceName	|	修改云数据库实例名

```python
#!/usr/bin/python
# -*- coding: utf-8 -*-

# 引入云API入口模块
from tencentcloud.common import credential
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.cdb.v20170320 import cdb_client, models

try:
    # 实例化一个认证对象，入参需要传入腾讯云账户secretId，secretKey
    cred = credential.Credential("AKIDrY4UwCdhewLbhdG7f2DmDT4eFftKtWIz", "eGl4KUSEsmaFiyEKFID0bzFKNFvPh2EE")

    #实例化要请求产品(以cdb为例)的client对象
    client = cdb_client.CdbClient(cred, "ap-beijing")

    #实例化一个请求对象:req = models.ModifyInstanceParamRequest()
    req = models.ModifyDBInstanceNameRequest()
    req.InstanceId = "cdb-cukm86n2"
    req.InstanceName = "1s中文"

    # 通过client对象调用想要访问的接口，需要传入请求对象
    resp = client.ModifyDBInstanceName(req)

    # 输出json格式的字符串回包
    print(resp.to_json_string())
except TencentCloudSDKException as err:
    print(err)
```

### RestartDBInstances	|	重启实例

```python
#!/usr/bin/python
# -*- coding: utf-8 -*-

# 引入云API入口模块

from tencentcloud.common import credential
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.cdb.v20170320 import cdb_client, models

try:
    # 实例化一个认证对象，入参需要传入腾讯云账户secretId，secretKey
    cred = credential.Credential("AKIDrY4UwCdhewLbhdG7f2DmDT4eFftKtWIz", "eGl4KUSEsmaFiyEKFID0bzFKNFvPh2EE")

    #实例化要请求产品(以cdb为例)的client对象
    client = cdb_client.CdbClient(cred, "ap-shanghai")

    #实例化一个请求对象:req = models.ModifyInstanceParamRequest()
    req = models.RestartDBInstancesRequest()
    req.InstanceIds = ["cdb-7ghaiocc"]

    # 通过client对象调用想要访问的接口，需要传入请求对象
    resp = client.RestartDBInstances(req)

    # 输出json格式的字符串回包
    print(resp.to_json_string())
except TencentCloudSDKException as err:
    print(err)
```

### UpgradeDBInstance	|	升级云数据库实例

```python
#!/usr/bin/python
# -*- coding: utf-8 -*-

# 引入云API入口模块

from tencentcloud.common import credential
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.cdb.v20170320 import cdb_client, models

try:
    # 实例化一个认证对象，入参需要传入腾讯云账户secretId，secretKey
    cred = credential.Credential("AKIDrY4UwCdhewLbhdG7f2DmDT4eFftKtWIz", "eGl4KUSEsmaFiyEKFID0bzFKNFvPh2EE")

    #实例化要请求产品(以cdb为例)的client对象
    client = cdb_client.CdbClient(cred, "ap-shanghai")

    #实例化一个请求对象:req = models.ModifyInstanceParamRequest()
    req = models.UpgradeDBInstanceRequest()
    req.InstanceId = "cdb-7ghaiocc"
    req.Memory = 4000
    req.Volume = 200

    # 通过client对象调用想要访问的接口，需要传入请求对象
    resp = client.UpgradeDBInstance(req)

    # 输出json格式的字符串回包
    print(resp.to_json_string())
except TencentCloudSDKException as err:
    print(err)
```

### UpgradeDBInstanceEngineVersion	|	升级实例版本

```python
#!/usr/bin/python
# -*- coding: utf-8 -*-

# 引入云API入口模块

from tencentcloud.common import credential
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.cdb.v20170320 import cdb_client, models

try:
    # 实例化一个认证对象，入参需要传入腾讯云账户secretId，secretKey
    cred = credential.Credential("AKIDrY4UwCdhewLbhdG7f2DmDT4eFftKtWIz", "eGl4KUSEsmaFiyEKFID0bzFKNFvPh2EE")

    #实例化要请求产品(以cdb为例)的client对象
    client = cdb_client.CdbClient(cred, "ap-chengdu")

    #实例化一个请求对象:req = models.ModifyInstanceParamRequest()
    req = models.UpgradeDBInstanceEngineVersionRequest()
    req.InstanceId = "cdb-qf8l27kx"
    req.EngineVersion = "5.7"

    # 通过client对象调用想要访问的接口，需要传入请求对象
    resp = client.UpgradeDBInstanceEngineVersion(req)

    # 输出json格式的字符串回包
    print(resp.to_json_string())
except TencentCloudSDKException as err:
    print(err)

```

### CreateDBImportJob	|	创建数据导入任务

```python
#!/usr/bin/python
# -*- coding: utf-8 -*-

# 引入云API入口模块
import logging
import traceback
from tencentcloud.common import credential
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.cdb.v20170320 import cdb_client, models

try:
    # 实例化一个认证对象，入参需要传入腾讯云账户secretId，secretKey
    cred = credential.Credential("AKIDrY4UwCdhewLbhdG7f2DmDT4eFftKtWIz", "eGl4KUSEsmaFiyEKFID0bzFKNFvPh2EE")

    #实例化要请求产品(以cdb为例)的client对象
    client = cdb_client.CdbClient(cred, "ap-shanghai")

    #实例化一个请求对象:req = models.ModifyInstanceParamRequest()
    req = models.CreateDBImportJobRequest()
    req.InstanceId = "cdb-7ghaiocc"
    req.User = "root"
    req.Password = "CDB@Qcloud"
    #控制台上传文件
    req.FileName = "sissi.sql"

    # 通过client对象调用想要访问的接口，需要传入请求对象
    resp = client.CreateDBImportJob(req)

    # 输出json格式的字符串回包
    print(resp.to_json_string())
except TencentCloudSDKException as err:
        msg = traceback.format_exc() # 方式1  
        print (msg) 
```

### DescribeDatabases	|	查询数据库

```python
#!/usr/bin/python
# -*- coding: utf-8 -*-

# 引入云API入口模块

from tencentcloud.common import credential
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.cdb.v20170320 import cdb_client, models

try:
    # 实例化一个认证对象，入参需要传入腾讯云账户secretId，secretKey
    cred = credential.Credential("AKIDrY4UwCdhewLbhdG7f2DmDT4eFftKtWIz", "eGl4KUSEsmaFiyEKFID0bzFKNFvPh2EE")

    #实例化要请求产品(以cdb为例)的client对象
    client = cdb_client.CdbClient(cred, "ap-shanghai")

    #实例化一个请求对象:req = models.ModifyInstanceParamRequest()
    req = models.DescribeDatabasesRequest()
    req.InstanceId = "cdb-7ghaiocc"


    # 通过client对象调用想要访问的接口，需要传入请求对象
    resp = client.DescribeDatabases(req)

    # 输出json格式的字符串回包
    print(resp.to_json_string())
except TencentCloudSDKException as err:
    print(err)
```


### CreateAccounts	|	创建云数据库的账户

```python
#!/usr/bin/python
# -*- coding: utf-8 -*-

# 引入云API入口模块

from tencentcloud.common import credential
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.cdb.v20170320 import cdb_client, models

try:
    # 实例化一个认证对象，入参需要传入腾讯云账户secretId，secretKey
    cred = credential.Credential("AKIDrY4UwCdhewLbhdG7f2DmDT4eFftKtWIz", "eGl4KUSEsmaFiyEKFID0bzFKNFvPh2EE")

    #实例化要请求产品(以cdb为例)的client对象
    client = cdb_client.CdbClient(cred, "ap-beijing")

    #实例化一个请求对象:req = models.ModifyInstanceParamRequest()
    req = models.CreateAccountsRequest()
    req.InstanceId = "cdb-cukm86n2"
    req.Accounts = [{"user":"abc","host":"%"},{"user":"sss","host":"%"}]
    req.Password = "CDB@Qcloud"


    # 通过client对象调用想要访问的接口，需要传入请求对象
    resp = client.CreateAccounts(req)

    # 输出json格式的字符串回包
    print(resp.to_json_string())
except TencentCloudSDKException as err:
    print(err)
```
### DeleteAccounts	|	删除云数据库的账号

```python
#!/usr/bin/python
# -*- coding: utf-8 -*-

# 引入云API入口模块
import logging
import traceback
from tencentcloud.common import credential
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.cdb.v20170320 import cdb_client, models

try:
    # 实例化一个认证对象，入参需要传入腾讯云账户secretId，secretKey
    cred = credential.Credential("AKIDrY4UwCdhewLbhdG7f2DmDT4eFftKtWIz", "eGl4KUSEsmaFiyEKFID0bzFKNFvPh2EE")

    #实例化要请求产品(以cdb为例)的client对象
    client = cdb_client.CdbClient(cred, "ap-beijing")

    #实例化一个请求对象:req = models.ModifyInstanceParamRequest()
    req = models.DeleteAccountsRequest()
    req.InstanceId = "cdb-cukm86n2"
    req.Accounts = [{"user":"sss","host":"%"}]

    # 通过client对象调用想要访问的接口，需要传入请求对象
    resp = client.DeleteAccounts(req)

    # 输出json格式的字符串回包
    print(resp.to_json_string())
except TencentCloudSDKException as err:
        msg = traceback.format_exc() # 方式1  
        print (msg) 

```
### DescribeAccountPrivileges	|	查询云数据库账户的权限信息

```python
#!/usr/bin/python
# -*- coding: utf-8 -*-

# 引入云API入口模块

from tencentcloud.common import credential
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.cdb.v20170320 import cdb_client, models

try:
    # 实例化一个认证对象，入参需要传入腾讯云账户secretId，secretKey
    cred = credential.Credential("AKIDrY4UwCdhewLbhdG7f2DmDT4eFftKtWIz", "eGl4KUSEsmaFiyEKFID0bzFKNFvPh2EE")

    #实例化要请求产品(以cdb为例)的client对象
    client = cdb_client.CdbClient(cred, "ap-beijing")

    #实例化一个请求对象:req = models.ModifyInstanceParamRequest()
    req = models.DescribeAccountPrivilegesRequest()
    req.InstanceId = "cdb-cukm86n2"
    req.User = "root"
    req.Host = "%"

    # 通过client对象调用想要访问的接口，需要传入请求对象
    resp = client.DescribeAccountPrivileges(req)

    # 输出json格式的字符串回包
    print(resp.to_json_string())
except TencentCloudSDKException as err:
    print(err)

```

### DescribeAccounts	|	查询云数据库的所有账号信息

```python
#!/usr/bin/python
# -*- coding: utf-8 -*-

# 引入云API入口模块

from tencentcloud.common import credential
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.cdb.v20170320 import cdb_client, models

try:
    # 实例化一个认证对象，入参需要传入腾讯云账户secretId，secretKey
    cred = credential.Credential("AKIDrY4UwCdhewLbhdG7f2DmDT4eFftKtWIz", "eGl4KUSEsmaFiyEKFID0bzFKNFvPh2EE")

    #实例化要请求产品(以cdb为例)的client对象
    client = cdb_client.CdbClient(cred, "ap-beijing")

    #实例化一个请求对象:req = models.ModifyInstanceParamRequest()
    req = models.DescribeAccountsRequest()
    req.InstanceId = "cdb-cukm86n2"


    # 通过client对象调用想要访问的接口，需要传入请求对象
    resp = client.DescribeAccounts(req)

    # 输出json格式的字符串回包
    print(resp.to_json_string())
except TencentCloudSDKException as err:
    print(err)
```
### ModifyAccountDescription	|	修改云数据库实例账号的备注信息

```python
#!/usr/bin/python
# -*- coding: utf-8 -*-

# 引入云API入口模块
import logging
import traceback
from tencentcloud.common import credential
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.cdb.v20170320 import cdb_client, models

try:
    # 实例化一个认证对象，入参需要传入腾讯云账户secretId，secretKey
    cred = credential.Credential("AKIDrY4UwCdhewLbhdG7f2DmDT4eFftKtWIz", "eGl4KUSEsmaFiyEKFID0bzFKNFvPh2EE")

    #实例化要请求产品(以cdb为例)的client对象
    client = cdb_client.CdbClient(cred, "ap-beijing")

    #实例化一个请求对象:req = models.ModifyInstanceParamRequest()
    req = models.ModifyAccountDescriptionRequest()
    req.InstanceId = "cdb-cukm86n2"
    req.Accounts = [{"user":"root","host":"%"}]
    req.Description = "管理员"

    # 通过client对象调用想要访问的接口，需要传入请求对象
    resp = client.ModifyAccountDescription(req)

    # 输出json格式的字符串回包
    print(resp.to_json_string())
except TencentCloudSDKException as err:
        msg = traceback.format_exc() # 方式1  
        print (msg) 

```
### ModifyAccountPassword	|	修改云数据库实例账号的密码

```python
#!/usr/bin/python
# -*- coding: utf-8 -*-

# 引入云API入口模块
import logging
import traceback
from tencentcloud.common import credential
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.cdb.v20170320 import cdb_client, models

try:
    # 实例化一个认证对象，入参需要传入腾讯云账户secretId，secretKey
    cred = credential.Credential("AKIDrY4UwCdhewLbhdG7f2DmDT4eFftKtWIz", "eGl4KUSEsmaFiyEKFID0bzFKNFvPh2EE")

    #实例化要请求产品(以cdb为例)的client对象
    client = cdb_client.CdbClient(cred, "ap-beijing")

    #实例化一个请求对象:req = models.ModifyInstanceParamRequest()
    req = models.ModifyAccountPasswordRequest()
    req.InstanceId = "cdb-cukm86n2"
    req.Accounts = [{"user":"abc","host":"%"}]
    req.NewPassword ="CDB@Qcloud111"

    # 通过client对象调用想要访问的接口，需要传入请求对象
    resp = client.ModifyAccountPassword(req)

    # 输出json格式的字符串回包
    print(resp.to_json_string())
except TencentCloudSDKException as err:
        msg = traceback.format_exc() # 方式1  
        print (msg) 
```
### ModifyAccountPrivileges	|	修改云数据库实例账号的权限

```python
#!/usr/bin/python
# -*- coding: utf-8 -*-

# 引入云API入口模块
import logging
import traceback
from tencentcloud.common import credential
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.cdb.v20170320 import cdb_client, models

try:
    # 实例化一个认证对象，入参需要传入腾讯云账户secretId，secretKey
    cred = credential.Credential("AKIDrY4UwCdhewLbhdG7f2DmDT4eFftKtWIz", "eGl4KUSEsmaFiyEKFID0bzFKNFvPh2EE")

    #实例化要请求产品(以cdb为例)的client对象
    client = cdb_client.CdbClient(cred, "ap-beijing")

    #实例化一个请求对象:req = models.ModifyInstanceParamRequest()
    req = models.ModifyAccountPrivilegesRequest()
    req.InstanceId = "cdb-cukm86n2"
    req.Accounts = [{"user":"abc","host":"%"}]
    '''req.GlobalPrivileges后参数必须大写'''
    req.GlobalPrivileges = ["SELECT","INSERT","UPDATE","DELETE"]

    # 通过client对象调用想要访问的接口，需要传入请求对象
    resp = client.ModifyAccountPrivileges(req)

    # 输出json格式的字符串回包
    print(resp.to_json_string())
except TencentCloudSDKException as err:
        msg = traceback.format_exc() # 方式1  
        print (msg) 
```
### VerifyRootAccount	|	验证root账号权限

```python
#!/usr/bin/python
# -*- coding: utf-8 -*-

# 引入云API入口模块

from tencentcloud.common import credential
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.cdb.v20170320 import cdb_client, models

try:
    # 实例化一个认证对象，入参需要传入腾讯云账户secretId，secretKey
    cred = credential.Credential("AKIDrY4UwCdhewLbhdG7f2DmDT4eFftKtWIz", "eGl4KUSEsmaFiyEKFID0bzFKNFvPh2EE")

    #实例化要请求产品(以cdb为例)的client对象
    client = cdb_client.CdbClient(cred, "ap-beijing")

    #实例化一个请求对象:req = models.ModifyInstanceParamRequest()
    req = models.VerifyRootAccountRequest()
    req.InstanceId = "cdb-cukm86n2"
    req.Password = "CDB@Qcloud"

    # 通过client对象调用想要访问的接口，需要传入请求对象
    resp = client.VerifyRootAccount(req)

    # 输出json格式的字符串回包
    print(resp.to_json_string())
except TencentCloudSDKException as err:
    print(err)
```
### GetMonitorData	|	读取监控数据(新)

```python
#!/usr/bin/python
# -*- coding: utf-8 -*-

# 引入云API入口模块
import sys
import os
#os.environ['http_proxy'] = '127.0.0.1:12759'
#os.environ['https_proxy'] = '127.0.0.1:12759'
from QcloudApi.qcloudapi import QcloudApi
module = 'monitor'

'''
action 对应接口的接口名，请参考产品文档上对应接口的接口名
'''
action = 'GetMonitorData'

config = {
    'Region': 'sh',
    'secretId': 'AKIDrY4UwCdhewLbhdG7f2DmDT4eFftKtWIz',
    'secretKey': 'eGl4KUSEsmaFiyEKFID0bzFKNFvPh2EE',
    'method': 'get',
}

'''
params 请求参数，请参考产品文档上对应接口的说明
'''
params = {
    'namespace': 'qce/cdb',
    'dimensions.0.name': 'uInstanceId',
    'dimensions.0.value': 'cdb-7ghaiocc',
    'metricName': 'slow_queries',
    'startTime': '2018-08-04 14:10:00',
    'endTime': '2018-08-04 17:10:00',
    'period': 60
}
try:
    service = QcloudApi(module, config)

    # 生成请求的URL，不发起请求
    print service.generateUrl(action, params)
    # 调用接口，发起请求
    print service.call(action, params)
except Exception, e:
    print 'exception:', e


```
### DescribeBaseMetrics	|	获取监控指标列表(新)

```python
#!/usr/bin/python
# -*- coding: utf-8 -*-

# 引入云API入口模块
import sys
import os
#os.environ['http_proxy'] = '127.0.0.1:12759'
#os.environ['https_proxy'] = '127.0.0.1:12759'
from QcloudApi.qcloudapi import QcloudApi
module = 'monitor'

'''
action 对应接口的接口名，请参考产品文档上对应接口的接口名
'''
action = 'DescribeBaseMetrics'

config = {
    'Region': 'sh',
    'secretId': 'AKIDrY4UwCdhewLbhdG7f2DmDT4eFftKtWIz',
    'secretKey': 'eGl4KUSEsmaFiyEKFID0bzFKNFvPh2EE',
    'method': 'get',
}

'''
params 请求参数，请参考产品文档上对应接口的说明
'''
params = {
    'namespace': 'qce/cdb',
    'dimensions.0.name': 'uInstanceId',
    'dimensions.0.value': 'cdb-7ghaiocc',
    'startTime': '2018-08-06 08:10:00',
    'endTime': '2018-08-06 10:10:00',
    'period': 60
}
try:
    service = QcloudApi(module, config)

    # 生成请求的URL，不发起请求
    print service.generateUrl(action, params)
    # 调用接口，发起请求
    print service.call(action, params)
except Exception, e:
    print 'exception:', e


```
### SendCustomAlarmMsg	|	发送自定义消息告警

```python
#!/usr/bin/python
# -*- coding: utf-8 -*-

# 引入云API入口模块
import sys
import os
#os.environ['http_proxy'] = '127.0.0.1:12759'
#os.environ['https_proxy'] = '127.0.0.1:12759'
from QcloudApi.qcloudapi import QcloudApi
module = 'monitor'

'''
action 对应接口的接口名，请参考产品文档上对应接口的接口名
'''
action = 'SendCustomAlarmMsg'

config = {
    'Region': 'sh',
    'secretId': 'AKIDrY4UwCdhewLbhdG7f2DmDT4eFftKtWIz',
    'secretKey': 'eGl4KUSEsmaFiyEKFID0bzFKNFvPh2EE',
    'method': 'get',
}

'''
params 请求参数，请参考产品文档上对应接口的说明
'''
params = {
    'namespace': 'qce/cvm',
    'policyId': 'cm-fbi1mygr',
    'msg': 'CPU利用率大于20%'
}
try:
    service = QcloudApi(module, config)

    # 生成请求的URL，不发起请求
    print service.generateUrl(action, params)
    # 调用接口，发起请求
    print service.call(action, params)
except Exception, e:
    print 'exception:', e

```
### DTS数据迁移：
| API        | 描述   | 
| --------   | -----  | 
|CreateMigrateJob	|	创建数据迁移任务|
|CreateMigrateCheckJob	|	创建校验迁移任务|
|DescribeMigrateCheckJob	|	获取迁移校验结果|
|StartMigrateJob	|	启动数据迁移任务|
|DescribeMigrateJobs	|	查询数据迁移任务|
|DeleteMigrateJob	|	删除数据迁移任务|
|ModifyMigrateJob	|	修改数据迁移任务|
|CompleteMigrateJob	|	完成数据迁移任务|
####demo如下：
```python

# -*- coding: utf-8 -*-
from tencentcloud.common import credential
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
# 导入对应产品模块的client models。
from tencentcloud.dts.v20180330 import dts_client, models

def returnClient():
    cred = credential.Credential("AKIDrY4UwCdhewLbhdG7f2DmDT4eFftKtWIz", "eGl4KUSEsmaFiyEKFID0bzFKNFvPh2EE")
    client = dts_client.DtsClient(cred, "ap-guangzhou")
    return client

def CreateMigrateJobTask(client,jobname,src_ins,des_ins,dbname):
    try:

        # 实例化一个请求对象
        req = models.CreateMigrateJobRequest()

        params = '''{
            "Region" : "ap-guangzhou-2",
            "JobName" : "%s",
            "MigrateOption" : {"RunMode":1,"MigrateType":2,"MigrateObject":2,"ConsistencyType":5,"IsOverrideRoot":0},
            "SrcDatabaseType" : "mysql",
            "SrcAccessType" : "cdb",
            "SrcInfo" : {"InstanceId":"%s","Region":"ap-guangzhou","Supplier":"others","User":"root","Password":"CDB@Qcloud"},
            "DstDatabaseType" : "mysql",
            "DstAccessType" : "cdb",
            "DstInfo" : {"InstanceId":"%s","Region":"ap-guangzhou"}
        }'''%(jobname,src_ins,des_ins)

        print(params)
        req.from_json_string(params)

        req.DatabaseInfo = """[{"Database":"%s"}]""" % (dbname)
	    # 通过client对象调用想要访问的接口，需要传入请求对象
        resp = client.CreateMigrateJob(req)
        # 输出json格式的字符串回包

        ret = eval(resp.to_json_string())
        #print(resp.to_json_string())
        return ret

    except TencentCloudSDKException as err:
        print(err)

def ModifyMigrateJobTask(client,jobid,newname,src_ins,des_ins,dbname):
    try:

        # 实例化一个请求对象
        req = models.ModifyMigrateJobRequest()

        params = '''{
            "Region" : "ap-guangzhou-2",
            "JobId" : "%s",
            "JobName" : "%s",
            "MigrateOption" : {"RunMode":1,"MigrateType":2,"MigrateObject":2,"ConsistencyType":5,"IsOverrideRoot":0},
            "SrcDatabaseType" : "mysql",
            "SrcAccessType" : "cdb",
            "SrcInfo" : {"InstanceId":"%s","Region":"ap-guangzhou","Supplier":"others","User":"root","Password":"CDB@Qcloud"},
            "DstDatabaseType" : "mysql",
            "DstAccessType" : "cdb",
            "DstInfo" : {"InstanceId":"%s","Region":"ap-guangzhou"}
        }'''%(jobid,newname,src_ins,des_ins)

        print(params)
        req.from_json_string(params)

        req.DatabaseInfo = """[{"Database":"%s"}]""" % (dbname)
	    # 通过client对象调用想要访问的接口，需要传入请求对象
        resp = client.ModifyMigrateJob(req)
        # 输出json格式的字符串回包

        ret = eval(resp.to_json_string())
        #print(resp.to_json_string())
        return ret

    except TencentCloudSDKException as err:
        print(err)



def CreateMigrateCheckJobTask(client,jobid):
    try:
        req = models.CreateMigrateCheckJobRequest()
        params = '''{
            "Region": "ap-guangzhou-2",
            "JobId": "%s"
        }''' %(jobid)
        req.from_json_string(params)
        resp = client.CreateMigrateCheckJob(req)
        print resp
        return eval(resp.to_json_string())
    except TencentCloudSDKException as err:
        print(err)

def DeleteMigrateJobTask(client,jobid):
    try:
        req = models.DeleteMigrateJobRequest()
        params = '''{
            "Region": "ap-guangzhou-2",
            "JobId": "%s"
        }''' %(jobid)
        req.from_json_string(params)
        resp = client.DeleteMigrateJob(req)
        print resp
        return eval(resp.to_json_string())
    except TencentCloudSDKException as err:
        print(err)

def DescribeMigrateCheckJobTask(client,jobid):
    try:
        req = models.DescribeMigrateCheckJobRequest()
        params = '''{
            "Region": "ap-guangzhou-2",
            "JobId": "%s"
        }''' %(jobid)
        req.from_json_string(params)
        resp = client.DescribeMigrateCheckJob(req)
        print resp
        return eval(resp.to_json_string())
    except TencentCloudSDKException as err:
        print(err)




def DescribeMigrateJobsTask(client,jobid):
    try:
        req = models.DescribeMigrateJobsRequest()
        params = '''{
            "Region": "ap-guangzhou-2",
            "JobId": "%s"
        }''' %(jobid)
        req.from_json_string(params)
        resp = client.DescribeMigrateJobs(req)
        print eval(resp.to_json_string())
        return eval(resp.to_json_string())
    except TencentCloudSDKException as err:
        print(err)

def StartMigrateJobTask(client,jobid):
    try:
        req = models.StartMigrateJobRequest()
        params = '''{
            "Region": "ap-guangzhou-2",
            "JobName": "%s"
        }''' %(jobid)
        req.from_json_string(params)
        resp = client.StartMigrateJob(req)
        return eval(resp.to_json_string())
    except TencentCloudSDKException as err:
        print(err)





def CompleteMigrateJobTask(client,jobid):
    try:
        req = models.CompleteMigrateJobRequest()
        params = '''{
            "Region": "ap-guangzhou",
            "JobId": "%s"
        }''' %(jobid)
        req.from_json_string(params)
        resp = client.CompleteMigrateJob(req)
        print resp
        return eval(resp.to_json_string())
    except TencentCloudSDKException as err:
        print(err)




if __name__ == '__main__':
        client = returnClient()
        src_ins = "cdb-m916ju6n"
        des_ins = "cdb-niiv38yi"
        jobname = "sissi_02job"
        dbname ="sissi_02"
        #jobid = "dts-3axqfywj"
        newname = "sissi_02_job"
        '''数据迁移任务'''
        CreateMigrateJobTask(client,jobname,src_ins,des_ins,dbname)
        #CreateMigrateCheckJobTask(client,jobid)
        #DescribeMigrateCheckJobTask(client,jobid)
        #StartMigrateJobTask(client,jobid)
        #DescribeMigrateJobsTask(client,jobid)
        #DeleteMigrateJobTask(client,jobid)
        #ModifyMigrateJobTask(client,jobid,newname,src_ins,des_ins,dbname)

        #jobid = "dts-et9hvor7"
        #CompleteMigrateJobTask(client,jobid)


```



### 灾备数据同步：
| API        | 描述   | 
| --------   | -----  | 
|	CreateSyncCheckJob	|	校验灾备同步任务|
|	CreateSyncJob	|	创建灾备同步任务|
|	DeleteSyncJob	|	删除灾备同步任务|
|	DescribeSyncCheckJob	|	查询灾备同步任务校验结果|
|	DescribeSyncJobs	|	查询在迁移平台发起的灾备同步任务|
|	ModifySyncJob	|	修改灾备同步任务|
|	StartSyncJob	|	开始灾备同步任务|
|	StopMigrateJob	|	撤销数据迁移任务|
|	SwitchDrToMaster	|	灾备升级为主实例|

####demo如下：
```python

# -*- coding: utf-8 -*-
from tencentcloud.common import credential
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
# 导入对应产品模块的client models。
from tencentcloud.dts.v20180330 import dts_client, models

def returnClient():
    cred = credential.Credential("AKIDrY4UwCdhewLbhdG7f2DmDT4eFftKtWIz", "eGl4KUSEsmaFiyEKFID0bzFKNFvPh2EE")
    client = dts_client.DtsClient(cred, "ap-guangzhou")
    return client


def DescribeMigrateCheckJobTask(client,jobid):
    try:
        req = models.DescribeMigrateCheckJobRequest()
        params = '''{
            "Region": "ap-guangzhou-2",
            "JobId": "%s"
        }''' %(jobid)
        req.from_json_string(params)
        resp = client.DescribeMigrateCheckJob(req)
        print resp
        return eval(resp.to_json_string())
    except TencentCloudSDKException as err:
        print(err)

def StopMigrateJobTask(client,jobid):
    try:
        req = models.StopMigrateJobRequest()
        params = '''{
            "Region": "ap-shanghai",
            "JobId": "%s"
        }''' %(jobid)
        req.from_json_string(params)
        resp = client.StopMigrateJob(req)
        print resp
        return eval(resp.to_json_string())
    except TencentCloudSDKException as err:
        print(err)

def DescribeMigrateJobsTask(client,jobid):
    try:
        req = models.DescribeMigrateJobsRequest()
        params = '''{
            "Region": "ap-guangzhou-2",
            "JobId": "%s"
        }''' %(jobid)
        req.from_json_string(params)
        resp = client.DescribeMigrateJobs(req)
        print eval(resp.to_json_string())
        return eval(resp.to_json_string())
    except TencentCloudSDKException as err:
        print(err)

def StartMigrateJobTask(client,jobid):
    try:
        req = models.StartMigrateJobRequest()
        params = '''{
            "Region": "ap-guangzhou-2",
            "JobName": "%s"
        }''' %(jobid)
        req.from_json_string(params)
        resp = client.StartMigrateJob(req)
        return eval(resp.to_json_string())
    except TencentCloudSDKException as err:
        print(err)


def CreateSyncJobTask(client,drjobname):
    try:
        req = models.CreateSyncJobRequest()
        params = '''{
            "Region": "ap-shanghai",
            "JobName": "%s",
            "SyncOption" : {"SyncObject":1},
            "SrcDatabaseType" : "mysql",
            "SrcAccessType" : "cdb",
            "SrcInfo" : {"Region":"ap-shanghai","InstanceId":"cdb-7ghaiocc"},
            "DstDatabaseType" : "mysql",
            "DstAccessType" : "cdb",
            "DstInfo" : {"Region":"ap-beijing","InstanceId":"cdb-58vafloq"}
        }'''%(drjobname)
        req.from_json_string(params)
        resp = client.CreateSyncJob(req)
        print resp
        return eval(resp.to_json_string())
    except TencentCloudSDKException as err:
        print(err)

def CreateSyncCheckJobTask(client,jobidrd):
    try:
        req = models.CreateSyncCheckJobRequest()
        params = '''{
            "Region": "ap-shanghai",
            "JobId": "%s"
        }''' %(jobidrd)
        req.from_json_string(params)
        print params
        resp = client.CreateSyncCheckJob(req)
        print resp
        return eval(resp.to_json_string())
    except TencentCloudSDKException as err:
        print(err)


def DescribeSyncCheckJobTask(client,jobidrd):
    try:
        req = models.DescribeSyncCheckJobRequest()
        params = '''{
            "Region": "ap-guangzhou",
            "JobId": "%s"
        }''' %(jobidrd)
        req.from_json_string(params)
        resp = client.DescribeSyncCheckJob(req)
        print resp
        return eval(resp.to_json_string())
    except TencentCloudSDKException as err:
        print(err)



def StartSyncJobTask(client,jobid):
    try:
        req = models.StartSyncJobRequest()
        params = '''{
            "Region": "ap-shanghai",
            "JobId": "%s"
        }''' %(jobid)
        req.from_json_string(params)
        resp = client.StartSyncJob(req)
        print resp
        return eval(resp.to_json_string())
    except TencentCloudSDKException as err:
        print(err)

def DescribeSyncJobsTask(client,jobidrd):
    try:
        req = models.DescribeSyncJobsRequest()
        params = '''{
            "Region": "ap-guangzhou-2",
            "JobId": "%s"
        }''' %(jobidrd)
        req.from_json_string(params)
        resp = client.DescribeSyncJobs(req)
        print resp
        return eval(resp.to_json_string())
    except TencentCloudSDKException as err:
        print(err)

def ModifySyncJobTask(client,jobidrd):
    try:
        req = models.ModifySyncJobRequest()
        params = '''{
            "Region": "ap-beijing",
            "JobId": "%s",
            "JobName" : "aaaaa"
        }''' %(jobidrd)
        req.from_json_string(params)
        resp = client.ModifySyncJob(req)
        print resp
        return eval(resp.to_json_string())
    except TencentCloudSDKException as err:
        print(err)


def DeleteSyncJobTask(client,jobidrd):
    try:
        req = models.DeleteSyncJobRequest()
        params = '''{
            "Region": "ap-guangzhou",
            "JobId": "%s"
        }''' %(jobidrd)
        req.from_json_string(params)
        resp = client.DeleteSyncJob(req)
        print resp
        return eval(resp.to_json_string())
    except TencentCloudSDKException as err:
        print(err)



def SwitchDrToMasterTask(client,InstanceId):
    try:
        req = models.SwitchDrToMasterRequest()
        params = '''{
            "Region": "ap-beijing",
            "DstInfo" : {"Region":"ap-beijing","InstanceId":"%s"},
            "DatabaseType" : "mysql"
        }'''%(InstanceId)
        req.from_json_string(params)
        resp = client.SwitchDrToMaster(req)
        print resp
        return eval(resp.to_json_string())
    except TencentCloudSDKException as err:
        print(err)



if __name__ == '__main__':
        client = returnClient()
        
        '''灾备同步任务'''
        #drjobname = "58vafloq_dr_job"
        #CreateSyncJobTask(client,drjobname)
        #jobidrd = "sync-axip2d8l"
        #ModifySyncJobTask(client,jobidrd)
        #CreateSyncCheckJobTask(client,jobidrd)
        #DescribeSyncCheckJobTask(client,jobidrd)
        #DescribeSyncJobsTask(client,jobidrd)
        #jobid = "sync-axip2d8l"
        #StartSyncJobTask(client,jobid)
        #DeleteSyncJobTask(client,jobidrd)
        #StopMigrateJobTask(client,jobid)
        InstanceId = "cdb-imcoa0ng"
        SwitchDrToMasterTask(client,InstanceId)

```
