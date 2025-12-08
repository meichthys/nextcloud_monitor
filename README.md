# NextcloudMonitor

Python wrapper around Nextcloud monitor api

## Installation

```bash
pip install nextcloudmonitor
```

## QuickStart

### Using an app password
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

### Using an access token
```python
>>> from nextcloudmonitor import NextcloudMonitor
>>> ncm = NextcloudMonitor("https://your_nextcloud_url", "", "serverinfo_access_token")
>>> ncm.data['nextcloud']['system']['version']
'16.0.5.1'
>>> ncm.data['activeUsers']['last24hours']
1
```

Notes:
 - The access token is a self-generated string set using `occ config:app:set serverinfo token --value your_access_token`
 - The access token is currently limited to the serverinfo app

## Change Log

- v1.0.0 : Initial Release
- v1.1.0 : Added basic error handling for api errors
- v1.2.0 : Allow ssl verification bypass
- v1.2.1 : Privide more detailed feedback for api connection errors
- v1.3.0 : Add more specific exceptions (Thanks @mib1185)
- v1.4.0 : Fix #4 key error (Thanks @mib1185)
- v1.5.0 : Support 'skip' parameter (Thanks @mib1185)
- v1.5.1 : Fix License Classifier (Thanks @joostlek)
- v1.5.2 : Add url and additional classifiers (Fixes #1)
