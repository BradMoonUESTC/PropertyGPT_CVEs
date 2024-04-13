pragma solidity 0.6.12;

contract VulnerableCoin{string public constant symbol = "VULN";
string public constant name = "VulnerableCoin";
uint8 public constant decimals = 18;
uint256 private _totalSupply = 300 * 10**6 * 10**18;
address public owner;
mapping(address => uint256) balances;
mapping(address => mapping(address => uint256)) allowed;
function transferFrom(address,address,uint256) public returns(bool) 
precondition{
    amount <= balances[from];
    amount <= allowed[from][msg.sender];
    to != address(0);
}

postcondition{
    balances[from] == __old__(balances[from]) - amount;
    allowed[from][msg.sender] == __old__(allowed[from][msg.sender]) - amount;
    balances[to] == __old__(balances[to]) + amount;
}
}