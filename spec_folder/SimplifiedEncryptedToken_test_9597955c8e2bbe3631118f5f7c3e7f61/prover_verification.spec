pragma solidity 0.6.12;

contract SimplifiedEncryptedToken {address public owner;
uint256 public totalSupply;
uint256 public buyPrice;
mapping (address => uint256) public balanceOf;
uint256 public testVar;

function test(uint256) public  {}

rule TestFunctionValuePreservation() {
    uint256 $newBuyPrice;
    uint256 $msg_value;
    __assume__(msg.sender == 0x0000000000000000000000000000000000000001);

    uint256 amountBefore = testVar;
    uint256 expectedIncrease = $msg_value * $newBuyPrice;
    test($newBuyPrice);
    assert(testVar == amountBefore + expectedIncrease);
}}