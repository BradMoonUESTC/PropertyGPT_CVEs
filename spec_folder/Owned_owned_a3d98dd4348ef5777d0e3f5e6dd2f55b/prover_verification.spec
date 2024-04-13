pragma solidity 0.4.26;

contract Owned {address public owner;

function owned() public  {}

rule ownerSetCorrectlyAfterOwnedCall() {
    address $newOwner;
    __assume__(msg.sender == $newOwner);
    owned();

    assert(owner == $newOwner);
}}