import unittest
from flask.wrappers import Response
from app import app, user_service 

class TestUserService(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.user_service = user_service.UserService()

    def test_create_user(self):
        data = {'firstName': 'John', 'lastName': 'Doe', 'birthYear': 1990, 'group': 'user'}
        response: Response = self.app.post('/users', json=data)
        user = response.get_json()
        self.assertEqual(response.status_code, 201)
        self.assertEqual(user['id'], 1)
        self.assertEqual(user['firstName'], 'John')

    def test_get_all_users(self):
        response: Response = self.app.get('/users')
        users = response.get_json()
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(users, list)

    def test_get_user_by_id(self):
        data = {'firstName': 'John', 'lastName': 'Doe', 'birthYear': 1990, 'group': 'user'}
        user = self.user_service.create_user(data)  # Poprawione wywołanie metody
        response: Response = self.app.get(f'/users/{user["id"]}')
        user_result = response.get_json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(user_result['id'], user['id'])

    def test_update_user(self):
        data = {'firstName': 'John', 'lastName': 'Doe', 'birthYear': 1990, 'group': 'user'}
        user = user_service.create_user(data)
        updated_data = {'firstName': 'Updated John'}
        response: TestResponse = self.app.patch(f'/users/{user["id"]}', json=updated_data)
        updated_user = response.get_json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(updated_user['firstName'], 'Updated John')

    def test_delete_user(self):
        data = {'firstName': 'John', 'lastName': 'Doe', 'birthYear': 1990, 'group': 'user'}
        user = user_service.create_user(data)
        response: TestResponse = self.app.delete(f'/users/{user["id"]}')
        deleted_user = response.get_json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(deleted_user['id'], user['id'])

    def test_create_user_invalid_data(self):
        data = {'firstName': 'John', 'lastName': 'Doe'} 
        response: TestResponse = self.app.post('/users', json=data)
        error = response.get_json()
        self.assertEqual(response.status_code, 400)
        self.assertEqual(error['error'], 'Invalid data')

    def test_get_user_by_id_not_found(self):
        response: TestResponse = self.app.get('/users/999') 
        error = response.get_json()
        self.assertEqual(response.status_code, 404)
        self.assertEqual(error['error'], 'User not found')

    def test_update_user_not_found(self):
        updated_data = {'firstName': 'Updated John'}
        response: TestResponse = self.app.patch('/users/999', json=updated_data) 
        error = response.get_json()
        self.assertEqual(response.status_code, 404)
        self.assertEqual(error['error'], 'User not found')

    def test_delete_user_not_found(self):
        response: TestResponse = self.app.delete('/users/999') 
        error = response.get_json()
        self.assertEqual(response.status_code, 404)
        self.assertEqual(error['error'], 'User not found')

if __name__ == '__main__':
    unittest.main()
