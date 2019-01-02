TcaplusDB 使用 Google Protobuf 文件定义业务数据表，支持 proto2 和 proto3 的语法规范，以下是 proto 建表文件的规则描述。

## proto2 加表文件规范

以下是一个符合 proto2 语法规范的加表文件示例。

```
syntax = "proto2";                      // 指明符合proto2语法规范
package myTcaplusTable;                 // 自定义包名

import "tcaplusservice.optionv1.proto"; // 这个文件定义了Tcaplus表的一些公共信息，需要在您的表定义中被引用(import)

message tb_example {  //使用message定义表，message名即表名

    // 必须是指定了主键选项（tcaplusservice.tcaplus_primary_key）的message才能被识别为一张TcaplusDB业务数据表，否则此message只是一个结构体
    // 主键选项指定了主键字段名列表，字段名用逗号分割，最多四个字段能够被指定为主键
    option(tcaplusservice.tcaplus_primary_key) = "uin,name,region";

    // tcaplusservice.tcaplus_index选项指定Tcaplus索引
    // 每个索引所包含的索引键必须是主键，并且所有索引字段集合的交集不能为空
    option(tcaplusservice.tcaplus_index) = "index_1(uin,region)";
    option(tcaplusservice.tcaplus_index) = "index_2(uin,name)";

    //option(tcaplusservice.tcaplus_sharding_key) = "uin"; 用户可以自己显式设置索引分片键，原则是索引分片键必须是所有索引键字段交集的子集。如果用户不显式设置，那系统将默认采用索引键集合的交集作为分片键。

    option(tcaplusservice.tcaplus_field_cipher_suite) = "DefaultAesCipherSuite"; // 使用默认的DefaultAesCipherSuite加密函数，非必须设置选项
    option(tcaplusservice.tcaplus_cipher_md5)= "62fee3b53619b7f303c939964c6f2c4b"; //设置加密密码字符串的md5值，非必须设置选项

    // 接下来是表的字段定义
    // Tcaplus 表支持以下的数据类型：
    // 非嵌套类型：int32, int64, uint32, uint64, sint32, sint64, bool, fixed64, sfixed64, double, fixed32, sfixed32, float, string, bytes
    // 嵌套类型：message
    // Tcaplus支持REQUIRED, OPTIONAL和REPEATED作为字段修饰符

    // 主键字段 (最多4个)
    required int64 uin = 1;  // 主键字段必须被required类型修饰，并且不能是嵌套类型
    required string name = 2[(tcaplusservice.tcaplus_crypto) = true]; //message中string和bytes类型的字段可以指定为加密字段，非必须设置选项
    required int32 region = 3;
    // 一张表最多只能包含4个主键字段

    // 普通值字段
    required int32 gamesvrid = 4; // 普通字段可以被required,optional或repeated类型修饰
    optional int32 logintime = 5 [default = 1];
    repeated int64 lockid = 6 [packed = true]; // repeated修饰的字段需要指定packed=true选项
    optional bool is_available = 7 [default = false]; //optional类型字段可以指定默认值
    optional pay_info pay = 8; // 值字段的类型可以是自定义的结构体类型
}

message pay_info { //使用message定义结构体

    required int64 pay_id = 1;
    optional uint64 total_money = 2;
    optional uint64 pay_times = 3;
    optional pay_auth_info auth = 4;

    message pay_auth_info { // 结构体类型支持嵌套定义
        required string pay_keys = 1;
        optional int64 update_time = 2;
    }
}
```

