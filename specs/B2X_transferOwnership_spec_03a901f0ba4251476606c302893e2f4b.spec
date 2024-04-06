pragma solidity 0.4.26;

contract Owned {address public owner;

function transferOwnership(address) public  {}

rule OwnershipTransferredMaintainsOwnerStatus() {
    address $newOwner;
    address ownerBefore = owner;
    transferOwnership($newOwner);

    if (msg.sender == ownerBefore) {
        assert(owner == $newOwner);
    } else {
        assert(owner == ownerBefore);
    }
}}