



### Token 合约代码示例
Token 合约代码示例如下，实现功能 ERC20。
```solidity
/*
SPDX-License-Identifier: Apache-2.0
*/
pragma solidity >0.5.11;
contract Token {

    string public name = "token";      //  token name
    string public symbol = "TK";           //  token symbol
    uint256 public decimals = 6;            //  token digit

    mapping (address => uint256) public balanceOf;
    mapping (address => mapping (address => uint256)) public allowance;

    uint256 public totalSupply = 0;
    bool public stopped = false;

    uint256 constant valueFounder = 100000000000000000;
    address owner = address (0x0);

    modifier isOwner {
        assert (owner == msg.sender);
        _;
    }

    modifier isRunning {
        assert (!stopped);
        _;
    }

    modifier validAddress {
        assert (address (0x0) != msg.sender);
        _;
    }

    constructor (address _addressFounder) {
        owner = msg.sender;
        totalSupply = valueFounder;
        balanceOf [_addressFounder] = valueFounder;
        
        emit Transfer (address (0x0), _addressFounder, valueFounder);
    }

    function transfer (address _to, uint256 _value) public isRunning validAddress returns (bool success) {
        require (balanceOf [msg.sender] >= _value);
        require (balanceOf [_to] + _value >= balanceOf [_to]);
        balanceOf [msg.sender] -= _value;
        balanceOf [_to] += _value;
        emit Transfer (msg.sender, _to, _value);
        return true;
    }

    function transferFrom (address _from, address _to, uint256 _value) public isRunning validAddress returns (bool success) {
        require (balanceOf [_from] >= _value);
        require (balanceOf [_to] + _value >= balanceOf [_to]);
        require (allowance [_from][msg.sender] >= _value);
        balanceOf [_to] += _value;
        balanceOf [_from] -= _value;
        allowance [_from][msg.sender] -= _value;
        emit Transfer (_from, _to, _value);
        return true;
    }

    function approve (address _spender, uint256 _value) public isRunning validAddress returns (bool success) {
        require (_value == 0 || allowance [msg.sender][_spender] == 0);
        allowance [msg.sender][_spender] = _value;
        emit Approval (msg.sender, _spender, _value);
        return true;
    }

    function stop () public isOwner {
        stopped = true;
    }

    function start () public isOwner {
        stopped = false;
    }

    function setName (string memory _name) public isOwner {
        name = _name;
    }

    function burn (uint256 _value) public {
        require (balanceOf [msg.sender] >= _value);
        balanceOf [msg.sender] -= _value;
        balanceOf [address (0x0)] += _value;
        emit Transfer (msg.sender, address (0x0), _value);
    }

    event Transfer (address indexed _from, address indexed _to, uint256 _value);
    event Approval (address indexed _owner, address indexed _spender, uint256 _value);
}
```


### Token 合约代码说明


- constructor：合约构造函数，在合约部署时被调用，将 `_addressFounder` 的余额设置为 `valueFounder`。
- transfer：转账函数，该函数具有两个入参，接收者地址 `_to` 和转账金额 `_value`，该函数将调用者 `msg.sender` 的余额减去 `_value`，将接收者的余额加上 `_value`。
- transferFrom：转账函数，该函数具有三个入参，转账者地址 `_from`，接收者地址 `_to` 和转账金额 `_value`，该函数将转账者 `_from` 的余额减去 `_value`，将接收者的余额加上 `_value`。
- approve：批准函数，该函数具有两个入参，接收者地址 `_spender` 和 token 数量 `_value`，该函数将接收者 `_spender` 可以从调用者 `msg.sender` 处转出的 token 数量设置为 `_value`。
- stop：停止函数，该函数执行后，`transfer`，`transferFrom` 和 `approve` 函数将不能再被执行。
- start：启动函数，该函数执行后，`transfer`，`transferFrom` 和 `approve` 函数将可以再被执行。
- setName：设置 token 名字函数，该函数具有一个入参 `_name`，将 token 的名字设置为 `_name`。
- burn：销毁函数，该函数具有一个入参 `_value`，将调用者 `msg.sender` 的余额减去 `_value`。

