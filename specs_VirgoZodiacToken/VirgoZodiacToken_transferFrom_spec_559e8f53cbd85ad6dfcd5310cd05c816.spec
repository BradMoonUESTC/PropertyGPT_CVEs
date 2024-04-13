pragma solidity 0.6.12;

contract VirgoZodiacToken{address owner;
mapping(address => uint256) private balances;
mapping(address => mapping(address => uint256)) private allowed;
function transferFrom(address,address,uint256) public returns(bool) 
precondition{
_value != 0;
balances[_from] >= _value;
allowed[_from][msg.sender] >= _value;
balances[_to] + _value > balances[_to]; // Checking for overflow
}

postcondition{
balances[_from] == __old__(balances[_from]) - _value;
balances[_to] == __old__(balances[_to]) + _value;
allowed[_from][msg.sender] == __old__(allowed[_from][msg.sender]) - _value;
}
}