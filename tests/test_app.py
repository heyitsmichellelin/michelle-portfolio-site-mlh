# tests/test_app.py

import unittest
import os
os.environ['TESTING'] = 'true'

from app import app

class AppTestCase(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()
    
    def test_home(self):
        response = self.client.get('/')
        assert response.status_code == 200
        html = response.get_data(as_text=True)
        assert '<title>MLH Fellow</title>' in html

        # Tests relating to the home page
        assert '<h1>MLH Fellow </h1>' in html
        assert '<img src="./static/img/logo.svg" />' in html

        # Ensure that the links in the navigation bar are present
        assert '<a href=\'/hobbies\'>' in html
        assert '<a href=\'/travels\'>' in html
        assert '<a href=\'/timeline\'>' in html

    def test_timeline(self):
        response = self.client.get('/api/timeline_post')
        assert response.status_code == 200
        assert response.is_json
        json = response.get_json()
        assert "timeline_posts" in json
        assert len(json["timeline_posts"]) == 0

        # Test POST request to /api/timeline_post
        response = self.client.post("/api/timeline_post", 
                                data={"name": "John Doe", 
                                      "email": "john@example.com",
                                      "content": "Hello world, I'm John!"})
        assert response.status_code == 200
        assert response.is_json
        json = response.get_json()
        assert json["name"] == "John Doe"
        assert json["email"] == "john@example.com"
        assert json["content"] == "Hello world, I'm John!"
        assert "id" in json
        assert json["id"] == 1

        # Test GET request to /api/timeline_post after posting
        response = self.client.get('/api/timeline_post')
        assert response.status_code == 200
        assert response.is_json
        json = response.get_json()
        assert "timeline_posts" in json
        assert len(json["timeline_posts"]) == 1
        assert json["timeline_posts"][0]["name"] == "John Doe"
        assert json["timeline_posts"][0]["email"] == "john@example.com"
        assert json["timeline_posts"][0]["content"] == "Hello world, I'm John!"
        assert json["timeline_posts"][0]["id"] == 1

        # Test releating to /timeline
        response = self.client.get('/timeline')
        assert response.status_code == 200
        html = response.get_data(as_text=True)
        assert '<title>Timeline</title>' in html
        assert '<h1>Timeline</h1>' in html
        assert '<th>Name</th>' in html
        assert '<th>Email</th>' in html
        assert '<th>Created on</th>' in html
        assert '<th>Content</th>' in html

    def test_malformed_timeline_post(self):
        # POST request missing name
        response = self.client.post("/api/timeline_post", 
                                    data={"email": "john@example.com",
                                          "content": "Hello world, I'm John!"})
        assert response.status_code == 400
        html = response.get_data(as_text=True)
        assert "Invalid name" in html
        
        # POST request with empty content
        response = self.client.post("/api/timeline_post", 
                                    data={"name": "John Doe", 
                                          "email": "john@example.com",
                                          "content": ""})
        assert response.status_code == 400
        html = response.get_data(as_text=True)
        assert "Invalid content" in html
        
        # POST request with malformed email
        response = self.client.post("/api/timeline_post", 
                                    data={"name": "John Doe", 
                                          "email": "not-an-email",
                                          "content": "Hello world, I'm John!"})
        assert response.status_code == 400
        html = response.get_data(as_text=True)
        assert "Invalid email" in html