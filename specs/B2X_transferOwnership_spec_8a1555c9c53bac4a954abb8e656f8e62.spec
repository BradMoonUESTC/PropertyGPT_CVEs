pragma solidity 0.4.26;

contract Owned {address public owner;

function transferOwnership(address) public  {}

rule OwnershipTransferEffect() {
    address $newOwner;
    address initialOwner = owner;
    transferOwnership($newOwner);

    assert(owner == $newOwner);
}}