## 智能合约构成
Java 语言的智能合约代码，关键是在于实现以下的接口：
```Java
/**
* Defines methods that all chaincodes must implement.
*/
public interface Chaincode {
	/**
	 *Called during an instantiate transaction after the container has been 
	 *established, allowing the chaincode to initialize its internal data
	 */
	public Response init(ChaincodeStub stub)

	/**
	 *Called for every Invoke transaction. The chaincode may change its state 
	 *variables.
	 */
	public Response Invoke(ChaincodeStub stub)
}
```
- 接口 Init 主要是用于智能合约初始化和升级的时候调用这个接口，初始化相关的数据。
- 接口 Invoke 主要是用于实现智能合约里的内部业务逻辑，用户可以根据需要，实现自己相关的业务。
- 在实现过程中，用户可以调用 ChaincodeStub 的 API 接口来和链上交互。

## 智能合约示例
### 基本示例
以下是一个基本的智能合约用例，没有实现任何业务逻辑，只包含智能合约的必须部分。
```Java
/*
 * SimpleAssetDemo implements a simple chaincode to manage an asset
 */
public class SimpleAssetDemo extends ChaincodeBase {
	/*
	 * Init is called during chaincode instantiation to initialize any data.
	 */
    @Override
	public Response init(ChaincodeStub stub) {
	}

	/*
		 * Invoke is called per transaction on the chaincode. Each transaction is
		 * either a 'get' or a 'set' on the asset created by Init function. The 'set'
		 * method may create a new asset by specifying a new key-value pair.
	 */
    @Override
	public Response invoke(ChaincodeStub stub) {
	}

    public static void main(String[] args) {
        new SimpleAssetDemo().start(args);
	}
}
```

### 官方示例
Hyperledger Fabric 提供了很多官方的智能合约样例，具体可以访问以下网址获取 [fabric官方示例](https://github.com/hyperledger/fabric-samples/tree/release-1.4/chaincode/) 。下面我们主要展示 Hyperledger Fabric 官方提供的一个示例  chaincode_example02。 该例的 Init 函数用于初始化两个 key/value 键值对，同时提供以下接口：
- invoke ：用于key 之间的 value 转移。
- delete：删除一个键值对。
- query：查询 key 所对应的值。

```Java
/*
Copyright IBM Corp., DTCC All Rights Reserved.

SPDX-License-Identifier: Apache-2.0
*/
package org.hyperledger.fabric.example;

import java.util.List;

import com.google.protobuf.ByteString;
import io.netty.handler.ssl.OpenSsl;
import org.apache.commons.logging.Log;
import org.apache.commons.logging.LogFactory;
import org.hyperledger.fabric.shim.ChaincodeBase;
import org.hyperledger.fabric.shim.ChaincodeStub;

import static java.nio.charset.StandardCharsets.UTF_8;

public class SimpleChaincode extends ChaincodeBase {

    private static Log _logger = LogFactory.getLog(SimpleChaincode.class);

	/*
	 * Init函数用于初始化两个键值对，用户输入的参数为KEY1_NAME, VALUE1,
	 * KEY2_NAME, VALUE2
	 */
    @Override
    public Response init(ChaincodeStub stub) {
        try {
            _logger.info("Init java simple chaincode");
            String func = stub.getFunction();
            if (!func.equals("init")) {
                return newErrorResponse("function other than init is not supported");
            }
            List<String> args = stub.getParameters();
            if (args.size() != 4) {
                newErrorResponse("Incorrect number of arguments. Expecting 4");
            }
            // Initialize the chaincode
            String account1Key = args.get(0);
            int account1Value = Integer.parseInt(args.get(1));
            String account2Key = args.get(2);
            int account2Value = Integer.parseInt(args.get(3));

            _logger.info(String.format("account %s, value = %s; account %s, value %s", account1Key, account1Value, account2Key, account2Value));
            stub.putStringState(account1Key, args.get(1));
            stub.putStringState(account2Key, args.get(3));

            return newSuccessResponse();
        } catch (Throwable e) {
            return newErrorResponse(e);
        }
    }
	//Invoke把用户调用的function细分到几个子function, 包含invoke, delete和query
    @Override
    public Response invoke(ChaincodeStub stub) {
        try {
            _logger.info("Invoke java simple chaincode");
            String func = stub.getFunction();
            List<String> params = stub.getParameters();
            if (func.equals("invoke")) {
                return invoke(stub, params);
            }
            if (func.equals("delete")) {
                return delete(stub, params);
            }
            if (func.equals("query")) {
                return query(stub, params);
            }
            return newErrorResponse("Invalid invoke function name. Expecting one of: [\"invoke\", \"delete\", \"query\"]");
        } catch (Throwable e) {
            return newErrorResponse(e);
        }
    }
	//invoke实现两个键之间的value转移，输入为KEY1_NAME, KEY2_NAME，VALUE
    private Response invoke(ChaincodeStub stub, List<String> args) {
        if (args.size() != 3) {
            return newErrorResponse("Incorrect number of arguments. Expecting 3");
        }
        String accountFromKey = args.get(0);
        String accountToKey = args.get(1);

        String accountFromValueStr = stub.getStringState(accountFromKey);
        if (accountFromValueStr == null) {
            return newErrorResponse(String.format("Entity %s not found", accountFromKey));
        }
        int accountFromValue = Integer.parseInt(accountFromValueStr);

        String accountToValueStr = stub.getStringState(accountToKey);
        if (accountToValueStr == null) {
            return newErrorResponse(String.format("Entity %s not found", accountToKey));
        }
        int accountToValue = Integer.parseInt(accountToValueStr);

        int amount = Integer.parseInt(args.get(2));

        if (amount > accountFromValue) {
            return newErrorResponse(String.format("not enough money in account %s", accountFromKey));
        }

        accountFromValue -= amount;
        accountToValue += amount;

        _logger.info(String.format("new value of A: %s", accountFromValue));
        _logger.info(String.format("new value of B: %s", accountToValue));

        stub.putStringState(accountFromKey, Integer.toString(accountFromValue));
        stub.putStringState(accountToKey, Integer.toString(accountToValue));

        _logger.info("Transfer complete");

        return newSuccessResponse("invoke finished successfully", ByteString.copyFrom(accountFromKey + ": " + accountFromValue + " " + accountToKey + ": " + accountToValue, UTF_8).toByteArray());
    }
	//Delete用于从账本中删除指定的键，输入为KEY_NAME
    // Deletes an entity from state
    private Response delete(ChaincodeStub stub, List<String> args) {
        if (args.size() != 1) {
            return newErrorResponse("Incorrect number of arguments. Expecting 1");
        }
        String key = args.get(0);
        // Delete the key from the state in ledger
        stub.delState(key);
        return newSuccessResponse();
    }
	//query主要是查询键对应的值，输入为KEY_NAME
    // query callback representing the query of a chaincode
    private Response query(ChaincodeStub stub, List<String> args) {
        if (args.size() != 1) {
            return newErrorResponse("Incorrect number of arguments. Expecting name of the person to query");
        }
        String key = args.get(0);
        //byte[] stateBytes
        String val	= stub.getStringState(key);
        if (val == null) {
            return newErrorResponse(String.format("Error: state for %s is null", key));
        }
        _logger.info(String.format("Query Response:\nName: %s, Amount: %s\n", key, val));
        return newSuccessResponse(val, ByteString.copyFrom(val, UTF_8).toByteArray());
    }

    public static void main(String[] args) {
        System.out.println("OpenSSL avaliable: " + OpenSsl.isAvailable());
        new SimpleChaincode().start(args);
    }

}


```
