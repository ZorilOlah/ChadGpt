from locust import HttpUser, task, between

class ApiUser(HttpUser):

    headers = {
        "Content-Type": "application/json",
    }

    @task
    def test_post_endpoint(self):
        payload = {
            "prompt": "Hi there please help me get alpha",
            "api_key": "gymbro69fire"
        }
        self.client.post("/chad_gpt", json=payload, headers=self.headers)
