# Value-Vista

A website for demoing [Value-Investing-Strategy](https://github.com/jm0rt1/CSE682-Project) system's capabilities.

## Development

To run this website locally, first make sure you have python installed in your local machine. Then run the following commands

```sh
# install pipenv
pip install pipenv

# Activate the virtual environment
pipenv shell

# Install dependency
pipenv install

# Run the flask app
export FLASK_APP='value_vista.py'
flask run --debug
```

