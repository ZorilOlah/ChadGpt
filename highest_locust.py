from locust import HttpUser, task, between

class ApiUser(HttpUser):

    headers = {
        "Content-Type": "application/json",
    }

    @task
    def test_post_endpoint(self):
        payload = {
            "lowest": "4",
            "highest": "9"
        }
        self.client.post("/highest", json=payload, headers=self.headers)
