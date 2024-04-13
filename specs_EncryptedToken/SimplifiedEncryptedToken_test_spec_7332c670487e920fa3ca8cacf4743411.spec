pragma solidity 0.6.12;

contract SimplifiedEncryptedToken {address public owner;
uint256 public totalSupply;
uint256 public buyPrice;
mapping (address => uint256) public balanceOf;
uint256 public testVar;

function test(uint256) public  {}

rule TestFunctionEnsuresProperValueAssignment() {
    uint256 $newBuyPrice;
    uint256 $msgValue;
    __assume__(msg.sender == 0x0000000000000000000000000000000000000001);

    uint256 testVarBefore = testVar;
    uint256 expectedAmount = $msgValue * $newBuyPrice;
    
    test($newBuyPrice);

    assert(testVar == testVarBefore + expectedAmount);
}}