from IPy import IP


def gen_debug(request, extras=None):
    """Generate a debug object we can log."""
    dbg = {
        'X-Origin-Request': request.remote_addr,
        'X-Requested-Url': request.url,
        'X-Origin-UA': request.environ.get('HTTP_USER_AGENT'),
        'X-App-Version': '1.0.0'
    }
    if extras:
        dbg.update(extras)

    return dbg


def value_type(value):
    """Value type simply identifies if the passed value
    is a domain or IP address.

    @param  string  text to test as an IP
    @returns    domain or IP
    """
    try:
        IP(value)
        return 'ip'
    except:
        return 'domain'


def upper_first(x):
    """Capitalize the first letter only while keeping existing case.

    :param x: String value to capitalize
    :return: String with the first letter capitalized
    """
    return x[0].upper() + x[1:]


def bool_to_string(value):
    """Take in a boolean and convert it to a str type

    :param value: boolean value
    :type value: str
    :returns: converted string to a real bool
    """
    positive = ("yes", "y", "true",  "t", "1")
    if str(value).lower() in positive:
        return True
    negative = ("no",  "n", "false", "f", "0", "0.0", "", "none", "[]", "{}")
    if str(value).lower() in negative:
        return False
    raise Exception('Invalid value for boolean conversion: ' + str(value))


def safe_symbols(text):
    """Convert non-XML characters to safe values.

    :param text: Text to inspect
    :return: Cleaned up version of text
    """
    if type(text) in [str, unicode]:
        text = text.replace("&", "&amp;")
        text = text.replace("\"", "&quot;")
        text = text.replace("'", "&apos;")
        text = text.replace("<", "&lt;")
        text = text.replace(">", "&gt;")
    if type(text) == bool:
        text = str(text).lower()
    if type(text) in [dict, list, int]:
        text = str(text)

    return text
