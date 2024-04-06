pragma solidity 0.4.26;

contract Owned {address public owner;

function transferOwnership(address) public  {}

rule OwnershipTransferMaintainsInvariant() {
    address $newOwner;
    address ownerBefore = owner;
    transferOwnership($newOwner);
    
    if ($newOwner != address(0)) {
        assert(owner == $newOwner);
    } else {
        assert(owner == ownerBefore);
    }
}}