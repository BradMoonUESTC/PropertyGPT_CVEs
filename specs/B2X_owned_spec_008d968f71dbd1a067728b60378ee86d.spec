pragma solidity 0.4.26;

contract Owned {address public owner;

function owned() public  {}

rule VerifyOwnerSetCorrectly() {
    address $expectedOwner = msg.sender; // Initialize $expectedOwner with the address calling the function
    owner = address(0); // Set owner to the zero address to ensure it is unset before the test
    owned(); // Call the owned function to set the owner
    assert(owner == $expectedOwner); // Verify that the owner is set correctly
}}