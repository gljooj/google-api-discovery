#!/bin/sh

# Credits: http://stackoverflow.com/a/750191

git filter-branch -f --env-filter "
    GIT_AUTHOR_NAME='Gabriel Jesus'
    GIT_AUTHOR_EMAIL='gabrielthe13@hotmail.com'
    GIT_COMMITTER_NAME='Gabriel Jesus'
    GIT_COMMITTER_EMAIL='gabrielthe13@hotmail.com'
  " HEAD