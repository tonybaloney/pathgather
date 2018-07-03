=======
History
=======

1.9.0
-----

* Added support for comments on paths, creating and listing comments. Delete comment added but API returns 404.
* Added support for comments on content

1.8.0
-----

* Allow filtering of paths and users by custom query
* Added `get_by_email` to users class

1.7.0
-----

* Use arrow dates on formatted UserPath

1.4.0 (2018-03-12)
------------------

* Add support for filtering content
* Add support for updating a piece of content

1.3.0 (2017-12-11)
------------------

* Add pathgather.skills API for gathering, listing and adding skills
* Add support to invite a user from a gathering
* Remove `add_user` feature, since the API doesn't work
* Add ability to list content in a gathering and delete content
* Add support to list paths within a gathering
* Update production path and user models

1.2.0 (2017-12-09)
------------------

* Fetch content completions and starts for users
* Register content completion for a user and a piece of content
* Fetch path starts and completions for users
* Gatherings API for listing, getting, creating, updating and deleting Gatherings
* List users within a gathering
* Add or remove users from a gathering

1.1.0 (2017-12-08)
------------------

* Updated content models with new fields
* Added support to specific content provider by name or custom_id
* Fixed doc issue with content.create
* Added pathgather.models package to setup.py
* Added SSL check disable flag on client and HTTP proxy settings

1.0.0 (2017-09-01)
------------------

* Introduce models for all methods, created tests based on documented and real API results. 91% test coverage
* Add support for adding skills to users, setting the skill level and deleting skills

0.5.0 (2017-09-01)
------------------

* Added some unit tests to the base client and improved doc strings for documentation

0.4.0 (2017-08-29)
------------------

* [FIX] Remove default proxy settings
* Add support to page out all() methods in content, users and paths. Method will now return all results

0.3.0 (2017-08-29)
------------------

* Add proxy support

0.2.0 (2017-08-28)
------------------

* Added path and content API endpoints

0.1.0 (2017-08-28)
------------------

* First release on PyPI.
