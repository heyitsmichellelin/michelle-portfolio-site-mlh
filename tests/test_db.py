import unittest 
from peewee import *

from app import TimelinePost
from app import get_timeline_posts
from playhouse.shortcuts import model_to_dict 


MODELS= [TimelinePost]


test_db = SqliteDatabase(':memory:')


class TestTimelinePost(unittest.TestCase):
    def setup(self):
        test_db.bind(MODELS, bind_refs=False, bind_backrefs=False)
        test_db.connect()
        test_db.create_tables(MODELS)


    def tearDown(self):
        test_db.drop_tables(MODELS)


        test_db.close()


    def test_timeline_post(self):

        first_post = TimelinePost.create(name = 'John Doe', 
                                         email = "john@example.come",
                                         content ="sorry ya'll, this is a test")
        first_dict = model_to_dict(first_post)
        assert first_post.id == 1

        second_post = TimelinePost.create(name = 'Idris Doe', 
                                         email = "Idris@example.come",
                                         content ="sorry ya'll, this is a test")
        second_dict = model_to_dict(second_post)
        assert second_post.id == 2

        print("\n")

        posts = get_timeline_posts()['timeline_posts']

    #to account for the fact that when only this file is run both files have the
    #exact same post time so the order is messed up, having the first post be at index [1] but when i run both files
    #the first post is acually at index 0
        if posts[0]['id'] ==1:
            first_post_test = posts[0]
            second_post_test = posts[1]
        else:
            first_post_test = posts[1]
            second_post_test = posts[0]


        assert first_dict['name'] == first_post_test['name']
        assert first_dict['email'] == first_post_test['email']
        assert first_dict['content'] == first_post_test['content']

        assert second_dict['name'] == second_post_test['name']
        assert second_dict['email'] == second_post_test['email']
        assert second_dict['content'] == second_post_test['content']