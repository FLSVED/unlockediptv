import logging
from app.models.subscription import Subscription
from app.core.exceptions import AuthenticationError

class SecurityManager:
    def __init__(self, config_manager, subscription_manager):
        self.config_manager = config_manager
        self.subscription_manager = subscription_manager

    async def verify_subscription(self, server_url, mac_address):
        subscription = await Subscription.get_by_server_and_mac(server_url, mac_address)
        if subscription and subscription.is_active():
            return True
        else:
            logging.warning(f"Invalid subscription for server {server_url} and MAC {mac_address}")
            raise AuthenticationError("Invalid subscription")

    async def block_suspicious_connections(self, mac_address):
        # Implement logic to block suspicious connection attempts
        logging.warning(f"Blocking suspicious connection attempt from MAC {mac_address}")
