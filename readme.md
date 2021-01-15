# Media Suite Coding Exercise

To get the project up and running:

- Create and activate a virtual environment. For example:

```
$ python3 -m virtualenv --python=python3.x venv
$ . venv/bin/activate
```

- Install packages into the environment:

```
pip3 install -r blog/requirements.txt
```

- Load the post data into the Database:

```
python3 blog/manage.py loadposts
```

- Run the server

```
./run_django.sh
```

Open your preferred web browser to the URL localhost:3000 and you should see a list of posts!

You can test the API from the command line.

To get the list of posts and their data:
```
curl http://localhost:3000/posts-list Accept:application/json
```

To get a singular post and it's data:
```
curl http://localhost:3000/post-detail/<slug> Accept:application/json
```

The Django REST framework also offers a web browsable API. The following links will open the API in your browser:

- List of posts: http://localhost:3000/posts-list
- Singular post: http://localhost:3000/post-detail/<slug> (e.g http://localhost:3000/post-detail/people-do-good)