加表文件规则：
* TcaplusDB proto 表定义文件必须符合 protobuf 语法规范，在文件头用`syntax = "proto2";`标识。
* 加表文件必须引用`tcaplusservice.optionv1.proto`公共定义文件。
* 使用 message 定义表和普通结构体，如果 message 中包含`tcaplusservice.tcaplus_primary_key`选项，则此 message 是一个 TcaplusDB 业务数据表定义，否则此 message 只是一个结构体定义。
* TcaplusDB 表支持定义 int32，int64，uint32，uint64，sint32，sint64，bool，fixed64，sfixed64，double，fixed32，sfixed32，float，string，bytes 非嵌套类型字段，以及 message 嵌套类型字段。
* TcaplusDB 表支持 REQUIRED，OPTIONAL 和 REPEATED 作为字段修饰符。
* TcaplusDB 表的主键是1至4个 REQUIRED 非嵌套类型字段，通过`tcaplusservice.tcaplus_primary_key`选项指定，该选项的值为主键字段名列表字符串，各主键字段用逗号分隔，如：`option(tcaplusservice.tcaplus_primary_key) = "uin,name,region"; `。
* TcaplusDB 单个表支持创建0至4个索引，通过`tcaplusservice.tcaplus_index`选项指定，例如：`option(tcaplusservice.tcaplus_index) = "index_1(uin,region)";` 其中 “index_1” 是自定义的索引名称，"uin,region" 是通过逗号分隔的指定索引键字段名列表。
* TcaplusDB 表的索引键必须是主键，如果定义多个索引键，那么多个索引键集合的交集不能为空。
* 用户可以通过`tcaplusservice.tcaplus_sharding_key`选项显式设置分片键，原则是分片键必须是所有索引键字段交集的子集。如果用户不显式设置，那系统将默认采用索引键集合的交集作为分片键。分片键的设置与后台数据分布相关，用户需要评估作为分片键的字段取值是否离散，取值有限的字段如性别，星期等都不建议设置为分片键。
* TcaplusDB 表最多包含4个主键字段以及128个非主键字段。
* 支持定义嵌套的结构体类型非主键字段，嵌套深度最深支持30层，嵌套深度太深将会影响数据访问性能。
* 单条 TcaplusDB 数据记录最大支持256KB。
* REPEATED 类型字段必须指定 [packed=true]。
* TcaplusDB 表定义中，string 和 bytes 类型的字段可以指定为加密字段，TcaplusAPI 将使用`tcaplusservice.tcaplus_field_cipher_suite`选项指定的加密工具，和用户指定的密码对设置了`[(tcaplusservice.tcaplus_crypto) = true]`选项的字段进行加密传输和存储。

## proto3 加表文件规范

```
syntax = "proto3";                      // 指明符合proto3语法规范
package myTcaplusTable;                 // 自定义包名

import "tcaplusservice.optionv1.proto"; // 这个文件定义了Tcaplus表的一些公共信息，需要在您的表定义中被引用(import)

message tb_example {  //使用message定义表，message名即表名

    // 必须是指定了主键选项（tcaplusservice.tcaplus_primary_key）的message才能被识别为一张TcaplusDB业务数据表，否则此message只是一个结构体
    // 主键选项指定了主键字段名列表，字段名用逗号分割，最多四个字段能够被指定为主键
    option(tcaplusservice.tcaplus_primary_key) = "uin,name,region";

    // tcaplusservice.tcaplus_index选项指定Tcaplus索引
    // 每个索引所包含的索引键必须是主键，并且所有索引字段集合的交集不能为空
    option(tcaplusservice.tcaplus_index) = "index_1(uin,region)";
    option(tcaplusservice.tcaplus_index) = "index_2(uin,name)";

    //option(tcaplusservice.tcaplus_sharding_key) = "uin"; 用户可以自己显式设置索引分片键，原则是索引分片键必须是所有索引键字段交集的子集。如果用户不显式设置，那系统将默认采用索引键集合的交集作为分片键。

    option(tcaplusservice.tcaplus_field_cipher_suite) = "DefaultAesCipherSuite"; // 使用默认的DefaultAesCipherSuite加密函数，非必须设置选项
    option(tcaplusservice.tcaplus_cipher_md5)= "62fee3b53619b7f303c939964c6f2c4b"; //设置加密密码字符串的md5值，非必须设置选项

    // 接下来是表的字段定义
    // Tcaplus 表支持以下的数据类型：
    // 非嵌套类型：int32, int64, uint32, uint64, sint32, sint64, bool, fixed64, sfixed64, double, fixed32, sfixed32, float, string, bytes
    // 嵌套类型：message

    // 主键字段 (最多4个)
    int64 uin = 1;  // 主键字段必须是非嵌套类型
    string name = 2[(tcaplusservice.tcaplus_crypto) = true]; //message中string和bytes类型的字段可以指定为加密字段，非必须设置选项
    int32 region = 3;
    // 一张表最多只能包含4个主键字段

    // 普通值字段
    int32 gamesvrid = 4;
    int32 logintime = 5;
    int64 lockid = 6;
    bool is_available = 7;
    pay_info pay = 8; // 值字段的类型可以是自定义的结构体类型
}

message pay_info { //使用message定义结构体

    int64 pay_id = 1;
    uint64 total_money = 2;
    uint64 pay_times = 3;
    pay_auth_info auth = 4;

    message pay_auth_info { // 结构体类型支持嵌套定义
        string pay_keys = 1;
        int64 update_time = 2;
    }
}
```

