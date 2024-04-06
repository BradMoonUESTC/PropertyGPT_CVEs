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
    uint256 $init_gameBalance;
    currentGameBalance = $init_gameBalance;
    uint256 winningAmountBefore = pendingWithdrawals[$winner];
    uint256 gameEarningsBefore = gameEarnings;
    uint256 $currentGameNumberBefore = currentGameNumber;
    uint256 $numTilesClaimedBefore = numTilesClaimed;

    resetGame($winner);

    uint256 expectedWinningAmount = uint($init_gameBalance) * 9 / 10;
    uint256 expectedRemainder = $init_gameBalance - expectedWinningAmount;
    
    // Check if winner's pending withdrawal has increased correctly
    assert(pendingWithdrawals[$winner] == winningAmountBefore + expectedWinningAmount);

    // Check if game earnings updated correctly
    assert(gameEarnings == gameEarningsBefore + expectedRemainder);

    // Check if the game balance is reset to 0
    assert(currentGameBalance == 0);

    // Check if the currentGameNumber is incremented
    assert(currentGameNumber == $currentGameNumberBefore + 1);

    // Check if numTilesClaimed is reset to 0
    assert(numTilesClaimed == 0);

    // Verify gameToWinner mapping is updated correctly.
    assert(gameToWinner[$currentGameNumberBefore] == $winner);
}}