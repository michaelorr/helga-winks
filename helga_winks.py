from helga.plugins import command


@command('wink', aliases=['winks'], help='winks @ u')
def winks(client, channel, nick, message, cmd, args):
    """
    ~*~*~* winks @ u *~*~*~
    """
    if len(args) == 0:
        return u'~*~*~* {0} winks @ u *~*~*~'.format(nick)
    elif len(args) == 1:
        return u'~*~*~* {0} winks @ {1} *~*~*~'.format(nick, args[0])
    else:
        return u'~*~*~* {0} {1} {2} *~*~*~'.format(nick, args[0], args[1])
