pragma solidity 0.6.12;

contract VulnerableWallet {address public owner;
mapping(address => address) private sweepers;

function sweep(address,uint256) public returns(bool) {}

rule sweepSuccessDelegatecall() {
    address $token;
    uint256 $amount;
    address $sweeper = sweepers[$token];
    __assume__($sweeper != address(0));
    __assume__(msg.sender == 0x0000000000000000000000000000000000000001);

    bool successBefore = false;
    (successBefore, ) = $sweeper.delegatecall(abi.encodeWithSignature("sweep(address,uint256)", $token, $amount));
    sweep($token, $amount);
    bool successAfter;
    (successAfter, ) = $sweeper.delegatecall(abi.encodeWithSignature("sweep(address,uint256)", $token, $amount));

    assert(successBefore == false && successAfter == true);
}}