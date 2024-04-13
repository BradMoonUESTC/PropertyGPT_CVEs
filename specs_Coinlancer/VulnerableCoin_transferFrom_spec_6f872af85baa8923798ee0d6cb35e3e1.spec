pragma solidity 0.6.12;

contract VulnerableCoin {string public constant symbol = "VULN";
string public constant name = "VulnerableCoin";
uint8 public constant decimals = 18;
uint256 private _totalSupply = 300 * 10**6 * 10**18;
address public owner;
mapping(address => uint256) balances;
mapping(address => mapping(address => uint256)) allowed;

function transferFrom(address,address,uint256) public returns(bool) {}

rule TransferFromTotalBalanceInvariant() {
    address $from;
    address $to;
    uint256 $amount;
    uint256 balancesFromBefore = balances[$from];
    uint256 balancesToBefore = balances[$to];

    __assume__($from != address(0));
    __assume__($to != address(0));
    __assume__($from != $to); // Ensure from and to are different addresses
    __assume__(msg.sender == 0x0000000000000000000000000000000000000001);

    transferFrom($from, $to, $amount);

    assert(balances[$from] == balancesFromBefore - $amount);
    assert(balances[$to] == balancesToBefore + $amount);
}}