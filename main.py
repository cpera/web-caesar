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

class MainHandler(webapp2.RequestHandler):
	def post(self):
		message = self.request.get("userTextArea")
		rotVal = self.request.get("userInpRotation")	
		rotVal = int(rotVal)
		encrypted_message = caesar.encrypt(message, rotVal) 
		self.response.write("secret message:" + encrypted_message)
	def get(self):		
		message = "Hello World!" 		
		rotation_input ="<input type='number' name='userInpRotation'/>"
		textarea = "<textarea name='userTextArea'>" + "</textarea>"
		break_tag = "<br>"
		submit = "<input type='submit'/>"
 		form ="<form action='.' method='post'>" + rotation_input + break_tag + textarea + break_tag + submit + "</form>"
		self.response.write(form)
		
app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
















