class UserService:
    def __init__(self):
        self.users = []
        self.next_id = 1

    def get_all_users(self):
        return self.users

    def get_user_by_id(self, user_id):
        for user in self.users:
            if user['id'] == user_id:
                return user
        return None

    def create_user(self, data):
        user = {
            'id': self.next_id,
            'firstName': data.get('firstName', 'Unknown'),
            'lastName': data.get('lastName', 'Unknown'),
            'age': data.get('birthYear', 0),
            'group': data.get('group', 'user')
        }
        self.users.append(user)
        self.next_id += 1
        return user

    def update_user(self, user_id, data):
        for user in self.users:
            if user['id'] == user_id:
                user['firstName'] = data.get('firstName', user['firstName'])
                user['lastName'] = data.get('lastName', user['lastName'])
                user['age'] = data.get('birthYear', user['age'])
                user['group'] = data.get('group', user['group'])
                return user
        return None

    def delete_user(self, user_id):
        for user in self.users:
            if user['id'] == user_id:
                self.users.remove(user)
                return user

