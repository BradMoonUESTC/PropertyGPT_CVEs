pragma solidity 0.4.26;

contract Owned {address public owner;

function owned() public  {}

rule OwnerAssignmentConsistency() {
    address $previousOwner = owner;
    address $newOwner = msg.sender;
    owned();

    assert(owner == $newOwner && owner != $previousOwner);
}}