加表文件规则：
* TcaplusDB proto 表定义文件必须符合 protobuf 语法规范，在文件头用`syntax = "proto3";`标识。
* 加表文件必须引用`tcaplusservice.optionv1.proto`公共定义文件。
* 使用 message 定义表和普通结构体，如果 message 中 包含`tcaplusservice.tcaplus_primary_key`选项，则此 message 是一个 TcaplusDB 业务数据表定义，否则此 message 只是一个结构体定义。
* TcaplusDB 表支持定义 int32，int64，uint32，uint64，sint32，sint64，bool，fixed64，sfixed64，double，fixed32，sfixed32，float，string，bytes 非嵌套类型字段，以及 message 嵌套类型字段。
* TcaplusDB 表的主键是1至4个非嵌套类型字段，通过`tcaplusservice.tcaplus_primary_key`选项指定，该选项的值为主键字段名列表的字符串，各主键字段用逗号分隔，如：`option(tcaplusservice.tcaplus_primary_key) = "uin,name,region";` 。
* TcaplusDB 单个表支持创建0至4个索引，通过`tcaplusservice.tcaplus_index`选项指定，例如：`option(tcaplusservice.tcaplus_index) = "index_1(uin,region)";` 其中 “index_1” 是自定义的索引名称，"uin,region" 是通过逗号分隔的指定索引键字段名列表。
* TcaplusDB 表的索引键必须是主键，如果定义多个索引键，那么多个索引键集合的交集不能为空。
* 用户可以通过`tcaplusservice.tcaplus_sharding_key`选项显式设置分片键，原则是分片键必须是所有索引键字段交集的子集。如果用户不显式设置，那系统将默认采用索引键集合的交集作为分片键。分片键的设置与后台数据分布相关，用户需要评估作为分片键的字段取值是否离散，取值有限的字段如性别，星期等都不建议设置为分片键。
* TcaplusDB 表最多包含4个主键字段以及128个非主键字段。
* 支持定义嵌套的结构体类型非主键字段，嵌套深度最深支持30层，嵌套深度太深将会影响数据访问性能。
* 单条 TcaplusDB 数据记录最大支持256KB。
* TcaplusDB 表定义中，string 和 bytes 类型的字段可以指定为加密字段，TcaplusAPI 将使用`tcaplusservice.tcaplus_field_cipher_suite`选项指定的加密工具，和用户指定的密码对设置了`[(tcaplusservice.tcaplus_crypto) = true]`选项的字段进行加密传输和存储。


## tcaplusservice.tcaplus_* 选项说明

TcaplusDB 的表定义文件在 protobuf 语法基础上通过 option 进行扩展，实现更丰富的语义功能，在此做一下总结。

| 选项名称 | 功能说明 | 设置示例 | 是否必填 |
| --- | --- | --- | --- |
| tcaplus_primary_key | 设置 TcaplusDB 表主键字段 | option(tcaplusservice.tcaplus_primary_key) = "uin,name,region"; | 是 |
| tcaplus_index | 设置 TcaplusDB 表索引键字段 | option(tcaplusservice.tcaplus_index) = "index_1(uin,region)"; | 否 |
| tcaplus_sharding_key | 在设置了表索引键的前提下，用户可以自定义表分片键 | option(tcaplusservice.tcaplus_sharding_key) = "uin"; | 否 |
| tcaplus_field_cipher_suite | 如果需要使用字段加密功能，需要设置，如果用户需要指定自己的加密算法，请参考 API 中的例子 | option(tcaplusservice.tcaplus_field_cipher_suite) = "DefaultAesCipherSuite"; | 否 |
| tcaplus_cipher_md5 | 如果需要使用字段加密功能，需要设置用户侧保存加密密码字符串的 MD5 | option(tcaplusservice.tcaplus_cipher_md5)= "62fee3b53619b7f303c939964c6f2c4b"; | 否 |


