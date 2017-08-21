# CSResumeBot
----
The CSResumeBot is a collection of scripts that scrapes the [/r/cscareerquestions](https://www.reddit.com/r/cscareerquestions/) reoccurring resume advice thread. Initially the bot searches for previous Resume Advice threads, parses the top levle comments for hyperlinks, determines the valid links, then retrieves the image link.

Subsequent scripts the download the images storing both their original URL and system paths in a MongoDB. 

Once the resumes have been collected, custom image filtering is conducted on each resume in preparation for scanning with the open source Tesseract Optical Character Recognition (OCR) libraries.

The parsed resumes are then validated and the data is extracted into the database for future analysis.

## Instructions
----

### Requirements

The CSResumeBot assumes that you have properly installed Python and are operating in virtual environments using [virtualenv](https://virtualenv.pypa.io/en/stable/) and [virtualenvwrapper](http://virtualenvwrapper.readthedocs.io/en/latest/), in addition to ahving a function installation of [MongoDB](https://docs.mongodb.com/manual/installation/).

### Setup
Once the requirements have been met, clone or download the repository and witch to your virtual environment. Then install the required packages using pip:

`$ pip freeze install -r requirements.txt`

Once the required packages have been installed run `bot.py` to begin building and populating the initial database from the archived Resume Advice threads.