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

function claimOwnersEarnings() public  {}

rule VerifyOwnersEarningsAfterClaim(){
    uint256 $initialEarnings;
    address payable $contractOwner;
    gameEarnings = $initialEarnings;

    // Simulate the claimOwnersEarnings function call
    claimOwnersEarnings();

    if ($initialEarnings != 0 && $contractOwner.send($initialEarnings)) {
        // If gameEarnings was not 0 and the send to owner was successful,
        // validate that gameEarnings is reset to 0.
        assert(gameEarnings == 0);
    } else {
        // If gameEarnings was 0 initially or send failed,
        // validate that gameEarnings remains the same.
        assert(gameEarnings == $initialEarnings);
    }
}}