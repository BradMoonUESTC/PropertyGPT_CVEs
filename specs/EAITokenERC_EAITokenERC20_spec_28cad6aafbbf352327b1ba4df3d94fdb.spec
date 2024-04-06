pragma solidity 0.4.26;

contract EAI_TokenERC{string public name;
string public symbol;
uint8 public decimals = 8;
uint256 public totalSupply;
mapping (address => uint256) public balanceOf;
mapping (address => mapping (address => uint256)) public allowance;
function EAI_TokenERC20(uint256,string memory,string memory) public   
precondition{}

postcondition{
    totalSupply == __old__(totalSupply) + totalSupply;
    balanceOf[msg.sender] == __old__(balanceOf[msg.sender]) + totalSupply;
}
}