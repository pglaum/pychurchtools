# pychurchtools

This is a python wrapper for the ChurchTools API.
The API from ChurchTools is provided using the Swagger toolset.

__Note:__ This library is WIP.
Some endpoints are not implemented at all and the others are only partly
implemented.

## Installation

To install from PyPI, you can use "`pip install churchtools`".
Type "`pip uninstall churchtools`" to remove the library.

Dependencies:

- `pydantic`
- `requests`

## Usage

### Authentication

#### Via a cookie

Login to churchtools in your browser and copy the cookie.
The cookie object looks something like this:

```python3
cookie = {
  'ChurchTools_ct_<church_name>': 'some_random_text',
}
```

Pass this object to the init function of the `ChurchTools` class or set the
field `cookie` in the `ChurchTools` object.

#### Via REST API

The `ChurchTools` class provides a method `login` to log you in and set the
cookie automatically.

```python3
ct.login('your_email', 'your_password')
```

### Example

You can execute the following in a python script to test the functionality.

```python3
from churchtools import ChurchTools

c = ChurchTools('https://<church_name>.church.tools')
c.login('your_email', 'your_password')

events = c.events.list()
print('Upcoming event:', events[0].__repr__())
print(events[0].dict())
print()

me = c.general.whoami()
print('Logged in as:', me.__repr__())
print()

my_events = c.person.events(me.id)
print('Your next events:')
[print(f'- {e.__repr__()}') for e in my_events]
```

### Notes

- Set the `debugging` field from 0 - 2 for none to many debug messages.
- Times are in UTC

## Tests

- Create a CT instance here: <https://ccp.church.tools/demo>
- Set the environment variables `CHURCHTOOLS_URL`, `CHURCHTOOLS_USER` & `CHURCHTOOLS_PASSWORD`
- Run `pytest`
