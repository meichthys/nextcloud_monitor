# NextcloudMonitor

Python wrapper around Nextcloud monitor api

## Installation

```bash
pip install nextcloudmonitor
```

## QuickStart

```python
>>> from nextcloudmonitor import NextcloudMonitor
>>> ncm = NextcloudMonitor("https://your_nextcloud_url", "nextcloud_admin_username", "nextcloud_app_password")
>>> ncm.data['nextcloud']['system']['version']
'16.0.5.1'
>>> ncm.data['activeUsers']['last24hours']
1
```

Notes:

- The user must be a user that has access to the nextcloud monitor api (generally an admin user)
- The nextcloud app password should be generated from the nextcoud security settings page.

## Change Log

- v1.0.0 : Initial Release
- v1.1.0 : Added basic error handling for api errors
- v1.2.0 : Allow ssl verification bypass