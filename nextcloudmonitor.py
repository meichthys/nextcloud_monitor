"""Contains the NextcloudMonitor class"""

import requests


class NextcloudMonitor:
    """An object containing a dictionary representation of dat returned by
    Nextcloud's monitoring api

    Attributes:
        nextcloud_url (str): Full https url to a nextcloud instance
        user (str): Username of the Nextcloud user with access to the monitor api
        app_password (str): App password generated from Nextcloud security settings page
        verify_ssl (bool): Allow bypassing ssl verification, but verify by default
    """

    def __init__(self, nextcloud_url, user, app_password, verify_ssl=True):
        self.data = dict()
        self.api_url = (
            f"{nextcloud_url}/ocs/v2.php/apps/serverinfo/api/v1/info?format=json"
        )
        self.user = user
        self.password = app_password
        self.verify_ssl = verify_ssl
        self.update()

    def update(self):
        try:
            response = requests.get(
                self.api_url, auth=(self.user, self.password), verify=self.verify_ssl
            )
            self.data = response.json()["ocs"]["data"]
        except:
            raise NextcloudMonitorError(
                "Could not fetch nextcloud api data. Check your url, username and password and try again"
            )


class NextcloudMonitorError(Exception):
    """Failed to fetch nextcloud monitor data."""

    pass
