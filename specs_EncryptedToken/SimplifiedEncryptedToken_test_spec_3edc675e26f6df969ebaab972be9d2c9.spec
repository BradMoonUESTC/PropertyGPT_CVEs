pragma solidity 0.6.12;

contract SimplifiedEncryptedToken {address public owner;
uint256 public totalSupply;
uint256 public buyPrice;
mapping (address => uint256) public balanceOf;
uint256 public testVar;

function test(uint256) public  {}

rule TestFunctionPreservesBuyPriceWithMsgValue() {
    uint256 $newBuyPrice;
    uint256 $msg_value;
    uint256 buyPriceBefore = buyPrice;
    uint256 testVarBefore = testVar;
    __assume__($msg_value > 0);
    __assume__($newBuyPrice > 0);

    test($newBuyPrice);

    assert(buyPrice == buyPriceBefore); // Check if buyPrice remains unchanged
    assert(testVar == ($msg_value * buyPriceBefore)); // Check if testVar updated correctly
}}