pragma solidity 0.6.12;

contract BlocklancerToken{string public name = "Lancer Token";
string public symbol = "LNC";
uint8 public decimals = 18;
mapping(address => uint256) public balances;
mapping(address => mapping (address => uint256)) public allowed;
uint256 totalTokens;
function transferFrom(address,address,uint256) public returns(bool) 
precondition{
    balances[_from] >= _amount;
    allowed[_from][msg.sender] >= _amount;
    _amount > 0 && balances[_to] + _amount > balances[_to];
}

postcondition{
    balances[_from] == __old__(balances[_from]) - _amount;
    allowed[_from][msg.sender] == __old__(allowed[_from][msg.sender]) - _amount;
    balances[_to] == __old__(balances[_to]) + _amount;
}
}