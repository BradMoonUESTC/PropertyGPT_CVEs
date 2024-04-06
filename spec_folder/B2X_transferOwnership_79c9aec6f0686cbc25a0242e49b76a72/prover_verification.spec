pragma solidity 0.4.26;

contract Owned {address public owner;

function transferOwnership(address) public  {}

rule ValidateTransferOwnershipEffect() {
    address $newOwner;
    address $originalOwner = owner;
    require($newOwner != $originalOwner);

    transferOwnership($newOwner);

    assert(owner == $newOwner);
}}