#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Use text editor to edit the script and type in valid Instagram username/password

from InstagramAPI import InstagramAPI
import time


if __name__ == "__main__":
    username = ""
    password = ""

    api = InstagramAPI(username, password)
    api.login()
    time.sleep(2)

    # user_id = '1461295173'
    if hasattr(api, 'username_id'):
        user_id = api.username_id
    else:
        for i in range(0, 10):
            print("please Patient 500 secondes for retry")
            time.sleep(500)

            api = InstagramAPI(username, password)
            api.login()
            time.sleep(2)

            if hasattr(api, 'username_id'):
                user_id = api.username_id
                break

    # Alternatively, use the code below
    # (check evaluation.evaluate_user_followers for further details).

    # check followers
    followers = api.getTotalFollowers(user_id)
    time.sleep(2)

    # check followings
    followings = api.getTotalFollowings(user_id)
    time.sleep(2)

    suivis = set()
    for users in followers:
        suivis.add(tuple(users.iteritems()))

    for users in followings:
        suivis.add(tuple(users.iteritems()))

    for users in suivis:
        Id_user = False
        username = False

        for attrib in users:
            if attrib[0] == "pk":
                Id_user = attrib[1]

            if attrib[0] == "username":
                username = attrib[1]

            if Id_user and username:
                break

        if Id_user and username:
            check_user = any(Id_user == users['pk'] for users in followers)
            check_user_following = any(Id_user == users['pk'] for users in followings)

            if not check_user:
                time.sleep(5)
                unfollow = api.unfollow(Id_user)
                if unfollow:
                    print("unfollow: {}".format(username))

            if check_user and not check_user_following:
                time.sleep(5)
                follow = api.follow(Id_user)
                if follow:
                    print("follow: {}".format(username))
