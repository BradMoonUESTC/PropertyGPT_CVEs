pragma solidity 0.4.26;

contract Owned {address public owner;

function owned() public  {}

rule EnsureOwnerChangedSuccessfully() {
    address $previousOwner;
    owner = $previousOwner;   // Assuming 'owner' is the state variable representing the current owner of the contract

    __assume__(msg.sender == 0x0000000000000000000000000000000000000001);

    owned(); // Call to the owned function, attempting to change the owner to msg.sender

    assert(owner != $previousOwner); // Ensure that the owner has indeed changed
}}