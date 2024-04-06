pragma solidity 0.4.26;

contract Owned {address public owner;


rule OwnershipTransferDoesNotChangeOwnerWithoutExecution() {
    address $newOwner;
    address ownerBefore = owner;
    // This simulates the scenario before actually calling the transferOwnership function
    // Asserting that without the execution of transferOwnership, the owner should remain the same.

    if ($newOwner != owner) {
        assert(ownerBefore == owner);
    }
}}