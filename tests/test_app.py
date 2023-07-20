import unittest
import os
testing = os.environ.get('TESTING')
testing

from app import app

class AppTestCase(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()
    
    def test_home(self):
        response = self.client.get("/")
        assert response.status_code == 200
        html = response.get_data(as_text=True)
        assert "<title>MLH Fellow</title>" in html

        #New Test
        hobbyResponse = self.client.get("/hobbies")
        assert hobbyResponse.status_code == 200

    def test_timeline(self):
        response = self.client.get("/api/timeline_post")
        assert response.status_code == 200
        assert response.is_json
        json = response.get_json()
        assert "timeline_posts" in json
        assert len(json['timeline_posts']) == 0

        # New Test
        postResponse = self.client.post("/api/timeline_post")
        assert postResponse.status_code == 200

        # New Test
        timelineResponse = self.client.get("/timelinePost")
        assert timelineResponse.status_code == 400

    def test_malformed_timeline_post(self):

        response = self.client.post("/api/timeline_post", data={"name": "John Doe", "email": "john@example.com", "content": "Hello world, I'm John!"})
        assert response.status_code == 200
        html = response.get_data(as_text=True)


        response = self.client.post("/api/timeline_post", data={"name": "John Doe", "email": "john@example.com", "content": "TEXT"})
        assert response.status_code != 400
        html = response.get_data(as_text=True)
        

        response = self.client.post("/api/timeline_post", data={"name": "John Doe", "email": "john@doe.com", "content": "Hello world, I'm John!"})
        assert response.status_code == 200
        html = response.get_data(as_text=True)
        