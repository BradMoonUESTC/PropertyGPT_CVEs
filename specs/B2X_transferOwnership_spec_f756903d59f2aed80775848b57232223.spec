pragma solidity 0.4.26;

contract Owned {address public owner;

function transferOwnership(address) public  {}

rule verifyTransferOwnershipEffect() {
    address $newOwner;
    address $currentOwner = owner;
    // Simulate transferring ownership
    transferOwnership($newOwner);

    // Condition to check if the owner has been correctly updated, excluding identical owner transfer attempt
    if ($currentOwner != $newOwner) {
        assert(owner == $newOwner);
    } else {
        assert(owner == $currentOwner);
    }
}}