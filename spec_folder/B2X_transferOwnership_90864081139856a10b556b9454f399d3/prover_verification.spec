pragma solidity 0.4.26;

contract Owned {address public owner;

function transferOwnership(address) public  {}

rule OwnershipTransferWithEnforcedOwnerChange() {
    address $newOwner;
    address initialOwner = owner;
    require(initialOwner != $newOwner);

    transferOwnership($newOwner);

    assert(owner == $newOwner);
}}