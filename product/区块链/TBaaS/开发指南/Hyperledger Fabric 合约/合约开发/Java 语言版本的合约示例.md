## 智能合约构成
Java 语言的智能合约代码，关键是在于实现以下接口：
```Java
/**
 * Defines methods that all chaincodes must implement.
 */
public interface Chaincode {
	/**
	 *Called during an instantiate transaction after the container has been 
	 *established, allowing the chaincode to initialize its internal data
	 */
	public Response init(ChaincodeStub stub);

	/**
	 *Called for every Invoke transaction. The chaincode may change its state 
	 *variables.
	 */
	public Response invoke(ChaincodeStub stub);
}
```
- 接口 init 主要是用于智能合约初始化和升级的时候调用这个接口，初始化相关的数据。
- 接口 invoke 主要是用于实现智能合约里的内部业务逻辑，用户可以根据需要，实现相关的业务。
- 在实现过程中，用户可以调用 ChaincodeStub 的 API 接口来和链上交互。



## 智能合约示例
### 基本示例
本示例以一个基本的智能合约用例为例，只包含智能合约的必须部分，没有实现任何业务逻辑。
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
Hyperledger Fabric 提供了很多官方的智能合约样例，具体请参考 [fabric 官方示例](https://github.com/hyperledger/fabric-samples/tree/release-1.4/chaincode/) 。本示例以 Hyperledger Fabric 官方提供的 chaincode_example02 样例为例。该示例的 init 函数用于初始化两个 key/value 键值对，invoke 函数用于根据不同业务逻辑进行细分调用，最终调用以下业务逻辑接口：
- invoke ：用于 key 之间的 value 转移。
- delete：删除一个键值对。
- query：查询 key 所对应的值。

#### init 函数示例
init 函数在智能合约实例化以及升级的时候会被调用。在实现 init 函数的过程中，可使用 [Java 语言版本的合约 API 列表](https://cloud.tencent.com/document/product/663/30530) 来对参数和账本进行操作。本例通过调用 API getFunction 和 getParameters 获取到用户输入参数。在获取用户输入参数后，通过调用 API putStringState 将数据写到账本中。具体代码如下：
```Java
	/*
	 * init函数用于初始化两个键值对，用户输入的参数为KEY1_NAME, VALUE1,
	 * KEY2_NAME, VALUE2
	 */
    @Override
    public Response init(ChaincodeStub stub) {
        try {
            _logger.info("Init java simple chaincode");
			// 调用API getFunction获取当前的输入函数
            String func = stub.getFunction();
            if (!func.equals("init")) {
                return newErrorResponse("function other than init is not supported");
            }
			// 调用API getParameters 获取用户输入参数
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
			// 调用API putStringState 把数据写入账本
            stub.putStringState(account1Key, args.get(1));
            stub.putStringState(account2Key, args.get(3));

            return newSuccessResponse();
        } catch (Throwable e) {
            return newErrorResponse(e);
        }
    }
```

#### invoke 函数示例
invoke 函数对用户的不同的智能合约业务逻辑进行拆分。本例通过调用 API getFunction 和 getParameters 获取到用户的具体业务类型和参数，根据用户的不同业务类型，分别调用不同的业务函数，如 invoke，delete 和 query 函数。具体代码如下：
```
	// invoke把用户调用的function细分到几个子function, 包含invoke, delete和query
    @Override
    public Response invoke(ChaincodeStub stub) {
        try {
            _logger.info("Invoke java simple chaincode");
			// 调用API getFunction和getParameters获取用户输入的业务类型和参数
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
```

#### 业务逻辑 invoke 函数示例
业务逻辑 invoke 函数主要用于实现业务逻辑中的资产转移。本例中通过调用 API getStringState 获取到 KEY 对应的资产总值，通过调用用户业务逻辑实现资产转移，通过调用 API putStringState 将用户最终资产写入账本。具体代码如下：
```
	// invoke实现两个键之间的value转移，输入为KEY1_NAME, KEY2_NAME，VALUE
    private Response invoke(ChaincodeStub stub, List<String> args) {
        if (args.size() != 3) {
            return newErrorResponse("Incorrect number of arguments. Expecting 3");
        }
        String accountFromKey = args.get(0);
        String accountToKey = args.get(1);
			
		// API getStringState获取对应账户的资产
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
		// 执行具体业务逻辑，这里对应资产进行转移
        if (amount > accountFromValue) {
            return newErrorResponse(String.format("not enough money in account %s", accountFromKey));
        }

        accountFromValue -= amount;
        accountToValue += amount;

        _logger.info(String.format("new value of A: %s", accountFromValue));
        _logger.info(String.format("new value of B: %s", accountToValue));

		// API putStringState将对应资产写入账本
        stub.putStringState(accountFromKey, Integer.toString(accountFromValue));
        stub.putStringState(accountToKey, Integer.toString(accountToValue));

        _logger.info("Transfer complete");

        return newSuccessResponse("invoke finished successfully", ByteString.copyFrom(accountFromKey + ": " + accountFromValue + " " + accountToKey + ": " + accountToValue, UTF_8).toByteArray());
    }
```

#### delete 函数示例
业务逻辑 delete 函数主要用于实现业务逻辑中的账户删除功能，本示例通过调用 API delState 删除对应账户。具体代码如下：
```
	// delete用于从账本中删除指定的键，输入为KEY_NAME
    // Deletes an entity from state
    private Response delete(ChaincodeStub stub, List<String> args) {
        if (args.size() != 1) {
            return newErrorResponse("Incorrect number of arguments. Expecting 1");
        }
        String key = args.get(0);
		// API delState删除特定的账户
        // Delete the key from the state in ledger
        stub.delState(key);
        return newSuccessResponse();
}
```

#### query 函数示例
业务逻辑 query 函数主要用于实现业务逻辑中账户查询功能，本示例通过调用 API getStringState 查询对应账户的资产。具体代码如下：
```
	// query主要是查询键对应的值，输入为KEY_NAME
    // query callback representing the query of a chaincode
    private Response query(ChaincodeStub stub, List<String> args) {
        if (args.size() != 1) {
            return newErrorResponse("Incorrect number of arguments. Expecting name of the person to query");
        }
        String key = args.get(0);
		// API getStringState查询特定的账户
        String val	= stub.getStringState(key);
        if (val == null) {
            return newErrorResponse(String.format("Error: state for %s is null", key));
        }
        _logger.info(String.format("Query Response:\nName: %s, Amount: %s\n", key, val));
        return newSuccessResponse(val, ByteString.copyFrom(val, UTF_8).toByteArray());
    }
```

