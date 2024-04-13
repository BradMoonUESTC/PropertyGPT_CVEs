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

contract Primeo{address public owner;
mapping (address => uint256) private balances;
mapping (address => mapping (address => uint256)) private allowed;
string public constant name = "Primeo";
string public constant symbol = "PEO";
uint public constant decimals = 8;
uint256 public totalSupply = 10000000000 * 10**decimals;
uint256 public totalDistributed = 0;
bool public distributionFinished = false;
function doAirdrop(address,uint256) public   
precondition{
    amount > 0;
    totalDistributed + amount <= totalSupply;
}

postcondition{
    balances[participant] == __old__(balances[participant]) + amount;
    totalDistributed == __old__(totalDistributed) + amount;
    distributionFinished == (totalDistributed >= totalSupply) ? true : __old__(distributionFinished);
}
}