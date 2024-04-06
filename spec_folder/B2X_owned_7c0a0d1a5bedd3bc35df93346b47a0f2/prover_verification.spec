pragma solidity 0.4.26;

contract Owned {address public owner;

function owned() public  {}

rule OwnedFunctionChangesOwnerOnly() {
    address $initialOwner = owner;
    address $newOwner = msg.sender;

    owned();

    assert(owner == $newOwner);
    assert(owner != $initialOwner);
}}