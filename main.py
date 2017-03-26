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
import caesar
import cgi

# html boilerplate for the top of every page
page_header = """
<!DOCTYPE html>
<html>
<head>
    <title>Web Caesar</title>
	<!-- <link type="text/css" rel="stylesheet" href="style.css" /> -->
</head>
<body>    
<div>
"""

# html boilerplate for the bottom of every page
page_footer = """
</div>
</body>
</html>
"""

def page_build(text_content):		
		rotate_label = "<label style='font-family: Arial; color: green;'> Rotate by: </label>"
		rotation_input ="<input style='font-family: Arial; color: green; width:153px;' type='number' name='userInpRotation'/>"
		message_label = "<label style='font-family: Arial; color: green;'> Type a message: </label>"
		textarea = "<textarea style='font-family: Arial; color: green; width:153px; height:60px' name='userTextArea'>" + text_content + "</textarea>"
		break_tag = "<br>"
		submit = "<input type='submit'/>"
 		form ="<form action='.' method='post'>" + "<table style='border: #000000 1px solid;'><tr><td>" + rotate_label + "</td><td></td><td>" + rotation_input + "</td></tr><tr><td>"+ break_tag + message_label + "</td><td></td><td>" + textarea + "</td></tr>"+ "<tr><td></td><td>"+ break_tag + submit + "</td><td></td></tr></table>"+ "</form>"
		header = "<h2 style='font-family: Arial; color: green;'> Web Caesar </h2>"
		
		retResponse = page_header + header + form + page_footer
		return retResponse
		

class MainHandler(webapp2.RequestHandler):
	def post(self):
		message = self.request.get("userTextArea")
		rotVal = self.request.get("userInpRotation")	
		rotVal = int(rotVal)
		encrypted_message = caesar.encrypt(message, rotVal) 
		escape_message = cgi.escape(encrypted_message)
		content = page_build(escape_message)
		self.response.write(content)
	def get(self):		
		message = "Hello World!" 		
		content = page_build("")
		self.response.write(content)
		
app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
















