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

function resetGame(address) public  {}

rule ResetGameUpdatesCorrectly() {
    address $winner;
    uint256 $winningAmount = uint(currentGameBalance) * uint(9) / uint(10);
    uint256 $remainder = currentGameBalance - $winningAmount;
    
    uint256 gameBalanceBefore = currentGameBalance;
    uint256 numTilesClaimedBefore = numTilesClaimed;
    uint256 currentGameNumberBefore = currentGameNumber;
    uint256 winnerPendingWithdrawalBefore = pendingWithdrawals[$winner];
    uint256 gameEarningsBefore = gameEarnings;
    bool willChangeCostBefore = willChangeCost;
    uint256 currentGameCostBefore = currentGameCost;

    resetGame($winner);

    assert(currentGameBalance == 0);
    assert(gameToWinner[currentGameNumberBefore] == $winner);
    assert(currentGameNumber == currentGameNumberBefore + 1);
    assert(numTilesClaimed == 0);
    assert(pendingWithdrawals[$winner] == winnerPendingWithdrawalBefore + $winningAmount);
    assert(gameEarnings == gameEarningsBefore + $remainder);
    
    if (willChangeCostBefore) {
        assert(currentGameCost != currentGameCostBefore);
        assert(willChangeCost == false);
    } else {
        assert(currentGameCost == currentGameCostBefore);
        assert(willChangeCost == false);
    }
}}