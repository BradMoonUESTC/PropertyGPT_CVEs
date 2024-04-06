pragma solidity 0.4.26;

contract Owned {address public owner;

function transferOwnership(address) public  {}

rule OwnershipTransferCorrectness() {
    address $newOwner;
    address $currentOwner = owner;
    require($newOwner != $currentOwner);

    transferOwnership($newOwner);

    assert(owner == $newOwner);
}}