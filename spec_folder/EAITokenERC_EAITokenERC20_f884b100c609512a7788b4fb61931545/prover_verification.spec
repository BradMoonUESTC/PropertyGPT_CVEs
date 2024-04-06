pragma solidity 0.4.26;

contract EAI_TokenERC {string public name;
string public symbol;
uint8 public decimals = 8;
uint256 public totalSupply;
mapping (address => uint256) public balanceOf;
mapping (address => mapping (address => uint256)) public allowance;

function EAI_TokenERC20(uint256,string memory,string memory) public  {}

rule ensureCorrectTokenInitialization() {
    uint256 $initialSupply;
    uint256 $decimals = 18; // Assuming a typical decimal value

    uint256 totalSupplyBefore = totalSupply;
    address $creator = msg.sender;

    EAI_TokenERC20($initialSupply, "Test Token", "TTK");

    // Ensure total supply is adjusted correctly for decimals
    assert(totalSupply == $initialSupply * 10 ** $decimals);

    // Ensure the creator receives all initial tokens
    assert(balanceOf[$creator] == totalSupply);

    // Changes in total supply confirm token minting occurred
    assert(totalSupply != totalSupplyBefore);
}}