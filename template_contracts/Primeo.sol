// SPDX-License-Identifier: MIT
pragma solidity 0.6.12;

/**
 * @title SafeMath
 * @dev Unsigned math operations with safety checks that revert on error.
 */
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

/**
 * @title Primeo Token Contract
 * @dev Implementation of a custom token with distribution mechanisms.
 */
contract Primeo {
    using SafeMath for uint256;

    address public owner;
    mapping (address => uint256) private balances;
    mapping (address => mapping (address => uint256)) private allowed;

    string public constant name = "Primeo";
    string public constant symbol = "PEO";
    uint public constant decimals = 8;
    
    uint256 public totalSupply = 10000000000 * 10**decimals;
    uint256 public totalDistributed = 0;
    
    bool public distributionFinished = false;

    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);
    event DistrFinished();
    event Airdrop(address indexed owner, uint256 amount, uint256 balance);

    modifier canDistr() {
        require(!distributionFinished, "Distribution is finished");
        _;
    }

    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    constructor() public {
        owner = msg.sender;
    }

    function doAirdrop(address participant, uint256 amount) public canDistr {
        require(amount > 0, "Amount must be greater than zero");
        require(totalDistributed.add(amount) <= totalSupply, "Would exceed total supply");

        balances[participant] = balances[participant].add(amount);
        totalDistributed = totalDistributed.add(amount);

        if (totalDistributed >= totalSupply) {
            distributionFinished = true;
        }

        emit Airdrop(participant, amount, balances[participant]);
        emit Transfer(address(0), participant, amount);
    }
}
