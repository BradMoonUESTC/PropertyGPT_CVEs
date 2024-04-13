// SPDX-License-Identifier: MIT
pragma solidity 0.6.12;

contract BlocklancerToken {
    string public name = "Lancer Token";
    string public symbol = "LNC";
    uint8 public decimals = 18;

    mapping(address => uint256) public balances;
    mapping(address => mapping (address => uint256)) public allowed;

    uint256 totalTokens;

    event Transfer(address indexed _from, address indexed _to, uint256 _value);
    event Approval(address indexed _owner, address indexed _spender, uint256 _value);

    constructor() public {
        // Initial setup can go here
    }

    function addToken(address invest, uint256 value) external {
        // This should have access control in real use cases
        balances[invest] += value;
        totalTokens += value;
        emit Transfer(address(0), invest, value);
    }

    function transferFrom(address _from, address _to, uint256 _amount) external returns (bool success) {
        require(balances[_from] >= _amount, "Insufficient balance");
        require(allowed[_from][msg.sender] >= _amount, "Insufficient allowance");
        require(_amount > 0 && balances[_to] + _amount > balances[_to], "Invalid amount");

        balances[_from] -= _amount;
        allowed[_from][msg.sender] -= _amount;
        balances[_to] += _amount;
        emit Transfer(_from, _to, _amount);
        return true;
    }

    function totalSupply() public view returns (uint256) {
        return totalTokens;
    }

    function balanceOf(address _owner) public view returns (uint256 balance) {
        return balances[_owner];
    }

    function transfer(address _to, uint256 _value) public returns (bool success) {
        require(balances[msg.sender] >= _value, "Insufficient balance");
        balances[msg.sender] -= _value;
        balances[_to] += _value;
        emit Transfer(msg.sender, _to, _value);
        return true;
    }

    function approve(address _spender, uint256 _value) public returns (bool success) {
        allowed[msg.sender][_spender] = _value;
        emit Approval(msg.sender, _spender, _value);
        return true;
    }

    function allowance(address _owner, address _spender) public view returns (uint256 remaining) {
        return allowed[_owner][_spender];
    }
}
