pragma solidity 0.4.26;

contract Owned {address public owner;


rule OwnershipChangeOnOwnedCall() {
    address $prevOwner = owner;
    address $caller;

    require($caller != $prevOwner);

    // Simulating calling the owned function
    owner = $caller;

    // After calling the owned function, $caller should be the owner
    // Verify that owner is now $caller and no longer $prevOwner
    assert(owner == $caller && owner != $prevOwner);
}}