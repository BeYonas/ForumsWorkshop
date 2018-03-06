import itertools


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
        result = None
        for member in MemberStore.members:
            if member.id == id:
                result = member
                break
        return result

    def update(self, updated_member):
        # update member data
        all_members = self.get_all()
        for index, member in enumerate(all_members):
            if updated_member.id == member.id:
                all_members[index] = updated_member
                break

    def delete(self, id):
        # delete member by id
        member_to_delete = self.get_by_id(id)
        MemberStore.members.remove(member_to_delete)

    def entity_exists(self, member):
        # checks if an entity exists in a store
        result = True

        if self.get_by_id(member.id) is None:
            result = False

        return result

    def get_by_name(self, name):
        return (member for member in self.get_all() if member.name == name)

    def get_members_with_posts(self, posts_list):
        all_members = self.get_all()
        for member, post in itertools.product(all_members, posts_list):
            if post.member_id == member.id:
                member.posts.append(post)
                posts_list.remove(post)
        return (member for member in all_members)

    def get_top_two(self, posts_list):
        sorted_members = sorted(self.get_members_with_posts(posts_list),
                                key=lambda member: len(member.posts),
                                reverse=True)
        return (member for member in sorted_members[:2])


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
        result = None
        for post in PostStore.posts:
            if post.id == id:
                result = post
                break
        return result

    def update(self, updated_post):
        # update post data
        all_posts = self.get_all()
        for index, post in enumerate(all_posts):
            if updated_post.id == post.id:
                all_posts[index] = updated_post
                break

    def delete(self, id):
        # delete post by id
        post_to_delete = self.get_by_id(id)
        PostStore.posts.remove(post_to_delete)

    def entity_exists(self, post):
        # checks if an entity exists in a store
        result = True

        if self.get_by_id(post.id) is None:
            result = False

        return result
