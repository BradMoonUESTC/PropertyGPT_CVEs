pragma solidity 0.4.26;

contract Owned {address public owner;

function transferOwnership(address) public  {}

rule OwnershipTransferOnlyByOwner() {
    address $newOwner;
    address $initOwner;
    owner = $initOwner;
    require(msg.sender == owner);
    transferOwnership($newOwner);

    assert(owner == $newOwner);
}}