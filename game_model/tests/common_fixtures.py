import pytest

from game_model.db_helper import DBHelper, create_inmemory_db


@pytest.fixture
def db_helper():
    db_helper = create_inmemory_db()
    yield db_helper
    db_helper.db.provider = db_helper.db.schema = None


@pytest.fixture
def db_helper_with_one_user(db_helper: DBHelper):
    new_user_id = 1
    db_helper.register_player_if_not_exist(user_id=new_user_id, username="username")
    return db_helper


@pytest.fixture
def db_helper_game_ready(db_helper: DBHelper):
    num_users = 3
    cards_per_user = 60

    for i in range(num_users):
        db_helper.register_player_if_not_exist(user_id=i, username=f"username-{i}")
        for j in range(cards_per_user):
            db_helper.add_card_to_user_deck(i, f"promt-{i}-{j}", f"path-{i}-{j}")

    return db_helper
