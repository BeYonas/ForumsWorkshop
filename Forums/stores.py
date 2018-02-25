class MemberStore:
    Last_id = 1
    members = []

    def get_all(self):
        # get all members
        return MemberStore.members

    def add(self, member):
        # append member
        member.id = MemberStore.Last_id

        MemberStore.members.append(member)

        MemberStore.Last_id += 1

    def get_by_id(self, id):
        # search for member by id
        for member in MemberStore.members:
            if member.id == id:
                return member
        return None

    def update(self, member):
        # update member data
        pass

    def delete(self, id):
        # delete member by id
        member_to_delete = MemberStore.get_by_id(id)
        MemberStore.members.remove(member_to_delete)

    def entity_exists(self, member):
        # checks if an entity exists in a store
        return member in MemberStore.members


class PostStore:
    Last_id = 1
    posts = []

    def get_all(self):
        # get all posts
        return PostStore.posts

    def add(self, post):
        # append post
        post.id = PostStore.Last_id

        PostStore.posts.append(post)

        PostStore.Last_id += 1

    def get_by_id(self, id):
        # search for post by id
        for post in PostStore.posts:
            if post.id == id:
                return post
        return None

    def update(self, post):
        # update post data
        pass

    def delete(self, id):
        # delete post by id
        post_to_delete = PostStore.get_by_id(id)
        PostStore.posts.remove(post_to_delete)

    def entity_exists(self, post):
        # checks if an entity exists in a store
        return post in PostStore.posts
