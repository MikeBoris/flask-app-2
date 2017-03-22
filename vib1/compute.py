from numpy import exp, cos, linspace
import matplotlib.pyplot as plt
import os, time, glob

def damped_vibrations(t, A, b, w):
	return A*exp(-b*t)*cos(w*t)

def compute(A, b, w, T, resolution=500):
	"""Return filename of plot of the damped_vibration function"""
	t = linspace(0, T, resolution+1)
	u = damped_vibrations(t, A, b, w)
	plt.figure() # needed to avoid adding curves in plot
	plt.plot(t, u)
	plt.title('A=%g, b=%g, w=%g' % (A, b, w))
	# Make Matplotlib write to BytesIO file object and grab
	# return the object's string
	from io import BytesIO
	figfile = BytesIO()
	plt.savefig(figfile, format='png')
	figfile.seek(0)  # rewind to beginning of file
	import base64
	figdata_png = base64.b64encode(figfile.getvalue())
	return figdata_png

if __name__ == '__main__':
	print compute(1, 0.1, 1, 20)
