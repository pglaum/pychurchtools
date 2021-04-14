# ChurchTools API

This is a python wrapper for the ChurchTools API.
The API from ChutchTools is provided using the Swagger toolset.
An overview of the available endpoints can be found here:
<https://wetzlar.church.tools/api>

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

You can execute the following in a python console to test the functionality.

```python3
from ct import CT

ct_wetzlar = CT()
ct_wetzlar.login('your_email', 'your_password')

events = c.Events.events()
events[0]
vars(events[0])
```

### Notes

- You can use the library for other ChurchTools instances by setting the
  `base_url` field to another URL.
- Set the `debugging` field from 0 - 2 for none to many debug messages.
- Times are in UTC
