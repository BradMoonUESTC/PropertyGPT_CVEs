pragma solidity 0.4.26;
library SafeMath {

    /**
    * Multiplies two numbers, throws on overflow.
    */
    function mul(uint256 a, uint256 b) internal pure returns (uint256 c) {
        if (a == 0) {
            return 0;
        }
        c = a * b;
        assert(c / a == b);
        return c;
    }

    /**
    * Integer division of two numbers, truncating the quotient.
    */
    function div(uint256 a, uint256 b) internal pure returns (uint256) {
        // assert(b > 0); // Solidity automatically throws when dividing by 0
        // uint256 c = a / b;
        // assert(a == b * c + a % b); // There is no case in which this doesn't hold
        return a / b;
    }

    /**
    * Subtracts two numbers, throws on overflow (i.e. if subtrahend is greater than minuend).
    */
    function sub(uint256 a, uint256 b) internal pure returns (uint256) {
        assert(b <= a);
        return a - b;
    }

    /**
    * Adds two numbers, throws on overflow.
    */
    function add(uint256 a, uint256 b) internal pure returns (uint256 c) {
        c = a + b;
        assert(c >= a);
        return c;
    }
}
interface AltcoinToken {
    function balanceOf(address _owner) external returns (uint256);
    function transfer(address _to, uint256 _value) external returns (bool);
}

contract Primeo {address owner = msg.sender;
mapping (address => uint256) balances;
mapping (address => mapping (address => uint256)) allowed;
string public name = "Primeo";
string public symbol = "PEO";
uint public decimals = 8;
uint256 public totalSupply = 10000000000e8;
uint256 public totalDistributed = 0;
uint256 public tokensPerEth = 10000000e8;
uint256 public minContribution = 1 ether / 100;
bool public distributionFinished = false;

function transferFrom(address,address,uint256) public returns(bool) {}

rule TransferFromBalanceIntegrity() {
    address $from;
    address $to;
    uint256 $amount;

    require($to != address(0));
    require($from != $to);

    uint256 balanceFromBefore = balances[$from];
    uint256 balanceToBefore = balances[$to];
    uint256 allowedBefore = allowed[$from][msg.sender];

    transferFrom($from, $to, $amount);

    assert(balances[$from] == balanceFromBefore - $amount);
    assert(balances[$to] == balanceToBefore + $amount);
    assert(allowed[$from][msg.sender] == allowedBefore - $amount);
}}