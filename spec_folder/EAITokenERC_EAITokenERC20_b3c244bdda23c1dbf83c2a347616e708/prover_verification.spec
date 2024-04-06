pragma solidity 0.4.26;

contract EAI_TokenERC {string public name;
string public symbol;
uint8 public decimals = 8;
uint256 public totalSupply;
mapping (address => uint256) public balanceOf;
mapping (address => mapping (address => uint256)) public allowance;


rule VerifyTokenInitialization(){
    // Define symbolic variables
    uint256 $initialSupply;
    string memory $tokenName;
    string memory $tokenSymbol;

    // Simulate the relevant primitives and constructs
    uint256 decimals = 18; // Assuming decimal is a constant value in the token contract
    address $creator = address(1); // Simulate an address for the creator
    uint256 expectedTotalSupply = $initialSupply * 10**decimals;
    uint256 creatorBalance; // Simulating the creator's balance without a mapping
    string memory name;
    string memory symbol;
    uint256 totalSupply;

    // Simulate the execution of the EAI_TokenERC20 function
    totalSupply = $initialSupply * 10**decimals; // Update total supply with the decimal amount
    creatorBalance = totalSupply; // Give the creator all initial tokens, simplifying without using mapping
    name = $tokenName; // Set the name for display purposes
    symbol = $tokenSymbol; // Set the symbol for display purposes

    // Assertions to validate the logic
    assert(totalSupply == expectedTotalSupply); // Verify totalSupply is correctly set
    assert(creatorBalance == totalSupply); // Verify creator received the correct amount of tokens
}}