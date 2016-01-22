# coding: utf8
from datetime import datetime
import re
import unittest

# Format for wiki links.
RE_LINKS = re.compile('(<<)(.*?)(>>)')

db.define_table('users',
    Field('user_id', db.auth_user, readable = False, writable = False),
    Field('username', label = 'Username ', requires=IS_NOT_EMPTY(error_message='Please enter a username')),
    Field('sex', label = 'Sex ', requires = IS_IN_SET(['Male', 'Female'], zero = None)),
    Field('weight', label = 'Weight (lbs) ', requires=IS_FLOAT_IN_RANGE(0,500,error_message='Please choose from 0-500lbs')),
    Field('height', label = 'Height (in) ', requires=IS_FLOAT_IN_RANGE(0,108,error_message='Please choose from 0-108 inches')),
    Field('age', label = 'Age (yrs)', requires=IS_INT_IN_RANGE(0,150,error_message='Please choose from 0-150 years')),
    Field('shoulders', label = 'Are your shoulders ', requires = IS_IN_SET(['Wide', 'Narrow'], zero = None)),
	Field('waist', label = 'Is your waist ', requires = IS_IN_SET(['Wide', 'Narrow'], zero = None)),
    Field('current_build', label = 'Is your current build ', requires = IS_IN_SET(['Round', 'Athletic', 'Lean'], zero = None)),
    Field('weight_gain', label = 'Describe your weight gain ', requires = IS_IN_SET(['Easily Gained, Difficult Losing', 'Gain and Lose Easily', 'Difficult Gaining'], zero = None)),
    Field('program', writable = False, readable = False),
    Field('body', writable = False, readable = False),
    Field('pushup', writable = False, readable = False),
    Field('pullup', writable = False, readable = False),
    Field('burpee', writable = False, readable = False),
    Field('squatjump', writable = False, readable = False),
    Field('pushup2', writable = False, readable = False),
    Field('pullup2', writable = False, readable = False),
    Field('burpee2', writable = False, readable = False),
    Field('squatjump2', writable = False, readable = False),
    Field('pushup3', writable = False, readable = False),
    Field('pullup3', writable = False, readable = False),
    Field('burpee3', writable = False, readable = False),
    Field('squatjump3', writable = False, readable = False),
    Field('pushup4', writable = False, readable = False),
    Field('pullup4', writable = False, readable = False),
    Field('burpee4', writable = False, readable = False),
    Field('squatjump4', writable = False, readable = False),
    Field('pushup5', writable = False, readable = False),
    Field('pullup5', writable = False, readable = False),
    Field('burpee5', writable = False, readable = False),
    Field('squatjump5', writable = False, readable = False),
    Field('counter', 'integer', writable = False, readable = False),
    )

db.define_table('forum',
      Field('title'),
    )

db.define_table('topics',
    Field('title'),
    Field('poster', 'text'),
    Field('user_id', db.auth_user),
    Field('f_table', 'reference forum'),
    Field('topic_posted', 'datetime'),
	Field('messages', 'text'),
	#Field('numposts'),
    )

db.define_table('threads',
	Field('body', 'text', length = 1000, notnull = True, represent = lambda text, row: PRE(text)), #text formatting
	Field('thread_poster', 'text'),
    Field('thread_posted', 'datetime'),
    Field('topic_table', 'reference topics'),
    )


db.forum.update_or_insert(title='General Discussion')
db.forum.update_or_insert(title='Exercises')
db.forum.update_or_insert(title='Nutrition')
db.forum.update_or_insert(title='Supplements')
db.forum.update_or_insert(title='Powerlifting')
db.forum.update_or_insert(title='Fitness Competitions')

def get_author_name():
    name = 'Nobody'
    if auth.user:
        name = auth.user.first_name
    return name

db.topics.user_id.default = auth.user_id
db.topics.user_id.readable = db.topics.user_id.writable = False
db.users.user_id.default = auth.user_id
db.users.user_id.readable = db.topics.user_id.writable = False

db.topics.poster.default = get_author_name()
db.topics.poster.writable = False

db.topics.topic_posted.default = datetime.utcnow()
db.topics.topic_posted.writable = False

db.threads.thread_poster.default = get_author_name()
db.threads.thread_poster.writable = False

db.threads.thread_posted.default = datetime.utcnow()
db.threads.thread_posted.writable = False
