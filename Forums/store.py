
class MemberStore:

    members = []

    def get_all(self):
        # get all members
        return MemberStore.members

    def add(self, member):
        # append member
        MemberStore.members.append(member)

    def get_by_id(self, id):
        # search for member by id

    def update(self, member):
        # update member data

    def delete(self, id):
        # delete member by id

    def entity_exists(self, member):
        # checks if an entity exists in a store

class PostStore:

    posts = []

    def get_all(self):
        # get all posts
        return PostStore.posts

    def add(self, post):
        # append post
        PostStore.posts.append(post)

    def get_by_id(self, id):
        # search for post by id

    def update(self, post):
        # update post data

    def delete(self, id):
        # delete post by id

    def entity_exists(self, post):
        # checks if an entity exists in a store
