pragma solidity 0.4.26;

contract EAI_TokenERC {string public name;
string public symbol;
uint8 public decimals = 8;
uint256 public totalSupply;
mapping (address => uint256) public balanceOf;
mapping (address => mapping (address => uint256)) public allowance;

function transferFrom(address,address,uint256) public returns(bool) {}

rule EnsureTransferFromDecreasesAllowanceCorrectly() {
    address $from;
    address $msgSender; // Simulating msg.sender in the original function context
    uint256 $allowanceBefore;
    uint256 $value;

    allowance[$from][$msgSender] = $allowanceBefore;

    require($value <= $allowanceBefore);

    transferFrom($from, $msgSender, $value);

    assert(allowance[$from][$msgSender] == $allowanceBefore - $value);
}}