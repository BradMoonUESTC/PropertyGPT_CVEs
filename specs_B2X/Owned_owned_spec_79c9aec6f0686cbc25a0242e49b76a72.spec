pragma solidity 0.4.26;

contract Owned {address public owner;

function owned() public  {}

rule OwnedSetsOwnerCorrectly() {
    address $newOwner;
    __assume__(msg.sender == $newOwner);
    owner = 0x0000000000000000000000000000000000000000; // Initial assumption for before the function call
    owned();
    assert(owner == $newOwner);
}}