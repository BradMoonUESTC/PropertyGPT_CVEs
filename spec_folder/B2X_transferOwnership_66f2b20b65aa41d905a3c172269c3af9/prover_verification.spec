pragma solidity 0.4.26;

contract Owned {address public owner;

function transferOwnership(address) public  {}

rule OwnershipChangePreservesOwnerBeforeAfter() {
    address $newOwner;
    address ownerBefore = owner;
    transferOwnership($newOwner);
    address ownerAfter = owner;
    
    assert(ownerBefore != ownerAfter);
    assert(ownerAfter == $newOwner);
}}