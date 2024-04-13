// SPDX-License-Identifier: MIT
pragma solidity 0.6.12;

contract SimplifiedEncryptedToken {
    address public owner;
    uint256 public totalSupply;
    uint256 public buyPrice;
    mapping (address => uint256) public balanceOf;
    uint256 public testVar;
    event Transfer(address indexed from, address indexed to, uint256 value);

    // Constructor
    constructor(uint256 initialSupply) public {
        owner = msg.sender;
        totalSupply = initialSupply * 10 ** uint256(18);
        balanceOf[msg.sender] = totalSupply;
    }

    modifier onlyOwner {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    function _transfer(address _from, address _to, uint _value) internal {
        require(_to != address(0), "Cannot transfer to the zero address");
        require(balanceOf[_from] >= _value, "Insufficient balance");
        require(balanceOf[_to] + _value >= balanceOf[_to], "Overflow detected");
        balanceOf[_from] -= _value;
        balanceOf[_to] += _value;
        emit Transfer(_from, _to, _value);
    }

    // Setting a new purchase price
    function setPrices(uint256 newBuyPrice) public {
        buyPrice = newBuyPrice;
    }

    // Testing function
    function test(uint256 newBuyPrice) public payable {
        setPrices(newBuyPrice);
        uint amount = msg.value * buyPrice; // Calculate amount
        testVar=amount;
    }

    // Transfer ownership
    function transferOwnership(address newOwner) public onlyOwner {
        owner = newOwner;
    }

    // Allow the contract to receive Ether
    receive() external payable {}
}
