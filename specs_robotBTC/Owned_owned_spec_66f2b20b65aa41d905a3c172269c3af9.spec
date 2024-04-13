pragma solidity 0.4.26;

contract Owned {address public owner;

function owned() public  {}

rule OwnedChangesOwnerOnly() {
    address $initialOwner;
    address $newOwner;

    __assume__(msg.sender == $newOwner);
    owner = $initialOwner; // Simulating the initial owner before the function call
    
    owned(); // Function call to change the owner
    
    assert(owner == $newOwner); // Check if the owner is correctly updated

    // Ensuring no other state variables are changed is out of scope
    // as there's no visibility on other state variables within this specific test rule
}}