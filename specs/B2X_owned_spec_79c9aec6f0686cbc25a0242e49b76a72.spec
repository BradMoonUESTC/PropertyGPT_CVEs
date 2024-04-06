pragma solidity 0.4.26;

contract Owned {address public owner;

function owned() public  {}

rule CheckOwnerAssignment() {
    address $expectedOwner;
    $expectedOwner = msg.sender;
    owned();

    assert(owner == $expectedOwner);
}}