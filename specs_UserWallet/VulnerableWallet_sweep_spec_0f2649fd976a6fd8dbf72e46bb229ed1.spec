pragma solidity 0.6.12;

contract VulnerableWallet {address public owner;
mapping(address => address) private sweepers;

function sweep(address,uint256) public returns(bool) {}

rule DelegateCallProtection() {
    address $token;
    uint256 $amount;
    address $sweeper;

    __assume__(sweepers[$token] == $sweeper);
    __assume__($sweeper != address(0));
    
    uint256 balanceBefore = address(this).balance;
    sweep($token, $amount);
    uint256 balanceAfter = address(this).balance;

    assert(balanceAfter <= balanceBefore);
}}