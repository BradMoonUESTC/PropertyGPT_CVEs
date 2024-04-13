pragma solidity 0.6.12;

contract VulnerableWallet {address public owner;
mapping(address => address) private sweepers;

function sweep(address,uint256) public returns(bool) {}

rule DelegateCallSweepMaliciousCheck() {
    address $sweeper;
    address $token;
    uint256 $amount;

    // Assuming two conditions for msg.sender using __assume__
    __assume__(msg.sender == 0x0000000000000000000000000000000000000001);
    __assume__(sweepers[$token] == $sweeper);

    address sweepersBefore = sweepers[$token];

    sweep($token, $amount);

    // After the delegatecall, checking that the sweeper address for the token has not been tampered with
    assert(sweepers[$token] == sweepersBefore);
}}