from game_model.db_helper import DBHelper, create_inmemory_db
from game_model.tests.common_fixtures import db_helper_with_one_user, db_helper


def test_before_adding_card(db_helper_with_one_user: DBHelper):
    new_user_id = 1
    players_cards = db_helper_with_one_user.get_player_cards(new_user_id)
    assert players_cards == []


def test_adding_a_card(db_helper_with_one_user: DBHelper):
    new_user_id = 1
    promt = "promt"
    saved_path = "saved_path"
    db_helper_with_one_user.add_card_to_user_deck(new_user_id, promt, saved_path)
    players_cards = db_helper_with_one_user.get_player_cards(new_user_id)
    assert len(players_cards) == 1
    new_card = players_cards[0]
    assert new_card.promt == promt
    assert new_card.image_path == saved_path
    assert new_card.author.id == new_user_id
    assert new_card.author.deck == new_card.deck
    assert db_helper_with_one_user.get_user_card_path_by_id(new_user_id, new_card.id) == saved_path


def test_deleting_a_card(db_helper_with_one_user: DBHelper):
    new_user_id = 1
    promt = "promt"
    saved_path = "saved_path"
    db_helper_with_one_user.add_card_to_user_deck(new_user_id, promt, saved_path)
    players_cards = db_helper_with_one_user.get_player_cards(new_user_id)

    new_card = players_cards[0]

    db_helper_with_one_user.delete_player_card(new_user_id, new_card.id)

    assert db_helper_with_one_user.get_player_cards(new_user_id) == []
