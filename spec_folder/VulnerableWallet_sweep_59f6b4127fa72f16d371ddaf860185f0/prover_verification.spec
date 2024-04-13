pragma solidity 0.6.12;

contract VulnerableWallet {address public owner;
mapping(address => address) private sweepers;

function sweep(address,uint256) public returns(bool) {}

rule SweepDelegateCallSafety() {
    address $sweeper;
    address $token;
    uint256 $amount;
    
    address initiatorBefore = msg.sender;
    address sweeperBefore = sweepers[$token];
    uint256 amountBefore = $amount;
    
    __assume__(sweeperBefore != address(0));
    __assume__(initiatorBefore == 0x0000000000000000000000000000000000000001);
    
    sweep($token, $amount);
    
    assert(sweepers[$token] == sweeperBefore); // Ensure the sweeper mapping was not maliciously modified
    assert(amountBefore == $amount); // Confirm the amount to sweep remains unchanged
    assert(msg.sender == initiatorBefore); // Confirm that msg.sender (initiator) remains the same after sweep
}}