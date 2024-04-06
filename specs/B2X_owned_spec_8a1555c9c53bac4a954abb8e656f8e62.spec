pragma solidity 0.4.26;

contract Owned {address public owner;

function owned() public  {}

rule OwnerAssignedCorrectly() {
    address $msgSender = address(0); // Correctly initializing $msgSender as an address type
    owner = address(0); // Correcting the type mismatch error by ensuring the owner is an address
    owned(); // Calling the function to test

    assert(owner == $msgSender);
}}