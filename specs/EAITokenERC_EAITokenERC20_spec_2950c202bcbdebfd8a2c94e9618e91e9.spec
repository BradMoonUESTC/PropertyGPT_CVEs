pragma solidity 0.4.26;

contract EAI_TokenERC {string public name;
string public symbol;
uint8 public decimals = 8;
uint256 public totalSupply;
mapping (address => uint256) public balanceOf;
mapping (address => mapping (address => uint256)) public allowance;

function EAI_TokenERC20(uint256,string memory,string memory) public  {}

rule ValidateInitialTokenSupply() {
    uint256 $initialSupply;

    uint256 totalSupplyBefore = totalSupply;
    EAI_TokenERC20($initialSupply, "TestToken", "TT");

    // After calling EAI_TokenERC20, totalSupply is updated using initialSupply * 10^decimals.
    // Assert that the new totalSupply is correct.
    assert(totalSupply == ($initialSupply * 10 ** uint256(decimals)));

    // Assert that the creator's balance is equal to the new totalSupply,
    // confirming all initial tokens are allocated to the creator.
    assert(balanceOf[msg.sender] == totalSupply);

    // Verify that totalSupply has increased after calling EAI_TokenERC20.
    assert(totalSupply > totalSupplyBefore);
}}