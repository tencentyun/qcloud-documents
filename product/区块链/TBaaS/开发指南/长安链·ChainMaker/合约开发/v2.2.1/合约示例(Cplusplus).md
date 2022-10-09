## 智能合约构成

ChainMaker C++ 语言的智能合约代码主要由以下接口构成：

```c++
#include "chainmaker/chainmaker.h"

using namespace chainmaker;

class Counter : public Contract {
public:
    void init_contract() {}
    void upgrade() {}
};
    
// 在创建本合约时，调用一次 init 方法。ChainMaker 不允许用户直接调用该方法。
WASM_EXPORT void init_contract() {
    // 安装时的业务逻辑，可为空
    
}

// 在升级本合约时，对于每一个升级的版本调用一次 upgrade 方法。ChainMaker 不允许用户直接调用该方法。
WASM_EXPORT void upgrade() {
    // 升级时的业务逻辑，可为空
    
}

// 对 SDK 暴露的函数
// 对外暴露 test1 方法，供用户由 SDK 调用
WASM_EXPORT void test1() {}
// 对外暴露 test2 方法，供用户由 SDK 调用
WASM_EXPORT void test2() {}
```

## 智能合约示例

### 存证合约示例
可实现如下功能：
1. 存储文件哈希、文件名称和时间等信息。
2. 通过文件哈希查询该条记录。

```c++
#include "chainmaker/chainmaker.h"

using namespace chainmaker;

class Counter : public Contract {
public:
    void init_contract() {}
    void upgrade() {}
    // 保存
    void save() {
        // 获取 SDK 接口上下文
        Context* ctx = context();
        // 定义变量
        std::string time;
        std::string file_hash;
        std::string file_name;
        std::string tx_id;
		// 获取参数
        ctx->arg("time", time);
        ctx->arg("file_hash", file_hash);
        ctx->arg("file_name", file_name);
        ctx->arg("tx_id", tx_id);
        // 发送合约事件
        // 向 topic:"topic_vx"发送 2 个 event 数据，file_hash,file_name
        ctx->emit_event("topic_vx",2,file_hash.c_str(),file_name.c_str());
		// 存储数据
        ctx->put_object("fact"+ file_hash,  tx_id+" "+time+" "+file_hash+" "+file_name);
        // 记录日志
        ctx->log("call save() result:" + tx_id+" "+time+" "+file_hash+" "+file_name);
        // 返回结果
        ctx->success(tx_id+" "+time+" "+file_hash+" "+file_name);
    }

    // 查询
    void find_by_file_hash() {
        // 获取 SDK 接口上下文
    	Context* ctx = context();

		// 获取参数
        std::string file_hash;
        ctx->arg("file_hash", file_hash);
		
        // 查询数据
    	std::string value;
        ctx->get_object("fact"+ file_hash, &value);
        // 记录日志
        ctx->log("call find_by_file_hash()-" + file_hash + ",result:" + value);
        // 返回结果
        ctx->success(value);
    }

};

// 在创建本合约时，调用一次 init 方法。ChainMaker 不允许用户直接调用该方法。
WASM_EXPORT void init_contract() {
    Counter counter;
    counter.init_contract();
}

// 在升级本合约时，对于每一个升级的版本调用一次 upgrade 方法。ChainMaker 不允许用户直接调用该方法。
WASM_EXPORT void upgrade() {
    Counter counter;
    counter.upgrade();
}

WASM_EXPORT void save() {
    Counter counter;
    counter.save();
}

WASM_EXPORT void find_by_file_hash() {
    Counter counter;
    counter.find_by_file_hash();
}
```

### 存证合约代码说明

<table>
<thead>
  <tr>
    <th>参数名称</th>
    <th>描述</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>init_contract</td>
    <td>合约的初始化函数，在合约部署时被调用，在本合约中为空。</td>
  </tr>
  <tr>
    <td>upgrade</td>
    <td>合约升级时调用的函数，在本合约中为空。</td>
  </tr>
  <tr>
    <td>save</td>
    <td>save 函数实现将文件哈希和文件名称记录到链上的功能。步骤如下：<br>1. save 函数先通过 [参数处理]API 接口 arg 函数拿到时间，文件哈希和文件名字等信息。<br>2. 通过调用 [其他辅助类]API 接口 emit_event 函数发送标识为 topic_vx 的合约事件。<br>3. 通过调用 [账本交互]API 接口 put_object 函数将文件等信息记录到链上。</td>
  </tr>
  <tr>
    <td>find_by_file_hash</td>
    <td>通过文件哈希查询该条记录。步骤如下：<br>1. find_by_file_hash 通过 context 和 [参数处理]API 接口 arg 函数拿到要查找的文件的文件哈希。<br>2. 通过 [账本交互]API 接口 get_object 函数获取文件的信息，通过 [其他辅助类]API 接口 log 函数和 success 函数记录相关日志并返回结果。</td>
  </tr>
</tbody>
</table>
