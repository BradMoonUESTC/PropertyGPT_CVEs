pragma solidity 0.4.26;

contract Owned {address public owner;

function owned() public  {}

rule EnsureOwnershipTransferConsistency() {
    address $previousOwner;
    address $newOwner = msg.sender;
    
    owner = $previousOwner;
    
    owned(); // Assuming this is the invocation of the "owned" method
    
    assert(owner == $newOwner);
}}