[app]
title = App Wrapper
package.name = appwrapper
package.domain = org.test
source.dir = .
source.include_exts = py

version = 0.1
requirements = python3,jnius
orientation = portrait
fullscreen = 1

android.permissions = INTERNET
android.arch = aarch64

# Use the 'webview' recipe from python-for-android
android.p4a.recipes = webview


android.ndk = 25b
android.build_tools = 31.0.0
android.accept_sdk_license = True