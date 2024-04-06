pragma solidity 0.4.26;

contract Owned{address public owner;
function transferOwnership(address) public   
precondition{
    __old__(owner) != owner;
}

postcondition{
    owner == owner;
}
}