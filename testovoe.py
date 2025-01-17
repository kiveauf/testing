from pprint import pprint
import random
import math

TIMESTAMPS_COUNT = 60000

PROBABILITY_SCORE_CHANGED = 0.0002

PROBABILITY_HOME_SCORE = 0.45

OFFSET_MAX_STEP = 4

INITIAL_STAMP = {
    "offset": 0,
    "score": {
        "home": 0,
        "away": 0
    }
}


def _print(thing):
    print(thing)


def generate_stamp(previous_value):
    score_changed = random.random() > 1 - PROBABILITY_SCORE_CHANGED
    home_score_change = 1 if score_changed and random.random() > 1 - \
        PROBABILITY_HOME_SCORE else 0
    away_score_change = 1 if score_changed and not home_score_change else 0
    offset_change = math.floor(random.random() * OFFSET_MAX_STEP) + 1

    return {
        "offset": previous_value["offset"] + offset_change,
        "score": {
            "home": previous_value["score"]["home"] + home_score_change,
            "away": previous_value["score"]["away"] + away_score_change
        }
    }


def generate_game():
    stamps = [INITIAL_STAMP, ]
    current_stamp = INITIAL_STAMP
    for _ in range(TIMESTAMPS_COUNT):
        current_stamp = generate_stamp(current_stamp)
        stamps.append(current_stamp)

    return stamps


def get_score(game_stamps, offset):  #binary search
    '''
        Takes list of game's stamps and time offset for which returns the scores for the home and away teams.
        Please pay attention to that for some offsets the game_stamps list may not contain scores.
    '''
    if isinstance(game_stamps, list) and isinstance(offset, int):
        begin = 0
        last = len(game_stamps)-1
        while begin <= last:
            mid = (last + begin)//2
            if game_stamps[mid]["offset"] == offset:
                home = game_stamps[mid]["score"]["home"]
                away = game_stamps[mid]["score"]["away"]

                return home, away
            else:
                if offset < game_stamps[mid]["offset"]:
                    last = mid - 1
                else:
                    begin = mid + 1

    return None, None



    

game_stamps = generate_game()

pprint(game_stamps)

pprint(get_score(game_stamps, 100000))
