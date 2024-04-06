pragma solidity 0.4.26;

contract EAI_TokenERC {string public name;
string public symbol;
uint8 public decimals = 8;
uint256 public totalSupply;
mapping (address => uint256) public balanceOf;
mapping (address => mapping (address => uint256)) public allowance;

function transferFrom(address,address,uint256) public returns(bool) {}

rule TransferFromMaintainsAllowance() {
    address $from;
    address $msgSender;
    uint256 $allowanceBefore = allowance[$from][$msgSender];
    uint256 $value;
    require($value <= $allowanceBefore);

    transferFrom($from, msg.sender, $value);

    assert(allowance[$from][$msgSender] == $allowanceBefore - $value);
}}