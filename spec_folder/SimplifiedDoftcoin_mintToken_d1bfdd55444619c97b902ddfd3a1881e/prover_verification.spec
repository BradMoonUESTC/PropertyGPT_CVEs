pragma solidity 0.4.26;

contract SimplifiedDoftcoin{string public name = "Doftcoin";
string public symbol = "DFC";
uint256 public decimals = 18;
uint256 public totalSupply;
mapping (address => uint256) public balanceOf;
address public owner;
function mintToken(address,uint256) public   
precondition{
    _target != address(0) ? true : false;
}

postcondition{
    totalSupply == __old__(totalSupply) + _mintedAmount ? true : false;
    balanceOf[_target] == __old__(balanceOf[_target]) + _mintedAmount ? true : false;
}
}