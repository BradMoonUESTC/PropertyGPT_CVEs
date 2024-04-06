pragma solidity 0.4.26;

contract EAI_TokenERC {string public name;
string public symbol;
uint8 public decimals = 8;
uint256 public totalSupply;
mapping (address => uint256) public balanceOf;
mapping (address => mapping (address => uint256)) public allowance;

function EAI_TokenERC20(uint256,string memory,string memory) public  {}

rule VerifyInitialSupplyAndOwnership() {
    uint256 $initialSupply;
    uint256 $decimals;
    address $creator;

    uint256 totalSupplyBefore = totalSupply;
    uint256 balanceOfCreatorBefore = balanceOf[$creator];

    // Simulating the function call
    EAI_TokenERC20($initialSupply, "TestToken", "TTK");

    // Verifying the new total supply is set correctly
    assert(totalSupply == $initialSupply * 10 ** $decimals);
    // Verifying the creator's balance is now equal to the total supply
    assert(balanceOf[$creator] == totalSupply);
    // Verifying that the total supply has indeed increased
    assert(totalSupply > totalSupplyBefore);
    // Verifying that the creator's balance has increased
    assert(balanceOf[$creator] > balanceOfCreatorBefore);
}}