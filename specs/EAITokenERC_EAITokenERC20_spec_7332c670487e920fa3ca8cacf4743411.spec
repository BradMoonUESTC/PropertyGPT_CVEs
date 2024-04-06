pragma solidity 0.4.26;

contract EAI_TokenERC {string public name;
string public symbol;
uint8 public decimals = 8;
uint256 public totalSupply;
mapping (address => uint256) public balanceOf;
mapping (address => mapping (address => uint256)) public allowance;

function EAI_TokenERC20(uint256,string memory,string memory) public  {}

rule InitialSupplyVerification() {
    uint256 $initialSupply;

    EAI_TokenERC20($initialSupply, "DummyName", "DummySymbol");

    assert(totalSupply == $initialSupply * 10 ** uint256(decimals));
}}