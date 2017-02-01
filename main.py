#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2

page_layout = """
<!DOCTYPE html>
<html>
<body>
<form method = "post">

<table>
    <tr>
        <td align="right">Username:</td>
        <td align="left"><input type="text" name="username" /></td>
    </tr>
    <tr>
        <td align="right">Password:</td>
        <td align="left"><input type="password" name="password" /></td>
     </tr>
     <tr>
        <td align="right">Confirm Password:</td>
        <td align="left"><input type="password" name="confirm_password" /></td>
    </tr>
    <tr>
        <td align="right">Email (optional):</td>
        <td align="left"><input type="text" name="email" /></td>
    </tr>
    <tr>
        <td align="left"><input type="submit" value="Submit" id="submit_button" /> </td>
    </tr>
</table>
</form>
</body>
</html>
"""


class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write(page_layout)

    def post(self):
        username = self.request.POST['username']
        password = self.request.get('password')
        confirm_password = self.request.get('confirm_password')
        email = self.request.get('email')


app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/welcome.html', )
], debug=True)
