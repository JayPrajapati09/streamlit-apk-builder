[app]
title = App Wrapper
package.name = appwrapper
package.domain = org.test
source.dir = .
source.include_exts = py
version = 0.1

# 
# THE REAL FIX IS HERE:
# 1. We require 'android', NOT 'kivy'.
# 2. We set the 'bootstrap' to 'webview'.
#
requirements = python3,android
bootstrap = webview

orientation = portrait
fullscreen = 1
android.permissions = INTERNET

# We use 'android.archs' (plural) for a modern, explicit build
android.archs = arm64-v8a

# Stability settings (these are all still needed)
android.ndk = 25b
android.build_tools = 31.0.0
android.accept_sdk_license = True