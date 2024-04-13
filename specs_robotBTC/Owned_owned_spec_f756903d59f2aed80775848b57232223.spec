pragma solidity 0.4.26;

contract Owned {address public owner;

function owned() public  {}

rule ownerAssignmentCorrectness() {
    address $previousOwner;
    address $newOwner;
    __assume__(owner == $previousOwner);
    owned();
    __assume__(msg.sender == $newOwner);
    assert(owner == $newOwner);
}}