

import gtk,webkit

def go_but(widget):
	add = addressbar.get_text()
	if add.startswith('https://'):
		web.open(add)
	else:
		add="https://"+add
		addressbar.set_text(add)
		web.open(add)
		
			
def stop_but(widget):
	web.stop_loading()

def new_title(view, frame, title):
	win.set_title(title)

def back_but(widget):
	web.go_back()
	
def for_but(widget):
	web.go_forward()

def refr_but(widget):
	web.reload()
	

win = gtk.Window()

win.connect('destroy',lambda w: gtk.main_quit())
win.set_default_size(800,600)
box1= gtk.VBox()




win.add(box1)


box2= gtk.HBox()

box1.pack_start(box2, False)

backbutton = gtk.Button("BACK")


backbutton.show()

forwardbutton=gtk.Button("FORWARD")

addressbar = gtk.Entry()
addressbar.connect("activate", go_but)
forwardbutton.show()
refr=gtk.Button("REFRESH")
web=webkit.WebView()
frame1=web.get_main_frame()
frame1.load_uri("https://www.google.com")
addressbar.set_text("https://www.google.com")

box2.pack_start(backbutton, False)
box2.pack_start(forwardbutton,False)
box2.pack_start(refr,False)
box2.pack_start(addressbar)

gobutton = gtk.Button("GO")
stopbutton = gtk.Button("STOP")

box2.pack_start(gobutton, False)
box2.pack_start(stopbutton, False)
gobutton.connect("clicked", go_but)

scroller = gtk.ScrolledWindow()
box1.pack_start(scroller)

web.connect("title-changed", new_title)
refr.connect("clicked",refr_but)
stopbutton.connect("clicked", stop_but )
backbutton.connect("clicked",back_but)
forwardbutton.connect("clicked",for_but)


scroller.add(web)

win.show_all()
gtk.main()


