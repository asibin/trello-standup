Prerequisites:
--------------
* python 2.7+
* git standup - install from here https://github.com/kamranahmedse/git-standup

Tested only on Mac OSX.

How to install
--------------
Create virtualenv (recommended) and switch to it.
Run `pip install -r requirements.txt` to install required packages

Configuration
-------------
Configure the app in `settings-sample.py` and rename it to `settings.py`. This file is
 ignored in `.gitignore` as to avoid pushin your credentials to git.


Running
-------
Run without parameters `python trello-standup.py` and if everything is ok you should see your
trello populated.

Caveats
-------
Script does not track existing comments so running it twice will duplicate comments.

TODO
----
* Exception handling
* Retrying on failed response
* Automate token retrieval