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


rule ValidateClaimOwnersEarningsProcessCorrected() {
    address payable $owner;
    uint256 $gameEarnings;
    bool $sendSuccess;

    // Store initial gameEarnings
    uint256 $gameEarningsBefore = $gameEarnings;

    // Simulating the execution of the claimOwnersEarnings function
    if ($gameEarningsBefore != 0) {
        $sendSuccess = $owner.send($gameEarningsBefore);
        if ($sendSuccess) {
            // After successful transfer, assert gameEarnings is reset to 0
            assert($gameEarnings == 0);
        } else {
            // If the send fails, gameEarnings should remain unchanged
            assert($gameEarnings == $gameEarningsBefore);
        }
    } else {
        // If gameEarnings was initially 0, ensure it remains 0 (no action taken condition)
        assert($gameEarnings == 0);
    }
}}