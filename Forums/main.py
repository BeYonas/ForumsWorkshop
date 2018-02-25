import models
import stores

member1 = models.Member("member1", 1)
member2 = models.Member("member2", 2)

members_store = stores.MemberStore()
members_store.add(member1)
members_store.add(member2)

post1 = models.Post("title1", "content1")
post2 = models.Post("title2", "content2")
post3 = models.Post("title3", "content3")

posts_store = stores.MemberStore()
posts_store.add(post1)
posts_store.add(post2)
posts_store.add(post3)
