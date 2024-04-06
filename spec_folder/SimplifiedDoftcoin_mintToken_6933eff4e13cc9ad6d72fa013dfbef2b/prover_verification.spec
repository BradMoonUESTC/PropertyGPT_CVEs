pragma solidity 0.4.26;

contract SimplifiedDoftcoin {string public name = "Doftcoin";
string public symbol = "DFC";
uint256 public decimals = 18;
uint256 public totalSupply;
mapping (address => uint256) public balanceOf;
address public owner;

function mintToken(address,uint256) public  {}

rule MintTokenIncreasesSupplyAndTargetBalance() {
    address $target;
    uint256 $mintedAmount;
    uint256 totalSupplyBefore = totalSupply;
    uint256 balanceOfTargetBefore = balanceOf[$target];
    mintToken($target, $mintedAmount);
    assert(totalSupply == totalSupplyBefore + $mintedAmount);
    assert(balanceOf[$target] == balanceOfTargetBefore + $mintedAmount);
}}