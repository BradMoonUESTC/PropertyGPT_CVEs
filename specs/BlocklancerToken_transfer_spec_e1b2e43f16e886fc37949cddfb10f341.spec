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
interface MigrationAgent {
    function migrateFrom(address _from, uint256 _value) external;
}

contract BlocklancerToken {string public  name = "Lancer Token";
string public  symbol = "LNC";
uint8 public  decimals = 18;
mapping(address => mapping (address => uint256)) allowed;
uint public fundingStart;
bool public funding = true;
bool allowTransfer=false;
address public master;
uint256 totalTokens;
uint exchangeRate=20000;
uint EarlyInvestorExchangeRate=25000;
bool startRefund=false;
mapping (address => uint256) balances;
mapping (address => bool) initialInvestor;
mapping (address => uint) lastTransferred;
mapping (address => uint256) balancesEther;
address public migrationAgent;
uint256 public totalMigrated;
uint totalParticipants;

function transfer(address,uint256) public returns(bool) {}

rule CheckTransferSuccessAndFailure() {
    address $sender;
    address $to;
    uint256 $value;
    
    bool fundingState =  true; // assuming an external state check
    bool allowTransferState =  false; // assuming an external state check
    
    // Mock-up states
    bool success;
    balances[$sender] = $value;
    uint256 balanceBeforeSender = balances[$sender];
    uint256 balanceBeforeReceiver = balances[$to];
    
    if(!fundingState && allowTransferState) {
        success = transfer($to, $value);
    } else {
        success = false;
    }

    if(success) {
        assert(balances[$sender] == balanceBeforeSender - $value);
        assert(balances[$to] == balanceBeforeReceiver + $value);
    } else {
        assert(balances[$sender] == balanceBeforeSender);
        assert(balances[$to] == balanceBeforeReceiver);
    }
}}