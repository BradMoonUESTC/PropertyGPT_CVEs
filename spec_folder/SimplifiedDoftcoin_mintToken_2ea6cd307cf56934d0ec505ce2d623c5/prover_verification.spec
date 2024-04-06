pragma solidity 0.4.26;

contract SimplifiedDoftcoin {string public name = "Doftcoin";
string public symbol = "DFC";
uint256 public decimals = 18;
uint256 public totalSupply;
mapping (address => uint256) public balanceOf;
address public owner;

function mintToken(address,uint256) public  {}

rule MintTokenUpdatesTotalSupplyCorrectly() {
    uint256 totalSupplyBefore = totalSupply;
    address $target;
    uint256 $mintedAmount;
    mintToken($target, $mintedAmount);
    assert(totalSupply == totalSupplyBefore + $mintedAmount);
}}