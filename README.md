# CORS Proxy Server

To solve the CORS (Cross-origin resource sharing) problem.

# Install

```
pip install tornado
```

# Config

Edit the `conf.py`

```
port = 8080
remote_host = 'https://your.hosts.com'
static_file_dir = '/Users/scrat/your_static_file_dir/'
```

# Run

```
$ python app.py
```
