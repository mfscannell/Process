import unittest
from assignment1 import Curve

class testCurve(unittest.TestCase):

    def test_ObjectCreation(self):
        myCurve = Curve(self.func)
        self.assertTrue(isinstance(myCurve, Curve), "Return value incorrect.")

    def test_setErrorTolerance(self):
        myCurve = Curve(self.func)
        myCurve.setErrorTolerance(1)
        self.assertTrue(myCurve.getErrTolerance(), 1)

    def test_setErrorTolerance2(self):
        def func(x):
            return x

        myCurve = Curve(func)
        self.assertRaises(ValueError, myCurve.setErrorTolerance, -4)

    def test_setErrorTolerance3(self):
        myCurve = Curve(self.func)
        self.assertRaises(ValueError, myCurve.setErrorTolerance, 'a')

    def test_getErrorTolerance(self):
        def func(x):
            return x

        myCurve = Curve(func)
        self.assertEqual(myCurve.getErrTolerance(), 0.5, "Retrieval of tolerance is incorrect.")

    def test_IntegrateValues(self):
        myCurve = Curve(self.func)
        self.assertRaises(ValueError, myCurve.integrate, 'a', 4)

    def test_IntegrateValues2(self):
        myCurve = Curve(self.func)
        self.assertRaises(ValueError, myCurve.integrate, 3, 'a')


    def test_integrate(self):
        def func(x):
            return x**2

        myCurve = Curve(func)
        myIntegration = round(myCurve.integrate(0, 5),4)

        self.assertEqual(myIntegration, 41.6667, "Integration is wrong."
                         + "Should have gotten: 41.6667. You got " + str(myIntegration))

    def test_integrate2(self):
        def func(x):
            return x**2

        myCurve = Curve(func)
        myCurve.setErrorTolerance(0.0001)
        myValue = round(myCurve.integrate(1, 3),2)

        self.assertAlmostEqual(myValue, 8.67, 2, "Integration is wrong."
            + "Should have gotten 8.67. You got " + str(myValue))

    def test_integrate3(self):
        def func(x):
            return x

        myCurve = Curve(func)

        self.assertRaises(ValueError, myCurve.integrate, 8, 7)

    def test_integrate4(self):
        def func(x):
            return 0.5*x**2 + 4

        myCurve = Curve(func)
        myCurve.setErrorTolerance(0.00001)
        myIntegration = round(myCurve.integrate(1.5, 15.1),3)

        self.assertEqual(myIntegration, 627.663, "Integration is wrong."
                         + "Should have gotten: 627.663. You got " + str(myIntegration))

    def func(self, x):
        return x**2


