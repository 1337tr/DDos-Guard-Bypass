<h1 align='center'>Bypass DDos-Guard.net</h1>

<p align='center'>  Python3 requests-based DDos-Guard bypass </p>

## Features
* Requests-based
* Proxy support
* lightweight
* Fast

## Requirements
```
pip install tls-client==0.2.1
```

## Usage
```python3
from DDosGuardBypasser.Bypass import ddosGuard

Bypass = ddosGuard().Bypass('https://targetSite.org/')

if Bypass['Success']:
    print('Successfully bypassed DDos-Guard')
else:
    print(Bypass['message'])
```
