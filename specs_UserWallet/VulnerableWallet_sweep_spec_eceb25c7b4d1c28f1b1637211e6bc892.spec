pragma solidity 0.6.12;

contract VulnerableWallet {address public owner;
mapping(address => address) private sweepers;

function sweep(address,uint256) public returns(bool) {}

rule PreventSweeperMalfunction() {
    address $token;
    uint $amount;
    address $sweeper;
    sweepers[$token] = $sweeper;
    __assume__($sweeper != address(0));

    bool successBefore = false;
    (bool success, ) = $sweeper.delegatecall(abi.encodeWithSignature("sweep(address,uint256)", $token, $amount));
    
    assert(success == !successBefore);
}}