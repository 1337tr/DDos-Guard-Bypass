from DDosGuardBypasser.Bypass import ddosGuard

Bypass = ddosGuard().Bypass('https://doxbin.org/')

if Bypass['Success']:
    print('Successfully bypassed DDos-Guard')
else:
    print(Bypass['message'])