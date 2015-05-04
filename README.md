# PYWEBKITGTK
A basic browser built using PyWebkitGTK module in python. The module contains the inbuilt methods of the Webkit module. 
The pygtkWebkit Module is only available on linux platform.

Basic steps involved:

1) First import the Webkit and Gtk Modules. (Import GTK, WEBKIT)
2) Creating a GTK.window() object for the browser.
3) The addressbar object catches the url we wish to open and uses the inbuilt WebkitWebView method called open() to provide
    the view.
4) Scroller object was added to the WebKitWebView Object so that the the webpage or rendered WebView can be scrolled.

The project also uses several other inbuilt WebKitWebView functions to provide the functionality of a basic browser
