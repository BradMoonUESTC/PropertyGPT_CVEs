pragma solidity 0.4.26;
interface ERC20Interface {
     // Get the total token supply
     function totalSupply() external returns (uint256 totalSupply);
  
     // Get the account balance of another account with address _owner
     function balanceOf(address _owner) external returns (uint256 balance);
  
     // Send _value amount of tokens to address _to
     function transfer(address _to, uint256 _value) external returns (bool success);
  
     // Send _value amount of tokens from address _from to address _to
     function transferFrom(address _from, address _to, uint256 _value) external returns (bool success);
  
     // Allow _spender to withdraw from your account, multiple times, up to the _value amount.
     // If this function is called again it overwrites the current allowance with _value.
     // this function is required for some DEX functionality
     function approve(address _spender, uint256 _value) external returns (bool success);
  
     // Returns the amount which _spender is still allowed to withdraw from _owner
     function allowance(address _owner, address _spender) external returns (uint256 remaining);
  
     // Triggered when tokens are transferred.
     event Transfer(address indexed _from, address indexed _to, uint256 _value);
  
     // Triggered whenever approve(address _spender, uint256 _value) is called.
     event Approval(address indexed _owner, address indexed _spender, uint256 _value);
 }

contract Coinlancer {string public constant symbol = "CL";
string public constant name = "Coinlancer";
uint8 public constant decimals = 18;
uint256 _totalSupply = 300000000000000000000000000;
address public owner;
mapping(address => uint256) balances;
mapping(address => mapping (address => uint256)) allowed;

function transfer(address,uint256) public returns(bool) {}

rule VerifyTransferDoesNotExceedBalance() {
    address $sender;
    address $recipient;
    uint256 $sendAmount;
    uint256 balanceBeforeSender = balances[$sender];
    uint256 balanceBeforeRecipient = balances[$recipient];
    
    transfer($recipient, $sendAmount);
    
    if ($sendAmount > 0 && balanceBeforeSender >= $sendAmount) {
        assert(balances[$sender] == balanceBeforeSender - $sendAmount);
        assert(balances[$recipient] == balanceBeforeRecipient + $sendAmount);
    } else {
        assert(balances[$sender] == balanceBeforeSender);
        assert(balances[$recipient] == balanceBeforeRecipient);
    }
}}