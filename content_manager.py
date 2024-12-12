import logging
from app.models.channel import Channel
from app.models.vod import VOD
from app.schemas.content import ChannelSchema, VODSchema
from app.utils.parser import IPTVContentParser
from app.core.exceptions import ConnectionError
from app.services.quality_manager import QualityManager
from app.services.cache_manager import CacheManager

class ContentManager:
    def __init__(self, config_manager, quality_manager, cache_manager):
        self.config_manager = config_manager
        self.quality_manager = quality_manager
        self.cache_manager = cache_manager

    async def connect(self, server_url, mac_address, driver, parser):
        try:
            if await self.test_connection(server_url, mac_address, driver, parser):
                return True
        except ConnectionError:
            logging.warning(f"Failed to connect to server {server_url} with MAC {mac_address}")
        return False

    async def test_connection(self, server_url, mac_address, driver, parser):
        try:
            content = await self.fetch_server_content(server_url, mac_address, driver)
            if content:
                channels, vod = parser.parse_content(content)
                logging.info(f"Channels: {[c.name for c in channels]}")
                logging.info(f"VOD: {[v.title for v in vod]}")
                await self.cache_content(server_url, channels, vod)
                return True
            else:
                raise ConnectionError(f"Failed to fetch server content for {server_url} with MAC {mac_address}")
        except Exception as e:
            logging.error(f"Error connecting to server: {e}")
            raise ConnectionError(f"Error connecting to server {server_url} with MAC {mac_address}")

    async def fetch_server_content(self, server_url, mac_address, driver):
        try:
            driver.get(server_url)
            content = driver.page_source
            return content
        except Exception as e:
            logging.error(f"Error fetching server content: {e}")
            return None

    async def cache_content(self, server_url, channels, vod):
        self.cache_manager.set_in_cache(f"channels_{server_url}", ChannelSchema(many=True).dump(channels))
        self.cache_manager.set_in_cache(f"vod_{server_url}", VODSchema(many=True).dump(vod))

    async def get_channels(self, server_url):
        cached_channels = self.cache_manager.get_from_cache(f"channels_{server_url}")
        if cached_channels:
            return ChannelSchema(many=True).load(cached_channels)
        else:
            # Fetch channels from server and cache them
            pass

    async def get_vod(self, server_url):
        cached_vod = self.cache_manager.get_from_cache(f"vod_{server_url}")
        if cached_vod:
            return VODSchema(many=True).load(cached_vod)
        else:
            # Fetch VOD from server and cache them
            pass

    async def play_stream(self, user_id, stream_url):
        adjusted_url = await self.quality_manager.adjust_quality(user_id, stream_url)
        # Use VLC or other player to play the stream
