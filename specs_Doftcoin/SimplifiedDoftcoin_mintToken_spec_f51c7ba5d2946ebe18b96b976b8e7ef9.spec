pragma solidity 0.6.12;

contract SimplifiedDoftcoin {string public name = "Doftcoin";
string public symbol = "DFC";
uint256 public decimals = 18;
uint256 public totalSupply;
mapping (address => uint256) public balanceOf;
address public owner;

function mintToken(address,uint256) public  {}

rule MintIncreasesTotalSupply() {
    uint256 $initTotalSupply = totalSupply;
    address $target;
    uint256 $mintedAmount;
    __assume__($target != address(0));
    mintToken($target, $mintedAmount);
    assert(totalSupply == $initTotalSupply + $mintedAmount);
}}