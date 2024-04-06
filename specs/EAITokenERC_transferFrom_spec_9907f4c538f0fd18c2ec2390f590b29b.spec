pragma solidity 0.4.26;

contract EAI_TokenERC {string public name;
string public symbol;
uint8 public decimals = 8;
uint256 public totalSupply;
mapping (address => uint256) public balanceOf;
mapping (address => mapping (address => uint256)) public allowance;

function transferFrom(address,address,uint256) public returns(bool) {}

rule CorrectAllowanceAndBalancesOnTransferFrom() {
    address $from;
    address $to;
    uint256 $value;
    uint256 $allowanceBefore = allowance[$from][msg.sender];

    // Assuming the existence of a '_transfer' function which updates balances.
    uint256 $balanceFromBefore = balanceOf($from);
    uint256 $balanceToBefore = balanceOf($to);

    require($value <= $allowanceBefore);

    transferFrom($from, $to, $value);

    assert(allowance[$from][msg.sender] == $allowanceBefore - $value);

    if ($from != $to) {
        assert(balanceOf($from) == $balanceFromBefore - $value);
        assert(balanceOf($to) == $balanceToBefore + $value);
    } else {
        // When $from and $to are the same, no balance change should be observed.
        assert(balanceOf($from) == $balanceFromBefore);
    }
}}