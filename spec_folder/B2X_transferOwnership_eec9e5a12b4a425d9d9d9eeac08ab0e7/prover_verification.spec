pragma solidity 0.4.26;

contract Owned {address public owner;

function transferOwnership(address) public  {}

rule OwnershipTransferWithCorrectOwner() {
    address $newOwner;
    address $initialOwner = owner;
    require(msg.sender == $initialOwner);
    
    transferOwnership($newOwner);

    assert(owner == $newOwner);
}}