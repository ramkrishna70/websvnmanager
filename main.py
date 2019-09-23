# 
# File Name: appsettings.py
#
# Version: 1.0.0
#
# Application Name: websvnmanager
#
# Author: Ram Krishna Kumar
# 
# Email: ramkrishna70@live.com
#
# Origin: India
#
# License: Apache License 2.0

import kivy
import os
import platform
import sys
from kivy.core.text import Label as CoreLabel
from kivy.uix.button import Button
from kivy.base import runTouchApp
from kivy.uix.spinner import Spinner

kivy.require('1.0.6') # replace with your current kivy version !

from kivy.app import App as websvn
from kivy.uix.label import Label


class WebSvnManager(websvn):
 
    def build_config(self, config):
        config.setdefaults('section1', {
            'key1': 'value1',
            'key2': '42'
        })

    def get_application_config(self):
        return super(TestApp, self).get_application_config(
            '~/.%(appname)s.ini')

    def build(self):

        config = self.config
        return Label: text: 
        ('[b]Hello[/b] [color = ff0099]World[/color]\n'
        '[color = ff0099]Hello[/color] [b]World[/b]\n'
        '[b]Hello[/b] [color = ff0099]World:):)[/color]') 
   		markup: True
    	font_size: '64pt'

if __name__ == '__main__':
    WebSvnManager().run()