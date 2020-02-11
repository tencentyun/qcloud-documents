## 操作场景
本文为您介绍如何通过控制台创建 TcaplusDB 数据表格。

##  前提条件
已创建 TcaplusDB [应用](https://cloud.tencent.com/document/product/596/38807) 和 [部署单元](https://cloud.tencent.com/document/product/596/38809)。

## 操作步骤
1. 登录 [TcaplusDB 控制台](https://console.cloud.tencent.com/tcaplusdb/table)，在左侧导航选择【表格列表】页，单击【新建表格】。
2. 在新建表格页面，配置表格信息。
 - **应用、部署单元**：选择目标应用和部署单元。
 - **表格文件**：从本地上传或从已经上传过的历史文件中选择表定义文件，用户可以同时选择新上传和已上传的历史文件来创建表格，不能上传或选择同名文件。
![](https://main.qcloudimg.com/raw/a63995e11b5b46c99d29bcec45b5e337.png)
如下是一个 proto 示例文件：
```
// tb_online.proto
syntax = "proto2";
package myTcaplusTable;
import "tcaplusservice.optionv1.proto";
message tb_online {
    option(tcaplusservice.tcaplus_primary_key) = "uin,name,region";
    required int64 uin = 1; 
    required string name = 2; 
    required int32 region = 3;
    required int32 gamesvrid = 4; 
    optional int32 logintime = 5 [default = 1];
    repeated int64 lockid = 6 [packed = true]; 
    optional bool is_available = 7 [default = false]; 
    optional pay_info pay = 8; 
}
message pay_info { 
    required int64 pay_id = 1;
    optional uint64 total_money = 2;
    optional uint64 pay_times = 3;
    optional pay_auth_info auth = 4;
    message pay_auth_info { 
        required string pay_keys = 1;
        optional int64 update_time = 2;
    }
}
```
3. 单击【下一步】，系统将校验用户选定的表格定义文件，
 - 校验不通过，将返回错误，请根据错误提示修改文件后重新上传。
 - 校验通过，将显示文件中定义的表格元信息，请继续执行下一步。
4. 在配置表格页，勾选要创建的表格，输入容量、预留读和预留写参数，系统将自动计算表格每日的花费价格。
![](https://main.qcloudimg.com/raw/806bff2925169199c41d6714d48c4aff.png)
5. 确认表格信息无误后，单击【创建】，系统返回创建成功提示。
![](https://main.qcloudimg.com/raw/848fa7ec3a512c65fc5be0a7f606eb53.png)
