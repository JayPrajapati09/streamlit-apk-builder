[app]
title = App Wrapper
package.name = appwrapper
package.domain = org.test
source.dir = .
source.include_exts = py
version = 0.1

# 
# THIS IS THE CRITICAL FIX:
# We must use the 'webview' bootstrap, not 'sdl2'.
# We also require 'android' instead of 'kivy'.
#
requirements = python3,android
bootstrap = webview

orientation = portrait
fullscreen = 1
android.permissions = INTERNET
android.archs = arm64-v8a

# Stability settings (these are all correct)
android.ndk = 25b
android.build_tools = 31.0.0
android.accept_sdk_license = True