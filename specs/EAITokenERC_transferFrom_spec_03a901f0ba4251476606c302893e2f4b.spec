pragma solidity 0.4.26;

contract EAI_TokenERC {string public name;
string public symbol;
uint8 public decimals = 8;
uint256 public totalSupply;
mapping (address => uint256) public balanceOf;
mapping (address => mapping (address => uint256)) public allowance;

function transferFrom(address,address,uint256) public returns(bool) {}

rule checkTransferFromDecrementingAllowance() {
    address $sender;
    address $from;
    address $to;
    uint256 $value;

    uint256 allowanceBefore = allowance[$from][$sender];
    transferFrom($from, $to, $value);
    assert(allowance[$from][$sender] == allowanceBefore - $value);
}}