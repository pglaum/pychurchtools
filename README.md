# ChurchTools API

This is a python wrapper for the ChurchTools API.
The API from ChurchTools is provided using the Swagger toolset.
An overview of the available endpoints can be found here:
<https://wetzlar.church.tools/api>

__Note:__ This library is very incomplete and WIP.
Many endpoints are not implemented at all and the others are only partly
implemented.

## Installation

Dependencies:

- `requests`

## Usage

### Authentication

#### Via a cookie

Login to churchtools in your browser and copy the cookie.
The cookie object looks like this:

```python3
cookie = {
  'ChurchTools_ct_wetzlar': 'some_random_text',
}
```

Pass this object to the init function of the CT class or set the field `cookie`
in the CT object.

#### Via old AJAX API

Since the login function does not seem to be implemented in the new REST API, we
have to use the old AJAX API.
The CT class provides a method `login` to log you in and set the cookie
automatically.

```python3
ct.login('your_email', 'your_password')
```

### Example

You can execute the following in a python script to test the functionality.

```python3
from ct import CT

c = CT()
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

- You can use the library for other ChurchTools instances by setting the
  `base_url` field to another URL.
- Set the `debugging` field from 0 - 2 for none to many debug messages.
- Times are in UTC
