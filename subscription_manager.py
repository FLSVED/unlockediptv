import re
import logging
import asyncio
from app.utils.chromedriver import setup_chromedriver
from app.core.exceptions import ConnectionError
from app.services.content_manager import ContentManager
from app.utils.xtream_parser import XtreamParser
from app.utils.mac_portal_parser import MacPortalParser
from app.utils.stalker_portal_parser import StalkerPortalParser
from app.models.subscription import Subscription

class SubscriptionManager:
    def __init__(self, config_manager, security_manager, connection_manager):
        self.config_manager = config_manager
        self.security_manager = security_manager
        self.connection_manager = connection_manager
        self.parsers = {
            "Xtream": XtreamParser(),
            "MAC Portal": MacPortalParser(),
            "Stalker Portal": StalkerPortalParser()
        }

    async def connect(self, server_url, mac_address, mode="Xtream"):
        try:
            driver = await setup_chromedriver()
            parser = self.parsers[mode]
            if await self.security_manager.verify_subscription(server_url, mac_address):
                if await self.connection_manager.handle_connection(server_url, mac_address):
                    if await self.content_manager.connect(server_url, mac_address, driver, parser):
                        return True
        except ConnectionError:
            logging.warning(f"Failed to connect to server {server_url} with MAC {mac_address}")
        finally:
            driver.quit()
        return False

    async def manage_subscriptions(self, data, mode="Xtream"):
        try:
            parser = self.parsers[mode]
            urls, devices = parser.parse_data(data)
            tasks = [self.connect(url, device['mac'], mode) for url in urls for device in devices]
            results = await asyncio.gather(*tasks)
            logging.info(f"Subscription results: {results}")
            return results
        except Exception as e:
            logging.error(f"Error managing subscriptions: {e}")
            return []

    async def check_connectivity(self):
        tasks = []
        for subscription in await Subscription.get_all():
            tasks.append(self.connection_manager.handle_connection(subscription.server_url, subscription.mac_address))
        await asyncio.gather(*tasks)
