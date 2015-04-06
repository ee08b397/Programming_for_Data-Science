import numpy
import matplotlib.pyplot as plt 
import warnings 
import time

class hw6:
    @staticmethod
    def q1():
        'question 1'
        arrinit = numpy.arange(1,16,1).reshape((3,5)).transpose()
        arr0 = arrinit[[1, 3], :]
        arr1 = arrinit[:, 1]
        arr2 = arrinit[1:4, 0:3]
        arr3 = arrinit[numpy.where((arrinit > 3) & (arrinit < 11))]
        # arr3 = arrinit[((arrinit > 3) & (arrinit < 11))]

        print "1. 2-D array: \n", arrinit 
        print "\n1.a.The 2nd and 4th rows: \n", arr0 
        print "\n1.b.Contains the 2nd column: \n", arr1
        print "\n1.c.Rectangular section between the coordinates [1,0] and [3,2]\n", arr2
        print "\n1.d.Values that are between 3 and 11: \n", arr3
        return (arrinit, arr0, arr1, arr2, arr3)

    @staticmethod
    def q2():
        ' question 2'
        a = numpy.arange(25).reshape(5, 5)
        b = numpy.array([1., 5, 10, 15, 20])
        print "\n2. \n", numpy.transpose(numpy.divide(numpy.transpose(a), b))

    @staticmethod
    def q3():
        ' question 3'
        arrinit= numpy.random.rand(10,3)
        print "\n3.a. \n", numpy.argsort(abs(arrinit - 0.5))[:,0].choose(arrinit.transpose())
        print "\n3.b. \n", numpy.argsort(abs(arrinit - 0.5))[:,0]
        print "\n3.c. \n", numpy.asarray([arrinit[j, numpy.argsort(abs(arrinit - 0.5))[:,0][j]] for j in range(0, numpy.argsort(abs(arrinit - 0.5))[:,0].size)])

    @staticmethod
    def q4():
        ' question 4'
        print "\n4. Working on question 4, very hard..."
        try:
            xRange = numpy.arange(-2.0, 1.01, 0.01)
            yRange = numpy.arange(-1.5, 1.51, 0.01)
            mask = numpy.ones((xRange.size, yRange.size), dtype = bool)
        
            for x in range(xRange.size):   
                for y in range(yRange.size):      
                    c = xRange[x] + 1j * yRange[y] 
                    z = c
                    for v in range(100):
                        z = z**2 + c 
                        if abs(z) >= 100:
                            mask[x,y] = False 
                            break
        except Warning: 
            print "\n Oops, overflow"
        finally:
            plt.imshow(mask.T, extent=[-2, 1, -1.5, 1.5]) 
            plt.gray() 
            
            # sometimes plt.show() forbids picture saving properly
            plt.show(block=False)
            print "   Done! Figures would disappear in 3 seconds\n"
            time.sleep(3)
            plt.savefig('mandelbrot.png') 
            plt.close('all')
