pragma solidity 0.4.26;

contract Owned {address public owner;

function owned() public  {}

rule OwnershipChangeRequiresCorrectSender() {
    address $previousOwner;
    address $newOwner;

    // Assuming the $previousOwner is the owner before calling owned()
    __assume__(owner == $previousOwner);
    // Assuming the msg.sender for the owned() function will be $newOwner
    __assume__(msg.sender == $newOwner);

    // Simulate the ownership change
    owned();
    
    // Assert the ownership has correctly changed to $newOwner
    assert(owner == $newOwner);
}}