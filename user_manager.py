import logging
from app.models.user import User
from app.models.favorite import Favorite

class UserManager:
    def __init__(self, config_manager):
        self.config_manager = config_manager

    async def get_user_favorites(self, user_id):
        favorites = await Favorite.get_by_user(user_id)
        return [f.content_id for f in favorites]

    async def add_to_favorites(self, user_id, content_id):
        favorite = Favorite(user_id=user_id, content_id=content_id)
        await favorite.save()
        logging.info(f"Added content {content_id} to favorites for user {user_id}")

    async def remove_from_favorites(self, user_id, content_id):
        favorite = await Favorite.get_by_user_and_content(user_id, content_id)
        if favorite:
            await favorite.delete()
            logging.info(f"Removed content {content_id} from favorites for user {user_id}")
