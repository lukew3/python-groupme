# python-groupme
Python wrapper for the GroupMe api

## Usage
Go to [https://dev.groupme.com/](https://dev.groupme.com/), sign in, and click on 'Access token' in the nav bar to see your access token. Then, use it in your program like this:
```
import groupme

token = '8hCBM8K65hH4nQdhvwHObjBBDTvR8MieakFFBSE6' # Use your own token
g = groupme.GroupMe(token)
print(g.groups())
```

## Development
Install requirements:
```
pip install -r requirements.txt
```

Install locally:
```
pip install -e .
```
