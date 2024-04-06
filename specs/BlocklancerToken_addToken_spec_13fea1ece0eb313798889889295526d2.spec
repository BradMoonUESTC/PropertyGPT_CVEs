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

function addToken(address,uint256) public  {}

rule PreventUnauthorisedTokenAddition() {
    address $invest;
    uint256 $value;
    uint256 totalTokensBefore = totalTokens;
    uint256 investBalanceBefore = balances[$invest];

    // Attempt to add tokens by an unauthorized sender
    address $unauthorizedSender;
    require(msg.sender == $unauthorizedSender && msg.sender != master);

    // Executing the function with an unauthorized sender should not change the state
    addToken($invest, $value);

    // Assertions to ensure no tokens were added
    assert(totalTokens == totalTokensBefore);
    assert(balances[$invest] == investBalanceBefore);
}}