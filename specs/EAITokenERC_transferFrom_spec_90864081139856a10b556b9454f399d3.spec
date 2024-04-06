pragma solidity 0.4.26;

contract EAI_TokenERC {string public name;
string public symbol;
uint8 public decimals = 8;
uint256 public totalSupply;
mapping (address => uint256) public balanceOf;
mapping (address => mapping (address => uint256)) public allowance;

function transferFrom(address,address,uint256) public returns(bool) {}

rule TransferFromStateVerification() {
    address $from;
    address $to;
    uint256 $value;

    // Pre-condition: Check if the allowance is sufficient for the transfer
    require($value <= allowance[$from][msg.sender], "Insufficient allowance.");

    // Save the initial states before executing transferFrom
    uint256 initialAllowance = allowance[$from][msg.sender];
    uint256 initialSenderBalance = balances[$from];
    uint256 initialRecipientBalance = balances[$to];

    // Execute transferFrom
    transferFrom($from, $to, $value);

    // Post-conditions: Validate state changes after transferFrom execution
    assert(allowance[$from][msg.sender] == initialAllowance - $value);
    assert(balances[$to] == initialRecipientBalance + $value);
    assert(balances[$from] == initialSenderBalance - $value);
}}