pragma solidity 0.6.12;

contract SimplifiedDoftcoin {string public name = "Doftcoin";
string public symbol = "DFC";
uint256 public decimals = 18;
uint256 public totalSupply;
mapping (address => uint256) public balanceOf;
address public owner;

function mintToken(address,uint256) public  {}

rule MintIncreasesTotalSupplyAndTargetBalance() {
    address $target;
    uint256 $mintedAmount;

    __assume__($target != address(0));

    uint256 totalSupplyBefore = totalSupply;
    uint256 targetBalanceBefore = balanceOf[$target];

    mintToken($target, $mintedAmount);

    assert(totalSupply == totalSupplyBefore + $mintedAmount);
    assert(balanceOf[$target] == targetBalanceBefore + $mintedAmount);
}}