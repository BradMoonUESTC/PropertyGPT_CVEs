pragma solidity 0.6.12;

contract SimplifiedEncryptedToken {address public owner;
uint256 public totalSupply;
uint256 public buyPrice;
mapping (address => uint256) public balanceOf;
uint256 public testVar;

function setPrices(uint256) public  {}
function test(uint256) public  {}

rule TestFunctionIntegrity() {
    uint256 $newBuyPrice;
    uint256 $msgValue;
    
    __assume__(msg.sender == 0x0000000000000000000000000000000000000001);
    
    uint256 buyPriceBefore = buyPrice;
    uint256 testVarBefore = testVar;
    uint256 amountCalculated = $msgValue * $newBuyPrice;
    
    setPrices($newBuyPrice);
    test($msgValue);
    
    assert(buyPrice == $newBuyPrice);
    assert(testVar == testVarBefore + amountCalculated);
}}