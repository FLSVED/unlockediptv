import logging
import asyncio
from app.core.exceptions import ConnectionError

class ConnectionManager:
    def __init__(self, config_manager, subscription_manager):
        self.config_manager = config_manager
        self.subscription_manager = subscription_manager
        self.reconnection_attempts = {}

    async def handle_connection(self, server_url, mac_address):
        try:
            if await self.subscription_manager.connect(server_url, mac_address):
                self.reconnection_attempts[mac_address] = 0
                return True
        except ConnectionError:
            self.reconnection_attempts[mac_address] = self.reconnection_attempts.get(mac_address, 0) + 1
            if self.reconnection_attempts[mac_address] < 3:
                delay = 2 ** self.reconnection_attempts[mac_address]
                logging.warning(f"Failed to connect to {server_url} with MAC {mac_address}. Retrying in {delay} seconds.")
                await asyncio.sleep(delay)
                return await self.handle_connection(server_url, mac_address)
            else:
                logging.error(f"Failed to connect to {server_url} with MAC {mac_address} after 3 attempts.")
                return False
        except Exception as e:
            logging.error(f"Error handling connection: {e}")
            return False
