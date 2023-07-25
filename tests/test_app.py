
import unittest
import os
os.environ['TESTING'] = 'true'

from app import app
import sys
sys.path.insert(0, './app/__init__')

class AppTestCase(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_home(self):
        response = self.client.get('/')
        assert response.status_code == 200
        html = response.get_data(as_text=True)
        assert "<title>MLH Fellow</title>" in html 
        assert "{{titleEdu}} == Education"
        assert ".jpeg" or ".jpg" or ".png" in html
        assert "{{titleExp}}=Experience"


  




    def test_malformed_timeline_post(self):
        response = self.client.post("/api/timeline_post", data = {
            "email": "john@example.com", "content": "Hello world" })
        assert response.status_code == 400
        html = response.get_data(as_text=True)

        assert "invalid name" in html

        response = self.client.post("/api/timeline_post", data = {
            "name": "Hello world", "email": "john@example.com" })
        assert response.status_code == 400
        html = response.get_data(as_text=True)

        assert "invalid content" in html

        response = self.client.post("/api/timeline_post", data = {
            "name":"John Doe","email": "not-an-email", "content": "Hello world" })
        assert response.status_code == 400
        html = response.get_data(as_text=True)

        

        assert "invalid email" in html 
        
def test_timeline(self):


        response = self.client.get('/api/timeline_post')
        assert response.status_code == 200
        assert response.is_json
        json = response.get_json()
        assert "timeline_posts" in json
        assert len(json['timeline_posts']) == 0
        html = response.get_data(as_test=True)
        assert "{{tite}} == Timeline"
        assert "<div class='container'>" in html 
        assert "<div class='timeline'>" in html


        response = self.client.post("/api/timeline_post", data = {
           "name":"John Doe", "email": "john@example.com", "content": "Hello world" })
        assert response.status_code == 200
        html = response.get_data(as_test=True)
        assert "Hello" in html