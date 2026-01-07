from locust import HttpUser, task, between

class EcommerceUser(HttpUser):
    wait_time = between(1, 3)

    @task(3)
    def homepage(self):
        self.client.get("/")

    @task(2)
    def search_product(self):
        self.client.get("/search?q=laptop")

    @task(2)
    def view_product(self):
        self.client.get("/laptop")

    @task(1)
    def add_to_cart(self):
        self.client.post("/cart/add", json={
            "productId": 1,
            "quantity": 1
        })

    @task(1)
    def checkout(self):
        self.client.get("/checkout")
