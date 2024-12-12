import logging
import asyncio
from app.utils.network_utils import get_network_stats

class QualityManager:
    def __init__(self, config_manager):
        self.config_manager = config_manager
        self.quality_levels = {
            "low": {"bitrate": 500, "resolution": "480p"},
            "medium": {"bitrate": 1000, "resolution": "720p"},
            "high": {"bitrate": 2000, "resolution": "1080p"},
            "ultra": {"bitrate": 4000, "resolution": "4K"}
        }

    async def get_optimal_quality(self, user_id):
        network_stats = await get_network_stats(user_id)
        for quality, specs in self.quality_levels.items():
            if network_stats["bandwidth"] >= specs["bitrate"] and network_stats["latency"] <= 100:
                logging.info(f"Optimal quality for user {user_id}: {quality}")
                return quality
        return "low"

    async def adjust_quality(self, user_id, stream_url):
        quality = await self.get_optimal_quality(user_id)
        specs = self.quality_levels[quality]
        adjusted_url = f"{stream_url}?bitrate={specs['bitrate']}&resolution={specs['resolution']}"
        return adjusted_url
