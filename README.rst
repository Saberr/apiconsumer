APICONSUMER: A super lightweight REST API requests wrapper
==========================================================

Following the same philosophy of Requests module (REST) ApiConsumer is here to make your life easier.

Are you lazy enough to configure authentication for every single request? How about handling errors? Wouldn't it be
great if all that could be done in 2 lines?


How to use
----------

Behold the power of ApiConsumer:

.. code-block:: python

    >>> from apiconsumer import ApiConsumer
    >>> my_api = ApiConsumer(url='https://myapi.com', extra_headers={'Authorization': 'JWT mytoken'})
    >>> users = my_api.get_users()


Making POST request is also easy:

.. code-block:: python

    >>> new_user = my_api.post_users(data={'email': 'someguy@something.com', 'password': 'correct-horse-battery-staple'})


Real example
------------

ReqRes.in provides a testing API, with fake data. Let's get all the users from their Users model. The endpoint for this is just GET reqres.in/api/users

.. code-block:: python

    >>> from apiconsumer import ApiConsumer
    >>> my_api = ApiConsumer(url='https://reqres.in/api', extra_headers={})
    >>> users = my_api.get_users()
    >>> print(users)
    {'data': [{'avatar': 'https://s3.amazonaws.com/uifaces/faces/twitter/calebogden/128.jpg',
               'first_name': 'George',
               'id': 1,
               'last_name': 'Bluth'},
              {'avatar': 'https://s3.amazonaws.com/uifaces/faces/twitter/josephstein/128.jpg',
               'first_name': 'Janet',
               'id': 2,
               'last_name': 'Weaver'},
              {'avatar': 'https://s3.amazonaws.com/uifaces/faces/twitter/olegpogodaev/128.jpg',
               'first_name': 'Emma',
               'id': 3,
               'last_name': 'Wong'}],
             'page': 1,
             'per_page': 3,
             'total': 12,
             'total_pages': 4}

So, if you want to PATCH a specific user with ID 2, the endpoint would be PATCH //resres.in/api/users/2. In that case, we could do:

.. code-block:: python

    >>> updated_user = my_api.patch_users_2(data={'age': 88})
    >>> print(updated_user)
    {'age': '88', 'updatedAt': '2017-11-29T12:10:31.986Z'}


ApiConsumer just turns attributes or method you ask for into request strings. So, you can user variables for IDs like this:

.. code-block:: python

    >>> user_id = 2
    >>> updated_user = my_api['patch_users_%d' % user_id](data={'age': 88})


How to install
--------------
.. code-block:: bash

    $ pip install apiconsumer


Contribute
----------
Be our guest. We'd like to see your awesome ideas. Just fork the repo, create a branch and create pull request.

