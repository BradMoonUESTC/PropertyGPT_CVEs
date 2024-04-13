// SPDX-License-Identifier: MIT
pragma solidity 0.6.12;

contract VulnerableCoin {
    string public constant symbol = "VULN";
    string public constant name = "VulnerableCoin";
    uint8 public constant decimals = 18;
    uint256 private _totalSupply = 300 * 10**6 * 10**18; // 300 million tokens with 18 decimals
    
    address public owner;
    mapping(address => uint256) balances;
    mapping(address => mapping(address => uint256)) allowed;
    
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);
    
    constructor() public {
        owner = msg.sender;
        balances[owner] = _totalSupply;
    }
    
    function totalSupply() public view returns (uint256) {
        return _totalSupply;
    }
    
    function balanceOf(address account) public view returns (uint256) {
        return balances[account];
    }
    
    function transfer(address to, uint256 amount) public returns (bool) {
        require(balances[msg.sender] >= amount, "Insufficient balance");
        require(to != address(0), "Transfer to the zero address");
        
        balances[msg.sender] -= amount;
        balances[to] += amount;
        emit Transfer(msg.sender, to, amount);
        return true;
    }
    
    function approve(address spender, uint256 amount) public returns (bool) {
        allowed[msg.sender][spender] = amount;
        emit Approval(msg.sender, spender, amount);
        return true;
    }
    
    function allowance(address owner, address spender) public view returns (uint256) {
        return allowed[owner][spender];
    }
    
    function transferFrom(address from, address to, uint256 amount) public returns (bool) {
        require(amount <= balances[from], "Insufficient balance");
        require(amount <= allowed[from][msg.sender], "Insufficient allowance");
        require(to != address(0), "Transfer to the zero address");
        
        balances[from] -= amount;
        allowed[from][msg.sender] -= amount;
        balances[to] += amount;
        emit Transfer(from, to, amount);
        return true;
    }

    function testFunction() public {
        require(msg.sender != owner, "Caller must be the owner");
    }
}
