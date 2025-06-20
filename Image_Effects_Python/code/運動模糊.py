import numpy as np
import cv2

def motion_blur( f, length, angle ):
	nr, nc = f.shape[:2]
	filter = np.zeros( [ length, length ] )   # W * W
	x0, y0 = length // 2, length // 2
	x_len  = round( x0 * np.cos( np.radians( angle ) ) )
	y_len  = round( y0 * np.sin( np.radians( angle ) ) )
	x1, y1 = int( x0 - x_len ), int( y0 - y_len )
	x2, y2 = int( x0 + x_len ), int( y0 + y_len )
	cv2.line( filter, ( y1, x1 ), ( y2, x2 ), ( 1, 1, 1 ) )   #白線
	filter /= np.sum( filter )   #加總=1
	g = cv2.filter2D( f, -1, filter )
	return g

def main( ):
	img1 = cv2.imread( "skyline.jpg", -1 )
	img2 = motion_blur( img1, 50, 135 )   #(影像,像素,角度)
	cv2.imshow( "Original Image", img1 )
	cv2.imshow( "Motion Blur", img2 )
	cv2.waitKey( 0 )

main( )