pragma solidity 0.6.12;
library SafeMath {
    /**
    * @dev Multiplies two unsigned integers, reverts on overflow.
    */
    function mul(uint256 a, uint256 b) internal pure returns (uint256) {
        if (a == 0) {
            return 0;
        }
        uint256 c = a * b;
        require(c / a == b, "SafeMath: multiplication overflow");
        return c;
    }

    /**
    * @dev Integer division of two unsigned integers, truncates and reverts on division by zero.
    */
    function div(uint256 a, uint256 b) internal pure returns (uint256) {
        require(b > 0, "SafeMath: division by zero");
        return a / b;
    }

    /**
    * @dev Subtracts two unsigned integers, reverts on overflow.
    */
    function sub(uint256 a, uint256 b) internal pure returns (uint256) {
        require(b <= a, "SafeMath: subtraction overflow");
        return a - b;
    }

    /**
    * @dev Adds two unsigned integers, reverts on overflow.
    */
    function add(uint256 a, uint256 b) internal pure returns (uint256) {
        uint256 c = a + b;
        require(c >= a, "SafeMath: addition overflow");
        return c;
    }
}

contract Primeo {address public owner;
mapping (address => uint256) private balances;
mapping (address => mapping (address => uint256)) private allowed;
string public constant name = "Primeo";
string public constant symbol = "PEO";
uint public constant decimals = 8;
uint256 public totalSupply = 10000000000 * 10**decimals;
uint256 public totalDistributed = 0;
bool public distributionFinished = false;

function doAirdrop(address,uint256) public  {}

rule EnsureAirdropComplianceWithTotalSupply() {
    uint256 $amount;
    __assume__(msg.sender == 0x0000000000000000000000000000000000000001);
    __assume__($amount > 0); // Assumption about valid airdrop amount since it's necessary for the doAirdrop function

    // Assume that the addition of $amount could potentially exceed totalSupply before the airdrop is attempted
    __assume__(totalDistributed + $amount > totalSupply);

    // Store the state before attempting the doAirdrop
    uint256 beforeDistributed = totalDistributed;

    // Due to the limitation in emulating try-catch constructs, an alternative approach to capturing failure due to supply constraint is required
    bool isAirdropAttempted = false; // This flag will help us detect if the function was at least called
    bool exceedsSupplyAfterAirdrop = (totalDistributed + $amount) > totalSupply; // This boolean denotes if after the airdrop, the supply is exceeded

    doAirdrop(msg.sender, $amount); // Attempting the airdrop
    isAirdropAttempted = true; // If it reaches here, the airdrop did not revert, so it was at least attempted

    if (!exceedsSupplyAfterAirdrop) {
        // If it was not supposed to exceed the supply, ensure the airdrop successfully modified totalDistributed
        assert(totalDistributed == beforeDistributed + $amount);
    } else {
        // If the addition of $amount was assumed to exceed totalSupply, yet the airdrop was attempted, it implies an error in our rules/logic
        assert(isAirdropAttempted == false);
    }
}}