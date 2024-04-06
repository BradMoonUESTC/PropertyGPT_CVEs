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


rule PreventShortAddressAttack() {
    uint256 inputDataLength = msg.data.length;
    assert(inputDataLength >= (3 * 32) + 4);
}}