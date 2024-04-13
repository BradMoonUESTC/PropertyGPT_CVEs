pragma solidity 0.6.12;

contract SimplifiedEncryptedToken {address public owner;
uint256 public totalSupply;
uint256 public buyPrice;
mapping (address => uint256) public balanceOf;
uint256 public testVar;

function setPrices(uint256) public  {}

rule ValidateAmountAfterBuy() {
    uint256 $newBuyPrice;
    uint256 $msg_value;
    __assume__(msg.sender == 0x0000000000000000000000000000000000000001);
    
    uint256 amountBefore = testVar;
    setPrices($newBuyPrice);
    uint256 amountAfter = $msg_value * buyPrice; // This mimics the process within the test function without directly calling it, as we're focusing on the result.
    
    assert(amountBefore != amountAfter);
}}