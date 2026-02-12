import arcade

from src.constants import SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE
from src.views.menu_view import MenuView


def main() -> None:
    print("INIT DB CALLED")
    from src.systems import stats_db
    stats_db.init_db()
    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE, resizable=False)
    window.show_view(MenuView())
    window.sound_enabled = True
    arcade.run()


if __name__ == "__main__":
    main()
