pragma solidity 0.6.12;

contract VulnerableWallet{address public owner;
mapping(address => address) private sweepers;
function sweep(address,uint256) public returns(bool) 
precondition{sweepers[_token] != address(0)}

postcondition{}
}