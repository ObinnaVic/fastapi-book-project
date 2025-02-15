from fastapi.testclient import TestClient
<<<<<<< HEAD

=======
>>>>>>> upstream/main
from main import app

client = TestClient(app, base_url="http://test/api/v1")
