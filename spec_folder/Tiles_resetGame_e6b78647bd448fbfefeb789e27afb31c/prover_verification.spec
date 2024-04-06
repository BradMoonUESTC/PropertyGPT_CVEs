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

rule VerifyResetGameFunction() {
    address $winner;
    uint256 currentBalanceBefore = currentGameBalance;
    uint256 winnerBalanceBefore = pendingWithdrawals[$winner];
    uint256 earningsBefore = gameEarnings;
    bool changeCostFlagBefore = willChangeCost;
    uint256 gameCostBefore = currentGameCost;
    uint256 currentGameNumberBefore = currentGameNumber;

    resetGame($winner);

    uint256 winningAmount = currentBalanceBefore * 9 / 10;
    uint256 remainder = currentBalanceBefore - winningAmount;

    assert(currentGameBalance == 0);
    assert(pendingWithdrawals[$winner] == winnerBalanceBefore + winningAmount);
    assert(gameEarnings == earningsBefore + remainder);
    assert(currentGameNumber == currentGameNumberBefore + 1);
    assert(numTilesClaimed == 0);
    
    if (changeCostFlagBefore) {
        assert(currentGameCost != gameCostBefore);
    } else {
        assert(currentGameCost == gameCostBefore);
    }
    assert(willChangeCost == false);
}}