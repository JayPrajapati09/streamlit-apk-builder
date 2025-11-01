# main.py
from jnius import autoclass

# We will replace this URL later with the user's input
# For now, we hard-code it for testing.
APP_URL = "https://google.com" 

# Import Android classes
PythonActivity = autoclass('org.kivy.android.PythonActivity')
WebView = autoclass('android.webkit.WebView')
WebViewClient = autoclass('android.webkit.WebViewClient')
LayoutParams = autoclass('android.view.ViewGroup$LayoutParams')
LinearLayout = autoclass('android.widget.LinearLayout')
Color = autoclass('android.graphics.Color')

class MyWebViewClient(WebViewClient):
    def shouldOverrideUrlLoading(self, view, url):
        view.loadUrl(url)
        return True

def main():
    # Get the current Android activity
    activity = PythonActivity.mActivity

    # Create a layout
    layout = LinearLayout(activity)
    layout.setOrientation(LinearLayout.VERTICAL)
    layout.setLayoutParams(LayoutParams(LayoutParams.MATCH_PARENT, LayoutParams.MATCH_PARENT))
    layout.setBackgroundColor(Color.BLACK) # Set background to black

    # Create the WebView
    webview = WebView(activity)
    webview.setWebViewClient(MyWebViewClient())
    webview.getSettings().setJavaScriptEnabled(True)
    webview.getSettings().setDomStorageEnabled(True)
    webview.getSettings().setUseWideViewPort(True)
    webview.getSettings().setLoadWithOverviewMode(True)
    #
    # Load the URL
    webview.loadUrl(APP_URL)
    
    # Add WebView to the layout
    layout.addView(webview, LayoutParams(LayoutParams.MATCH_PARENT, LayoutParams.MATCH_PARENT))
    
    # Set the activity's content view
    activity.setContentView(layout)

# This is the entry point for python-for-android
if __name__ == "__main__":
    main()