pragma solidity 0.4.26;

contract Owned {address public owner;

function transferOwnership(address) public  {}

rule CheckOwnershipTransferEffectiveness() {
    address $newOwner;
    address $currentOwner = owner;
    
    transferOwnership($newOwner);

    assert(owner == $newOwner && owner != $currentOwner);
}}