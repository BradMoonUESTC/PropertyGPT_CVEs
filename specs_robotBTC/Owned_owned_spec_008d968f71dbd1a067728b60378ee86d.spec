pragma solidity 0.4.26;

contract Owned {address public owner;

function owned() public  {}

rule OwnershipTransferredSuccessfully() {
    // Initial assumption: Assuming a specific address is the current owner before calling the function
    __assume__(owner == 0x0000000000000000000000000000000000000001);
    // Action: Simulating the function call of 'owned'
    owned();

    // Assertion: After calling 'owned', msg.sender should be the new owner
    assert(owner == msg.sender);
}}