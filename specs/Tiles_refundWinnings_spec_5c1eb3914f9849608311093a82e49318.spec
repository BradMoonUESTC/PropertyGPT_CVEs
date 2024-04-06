pragma solidity 0.4.26;

contract Tiles {uint public constant NUM_TILES = 256;
uint constant SIDE_LENGTH = 16;
uint private constant STARTING_GAME_NUMBER = 1;
uint public DEFAULT_GAME_COST = 5000000000000000;
address private owner;
uint public currentGameNumber;
uint public currentGameBalance;
uint public numTilesClaimed;
Tile[16][16] public tiles;
bool public gameStopped;
uint public gameEarnings;
bool public willChangeCost;
uint public currentGameCost;
uint public nextGameCost;
mapping (address => uint) public pendingWithdrawals;
mapping (uint => address) public gameToWinner;
struct Tile {
        uint gameClaimed;
        address claimedBy;
    }

function refundWinnings() public  {}

rule NoLossOfPendingWithdrawalAmount() {
    address $currAddress;
    uint $startAmount;
    pendingWithdrawals[$currAddress] = $startAmount;
    uint $currAmountBefore = pendingWithdrawals[$currAddress];
    refundWinnings();
    uint $currAmountAfter = pendingWithdrawals[$currAddress];
    
    if ($startAmount != 0) {
        assert($currAmountAfter <= $currAmountBefore);
    } else {
        assert($currAmountAfter == $currAmountBefore);
    }
}}