# The contents of this file are subject to the Common Public Attribution
# License Version 1.0. (the "License"); you may not use this file except in
# compliance with the License. You may obtain a copy of the License at
# http://code.reddit.com/LICENSE. The License is based on the Mozilla Public
# License Version 1.1, but Sections 14 and 15 have been added to cover use of
# software over a computer network and provide for limited attribution for the
# Original Developer. In addition, Exhibit A has been modified to be consistent
# with Exhibit B.
#
# Software distributed under the License is distributed on an "AS IS" basis,
# WITHOUT WARRANTY OF ANY KIND, either express or implied. See the License for
# the specific language governing rights and limitations under the License.
#
# The Original Code is reddit.
#
# The Original Developer is the Initial Developer.  The Initial Developer of
# the Original Code is reddit Inc.
#
# All portions of the code written by reddit are Copyright (c) 2006-2014 reddit
# Inc. All Rights Reserved.
###############################################################################

class MediaProvider(object):
    """Provider for storing media objects.

    Media objects are thumbnails, subreddit images/stylesheets, and app icons.
    A media provider must allow new objects to be added to the system and for
    users to be able to view those objects over HTTP.

    """
    def put(self, name, contents):
        """Put a media object on the media server and return its HTTP URL.

        `name` must be a local filename including an extension.

        `contents` is a byte string of the contents of the file.

        The return value should be an absolute URL with the `http` scheme but
        should also work if accessed with `https`.

        """
        raise NotImplementedError
