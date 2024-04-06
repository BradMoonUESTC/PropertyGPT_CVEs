pragma solidity 0.4.26;

contract EAI_TokenERC{string public name;
string public symbol;
uint8 public decimals = 8;
uint256 public totalSupply;
mapping (address => uint256) public balanceOf;
mapping (address => mapping (address => uint256)) public allowance;
function transferFrom(address,address,uint256) public returns(bool) 
precondition{
    _value <= allowance[_from][msg.sender];
}

postcondition{
    __old__(allowance[_from][msg.sender]) - _value == allowance[_from][msg.sender];
}
}