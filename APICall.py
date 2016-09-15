import requests

resp = requests.get("http://example.com/foo/bar")

if resp.status_code != 200:
    # This means something went wrong.
    raise ApiError('GET /bar/ {}'.format(resp.status_code))

