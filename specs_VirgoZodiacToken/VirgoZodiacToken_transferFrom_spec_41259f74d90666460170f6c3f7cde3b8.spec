pragma solidity 0.6.12;

contract VirgoZodiacToken {address owner;
mapping(address => uint256) private balances;
mapping(address => mapping(address => uint256)) private allowed;

function transferFrom(address,address,uint256) public returns(bool) {}

rule transferFromEnsuresBalancesAndAllowanceUpdate() {
    address $from;
    address $to;
    uint256 $value;
    uint256 $initBalanceFrom;
    uint256 $initBalanceTo;
    uint256 $allowance;

    require($value != 0);
    require(balances[$from] == $initBalanceFrom);
    require(allowed[$from][msg.sender] == $allowance);
    require($allowance >= $value);
    require($initBalanceFrom >= $value); // Ensure sufficient funds
    require(balances[$to] == $initBalanceTo); // Initial balance of receiver

    __assume__(msg.sender != $to); // Different sender and receiver

    transferFrom($from, $to, $value);

    assert(balances[$from] == $initBalanceFrom - $value); // from balance decreased
    assert(balances[$to] == $initBalanceTo + $value); // to balance increased
    assert(allowed[$from][msg.sender] == $allowance - $value); // allowance updated
}}