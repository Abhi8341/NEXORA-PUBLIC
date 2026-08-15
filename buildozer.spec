[app]

# (str) Title of your application
title = Nexora

# (str) Package name
package.name = nexora

# (str) Package domain
package.domain = org.nexora

# (str) Source code directory
source.dir = .

# (str) Application version
version = 5.1

# (list) Application requirements
requirements = python3,kivy,requests

# (str) Supported source file extensions
source.include_exts = py,png,jpg,jpeg,json,kv

# (str) Application icon
# Make sure icon.png is uploaded to the same folder as main.py
icon.filename = %(source.dir)s/icon.png

# (str) Application orientation
orientation = portrait

# (str) Supported Android architectures
android.archs = arm64-v8a,armeabi-v7a

# (bool) Fullscreen
fullscreen = 0

# (str) Android app theme
android.entrypoint = org.kivy.android.PythonActivity


[buildozer]

# (str) Build directory
build_dir = .buildozer

# (str) Output directory
bin_dir = bin

# (str) Log level
log_level = 2

# (bool) Warn when running Buildozer as root
warn_on_root = 1


[android]

# (str) Android API version
android.api = 35

# (str) Android minimum API version
android.minapi = 23

# (str) Android NDK version
android.ndk = 27c

# (str) Android NDK API
android.ndk_api = 23

# (list) Android permissions required by Nexora
android.permissions = INTERNET,ACCESS_FINE_LOCATION,ACCESS_COARSE_LOCATION,POST_NOTIFICATIONS

# (str) Android app activity
android.entrypoint = org.kivy.android.PythonActivity

# (bool) Allow Android backup
android.allow_backup = 1

# (str) Android application label
android.add_src = %(source.dir)s

# (bool) Enable AndroidX
android.enable_androidx = 1


[app:android]

# Keep Android configuration together with the app
android.accept_sdk_license = True
