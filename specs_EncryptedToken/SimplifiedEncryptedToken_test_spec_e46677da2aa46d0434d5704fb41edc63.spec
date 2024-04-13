pragma solidity 0.6.12;

contract SimplifiedEncryptedToken {address public owner;
uint256 public totalSupply;
uint256 public buyPrice;
mapping (address => uint256) public balanceOf;
uint256 public testVar;
function test(uint256) public   
precondition{
}

postcondition{
    __old__(testVar) != testVar;
}
}