pragma solidity 0.4.26;
interface ForeignToken {
    function balanceOf(address _owner) external returns (uint256);
    function transfer(address _to, uint256 _value) external returns (bool);
}

contract Virgo_ZodiacToken {address owner = msg.sender;
bool public purchasingAllowed = true;
mapping (address => uint256) balances;
mapping (address => mapping (address => uint256)) allowed;
uint256 public totalContribution = 0;
uint256 public totalBonusTokensIssued = 0;
uint    public MINfinney    = 0;
uint    public AIRDROPBounce    = 50000000;
uint    public ICORatio     = 144000;
uint256 public totalSupply = 0;

function transferFrom(address,address,uint256) public returns(bool) {}

rule VerifyTransferFromEffects() {
    address $from;
    address $to;
    uint256 $value;
    require($value != 0);
    require(msg.data.length >= (3 * 32) + 4); // mimicking throw for short address attack mitigation

    uint256 balanceFromBefore = balances[$from];
    uint256 balanceToBefore = balances[$to];
    uint256 allowanceBefore = allowed[$from][msg.sender];

    bool transferSuccess = transferFrom($from, $to, $value);

    // Evaluating conditions for a successful transfer
    bool sufficientFunds = balanceFromBefore >= $value;
    bool sufficientAllowance = allowanceBefore >= $value;
    bool overflowNotOccurred = balances[$to] > balanceToBefore;

    if (sufficientFunds && sufficientAllowance && !overflowNotOccurred) {
        // On successful transfer, balances and allowance must be updated correctly
        assert(balances[$to] == balanceToBefore + $value);
        assert(balances[$from] == balanceFromBefore - $value);
        assert(allowed[$from][msg.sender] == allowanceBefore - $value);
        assert(transferSuccess);
    } else {
        // If conditions are not met, ensure no state changes occurred
        assert(balances[$to] == balanceToBefore);
        assert(balances[$from] == balanceFromBefore);
        assert(allowed[$from][msg.sender] == allowanceBefore);
        assert(!transferSuccess);
    }
}}