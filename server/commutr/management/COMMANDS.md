## What the frick is going on here?

This package contains a directory called `commands`, in here we define custom Django commands which we can run from the `manage.py` Django manager script. Examples of custom commands we are using are for creating new news sources, and for scraping news articles for a specific source. These commands are usually just for easing development processes and speeding up mundane activities like generating spoof data for our local database.

## I wanna make a command!
Okay, copy one of the existing files. Your new command will be named after the file, so for a file `my_new_command.py` we would run it with: `python manage.py my_new_command`. Replace the logic in the `handle` method and don't forget to override the `help` field to briefly describe your command.