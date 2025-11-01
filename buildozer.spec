[app]
title = App Wrapper
package.name = appwrapper
package.domain = org.test
source.dir = .
source.include_exts = py
version = 0.1

# SOLUTION: Use the 'webview' bootstrap and require 'android'
requirements = python3,android
bootstrap = webview

orientation = portrait
fullscreen = 1
android.permissions = INTERNET

# SOLUTION: Use 'android.archs' for a modern, explicit build
android.archs = arm64-v8a

# Stability settings (these are all still needed)
android.ndk = 25b
android.build_tools = 31.0.0
android.accept_sdk_license = True