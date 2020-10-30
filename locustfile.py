import time
from locust import HttpUser, task, between

class QuickstartUser(HttpUser):
    wait_time = between(1, 2)

    @task
    def index_page(self):
        self.client.get("/")
        self.client.get("/predict")

    @task(3)
    def view_item(self):
        for item_id in range(10):
            self.client.get(f"/item?id={item_id}", name="/item")
            time.sleep(1)
     @task()
    def predict_endpoint(self):
        self.client.post('/predict', json = test_data)
        
    def on_start(self):
        self.client.post("/login", json={"username":"foo", "password":"bar"})
