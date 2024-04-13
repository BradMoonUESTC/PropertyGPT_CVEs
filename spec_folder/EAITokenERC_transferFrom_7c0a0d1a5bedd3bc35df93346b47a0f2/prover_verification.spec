pragma solidity 0.6.12;

contract EAITokenERC {string public name;
string public symbol;
uint8 public decimals = 8;
uint256 public totalSupply;
mapping (address => uint256) public balanceOf;
mapping (address => mapping (address => uint256)) public allowance;

function transferFrom(address,address,uint256) public returns(bool) {}

rule transferFromMaintainsAllowanceConsistency() {
    address $from;
    address $to;
    uint256 $value;
    uint256 $allowanceBefore = allowance[$from][msg.sender];
    
    __assume__($from != $to);
    __assume__(msg.sender != $from);

    transferFrom($from, $to, $value);
    
    assert(allowance[$from][msg.sender] == $allowanceBefore - $value);
}}