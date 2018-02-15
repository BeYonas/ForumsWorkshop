# allowed papers: 100, 50, 10, 5, and rest of request

money = 500

request = 277

if money >= request > 0:
    while request >= 100:
        print "give 100"
        request -= 100
    while request >= 50:
        print "give 50"
        request -= 50
    while request >= 10:
        print "give 10"
        request -= 10
    if request >= 5:
        print "give 5"
        request -= 5
    if request > 0:
        print "give " + str(request)
        request = 0
else:
    print "Invalid request !"
