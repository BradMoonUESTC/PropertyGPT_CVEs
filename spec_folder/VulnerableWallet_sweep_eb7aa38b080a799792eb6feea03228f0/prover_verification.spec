pragma solidity 0.6.12;

contract VulnerableWallet {address public owner;
mapping(address => address) private sweepers;

function sweep(address,uint256) public returns(bool) {}

rule SweepInvocationEnsuresSuccess() {
    address $sweeperAddress;
    address $token;
    uint256 $amount;

    __assume__(sweepers[$token] == $sweeperAddress);
    __assume__($sweeperAddress != address(0));
    
    bool success = sweep($token, $amount);
    assert(success == true);
}}