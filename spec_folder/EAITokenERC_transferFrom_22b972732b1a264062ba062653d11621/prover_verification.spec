pragma solidity 0.4.26;

contract EAI_TokenERC {string public name;
string public symbol;
uint8 public decimals = 8;
uint256 public totalSupply;
mapping (address => uint256) public balanceOf;
mapping (address => mapping (address => uint256)) public allowance;

function transferFrom(address,address,uint256) public returns(bool) {}

rule TransferFromDoesNotIncreaseAllowance() {
    address $from;
    address $to;
    address $operator;
    uint256 $value;
    
    uint256 allowanceBefore = allowance[$from][$operator];
    transferFrom($from, $to, $value);
    uint256 allowanceAfter = allowance[$from][$operator];

    assert(allowanceBefore >= allowanceAfter);
}}