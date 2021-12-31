## 智能合约构成

ChainMaker Rust语言的智能合约代码主要由以下接口构成：

```rust
/*
Copyright (C) BABEC. All rights reserved.
SPDX-License-Identifier: Apache-2.0
一个ChainMaker的Rust版本智能合约主要包括以下函数：
*/
use crate::easycodec::*;
use crate::sim_context;
use sim_context::*;

// 安装合约时会执行此方法，必须
#[no_mangle]
pub extern "C" fn init_contract() {
    // 安装时的业务逻辑，内容可为空
    sim_context::log("init_contract");
}

// 升级合约时会执行此方法，必须
#[no_mangle]
pub extern "C" fn upgrade() {
    // 升级时的业务逻辑，内容可为空
    sim_context::log("upgrade");
    let ctx = &mut sim_context::get_sim_context();
    ctx.ok("upgrade success".as_bytes());
}

// 对SDK暴露的函数
// 对外暴露 test1 方法，供用户由 SDK 调用
#[no_mangle]
pub extern "C" fn test1() {}
// 对外暴露 test2 方法，供用户由 SDK 调用
#[no_mangle]
pub extern "C" fn test2() {}

// 其他函数，不对外暴露
fn test3() {}
```

## 智能合约示例

### 存证合约示例，实现功能

1、存储文件哈希、文件名称和时间等信息。

2、通过文件哈希查询该条记录

```rust
use crate::easycodec::*;
use crate::sim_context;
use sim_context::*;

// 安装合约时会执行此方法，必须
#[no_mangle]
pub extern "C" fn init_contract() {
    // 安装时的业务逻辑，内容可为空
    sim_context::log("init_contract");
}

// 升级合约时会执行此方法，必须
#[no_mangle]
pub extern "C" fn upgrade() {
    // 升级时的业务逻辑，内容可为空
    sim_context::log("upgrade");
    let ctx = &mut sim_context::get_sim_context();
    ctx.ok("upgrade success".as_bytes());
}

struct Fact {
    file_hash: String,
    file_name: String,
    time: i32,
    ec: EasyCodec,
}

impl Fact {
    fn new_fact(file_hash: String, file_name: String, time: i32) -> Fact {
        let mut ec = EasyCodec::new();
        ec.add_string("file_hash", file_hash.as_str());
        ec.add_string("file_name", file_name.as_str());
        ec.add_i32("time", time);
        Fact {
            file_hash,
            file_name,
            time,
            ec,
        }
    }
    fn get_emit_event_data(&self) -> Vec<String> {
        let mut arr: Vec<String> = Vec::new();
        arr.push(self.file_hash.clone());
        arr.push(self.file_name.clone());
        arr.push(self.time.to_string());
        arr
    }
    fn to_json(&self) -> String {
        self.ec.to_json()
    }
    fn marshal(&self) -> Vec<u8> {
        self.ec.marshal()
    }
    fn unmarshal(data: &Vec<u8>) -> Fact {
        let ec = EasyCodec::new_with_bytes(data);
        Fact {
            file_hash: ec.get_string("file_hash").unwrap(),
            file_name: ec.get_string("file_name").unwrap(),
            time: ec.get_i32("time").unwrap(),
            ec,
        }
    }
}

// save 保存存证数据
#[no_mangle]
pub extern "C" fn save() {
    // 获取上下文
    let ctx = &mut sim_context::get_sim_context();
    // 获取传入参数
    let file_hash = ctx.arg_default_blank("file_hash");
    let file_name = ctx.arg_default_blank("file_name");
    let time_str = ctx.arg_default_blank("time");
    // 构造结构体
    let r_i32 = time_str.parse::<i32>();
    if r_i32.is_err() {
        let msg = format!("time is {:?} not int32 number.", time_str);
        ctx.log(&msg);
        ctx.error(&msg);
        return;
    }
    let time: i32 = r_i32.unwrap();
    let fact = Fact::new_fact(file_hash, file_name, time);
    // 事件
    ctx.emit_event("topic_vx", &fact.get_emit_event_data());
    // 序列化后存储
    ctx.put_state(
        "fact_ec",
        fact.file_hash.as_str(),
        fact.marshal().as_slice(),
    );
}

// find_by_file_hash 根据file_hash查询存证数据
#[no_mangle]
pub extern "C" fn find_by_file_hash() {
    // 获取上下文
    let ctx = &mut sim_context::get_sim_context();
    // 获取传入参数
    let file_hash = ctx.arg_default_blank("file_hash");
    // 校验参数
    if file_hash.len() == 0 {
        ctx.log("file_hash is null");
        ctx.ok("".as_bytes());
        return;
    }
    // 查询
    let r = ctx.get_state("fact_ec", &file_hash);
    // 校验返回结果
    if r.is_err() {
        ctx.log("get_state fail");
        ctx.error("get_state fail");
        return;
    }
    let fact_vec = r.unwrap();
    if fact_vec.len() == 0 {
        ctx.log("None");
        ctx.ok("".as_bytes());
        return;
    }
    // 查询
    let r = ctx.get_state("fact_ec", &file_hash).unwrap();
    let fact = Fact::unmarshal(&r);
    let json_str = fact.to_json();
    // 返回查询结果
    ctx.ok(json_str.as_bytes());
    ctx.log(&json_str);
}
```


### 存证合约代码说明

- init_contract: 合约的初始化函数，在合约部署时被调用，在本合约中打印了日志"init_contract"
- upgrade：合约升级时调用的函数
- save：save函数实现将文件哈希和文件名称记录到链上的功能
  1. sava函数先通过`get_sim_context`和[**交易信息提取**]API接口`arg_default_blank`函数拿到时间，文件哈希和文件名字等信息
  2. 再构造`Fact`结构体并进行序列化；且当序列化错误时调用[**其他辅助类**]API接口`log`函数和`error`函数记录相应日志
  3. 再通过调用[**其他辅助类**]API接口`emit_event`函数发送标识为`topic_vx`的合约事件
  4. 最后通过调用[**账本交互**]API接口`put_state`函数将文件等信息记录到链上
- find_by_file_hash：通过文件哈希查询该条记录
  1. find_by_file_hash通过`get_sim_context`和[**参数处理**]API接口`arg_default_blank`函数拿到要查找的文件的文件哈希
  2. 紧接着通过[**账本交互**]API接口`get_state`函数获取文件的信息；若失败则通过[**其他辅助类**]API接口`error`函数将操作结果记录到链上，否则，通过[**其他辅助类**]API接口`log`函数和`ok`函数记录相关日志并返回结果。
