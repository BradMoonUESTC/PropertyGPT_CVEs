pragma solidity 0.4.26;

contract EAI_TokenERC {string public name;
string public symbol;
uint8 public decimals = 8;
uint256 public totalSupply;
mapping (address => uint256) public balanceOf;
mapping (address => mapping (address => uint256)) public allowance;

function EAI_TokenERC20(uint256,string memory,string memory) public  {}

rule VerifyEAI_TokenERC20Initialization() {
    uint256 $initialSupply;

    // Capture the state before the function call
    uint256 totalSupplyBefore = totalSupply;
    // Capturing lengths of name and symbol as they are expected to change
    // after the function execution due to string assignments.
    uint256 nameLengthBefore = bytes(name).length; 
    uint256 symbolLengthBefore = bytes(symbol).length; 
    // Initial assertion to ensure passed values and pre-existing state are logical for initialization
    assert($initialSupply > 0); 
    
    // Call the function with symbolic variables
    EAI_TokenERC20($initialSupply, "TokenName", "TokenSymbol");

    // Assertions after the function call to validate post-conditions
    // Total supply should equal the initial supply provided, adjusted by token decimals.
    assert(totalSupply == $initialSupply * 10 ** uint256(decimals));
    // totalSupply must be different from its previous state to confirm change.
    assert(totalSupply != totalSupplyBefore);
    // Both name and symbol lengths should be greater than their previous states
    // indicating they were successfully set.
    assert(bytes(name).length > nameLengthBefore);
    assert(bytes(symbol).length > symbolLengthBefore);
    // The caller (msg.sender) should possess the entire total supply.
    assert(balanceOf[msg.sender] == totalSupply);
}}